from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

user_name = input("Enter Email ID: ")
pass_word = input("Enter the password: ")

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
driver.maximize_window()

user_box = driver.find_element(By.ID, 'email')
user_box.send_keys(user_name)
print ("Email Id entered")
sleep(1)

pass_box = driver.find_element(By.ID, 'pass')
pass_box.send_keys(pass_word)
print("Password entered")

login_box = driver.find_element(By.NAME, 'login')
login_box.click()

print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")


