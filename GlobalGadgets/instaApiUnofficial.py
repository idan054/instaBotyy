
photo_path = '../LastedPhoto.jpg'
caption = "Sample caption"
from instapy_cli import client

username = '3deal.com_' #your username
password = '3deal3252' #your password
text = 'Here you can put your caption for the post' + '\r\n' + 'you can also put your hashtags #pythondeveloper #webdeveloper'

with client(username, password) as cli:
    cli.upload(photo_path, text)

