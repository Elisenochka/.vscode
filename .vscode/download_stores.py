import requests
from lxml import html
import urllib
from bs4 import BeautifulSoup
import io
import os



def login():
        name = str(input("Enter name: "))
        password = str(input("Enter pass: "))
        return name, password


def main():
    s = requests.session()

    # Get login csrf token
    r = s.get(LOGIN_URL)
    #print(r.text)
    tree = html.fromstring(r.text)
    authenticity_token = list(set(tree.xpath("//input[@name='_csrf-frontend']/@value")))[0]
    
    while True:
        try:
            payloadlist = login()
            break
        except:
            payloadlist = login()

    
    name = payloadlist[0]
    password = payloadlist[1]

    # Create payload
    payload = {
        "LoginForm[name]": name, 
        "LoginForm[password]": password, 
        "_csrf-markup": authenticity_token
    }

    # Perform login
    r = s.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    
    print(r.status_code)
    
    # Scrape url

    i = list(range(3000,10000))
    class_id = []
    class_id2 = []

    for item in i:
        URL = BASE_URL + str(item) + "/update"
        r = s.get(URL, headers = dict(referer = URL)).content
        soup = BeautifulSoup(r, 'lxml')

        name = soup.find("title")
        print(i)
        print(name)
        div = soup.find('store-form')
        #print(table)
        class_id_div = div.find('store-external_id')
        class_id_value = class_id_dive.find_next('value')
        print(class_id_value)
        class_id2_div = tbody.find('store-external_id2')
        class_id2_value = class_id_dive.find_next('value')
        print(class_id2_value)
        class_id.append(class_id_value)
        class_id2.append(class_id2_value)

        

if __name__ == '__main__':
    
    portalname = str(input("Enter iqtools name: "))
    #brandownerid = str(input("Enter brandowner id: "))

    LOGIN_URL = f"https://{portalname}.intrtl.com/site/login"
    IR_URL = f"https://{portalname}.intrtl.com"
    BASE_URL = f"https://{portalname}.intrtl.com/store/"



    main()

