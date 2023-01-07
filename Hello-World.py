import datetime as dt
from math import floor

def get_age():
    # Creates data objects from today's date and my birthday.
    d1 = dt.date(2001,6,13)
    d2 = dt.date.today()

    # Finds difference between today's date and my birthday, then rounds it down
    tdelta = d2 - d1
    return floor(tdelta.days/365)

def hello_world():
    print("Hello World!")

    age = get_age()

    print(f"My name is Seth Hartman, I am a computer programmer who is {age} years old. I am currently a student at BYU-Idaho. ")


if __name__ == '__main__':
    hello_world()