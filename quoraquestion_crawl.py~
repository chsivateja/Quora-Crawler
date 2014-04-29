
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime
import urllib2
import time
import os
import sys

#use webdriver to get login cookies
email="sjtudyyjk@126.com"
password="13593006626yjk"

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


file_question_list = open("list_topic_question.txt", mode='r')
file_result_list = open("result.txt", mode = 'w')
file_answer_user_url = open("user_url.txt", mode = 'w')
file_questions = file_question_list.read()
file_question_list.close()
question_urls = file_questions.split('\n')


#in this case 

questions_wrapper = []
qid = 0
#question wrapper in format {qid, tags, question, question_user, datetime, answer_num, answers}
#answers in format {answer_user, answer_context, upvote}

 
#question_url = 'http://www.quora.com/Where-in-SF-Chinatown-can-I-get-dim-sum-to-go'

for i in range(0,len(question_urls)-1):
	question_url = question_urls[i]
	fstream = opener.open(question_url)
	fstream_log = opener.open(question_url+'/log')

	soup = BeautifulSoup(fstream.read())
	soup_log = BeautifulSoup(fstream_log.read())

#just to find element, delete then
#file_html = open("question_soup.txt", mode = 'w')
#file_html.write((soup.prettify()).encode('utf-8'))

#file_html_log = open("question_log_soup.txt", mode = 'w')
#file_html_log.write((soup_log.prettify()).encode('utf-8'))
##############################

	tags_soup = soup.find_all('a', class_="topic_name")
	tags=[]
	for tag_soup in tags_soup:
		tag = tag_soup.get_text()
		tag = (tag.strip()).encode("utf-8")
		tags.append(tag)
#print tags

	question_soup = soup.find_all('h1')
	question = question_soup[0].get_text()
	question = (question.strip()).encode("utf-8")
#print question

	answer_num_soup = soup.find_all('div', class_="e_col w4_5 answer_header_text")
	if answer_num_soup!=[]:
		answer_num_str = answer_num_soup[0].get_text()
		answer_num = int(answer_num_str.split(" ")[0])
	else:
		answer_num = 0
#print answer_num

	answer_wrappers_soup = soup.find_all('div', class_="pagedlist_item")

	answer_wrappers = []

	for i in range(0, len(answer_wrappers_soup)-1):
		answer_user_soup = answer_wrappers_soup[i].find_all('a', class_="user")
		if answer_user_soup!=[]:
			answer_user = (answer_user_soup[0]).get_text()
			###TODO:           
			###crawl  answer_user_href
			answer_user_href = answer_user_soup[0]['href'].encode('utf-8')
			answer_user_url = 'https://www.quora.com'+answer_user_href
			file_answer_user_url.write(str(answer_user_url)+'\n')
			print answer_user_href;
			######
			answer_user = (answer_user.strip()).encode("utf-8")
		else:
			answer_user = "Anonymous User"
	#print answer_user
	
		answer_upvote_soup = answer_wrappers_soup[i].find_all('a', class_="vote_item_link add_upvote")
		if answer_upvote_soup!=[]:
			upvote_count_soup = answer_upvote_soup[0].find_all('span', class_="count")
			if upvote_count_soup!=[]:
				upvote_count = int(upvote_count_soup[0].get_text())
		else:
			upvote_count = 0
	#print upvote_count
	
		answer_context_soup = answer_wrappers_soup[i].find_all('div', class_="answer_content")
		if answer_context_soup!=[]:
			answer_context = (answer_context_soup[0]).get_text()
			answer_context = (answer_context.strip()).encode("utf-8")
		else:
			answer_context = "null"
	#print answer_context
		answer_wrapper = {"answer_user":answer_user, "upvote":upvote_count, "answer":answer_context}
		answer_wrappers.append(answer_wrapper)

#print answer_wrappers

	log_pagedlist_soup = soup_log.find_all('div', class_="pagedlist_item")
	question_log_soup = log_pagedlist_soup[len(log_pagedlist_soup)-1]
	question_user_soup = question_log_soup.find_all('a', class_="user")
	if question_user_soup!=[]:
		question_user = question_user_soup[0].get_text()
		question_user = (question_user.strip()).encode("utf-8")
	else:
		question_user = "Anonymous User"
#print question_user
	datetime_soup = question_log_soup.find_all('span', class_="datetime")
	date_time = datetime_soup[0].get_text()
	date_time = (date_time.strip()).encode('utf-8')
	date_time = date_time[:21]
	date_time = datetime.strptime(date_time, '%b %d, %Y  %I:%M %p')

#print date_time
	qid+=1	

	question_wrapper={'qid':qid, 'tag':tags, 'question':question, 'question_user':question_user, 'datetime':date_time, 'ans_num':answer_num, 'answers': answer_wrappers}
	print qid
	file_result_list.write(str(question_wrapper)+'\n')
	























