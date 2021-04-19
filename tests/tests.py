import time
from selenium import webdriver

chromedriver = "C:\Program Files (x86)\chromedriver90.exe"

# option = webdriver.ChromeOptions()
# option.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# option.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

# from selenium.webdriver.support import ui


# global chrome_ver
options = webdriver.ChromeOptions()  # פיתחת כרום דרך משתמש רגיל
options.add_argument(f"user-data-dir=C:\\Users\\idanb\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\\chromedriver90.exe", options=options)

# options = webdriver.ChromeOptions()
# options.add_argument('--user-data-dir=./User_Data')
# driver = webdriver.Chrome(chromedriver, options=options)

whatsapp_url = "https://web.whatsapp.com"
driver.get(whatsapp_url)
print(driver.get_cookies())
time.sleep(30) # We are doing the manual QR code verification here
print(driver.get_cookies())