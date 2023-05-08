
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')


def test_google():
    var = driver.find_element(By.XPATH,"//img[@class='lnXdpd']").is_displayed()
    if var == True:
        assert True
    else:
        assert False
    driver.close()
