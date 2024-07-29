from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import emoji

if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    get_employees()
    print(emoji.emojize(' :thumbs_up:'))