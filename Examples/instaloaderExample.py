from datetime import datetime
from itertools import dropwhile, takewhile
from datetime import date, timedelta
import instaloader

print("Start")
L = instaloader.Instaloader()

# try: L.load_session_from_file("spider_modelsx")
# except (ValueError, Exception): L.login("spider_modelsx", "Idan05423")        # (login)

# for post in instaloader.Hashtag.from_name(L.context, 'cat').get_posts():
user = instaloader.Profile.from_username(L.context, "spider_modelsx").get_posts()
# for post in user:
#     L.download_post(post, target='stabilo')

forIndex = 1
for post in user:
    print(forIndex)
    if forIndex != 1: #S כל מה שלא..
        forIndex += 1
        continue # skip
    else:
        print(post.url)
        break
print("Done")

# posts = instaloader.Profile.from_username(L.context, "stabilo").get_posts()
# print(posts.count)
#
# SINCE = datetime(2020, 1, 1)
SINCE = date.today() - timedelta(days=1)
# UNTIL = datetime(2021, 1, 1)
UNTIL = date.today()
#
# for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
#     print("A")
#     print(post.date)
#     L.download_post(post, target="stabilo")
