import telegram_send
from GlobalGadgets.TelegramPrinter import telegram_printer
from time import sleep
import datetime
import schedule
import sys

## Values
from GlobalGadgets.googleDrive import g_drive_upload

USERNAME = "spider3d_models"
PASSWORD = "Idan05423"
minutesPast_sinceLaunch = 0
postIndex = 0

def main():
    log = input("Enable log .txt (y/n)")
    if log == "y" or log == "Y":
        log = True
    else:
        log = False
    print(log)

    current_time = datetime.datetime.now().strftime("%d.%m.%Y %H.%M.%S")
    if log: sys.stdout = open(f"instaBotyy_log_{str(current_time)}.txt", "w", encoding='utf-8')

    try:
        print("Start main()")

        from Lib.I_CleanStart import clean_start
        ## 1. delete config folder & login
        bot = clean_start(USERNAME, PASSWORD)
        print(bot)


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
        post_code = upload_post(bot=bot,
                                photo_link=photo_link,
                                post_caption=post_caption,
                                page_username=page_username)  # for credit
        ## 4. Telegram update
        global postIndex
        postIndex += 1
        telegram_printer(
            f"https://www.instagram.com/p/{post_code}/\n{postIndex} post Already upload since launch ({int(minutesPast_sinceLaunch / 60)} hours ago)")
        telegram_printer(f"instaBotyy run on pythonAnywhere\n{current_time}")
    except:
        ## Export failure log to Gdrive & Send Telegram msg
        if log:
            sys.stdout.close()  # Close instaBotyy_log_{current_time}.txt
            sys.stdout = open("googleDriveLink.txt", "w", encoding='utf-8')

            # link = g_drive_upload(file2upload=f"instaBotyy_log_{str(current_time)}.txt")
            link = ""
            print(link)
            telegram_printer(f"""WOW. something went wrong throw this upload.\nLuck everything on try except (:
{current_time}

Log of failure main() session:
{link}""")
        else:
            telegram_printer(f"WOW. something went wrong throw this upload.\nLuck everything on try except (:")


        sys.stdout.close()  # Close SpiderSticker_log.txt

main()
schedule.every(60).to(90).minutes.do(main)
# schedule.every(2).hours.do(main)
# schedule.every(90).minutes.do(main)
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




