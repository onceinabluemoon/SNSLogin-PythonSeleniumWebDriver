from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://www.instagram.com")
time.sleep(2)

main_login = browser.find_element_by_xpath("//*[contains(@href, '/accounts/login')]")
main_login.click()
time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("")  # You have to add username
password.send_keys("")  # add your password

login = browser.find_element_by_xpath("//*[text()='Giriş Yap']")
login.click()

time.sleep(4)
browser.quit()
