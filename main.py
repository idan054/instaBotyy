import datetime
import os
import shutil
import urllib.request
from time import sleep
import schedule
from GlobalGadgets.InUse.JobsSchedule import schedule_job
from color_printer import *

## 0 configure Instagram pages , day & time to post
from GlobalGadgets.InUse.get_random_post import post_generator
from GlobalGadgets.InUse.myPostUploader import my_post_uploader

pages4Posts = ["printedbyprusa", "josefprusa", "3dimensionprint", "matterhackers", "cults3d", "creality3d",
               "e3donline", "mosaicpalette", "italy3dprint", "fillamentum", "crazyfilament", "filaments.ca",
               "filamentarno" ,"simplify3d", "miniworld3d", "zimple3d", "all3dp", "esun3dprinting",
               "lc_design_modena", "davidzindustries", "hugo_hth", "the.artgallery__"]

days2post = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]


# def next_minute():
#     nxt_minute = datetime.datetime.now() + datetime.timedelta(minutes=1)
#     nxt_minute = nxt_minute.strftime("%H:%M")
#     # print(nxt_minute.strftime("%d/%m/%Y %H:%M:%S"))
#     print("nxt_minute: ", nxt_minute)
#     return nxt_minute

# time2post = next_minute()
time2post = ["01:00", "02:00", "03:00",
             # "04:00", "05:00", "06:00",
             # "07:00", "08:00", "09:00",
             # "10:00", "11:00", "12:00",
             # "13:00", "14:00", "15:00",
             # "16:00", "17:00", "18:00",
             "20:00", "20:05", "20:10i",
             "19:40", "23:00", "23:59"]

# region On time:

from instabot import Bot
def main():
    ## 0. delete config folder to login
    def clean_start():
        print("clean_start()")
        try:
            shutil.rmtree('config')  # Delete config folder
            printRed(f"config folder has been deleted...")
        except:
            printRed(f"config folder not found...")

        bot = Bot()
        bot.login(username="spider_modelsx", password="Idan05423")
        print(f"{bcolors.Yellow}{bcolors.BOLD}Successfully logged in{bcolors.Normal}")
        return bot
    bot = clean_start()

    ## 1 Scrape random post from page
    # from the 5 - 50 last posts.
    post_data = post_generator(pages4Posts)
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

    def upload_now():
        try:
            print('Delete "LastedPhoto.jpg.REMOVE_ME"')
            os.remove('LastedPhoto.jpg.REMOVE_ME')
        except:
            print('Error Delete "LastedPhoto.jpg.REMOVE_ME"')

        urllib.request.urlretrieve(f"{photo_link}", "LastedPhoto.jpg")

        bot.upload_photo("LastedPhoto.jpg",
                         caption=f"""{post_caption}
                                     post credit: @{page_username}""")
    upload_now()

main()
print("Done main() 1st")
sleep(5)
print("Slept 5 sec...")
sleep(5)
print("Slept 10 sec...")
print("Start main() 2st")
main()
print("Done main() 2st")



# for hour in time2post:
#     schedule_job(someDay="sunday",
#                  someTime=hour,
#                  someDef=main)

# endregion On time:

# whileIndex = 0
# while True:
    # looking for pending
    # schedule.run_pending()
    # sleep(30)
    # whileIndex += 1
    # print(f"{whileIndex} Still alive...",  datetime.datetime.now().strftime("%H:%M.%S"))



