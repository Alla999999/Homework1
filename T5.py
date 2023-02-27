from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class Tests:
    def case(self):
        driver = webdriver.Firefox(service=service)
        driver.get("https://www.demoblaze.com")
        wait = WebDriverWait(driver, 10)
        sign_in=wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="signin2"]')))
        sign_in.click()
        try:
            window=wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="signInModal"]/div/div')))
            print("Worked")
        except NoSuchElementException:
            print("Something wrong")
