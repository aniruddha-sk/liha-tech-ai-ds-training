dates = ["2026-12-01", "2025-05-10", "2026-01-15"]

def date_key(date):
    year, month, day = date.split("-")
    return int(year), int(month), int(day)

dates.sort(key=date_key)

print(dates)
