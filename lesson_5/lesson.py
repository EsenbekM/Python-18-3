import calculator
from person import Person as P

from random import randint as generate_number
from datetime import datetime, date
from termcolor import colored, cprint
from decouple import config
import os

# print(calculator.subtruction(23, 10))
#
p1 = P("Esen", 18)
# print(p1)

# print(generate_number(1, 100))

yesterday = datetime(2022, 5, 16, )
today = datetime.now()

day = datetime.strptime("2022.05.17", "%Y.%m.%d")
# print(day)
#
# print(yesterday)
# print(today.day)

# cprint("Hello world!", 'red', 'on_yellow', attrs=['underline', 'bold'])


# print(os.environ.get("MY_PASSWORD"))
# print(type(config("NUMBER", default=False, cast=int)))
# print(type(config("NUMBER")))
