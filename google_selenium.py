from selenium import webdriver   #treibt den browser
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()   #first of all we need a driver that opens the browser; acts like a bridge between our python code and
driver.maximize_window()
driver.get("https://www.google.com/")   #wenn Browser startet öffne diese URL
time.sleep(5)   #lass Browser für 10 sek laufen
search_field = driver.find_element(By.NAME,"q")
search_field.send_keys("kodlamaio")
button = driver.find_element(By.NAME, "btnK")   #bulacagim element driver'in icerisinde
button.click()
#search_field.submit()
time.sleep(60)    #einzelnen Prozesse brauchen Zeit, bis die entsprechenden Programmzeilen ausgeführt werden, deshalb muss vor der Ausführung der nächsten Programmzeile gewartet werden
driver.quit()
