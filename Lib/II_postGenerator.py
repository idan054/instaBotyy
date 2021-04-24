from instaloader import instaloader
from random import randint
from time import sleep


## 2. Scrape random post from USERNAME
# the 5 - 50 last posts.

# L = instaloader.Instaloader()
# try: L.load_session_from_file("spider_modelsx")
# print("Login 3deal.com_ for post_generator....")
# L.login(user="3deal.com_", passwd="3deal3252")
# L.login(user="spider3d_models", passwd="Idan05423")
# print("L.login() Done")
from Lib.I_CleanStart import clean_start

# main_user = Who to get pages he follow list. (AKA USERNAME)
def post_generator(_L, main_user): # Get list of all the pages this user follow on

    print("Start post_generator()")

    pages_data = instaloader.Profile.from_username(_L.context, main_user).get_followees()
    pages_list = []
    for page in pages_data:
        pages_list.append(page.username)

    # print(f' pages list from "following" {username}:')
    # print(pages_list)

    pages_list_len = len(pages_list)
    print("pages_list_len: ", pages_list_len)

    the_chosen_page = randint(1, pages_list_len - 1)
    print("the_chosen_page: ", the_chosen_page)

    overall_post_option = pages_list_len * 50
    print("overall_post_options:", overall_post_option)

    # for post in instaloader.Hashtag.from_name(L.context, 'cat').get_posts():
    user = instaloader.Profile.from_username(_L.context, pages_list[the_chosen_page]).get_posts()

    forIndex = 0
    the_chosen_post = randint(2, 49)
    print("the_chosen_post: ", the_chosen_post)

    for post in user:
        forIndex += 1
        # print(forIndex)
        if forIndex != the_chosen_post:  # (When...)
            pass
        else:
            print(f"@{post.owner_username}")
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


## Example
# bot, L = clean_start(username = "DoesntMatter",
#             password = "DoesntMatter",
#             sample = False
#             )
# post_generator(_L=L, main_user = "spider3d_models")
# print("Done generate nike")
# sleep(3)
# post_generator(_L=L, main_user = "spider3d_models")
# print("Done generate adidas")
