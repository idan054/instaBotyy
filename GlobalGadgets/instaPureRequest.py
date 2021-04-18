import re
import requests
import urllib.request
from datetime import datetime

link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

login = '3deal.com_'
password = '3deal3252'

time = int(datetime.now().timestamp())
print(time)
payload = {
    'username': login,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
    'queryParams': {},
    'optIntoOneTap': 'false'
}

with requests.Session() as s:
    r = s.get(link)
    # a = r.cookies['csrftoken']
    a = r.cookies.keys()
    print(a)
    print(r.cookies)
    print(a)
    csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
    print(csrf)

    r = s.post(login_url, data=payload, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    })
    print(r.status_code)
    print(r.url)
    print(r.text)
    print(s.cookies)
    r = s.get('https://www.instagram.com/accounts/edit/')
    print(login in r.text)


    microtime = int(datetime.now().timestamp())
    headers =  {
        "content-type": "image / jpg",
        "X-Entity-Name" : f"fb_uploader_{microtime}",
        "Offset": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "x-entity-length": "299255",
        "X-Instagram-Rupload-Params": f'{{"media_type": 1, "upload_id": {microtime}, "upload_media_height": 1080, "upload_media_width": 1080}}',
        "x-csrftoken": csrf,
        "x-ig-app-id": "1217981644879628"
    }

    img = urllib.request.urlopen('https://sun9-64.userapi.com/RVgUHSq9fXrDr8YBJ4a4h9xwN4EQA_8BXuQ5Vg/Mdx3LwawEmY.jpg')
    photo = img.read()
    r = s.post(f'https://www.instagram.com/rupload_igphoto/fb_uploader_{microtime}', data=open("4.jpg", "rb"), headers=headers)
    print(r.text)
    headers = {
        'Content-Length': '104',
        'content-type': 'application/x-www-form-urlencoded',
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/create/details/",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "x-csrftoken": csrf,
        "x-ig-app-id": "1217981644879628",
        "X-Requested-With": "XMLHttpRequest"
    }

    body = {
        'upload_id': f'{microtime}',
        "caption":'text for caption',
        'usertags':'',
        'custom_accessibility_caption': '',
        'retry_timeout':''
    }
    r = s.post('https://www.instagram.com/create/configure/', data=body, headers=headers)
    print(r.status_code)
    print(r.text)