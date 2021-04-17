from instabot import Bot



bot = Bot()
bot.login(username="3deal.com_", password="3deal3252")
bot.upload_photo("lol.jpg", caption="caption_for_photo")

# from instapy_cli import client
#
# username = "3deal.com_"
# password = "3deal3252"
# image = 'lol.png'
# text = 'Flask for Python' + '\r\n' + '#glitch #python #gif https://pythonprogramming.altervista.org/publish-app-or-blog-with-glitch-com-and-python-in-no-time/'
# with client(username, password) as cli:
#     cli.upload(image, text)
