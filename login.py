from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import sys




def login():
    email="YOUREMAILADDRESS"
    password = "YOUPASSWORD"
	
    driver = webdriver.Chrome()
    driver.get("http://www.quora.com")
	html_source= browser.page_source
	soup = BeautifulSoup(html_source)

	file_html = open("login.txt", mode = 'w')
	file_html.write((soup.prettify()).encode('utf-8'))

    elems = driver.find_elements_by_xpath("//form/div/div/input")

    try:
        elems[0].send_keys(email)
        elems[1].send_keys(password)
        elems[2].send_keys(Keys.RETURN)
    except Exception as exe:
        print "Login failed: ",exe
        return None,False
    else:
        print "Logged in successfully"
        return driver,True

driver,received = login()
if received:
    json_object = driver.page_source
    #print json_object
	

   
