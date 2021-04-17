#1. go to this adress: https://telegram.me/BotFather and follow the instructions
#2. in terminal: pip install telegram-send followed by telegram-send configure
import datetime
from time import sleep
import telegram_send

def telegram_printer(text):
    print("----------------------------")
    print("Also availble on Telegram:")
    print(text)
    telegram_send.send(messages=[text])
    print("----------------------------")


while True:
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    telegram_printer(f"Amazon AWS Ubuntu20 A Still Alive\n{current_time}")
    sleep(60)

