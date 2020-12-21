import requests
from lxml import html
import urllib
from bs4 import BeautifulSoup
import io
import os
import pandas as pd


def login():
        name = str(input("Enter name: "))
        password = str(input("Enter pass: "))
        return name, password


def main():
    s = requests.session()

    # Get login csrf token
    r = s.get(LOGIN_URL)
    tree = html.fromstring(r.text)
    authenticity_token = list(set(tree.xpath("//input[@name='_csrf-markup']/@value")))[0]
    
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

    i = list(range(1,2))
    l = []

    for item in i:
        URL = BASE_URL + str(item) + "&per-page=200"
        r = s.get(URL, headers = dict(referer = URL)).content
        soup = BeautifulSoup(r, 'lxml')
        print(r)
        table = soup.find("table", attrs={'table table-striped table-bordered'})

        print(table)
        table_rows = table.find_all('tr')

        for tr in table_rows:
            td = tr.find_all('td')
            row = [tr.text for tr in td]
            l.append(row)
        
        
    df = pd.DataFrame(l, columns=["#", "Checkbox", "Name eng", "Name local lang", "Tiny name", "Code", "Product Category", "Brand pic", "Brand name", "Market segment", "Extra"])

    df.to_excel("output_brands.xlsx")



if __name__ == '__main__':
    
    iqname = str(input("Enter iqtools name: "))
    LOGIN_URL = f"https://iqtools-{iqname}.intrtl.com/site/login"
    IR_URL = f"https://iqtools-{iqname}.intrtl.com"
    BASE_URL = f"https://iqtools-{iqname}.intrtl.com/brand?BrandSearch%5BmyPageSize%5D=200&BrandSearch%5Bname%5D=&BrandSearch%5Bname_local%5D=&BrandSearch%5Btiny_name%5D=&BrandSearch%5Bcode%5D=&BrandSearch%5Bproduct_category%5D=&BrandSearch%5Bbrand_name%5D=&BrandSearch%5Bmarket_name%5D=&page="

    main()

