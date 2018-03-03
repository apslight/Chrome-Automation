# Author : Aditya Pratap SIngh
# mailto : aps11@iitbbs.ac.in


import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mobileStr = raw_input('Email: ')
passwordStr = getpass.getpass()
tomobile = raw_input('To_mobile')
totext = raw_input('To_Text')

browser = webdriver.Chrome()
browser.get(('http://site24.way2sms.com/content/index.html?'))

username = browser.find_element_by_id('username')
username.send_keys(mobileStr)

password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

nextButton = browser.find_element_by_id('loginBTN')
nextButton.click()

sendsms = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.ID, 'sendSMS')))
sendsms.click()

browser.switch_to_frame(browser.find_element_by_id("frame"))

mobiletext = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'mobile')))
mobiletext.send_keys(tomobile)

text = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID,'message')))
text.send_keys(totext)

bhejosms = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.ID, 'Send')))
bhejosms.click()


browser.quit()





