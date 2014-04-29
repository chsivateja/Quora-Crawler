
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import time
import os
import sys
import glob




file_questions_url = open("list_topic_question.txt", mode='r')
questions_url = file_questions_url.read()
file_questions_url.close()

file_result = open("result_1.txt", mode = 'w')

question_url_array = questions_url.split('\n')


for i in range(0, len(question_url_array)):
	url = question_url_array[i]
	chromedriver = "chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	browser = webdriver.Chrome(chromedriver)

	browser.get(url)

	html_source= browser.page_source
	soup = BeautifulSoup(html_source)

	file_html = open("question_soup.txt", mode = 'w')
	file_html.write((soup.prettify()).encode('utf-8'))

	tags_soup = soup.find_all('a', class_="topic_name") 

	tag_array = []

	for tag_soup in tags_soup:
		tag = tag_soup.get_text()
		#print tag
		tag_array.append(tag.encode('utf-8'))
	print tag_array

	question_context_soup = soup.find_all('h1')
	question = (question_context_soup[0].get_text()).encode('utf-8')
	print question

	answer_num_soup = soup.find_all('div', class_="e_col w4_5 answer_header_text")
	if answer_num_soup != []:
		answer_num_str = answer_num_soup[0].get_text()
		answer_num = (answer_num_str.split(" "))[0]
	else:
		answer_num = "0"
	print answer_num

	browser.close()

################ get user who asked the question and when
##################
	chromedriver = "chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	browser = webdriver.Chrome(chromedriver)
 
	url_log = url+"\log"

	browser.get(url_log)

	html_source= browser.page_source
	soup_log = BeautifulSoup(html_source)

	file_html = open("question_soup_log.txt", mode = 'w')
	file_html.write((soup_log.prettify()).encode('utf-8'))



	users_wrapper_soup = soup_log.find_all("div", class_="pagedlist_item")
	user_wrapper = users_wrapper_soup[len(users_wrapper_soup)-1]

	user_soup = user_wrapper.find_all("a", class_="user")
	if user_soup !=[]:
		user = user_soup[0].get_text()
	else:
		user = "Anonymous user"
	print user

	datetime_soup = user_wrapper.find_all("span", class_="datetime")
	datetime = datetime_soup[0].get_text()
	print datetime
	
	browser.close()
	user_info = {"id":count,"tag":tag_array,"question":question,"answer_num":answer_num.encode('utf-8'),"user":user.encode('utf-8'), "datetime":datetime.encode('utf-8') }
	count+=1

	#print user_info
	file_result.write(str(user_info)+'\n')




