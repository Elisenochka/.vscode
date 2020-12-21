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
BASE_URL = "https://iqtools-grocery-prod.intrtl.com/klass?page="

def main():
    s = requests.session()

    # Get login csrf token
    r = s.get(LOGIN_URL)
    tree = html.fromstring(r.text)
    authenticity_token = list(set(tree.xpath("//input[@name='_csrf-markup']/@value")))[0]

    # Create payload
    payload = {
        "LoginForm[name]": "elina.duchinskaya", 
        "LoginForm[password]": "8KGGpg14", 
        "_csrf-markup": authenticity_token
    }

    # Perform login
    r = s.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    
    print(r.status_code)

    driver = webdriver.Firefox()
    link = "https://iqtools-grocery-prod.intrtl.com/validate?klass_id=5e7dc0691c007-3006&lots_id&size_id&confirm=&page=1&proposal=false&limit=0&klass_search="


    driver.get(link)

    htmlSource = driver.page_source
    print(htmlSource)

    



if __name__ == '__main__':
    main()
