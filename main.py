import datetime
from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    dt_now = datetime.datetime.now()
    print(dt_now)
