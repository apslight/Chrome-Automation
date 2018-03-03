# Author : Aditya Pratap SIngh
# mailto : aps11@iitbbs.ac.in

import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

roll = raw_input("Your username :")
password = getpass.getpass()

chrome = webdriver.Chrome()
chrome.set_window_position(0, 0)
chrome.get("http://webapps.iitbbs.ac.in/rerp/")
rl = chrome.find_element_by_name("email")
pw = chrome.find_element_by_name("password")
rl.send_keys(roll)
pw.send_keys(password)
pw.send_keys(Keys.RETURN)
chrome.find_element_by_xpath('//*[@id="nav-menu-item-9729"]/a/span[1]').click()


for i in range(2, 12):
       try:
           subject = chrome.find_element_by_xpath('//*[@id="content"]/div/div/table/tbody/tr['+ str(i) +']/td[2]')
           marks = chrome.find_element_by_xpath('//*[@id="content"]/div/div/table/tbody/tr['+ str(i) +']/td[5]')
           con = chrome.find_element_by_xpath('//*[@id="content"]/div/div/table/tbody/tr['+ str(i) +']/td[3]')
           att = chrome.find_element_by_xpath('//*[@id="content"]/div/div/table/tbody/tr['+ str(i) +']/td[4]')
           print '\n'+ subject.text +' has ' + att.text + '/'+ con.text +' Percentage '+marks.text
       except:
           pass
chrome.quit()
