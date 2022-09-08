from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from getpass import getpass

user_name = input('Enter the Twitch username: ')
pwd = getpass('Enter the password: ')

driver = webdriver.Chrome()
driver.get('https://www.twitch.tv/login')
driver.maximize_window()

username_box = driver.find_element(By.XPATH, '//*[@id="login-username"]')
username_box.send_keys(user_name)

password_box = driver.find_element(By.XPATH, '//*[@id="password-input"]')
password_box.send_keys(pwd)

login_box = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button/div/div')
login_box.click()

sleep(100)
driver.quit()

print("Finished.")





