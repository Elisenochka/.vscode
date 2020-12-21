import requests
from lxml import html
import urllib
from bs4 import BeautifulSoup
import io
from seleniumwire import webdriver
import time
from seleniumrequests import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType

#driver = webdriver.PhantomJS()
#options = webdriver.FirefoxOptions()
#options.add_argument('--headless')
#driver = webdriver.Firefox(options=options)
#profile = webdriver.FirefoxProfile()
#profile.accept_untrusted_certs = True

#driver = webdriver.Firefox(firefox_profile=profile)


def main():
    iqname = str(input("Enter iqtools name: "))
    classid = str(input("Enter class id: "))
    name = str(input("Enter name: "))
    password = str(input("Enter pass: "))

    #iter_link = f"https://iqtools-{iqname}.intrtl.com/validate?klass_id={classid}&lots_id&size_id&confirm=&page=1&proposal=false&limit=0&klass_search="
    base_url = f"https://iqtools-{iqname}.intrtl.com/validate?confirm=&page=1&proposal=false&limit=0"

    #profile = webdriver.FirefoxProfile()
    #profile.accept_untrusted_certs = True
    #options = webdriver.FirefoxOptions()
    #options.add_argument('--headless')

    

    driver = Firefox(executable_path=r'C:\Users\elili\Documents\Python\geckodriver')
    #driver = webdriver.Chrome(executable_path=r'C:\Users\elili\Documents\Python\chromedriver')
    driver.get (base_url)
    try:
        element_present = EC.presence_of_element_located((By.NAME, 'login-button'))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    driver.find_element_by_id("loginform-name").send_keys(name)
    driver.find_element_by_id ("loginform-password").send_keys(password)
    driver.find_element_by_name("login-button").click()
    
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'klass-wrapper'))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    # Create payload
    payload = {
        "confirm": "",
        "klass_id": classid,
        #"klass_search": "",
        #"limit": "0",
        #"lots_id": "null",
        #"page": 1,
        #"proposal": "false",
        #"size_id": "null"
    }

    driver.request('POST', base_url, data=payload)
    
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'klass-wrapper'))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    
    classes = driver.find_elements_by_class_name('klass-wrapper')

    for clas in classes:
        image = clas.find_element_by_tag_name('img')
        print(image.get_attribute('src'))
        markup = clas.find_element_by_tag_name('a')
        print(markup.get_attribute('href'))

    
    while(True):
        pass

    #driver.quit()

if __name__ == '__main__':

    main()
