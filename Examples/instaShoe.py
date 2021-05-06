## This func gives contact data of profiles based other profiles

from datetime import datetime
from itertools import dropwhile, takewhile
from datetime import date, timedelta
import instaloader

print("Start")
L = instaloader.Instaloader()

try:
    L.load_session_from_file("3deal.com_")
    print("Session Succeed")
except:
    # L.login(user="3deal.com_", passwd="3deal3252")
    L.login(user="sycho_shoes.il", passwd="shoes325245")
    print("L.login() Done")

# for post in instaloader.Hashtag.from_name(L.context, 'cat').get_posts():
user = instaloader.Profile.from_username(L.context, "nike").get_similar_accounts()

# matched_users = {
#     "spider_modelsx"  : {
#         "followers" : 90,
#         "external_link" : "https://spider3d.co.il",
#         "insta_link" : "https://instagram.com/spider_modelsx"
#     }
# }

matched_users = {}
print(len(matched_users))
forIndex = 0
# while len(matched_users) != 1:
for current_user in user:
    print(current_user)
    print(current_user.username)
    if forIndex / 10 == forIndex // 10: # Divide exactly
        print(forIndex)
        print(len(matched_users), "found")
        print(matched_users)
        print("------------------------")

    username = current_user.username
    print(username)
    followers = current_user.followers
    print(followers)
    external_url = current_user.external_url
    print(external_url)

    if followers > 3000 and external_url is not None:
        matched_users.update({
        username : {
        "followers" : followers,
        "external_link" : external_url,
        "insta_link" : f"https://instagram.com/{username}"
            }
        })
    forIndex += 1

    if len(matched_users) == 10:
        print(len(matched_users), "found")
        print(matched_users)
        break
    elif forIndex == 50:
        print("forIndex is already", forIndex)
        print(len(matched_users), "found")
        print(matched_users)
        break


# print()
# print(matched_users)

# for u in user:
#     print(forIndex)
#     print(u.username)
#     print(u.external_url)
#     print(u.followers)
#     # forIndex += 1
#     break