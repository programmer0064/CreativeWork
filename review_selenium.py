from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Chrome(ChromeDriverManager().install())
#                             class                function

driver.maximize_window()
driver.get("https://www.google.com/")

sleep(0)

cookies_button = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div")
sleep(0)
cookies_button.click()

sleep(0)

search_google = driver.find_element(By.ID,"APjFqb")
sleep(0)
search_google.send_keys("https://techwithtim.net")
sleep(0)

search_button = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")
sleep(0)
search_button.click()
sleep(2)

link = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[13]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3")
sleep(2)
link.click()
sleep(2)

coursesButton = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div/div[2]/a[3]/div/h3")
sleep(2)
coursesButton.click()
sleep(2)

listOfCourses = driver.find_elements(By.CLASS_NAME,"course__Title-sc-1pyfei8-5 elWfOd")
sleep(2)
print(f"Number of courses listed: {len(listOfCourses)}")
sleep(2)

driver.close()



#selenium is i a way to communicate with html elements from any website: get infos, create bots, test aspects of a website
#f12: seeing the html elements used to define the elements
#id is always unique, name and class not always 