from application.people import *
from application.salary import *
from datetime import *

if __name__ == '__main__':
    hello_people()
    hello_salary()
    print(f'Today is {datetime.now().date()}')
