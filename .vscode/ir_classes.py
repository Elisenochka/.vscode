import requests
from lxml import html
import urllib
from bs4 import BeautifulSoup
import io
from selenium import webdriver
import time
from seleniumrequests import Firefox

USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

LOGIN_URL = "https://iqtools-grocery-prod.intrtl.com/site/login"
IR_URL ="https://iqtools-grocery-prod.intrtl.com"
BASE_URL = "https://iqtools-grocery-prod.intrtl.com/validate?klass_id=5e7dc0691c007-3006&lots_id&size_id&confirm=1&page="

#https://iqtools-grocery-prod.intrtl.com/validate?klass_id=5e7dc0691c007-3006&lots_id&size_id&confirm=&page=1&proposal=false&limit=0&klass_search=

parsed_pages=[]
site_links=[]


def main():

    
    # Scrape url
    URL = BASE_URL + "1&proposal=false&limit=0"

    login_link = "https://iqtools-grocery-prod.intrtl.com/site/login"
    link = "https://iqtools-grocery-prod.intrtl.com/validate?klass_id=5e7dc0691c007-3006&lots_id&size_id&confirm=&page=1&proposal=false&limit=0&klass_search="

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = Firefox(options = options)

    try:
        response = driver.request('POST', login_link, data={
        #"_csrf-markup": "erEQFG7wJ6l9K9AHhbg_mLHT1aASSO_XzoY9DPPJgSogxChmJ7l1-h5Dvmb2_hLP3J74ynE62YGayV5LuKfHaA==",
        "LoginForm[name]": "elina.ducohinskaya",
        "LoginForm[password]": "8KGGpg14",
        "LoginForm[rememberMe]": "0",
        "login-button": ""
    })
    except TimeoutException as e:
        pass
    time.sleep(2)
    print(response)


    

if __name__ == '__main__':
    main()

