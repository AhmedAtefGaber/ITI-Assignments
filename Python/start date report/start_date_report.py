
#!/usr/bin/env python3
import csv
import datetime

wget "http://marga.com.ar/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines():
    """read the employees data into list then sorting the data based on date and return the sorted data"""
    lines = []
    with open('employees-with-date.csv','r' ) as f:
        reader = csv.reader(f)
        for line in reader:
            lines.append(line)
    lines=lines[1:]
    lines.sort(key=lambda date: datetime.datetime.strptime(date[3], '%Y-%m-%d'))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    lines = get_file_lines()
    min_date = datetime.datetime.today()
    min_date_employees = []
    for line in lines:
  for line in lines:
        line_date = datetime.datetime.strptime(line[3], '%Y-%m-%d')
        if line_date >= start_date:
            if line_date < min_date:
                min_date = line_date
                min_date_employees = []
        if line_date == min_date:
            min_date_employees.append("{} {}".format(line[0], line[1]))

    return min_date, min_date_employees

def list_newer(start_date):
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)


if __name__ == "__main__":
	main()

