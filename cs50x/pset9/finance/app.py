import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
    if request.method == "POST":
        try:
            add_cash = int(request.form.get("add_cash"))
        except (TypeError, ValueError):
            return apology("must provide a valid amount", 400)
        if add_cash <= 0:
            return apology("must provide a valid amount", 400)

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", add_cash, session["user_id"])
        return redirect("/")

    transactions = db.execute(
        "SELECT symbol, SUM(shares) AS total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", session["user_id"])
    portfolio = []
    total = 0

    for row in transactions:
        data = lookup(row["symbol"])
        if data:
            price = data["price"]
            value = row["total_shares"] * price
            total += value
            portfolio.append({
                "symbol": row["symbol"],
                "shares": row["total_shares"],
                "price": usd(price),
                "total": usd(value)
            })

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    total += cash

    return render_template("index.html", portfolio=portfolio, cash=usd(cash), total=usd(total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()

        try:
            shares = int(request.form.get("shares"))
        except (ValueError, TypeError):
            return apology("must provide a valid number of shares", 400)

        if shares < 1:
            return apology("must buy at least 1 share", 400)

        data = lookup(symbol)
        if data is None:
            return apology("must provide a valid symbol", 400)

        price = shares * data["price"]

        row = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = row[0]["cash"]

        if cash >= price:
            db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", price, session["user_id"])
            db.execute("INSERT INTO transactions(user_id, symbol, shares, price) VALUES(?, ?, ?, ?)",
                       session["user_id"], symbol, shares, data["price"])
        else:
            return apology("not enough cash", 400)

        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])
    for transaction in transactions:
        price = transaction["price"]
        shares = transaction["shares"]
        transaction["price"] = usd(price)              # format USD pour affichage
        transaction["total"] = usd(price * shares)
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == 'POST':
        symbol = request.form.get("symbol")
        data = lookup(symbol)

        if data is None:
            return apology("must provide a valid symbol", 400)

        data["price"] = usd(data["price"])
        return render_template("quote.html", data=data)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("must provide a username", 400)

        if not password or not confirmation:
            return apology("must provide a password", 400)

        if password != confirmation:
            return apology("password does not match", 400)

        password = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, password)
        except:
            return apology("username already exists", 400)

        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        if shares < 1:
            return apology("must sell at least 1 share", 400)

        row = db.execute(
            "SELECT SUM(shares) AS total_shares FROM transactions WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        owned = int(row[0]["total_shares"] or 0)
        if owned < shares:
            return apology("not enough shares", 400)

        data = lookup(symbol)
        if data is None:
            return apology("must provide a valid symbol", 400)

        price = data["price"] * shares
        db.execute("INSERT INTO transactions(user_id, symbol, shares, price) VALUES(?, ?, ?, ?)",
                   session["user_id"], symbol, -shares, data["price"])
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", price, session["user_id"])
        return redirect("/")

    else:
        transactions = db.execute(
            "SELECT symbol, SUM(shares) AS total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", session["user_id"])
        portfolio = [row for row in transactions]
        return render_template("sell.html", portfolio=portfolio)
