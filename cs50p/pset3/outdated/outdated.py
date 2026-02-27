months = {
            "january": 1,
            "february": 2,
            "march": 3,
            "april": 4,
            "may": 5,
            "june": 6,
            "july": 7,
            "august": 8,
            "september": 9,
            "october": 10,
            "november": 11,
            "december": 12
        }

while True:
    try:
        date = input("Date: ").strip().lower()

        if '/' in date:
            month, day, year = date.split('/')
            day = int(day)
            month = int(month)
            
            if day > 31 or day < 1 or month > 12 or month < 1: continue
            print(f"{year}-{int(month):02}-{day:02}")
            break

        if '-' in date:
            print(date)
            break

        month, day, year = date.split()
        if ',' in day:
            day = int(day.replace(',', ''))
        else:
            continue

        if day > 31 or day < 1: continue
        if month in months:
            print(f"{year}-{months[month]:02}-{int(day):02}")
            break

    except (ValueError, IndexError):
        continue
