from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Banka:

    def askQuestion(self):
        driver = webdriver.Chrome()  #webdriver haben wir heruntergeladen, damit wir 
        driver.get("https://www.halkbank.com.tr/")
        driver.maximize_window()
        sleep(2)
        cross = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[4]/div/div/button")
        cross.click()
        sleep(2)
        cookie_reject = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div/div/div/div/div/div[5]/div/div/div[2]/a[1]")
        cookie_reject.click()
        sleep(2)
        credit = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div[3]/input[1]")
        credit.clear()
        credit.send_keys("5000")
        sleep(2)
        length_credit = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/form/div[6]/div[3]/input")
        length_credit.clear()
        length_credit.send_keys("12")
        sleep(2)
        calculate = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/form/button")
        calculate.click()
        sleep(10)



halkbank = Banka()
halkbank.askQuestion()


