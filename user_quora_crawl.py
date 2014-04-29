from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime
import urllib2
import time
import os
import sys

#use webdriver to get login cookies
email=""
password=""

driver = webdriver.Chrome()
driver.get("http://www.quora.com")
elems = driver.find_elements_by_xpath("//form/div/div/input")
elems[0].send_keys(email)
elems[1].send_keys(password)
elems[2].send_keys(Keys.RETURN)

#wait 5 secs for entering email and password
cookies = driver.get_cookies()
opener = urllib2.build_opener()
for cookie in cookies:
	name = cookie['name']
	value=cookie['value']
	opener.addheaders.append(('Cookie', name+'='+value))
driver.close()


file_users_urls = open("user_url.txt", mode='r')
file_users_info = open("user_info.txt", mode='w')
users_urls = file_users_urls.read()
user_urls = users_urls.split('\n')

uid=0
#in this case
#user_url = 'http://www.quora.com/Jessica-Hui'

for user_url in user_urls:	

	fstream = opener.open(user_url+'/topics')
	soup = BeautifulSoup(fstream.read())

#file_html = open("user_topics_soup.html", mode = 'w')
#file_html.write((soup.prettify()).encode('utf-8'))

	user_name_soup = soup.find_all('a', class_="user")
	user_name = user_name_soup[0].get_text().encode('utf-8')
#print user_name
	user_wrapper = {}	
	topics=[]

	topics_soup = soup.find_all('a', class_="topic_name")
	for topic_soup in topics_soup:
		topic = topic_soup.get_text().encode('utf-8');
		topics.append(topic)
	uid+=1
	user_wrapper={'user_id':uid, 'user_name':user_name, 'user_topics':topics}

	print uid
	file_users_info.write(str(user_wrapper)+'\n')















