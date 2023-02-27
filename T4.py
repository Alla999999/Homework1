from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class Tests:
    def maxprice(self):
        driver = webdriver.Firefox(service=service)
        driver.get("https://www.demoblaze.com")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div/div/div/h5')))
        products = driver.find_elements(By.XPATH, '//*[@id="tbodyid"]/div/div/div/h5')
        max_price = 0
        product_name = ''
        for i in products:
            price = float(i.text.replace('$', ''))
            if price > max_price:
                max_price = price
                name = i.find_element(By.XPATH, '//*[@id="tbodyid"]/div/div/div/h4/a')
                product_name = name.text
        print(max_price, product_name)