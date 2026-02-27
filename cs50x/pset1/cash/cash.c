#include <cs50.h>
#include <stdio.h>

int count(int change);

int main(void)
{
    int change;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 0);

    int coins = count(change);
    printf("%i\n", coins);
}

int count(int change) // function to count the minimal number of coins required for change
{
    // count
    int coins = 0;

    // assign coins value for better reading
    int quarter = 25;
    int dime = 10;
    int nickel = 5;
    int penny = 1;

    coins += change / quarter; // divide change by quarter (25), add the result to coins
    change %= quarter;         // use mod quarter (25) to calculte the remaining change

    coins += change / dime; // repeat the process, divide with 10
    change %= dime;         // remaining change

    coins += change / nickel; // repeat the process, divide with 5
    change %= nickel;         // remaining change

    coins += change / penny; // no need to use mod because the rest is now 0

    return coins;
}
