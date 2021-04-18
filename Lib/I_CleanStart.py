import os
import shutil
from instabot import Bot

## 1. delete config folder & login
def clean_start(username, password, sample):
    print("clean_start()")

    def clean_logs(): # Clean logs files instaBotyy_log_CURRENT_DATE.txt
        files_and_directories = os.listdir()
        # print(files_and_directories)
        for item in files_and_directories:
            if "instaBotyy_log" in item:
                os.remove(item)
    try:
        clean_logs()
    except:
        print("No clean_logs()")

    try:
        # print("try!")
        shutil.rmtree('config')  # Delete config folder
        print(f"config folder has been deleted...")
        # printRed(f"config folder has been deleted...")
    except:
        print(f"config folder not found...")
        # printRed(f"config folder not found...")
        if sample:
            _bot = "Sample bot configured!"
        else:  # On real upload.
            _bot = Bot()
            _bot.login(username=username, password=password)
            # _bot.login(username="3deal.com_", password="3deal3252")
            print(f"Successfully logged in")
            # printYellow(f"Successfully logged in")

    return _bot