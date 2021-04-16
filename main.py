import datetime
import os
import shutil
import urllib.request
from random import randint
from time import sleep
import schedule
# from color_printer import *
# region color_printer

class bcolors:
    Normal = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    White = '\033[97m'
    Purple = '\033[95m'
    Blue = '\033[94m'
    Yellow = '\033[93m'
    Green = '\033[92m'
    Red = '\033[91m'
    Grey = '\033[90m'
# print(f'{bcolors.Green}User "{bcolors.BOLD}Arik{bcolors.Normal}{bcolors.Green}" Added!{bcolors.Normal}')

def printPurple(text):
    """
    Parameters
    ----------
    text : str
        the text value from user
    """
    print(f"{bcolors.Purple}{text}{bcolors.Normal}")

def printBlue(text):
    """
    Parameters
    ----------
    text : str
        the text value from user
    """
    print(f"{bcolors.Blue}{text}{bcolors.Normal}")

def printYellow(text):
    """
    Parameters
    ----------
    text : str
        the text value from user
    """
    print(f"{bcolors.Yellow}{text}{bcolors.Normal}")

def printGreen(text):
    """
    Parameters
    ----------
    text : str
        the text value from user
    """
    print(f"{bcolors.Green}{text}{bcolors.Normal}")

def printRed(text):
    """
    Parameters
    ----------
    text : str
        the text value from user
    """
    print(f"{bcolors.Red}{text}{bcolors.Normal}")

def printGrey(text):
    """
    Parameters
    ----------
    text : str
        the text value from user
    """
    print(f"{bcolors.Grey}{text}{bcolors.Normal}")

def printBold(text):
    """
    Parameters
    ----------
    text : str
        the text value from user
    """
    print(f"{bcolors.BOLD}{text}{bcolors.Normal}")

def printUnderline(text):
    """
    Parameters
    ----------
    text : str
        the text value from user
    """
    print(f"{bcolors.UNDERLINE}{text}{bcolors.Normal}")


# delete dist folder
# run py setup.py sdist

# endregion color_printer

## 0 configure Instagram pages , day & time to post
from instaloader import instaloader

pages4Posts = ["printedbyprusa", "josefprusa", "3dimensionprint", "matterhackers", "cults3d", "creality3d",
               "e3donline", "mosaicpalette", "italy3dprint", "fillamentum", "crazyfilament", "filaments.ca",
               "filamentarno" ,"simplify3d", "miniworld3d", "zimple3d", "all3dp", "esun3dprinting",
               "lc_design_modena", "davidzindustries", "hugo_hth"]

# days2post = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

# def next_minute():
#     nxt_minute = datetime.datetime.now() + datetime.timedelta(minutes=1)
#     nxt_minute = nxt_minute.strftime("%H:%M")
#     # print(nxt_minute.strftime("%d/%m/%Y %H:%M:%S"))
#     print("nxt_minute: ", nxt_minute)
#     return nxt_minute

# time2post = next_minute()


from instabot import Bot


## 0. delete config folder to login
def clean_start():
    print("clean_start()")
    try:
        # print("try!")
        shutil.rmtree('config')  # Delete config folder
        print(f"config folder has been deleted...")
        # printRed(f"config folder has been deleted...")
    except:
        print(f"config folder not found...")
        # printRed(f"config folder not found...")

    _bot = Bot()
    # _bot.login(username="3deal.com_", password="Idan05423")
    _bot.login(username="spider_modelsx", password="Idan05423")
    print(f"Successfully logged in")
    # printYellow(f"Successfully logged in")
    return _bot

bot = clean_start()

def main():
    printYellow("Start main()")
    print(bot)

    ## 1 Scrape random post from page
    # from the 5 - 50 last posts.
    def post_generator(pages_list):
        print("get_rand_post()")

        pages_list_len = len(pages_list)
        # print("pages_list_len: ", pages_list_len)
        the_chosen_page = randint(0, pages_list_len - 1)
        # print("the_chosen_page: ", the_chosen_page)

        L = instaloader.Instaloader()

        # try: L.load_session_from_file("spider_modelsx")
        # except (ValueError, Exception): L.login("spider_modelsx", "Idan05423")        # (login)

        # for post in instaloader.Hashtag.from_name(L.context, 'cat').get_posts():
        user = instaloader.Profile.from_username(L.context, pages_list[the_chosen_page]).get_posts()

        forIndex = 0
        the_chosen_post = randint(0, 49)
        print("the_chosen_post: ", the_chosen_post)
        for post in user:
            forIndex += 1
            # print(forIndex)
            if forIndex != the_chosen_post:  # (When...)
                pass
            else:
                print(post.url)
                # region post prints
                # print("post.get_is_videos()")
                # print(post.get_is_videos())
                # print("post.video_url")
                # print(post.video_url)
                # print("X___X___X___X___X___X___X___X___")
                # print("post.shortcode")
                # print(post.shortcode)
                # print("My link 2 Post")
                # print(f"https://www.instagram.com/p/{post.shortcode}/")
                # print("post.mediacount")
                # print(post.mediacount)
                # print("post.mediaid")
                # print(post.mediaid)
                ## print(post.mediaid_to_shortcode())
                ## print(post.shortcode_to_mediaid())
                # print("X___X___X___X___X___X___X___X___")
                # print("post.owner_username")
                # print(post.owner_username)
                # print("post.title")
                # print(post.title)
                # print("post.url")
                # print(post.url)
                # print("post.caption_hashtags")
                # print(post.caption_hashtags)
                # print("post.caption_mentions")
                # print(post.caption_mentions)
                # print("X___X___X___X___X___X___X___X___")
                # print("post.caption")
                # print(post.caption)
                # endregion post prints
                return post.owner_username, \
                       post.shortcode, \
                       f"https://www.instagram.com/p/{post.shortcode}/", \
                       post.url, \
                       post.get_is_videos(), \
                       post.video_url, \
                       post.mediacount, \
                       post.mediaid, \
                       post.caption_hashtags, \
                       post.caption_mentions, \
                       post.caption
        #     L.download_post(post, target='stabilo')
        # print(forIndex)
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
# main()
# schedule.every(2).hours.do(main)
# schedule.every(90).minutes.do(main)
schedule.every(60).to(90).minutes.do(main)
# schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

whileIndex = 0
while True:
    # looking for pending
    schedule.run_pending()
    sleep(60)
    whileIndex += 1
    print(f"{whileIndex} minutes past. Still alive...",  datetime.datetime.now().strftime("%H:%M.%S"))
    printYellow(f"{int(whileIndex / 30 + 1)} Posts already uploaded!")



