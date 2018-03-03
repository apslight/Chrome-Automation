# Author : Aditya Pratap SIngh
# mailto : aps11@iitbbs.ac.in


import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

emailto = raw_input('Email_to: ')
usernameStr = raw_input('Email: ')
passwordStr = getpass.getpass()

browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier'))

username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

password = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.NAME, 'password')))
password.send_keys(passwordStr)

signInButton = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.ID, 'passwordNext')))
signInButton.click()
 
compose = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, ':gd')))
compose.click()

toEmail = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, ':n0')))
toEmail.send_keys(emailto)
