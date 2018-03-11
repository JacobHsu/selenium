from selenium import webdriver
import time

#以進入中央氣象局網站為例 
chrome_path = "C:\selenium_driver_chrome\chromedriver.exe"
web = webdriver.Chrome(chrome_path)

web.get('http://www.cwb.gov.tw/V7/')
web.set_window_position(0,0) #瀏覽器位置
web.set_window_size(1110,710) #瀏覽器大小
time.sleep(5)

web.find_element_by_link_text('天氣預報').click() #點擊頁面上"天氣預報"的連結
time.sleep(2)

#web.close()