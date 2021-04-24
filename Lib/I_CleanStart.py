import os
import shutil
from instabot import Bot
from instaloader import instaloader

global bot, L
## 1. delete config folder & login
def clean_start(username, password, sample):
    global bot, L
    print("clean_start()")

    def clean_logs(): # Clean logs files instaBotyy_log_CURRENT_DATE.txt
        files_and_directories = os.listdir()
        # print(files_and_directories)
        for item in files_and_directories:
            if "instaBotyy_log" in item:
                os.remove(item)    
    try: clean_logs()
    except: print("No clean_logs()")

    # instabot package to upload posts
    def instabot_login():
        global bot, L
        try:
            # print("try!")
            shutil.rmtree('config')  # Delete config folder
            print(f"config folder has been deleted...")
            # printRed(f"config folder has been deleted...")
        except:
            print(f"config folder not found...")
            # printRed(f"config folder not found...")
        if sample:
            bot = "Sample bot configured!"
        else:  # On real upload.
            bot = Bot()
            bot.login(username=username, password=password)
            # bot.login(username="3deal.com_", password="3deal3252")
            print(f"Successfully logged in")
            # printYellow(f"Successfully logged in")
            return bot
    # bot = instabot_login()
    bot = "Sample bot configured!"
    
    def instaloader_login():
        global bot, L
        L = instaloader.Instaloader()
        # try: L.load_session_from_file("spider_modelsx")
        print("Login 3deal.com_ for post_generator....")
        L.login(user="3deal.com_", passwd="3deal3252")
        # L.login(user="spider3d_models", passwd="Idan05423")
        print("L.login() Done")
        return L
    L = instaloader_login()
    
    return bot, L
