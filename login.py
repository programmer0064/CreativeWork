from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Bockler:

    def loginBockler(self):
        driver = webdriver.Chrome()
        driver.get("https://www.myboeckler.de/")
        driver.maximize_window()
        sleep(1)
        input_mail = driver.find_element(By.NAME,"login")
        input_mail.send_keys("berkabkbulut64@gmail.com")
        sleep(1)
        input_password = driver.find_element(By.NAME,"pass")
        input_password.send_keys("Berk22012011")
        sleep(1)
        button = driver.find_element(By.XPATH,"/html/body/div/main/div[2]/div/div/div/div/div/div/form/div[4]/div/button")
        button.click()
        sleep(1)
        error_message = driver.find_element(By.XPATH,"/html/body/div/main/div[2]/div/div/div/div/div/div/form/div[3]/div")
        if error_message.text == "Anmeldung fehlgeschlagen":
            print(error_message)
            print(f"Die Rückmeldung {error_message.text} stimmt")
        sleep(55)


bockler = Bockler()
bockler.loginBockler()
