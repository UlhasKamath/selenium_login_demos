from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://twitter.com/')
driver.maximize_window()

#main_page = driver.current_window_handle
#sleep(4)

driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div').click()
sleep(4)
'''
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

driver.switch_to.window(login_page)
sleep(4)
'''
print("Email ID: ", end='')
email = input().strip()
print("Pass: ", end='')
password1 = input().strip()

driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(email)

next_box = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
next_box.click()
sleep(5)

driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password1)

driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()

#driver.switch_to.window(main_page)
sleep(10)

print('Done')
driver.quit()
print("Finished.")