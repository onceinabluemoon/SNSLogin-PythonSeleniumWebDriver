from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://www.facebook.com")
time.sleep(5)


# xpaths: //*[@id="email"]  & //*[@id="pass"]
email = browser.find_element_by_xpath('//*[@id="email"]')
password = browser.find_element_by_xpath('//*[@id="pass"]')


email.send_keys("")         # You have to add e-mail or phone number
password.send_keys("")      # add your password              
time.sleep(3)


login = browser.find_element_by_id('loginbutton')
login.click()

time.sleep(1)

browser.close()
