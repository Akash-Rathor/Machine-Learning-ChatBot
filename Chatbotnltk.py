import time
import random
import datetime
import calendar
from nltk.tokenize import word_tokenize, sent_tokenize

print("Hello I am your chatting bot :)")

time.sleep(1)
reply = word_tokenize(input("Hey! How May I help you Today?"))

GREATING_INPUTS = ["HEY","HI", "HELLO", "HOW ARE YOU", "HEYA", "SUP", "WHATS'S UP", "HOW R U"]
GREATING_RESPONSE = ["HELLO CUTIE","HEY MAN", "HEYAA!!", "AWESOMELY GREAT YOU ARE", "TODAY GETTING BORED PLEASE CHAT WITH ME", "CHAT WITH ME :(", "WOW! I WAS GETTING BORED FINALLY YOU AWAKE ME"]
for i in reply:
    if i.upper() in GREATING_INPUTS:
        print(random.choice(GREATING_RESPONSE))
    break

print("I can find days in calender for any date.\n I have to scroll so many pages . Its boring but I'll do it for you")

date = int(input("Enter your date(DD):"))
month = int(input("Enter your month(MM):"))
year = int(input("Enter your month(year):"))
print("Here you go")
print(calendar.month(year, month, date))


