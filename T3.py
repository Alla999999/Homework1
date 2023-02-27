from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class Tests:
    def categorise(self):
        driver=webdriver.Firefox(service=service)
        driver.get("https://www.demoblaze.com")
        wait=WebDriverWait(driver, 10)
        try:
            phones=wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a.list-group-item:nth-child(2)')))
            print("Element is lockated")
        except NoSuchElementException:
            print("No such element")
        try:
            laptops=wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a.list-group-item:nth-child(3)')))
            print("Element is lockated")
        except NoSuchElementException:
            print("No such element")
        try:
            monitors=wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a.list-group-item:nth-child(4)')))
            print("Element is lockated")
        except NoSuchElementException:
            print("No such element")