#!/usr/local/bin/python

import os
os.system('pip install -r requirements.txt')

from selenium import webdriver
from bs4 import BeautifulSoup
import re

#receive input from user through command line
input = input("Please input designated tag: ")

#check if OS is Mac/Windows
if (os.name == 'nt'):
    dir = os.getcwd() + '/ChromeDriver/chromedriver.exe'
elif (os.name == 'posix'):
    dir = os.getcwd() + '/ChromeDriver/chromedriver'

#setup chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
driver = webdriver.Chrome(executable_path= dir, chrome_options = chrome_options)

#enter tags page based on user's inpur
driver.get('https://www.instagram.com/explore/tags/' + input + '/')

#scrape top 3 posts based on tag
bs = BeautifulSoup(driver.page_source, 'lxml')
posts = bs.findAll('div', {'class': 'v1Nh3 kIKUG _bz0w'})
posts = posts[:3]

if not posts:
    print("Couldn\'t find the posts, please input different tag.")
else:
    print("Found posts . . .")

f = open("results.txt", "w+")
f.write("Hashtags of Top 3 Posts with #" + input + " :\n")


for post in posts:

    #scrape caption for each post
    a = post.find('a')
    driver2 = webdriver.Chrome(executable_path= dir, chrome_options = chrome_options)
    driver2.get('https://www.instagram.com' + str(a.get('href')))
    bs2 = BeautifulSoup(driver2.page_source, 'lxml')
    list = bs2.findAll('div', {'class': 'C4VMK'})
    caption = list[0].text

    #extract hashtags using Regex
    string = caption.lower()
    x = re.findall("#[^\s\u005B-\u0060\u0021-\u002F\u003A-\u0040\u00A1-\u00BC\u3000-\u301F\uFF00-\uFFEF\u2000-\u25FF\u27C0-\u2BFF]+", string)
    #print(x)

    #write all hashtags to file
    f.write("\n".join(x))
    f.write("\n")

#outputs to a file upon success
f.close()
print('RESULTS WRITTEN TO FILE')
