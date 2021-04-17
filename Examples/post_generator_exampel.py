from random import randint
import instaloader


def post_generator(pages_list):
    print("get_rand_post()")

    pages_list_len = len(pages_list)
    # print("pages_list_len: ", pages_list_len)
    the_chosen_page = randint(0, pages_list_len-1)
    # print("the_chosen_page: ", the_chosen_page)

    L = instaloader.Instaloader()

    # try: L.load_session_from_file("spider_modelsx")

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
                   post.shortcode,\
                   f"https://www.instagram.com/p/{post.shortcode}/", \
                   post.url, \
                   post.get_is_videos(),\
                   post.video_url, \
                   post.mediacount,\
                   post.mediaid, \
                   post.caption_hashtags, \
                   post.caption_mentions, \
                   post.caption
    #     L.download_post(post, target='stabilo')
    # print(forIndex)

# pages4Posts = ["printedbyprusa", "josefprusa", "3dimensionprint", "matterhackers", "cults3d", "creality3d",
#                "e3donline", "mosaicpalette", "italy3dprint", "fillamentum", "crazyfilament", "filaments.ca",
#                "filamentarno" ,"simplify3d", "miniworld3d", "zimple3d", "all3dp", "esun3dprinting",
#                "lc_design_modena", "davidzindustries", "hugo_hth", "the.artgallery__"]
# post_data = get_rand_post(pages4Posts)
# print(post_data)