import telegram_send
from GlobalGadgets.TelegramPrinter import telegram_printer
from time import sleep
import datetime
import schedule
import sys
import pytz

## Values
# from GlobalGadgets.googleDrive import g_drive_upload

USERNAME = "spider3d_models"
PASSWORD = "Idan05423"
minutesPast_sinceLaunch = 0
postIndex = 0

isSample = input("ATTENTION! Make a sample run? (y/n)") or "y"
if isSample == "y" or isSample == "Y":  # "or True" 2 save next runs
    isSample = True  # Change the True to False
    print("isSample run:", isSample)  # Because its else then y / Y...
    print("Start Testing mode!")
else:
    isSample = False
    print("Real LIVE Mode Enabled!")

from Lib.I_CleanStart import clean_start
## 0. delete config folder & login
# Only one time bot config
bot = clean_start(USERNAME, PASSWORD, isSample)  # True / False for is sample upload only? (No insta login)

def main():
    global isSample
    # print(isSample)
    # start_time = datetime.datetime.now()
    # start_time = datetime.datetime.now().strftime("%d.%m.%Y %H.%M.%S")
    start_time = datetime.datetime.now(pytz.FixedOffset(60 * 3))  # (Israel) Every 1 is minute
    start_time = start_time.strftime("%d/%m/%Y %H:%M:%S")
    print(start_time)

    try:
        print("Start main()")
        global bot
        print(bot) # When sample: bot = "Sample bot configured!"

        from Lib.II_postGenerator import post_generator
        post_data = post_generator(USERNAME)  # Get list of all the pages this user follow on
        ## 2. Mapped post data
        # print(post_data)
        # region map scrape
        page_username = post_data[0]
        shortcode = post_data[1]
        original_link = post_data[2]
        photo_link = post_data[3]
        is_videos = post_data[4]
        video_link = post_data[5]
        media_counter = post_data[6]
        media_id = post_data[7]
        caption_hashtags = post_data[8]
        caption_mentions = post_data[9]
        post_caption = post_data[10]
        # endregion map scrape

        from Lib.III_UploadPost import upload_post
        ## 3. Delete REMOVE_ME & Upload the chosen post
        post_code = upload_post(sample=isSample,
                                bot=bot,
                                photo_link=photo_link,
                                post_caption=post_caption,
                                page_username=page_username)  # for credit
        ## 4. Telegram update
        global postIndex
        postIndex += 1
        telegram_printer(
            f"https://www.instagram.com/p/{post_code}/\n{postIndex} post Already upload since launch ({int(minutesPast_sinceLaunch / 60)} hours ago)")
        if isSample:
            telegram_printer(f"SAMPLE MODE instaBotyy run on pythonAnywhere\n{start_time}")
        else:
            telegram_printer(f"instaBotyy run on pythonAnywhere\n{start_time}")
    except:
        ## Export failure log to Gdrive & Send Telegram msg
        telegram_printer(f"WOW. something went wrong on this upload...")

main()

if isSample:
    print(isSample)
    print("Sleep 4 2 sec")
    sleep(2)
    main()
    print("Done. (exit)")

else:
    print(isSample)
    schedule.every(60).to(90).minutes.do(main)


    # schedule.every(10).seconds.do(main) # Execution every 60 sec
    # schedule.every(2).hours.do(main)
    # schedule.every(10).seconds.do(job)
    # schedule.every(10).minutes.do(job)
    # schedule.every().hour.do(job)
    # schedule.every().day.at("10:30").do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
    # schedule.every().minute.at(":17").do(job)

    while True:
        # looking for pending
        schedule.run_pending()
        sleep(60)
        minutesPast_sinceLaunch += 1

        if minutesPast_sinceLaunch % 10 == 0 : # returns true ONLY if X is an exact multiple of Y (30/10 = True | 3/10 = False)
            print(f"{minutesPast_sinceLaunch} minutes past. Still alive...", datetime.datetime.now().strftime("%H:%M.%S"))
            # printYellow(f"{int(whileIndex / 30 + 1)} Posts already uploaded!")
            print(f"{int(postIndex + 1)} Posts already uploaded!")




