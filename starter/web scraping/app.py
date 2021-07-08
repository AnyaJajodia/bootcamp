"""Web Scraping tutorial
"""
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


DEBUG = True

#
# *** Warning ***
# Following URL is only for demo purpose, do not use public site without their permission 
# as it may violate their terms of use.
# 
url = 'https://www.udemy.com/courses/development/'

# body > div.main-content-wrapper > div.main-content > div > div > div:nth-child(8) > div.course-directory--container--5ZPhr > div.filter-container--container--3A8k6 > div.course-list--container--3zXPS
# XPath
xpath = '/html/body/div[2]/div[3]/div/div/div[6]/div[2]/div[1]/div[2]/div/div[2]/div[2]'

# Selenium
DRIVER_PATH = '/Users/cloudwrk/Source/chromedriver'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('https://google.com')

# [Optional] Headless
options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(url)

time.sleep(5)

# if DEBUG:
#     print(driver.page_source)
try:
    # table = driver.find_element_by_xpath(xpath)
    # print(table)
    for element in driver.find_elements_by_class_name('popper--popper--19faV'):
        data = element.text.split('\n')
        if len(data) >= 9:
            for value in data:
                print(value)
            print('-----')

except NoSuchElementException:
    print('Error: No such element found!')

driver.quit()



## BeautifulSoup

# url = 'https://www.udemy.com/courses/development/'
# response = requests.get(url=url)

# soup = BeautifulSoup(response.content, 'html5lib')
# if DEBUG:
#     print(soup.prettify())



# table = soup.find('div', attrs = {'class':'main-content'})
# if DEBUG:
#     print(table.div)
