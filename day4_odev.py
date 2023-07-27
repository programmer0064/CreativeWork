from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

class SwagLabs:

    def test_invalid_login_no_data(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        #sleep(1)
        usernameField = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
        passwordField = driver.find_element(By.ID,"password")
        #sleep(1)
        usernameField.send_keys("")
        passwordField.send_keys("")
        sleep(1)
        login_button = driver.find_element(By.ID,"login-button")
        login_button.click()
        #sleep(1)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"  #properties without (), methods with () # errorMessage.text == "Hatali giris" matiksal operatör
        print(testResult)
       # sleep(2)
        driver.close()

    def test_invalid_login_case_two(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
       # sleep(1)
        usernameField = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
        passwordField = driver.find_element(By.ID,"password")
       # sleep(1)
        usernameField.send_keys("standard_user")
        passwordField.send_keys("")
     #   sleep(1)
        login_button = driver.find_element(By.ID,"login-button")
        login_button.click()
       # sleep(1)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"  #properties without (), methods with () # errorMessage.text == "Hatali giris" matiksal operatör
        print(testResult)
     #   sleep(2)
        driver.close()

    def test_invalid_login_case_three(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        #sleep(1)
        usernameField = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
        passwordField = driver.find_element(By.ID,"password")
        #sleep(1)
        usernameField.send_keys("locked_out_user")
        passwordField.send_keys("secret_sauce")
        #sleep(1)
        login_button = driver.find_element(By.ID,"login-button")
        login_button.click()
        #sleep(1)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."  #properties without (), methods with () # errorMessage.text == "Hatali giris" matiksal operatör
        print(testResult)
        #sleep(2)
        driver.close()

    def test_invalid_login_case_four(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(0)
        usernameField = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
        passwordField = driver.find_element(By.ID,"password")
        sleep(0)
        usernameField.send_keys("")
        passwordField.send_keys("")
        sleep(0)
        login_button = driver.find_element(By.ID,"login-button")
        login_button.click()
        sleep(1)
        x = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg")
        if x.accessible_name != None:
            print(True)
        else:
            print(False)
        sleep(2)
        driver.close()


swaglabs = SwagLabs()
#swaglabs.test_invalid_login_no_data()
#swaglabs.test_invalid_login_case_two()
#swaglabs.test_invalid_login_case_three()
swaglabs.test_invalid_login_case_four()