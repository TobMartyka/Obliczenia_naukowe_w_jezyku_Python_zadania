from datetime import datetime, timedelta

def print_working_days(date1, date2):
    start_date = datetime.strptime(date1, '%Y-%m-%d')
    end_date = datetime.strptime(date2, '%Y-%m-%d')

    current_date = start_date
    while current_date < end_date:
        if current_date.weekday() < 5:
            print(current_date.date())
        current_date += timedelta(days=1)

print_working_days("1999-09-18", "1999-10-18")
