from application.people import hello_people
from application.salary import hello_salary
from datetime import datetime as dt

if __name__ == '__main__':
    hello_people()
    hello_salary()
    print(f'Today is {dt.now().date()}')
