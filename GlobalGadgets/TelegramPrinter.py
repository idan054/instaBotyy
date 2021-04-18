#1. go to this adress: https://telegram.me/BotFather and follow the instructions
#2. in terminal: pip install telegram-send followed by telegram-send configure
import datetime
from time import sleep
import telegram_send

def telegram_printer(text):
    print("----------------------------")
    print("Also available on Telegram:")
    print(text)
    telegram_send.send(messages=[text])
    print("----------------------------")

# import pytz
# my_date = datetime.datetime.now(pytz.FixedOffset(60*3)) # (Israel) Every 1 is minute
# my_date = my_date.strftime("%d/%m/%Y %H:%M:%S")
# telegram_printer(my_date)
