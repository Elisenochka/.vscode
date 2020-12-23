import requests
from lxml import html
import urllib
from bs4 import BeautifulSoup
import io
from selenium import webdriver
import time
from seleniumrequests import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#driver = webdriver.PhantomJS()
#options = webdriver.FirefoxOptions()
#options.add_argument('--headless')
#driver = webdriver.Firefox(options=options)
#profile = webdriver.FirefoxProfile()
#profile.accept_untrusted_certs = True

#driver = webdriver.Firefox(firefox_profile=profile)


def main():
    
    name = str(input("Enter name: "))
    password = str(input("Enter pass: "))

    driver = webdriver.Chrome(executable_path=r'C:\Users\elili\Documents\Python\chromedriver')
    driver.get (base_link)
    try:
        element_present = EC.presence_of_element_located((By.NAME, 'login-button'))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    driver.find_element_by_id("loginform-name").send_keys(name)
    driver.find_element_by_id ("loginform-password").send_keys(password)
    #driver.find_element_by_xpath ("/html/body/div[3]/div/div[2]/form/input").send_keys("hj8pTlRZKjtxFnRRzW4lcnHcGTzp7joTlH3SO6G9c2XfUEJ9DmBjSkhRTB6GIU0FC40gX7CIa17gNrN47_4HLQ==")

    #driver.find_element_by_name("_csrf-markup").send_keys("hj8pTlRZKjtxFnRRzW4lcnHcGTzp7joTlH3SO6G9c2XfUEJ9DmBjSkhRTB6GIU0FC40gX7CIa17gNrN47_4HLQ==")
    #driver.find_element_by_css_selector('.btn.btn-success.btn-block.btn-lg').click()
    #driver.find_element_by_css_selector('[class="btn btn-success btn-block btn-lg"]').click()
    driver.find_element_by_name("login-button").click()
    
    #button = "//button[@name='login-button']"
    #driver.find_elements_by_css_selector(button).click()
    
    #driver.find_elements_by_css_selector("button[class='btn btn-success btn-block btn-lg']").click()
    #driver.find_element_by_name("login-button").click()
    #button = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/form/div[4]/button").click()
 
    #/html/body/div[3]/div/div[2]/form/div[4]/button
    #html body.pace-top.pace-done div#page-container.fade.in div.login.bg-grey-800.animated.fadeInDown div.login-content form#login-form div.form-group button.btn.btn-success.btn-block.btn-lg
    WebDriverWait(driver, 50)

    print(driver.session_id)
    #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "section#header header navbar navbar-default navbar-fixed-top[href='/cart']"))).click()
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/ul/li[16]/a"))).click()
    
    i = list(range(1,5))

    for item in i:
        driver.get (iter_link + str(item) +"&proposal=false&limit=0&klass_search=")
        WebDriverWait(driver, 50)
        images = driver.find_elements_by_tag_name('img')
        
        for image in images:
            print(image.get_attribute('src'))

    #driver.quit()

# Create payload
    payload = {
        "confirm": "",
        "klass_id": classid,
        "klass_search": "",
        "limit": "0",
        "lots_id": "null",
        "page": 1,
        "proposal": "false",
        "size_id": "null"
    }

    headers = {
        'content-type': 'application/json;charset=utf-8',
        'referer': iter_url
    }

    driver.request('POST', iter_url, data=json.dumps(payload), headers = headers)
    
    WebDriverWait(driver, 20).until(
        ajax_complete,  "Timeout waiting for page to load")

    #payload = {
    #    "name":	"selectedProject",
    #    "value":	projectid,
    #    "expire":	"30000000"
    #}

    #headers = {
    #    'content-type': 'application/json;charset=utf-8',
    #    'referer': iter_url
    #}   



if __name__ == '__main__':

    iqname = str(input("Enter iqtools name: "))
    classid = str(input("Enter class id: "))

    login_link = f"https://iqtools-{iqname}.intrtl.com/site/login"
    IR_link = f"https://iqtools-{iqname}.intrtl.com"
    base_link = f"https://iqtools-{iqname}.intrtl.com/validate?confirm=&page=1&proposal=false&limit=0"
    iter_link = f"https://iqtools-{iqname}.intrtl.com/validate?klass_id={classid}&lots_id&size_id&confirm=&page="

    main()
