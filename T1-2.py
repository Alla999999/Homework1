from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

service = Service(executable_path="C:\drivers\chromedriver.exe")

class Tests:
    def findelement(self):
        driver = webdriver.Firefox(service=service)
        driver.get("https://www.demoblaze.com")
        wait = WebDriverWait(driver, 10)
        try:
            Home = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')))
            print('Element is located')
        except NoSuchElementException:
            print('No Such Element: Home')

        try:
            Contact=wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="navbarExample"]/ul/li[2]/a')))
            print('Element is located')
        except NoSuchElementException:
            print('No Such Element: Contact')

        try:
            Aboutus=wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="navbarExample"]/ul/li[3]/a')))
            print('Element is located')
        except NoSuchElementException:
            print('No Such Element: About us')

        try:
            Cart=wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="cartur"]')))
            print('Element is located')
        except NoSuchElementException:
            print('No Such Element: Cart')

        try:
            login=wait.until(ec.element_to_be_clickable((By.XPATH, '// *[ @ id = "login2"]')))
            print('Element is located')
        except NoSuchElementException:
            print('No Such Element: Log in')

        try:
            signup=wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="signin2"]')))
            print('Element is located')
        except NoSuchElementException:

            print('No Such Element: Sign up')