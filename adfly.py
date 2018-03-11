from selenium import webdriver
import time

chrome_path = "C:\selenium_driver_chrome\chromedriver.exe"
browser = webdriver.Chrome(chrome_path)

browser.get('http://briskrange.com/GhX7')
browser.set_window_position(0,0)
browser.set_window_size(1110,710)
time.sleep(6)

browser.find_element_by_id('skip_bu2tton').click()

time.sleep(2)
browser.close()
time.sleep(2)
browser.quit()

