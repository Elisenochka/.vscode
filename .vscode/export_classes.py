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
    main_table = []
    code = []

    for item in i:
        URL = BASE_URL + str(item) + "&per-page=200"
        r = s.get(URL, headers = dict(referer = URL)).content
        soup = BeautifulSoup(r, 'lxml')
        print(r)
        table = soup.find("table", attrs={'table table-bordered'})

        print(table)
        #table_body = table.find('tbody')
        table_rows = table.find_all('tr')


        for tr in table_rows:
            #print(soup.tr['data-key'])
            #row1 = str(soup.tr['data-key'])
            tds = tr.find_all('td')
            row = [tr.text for tr in tds]
            main_table.append(row)
            #code.append(row1)

        
        
    df = pd.DataFrame(main_table, columns=["#", "Checkbox", "Disabled", "Other", "Code", "Name eng",	"Name local lang", "Product pic", "Product Category", "Brand", "Subbrand", "Brand owner", "Package Miniature",	"Package Type Code",	"Filter Ss Except",	"Tubular",	"Promo",	"Tiny Name",	"Min Threshold",	"Unconfirmed boxes", "Confirmed boxes", "Extra"])
    #df.assign(Code=code)
    df.to_excel("output_classes.xlsx")



if __name__ == '__main__':
    
    iqname = str(input("Enter iqtools name: "))
    LOGIN_URL = f"https://iqtools-{iqname}.intrtl.com/site/login"
    IR_URL = f"https://iqtools-{iqname}.intrtl.com"
    BASE_URL = f"https://iqtools-{iqname}.intrtl.com/klass?KlassSearch%5BmyPageSize%5D=200&KlassSearch%5Bis_disabled%5D=&KlassSearch%5Bis_other%5D=&KlassSearch%5Bcode%5D=&KlassSearch%5Bname%5D=&KlassSearch%5Blocal_name%5D=&KlassSearch%5Bproduct_category_id%5D=&KlassSearch%5Bbrand_id%5D=&KlassSearch%5Bsubbrand_id%5D=&KlassSearch%5Bbrand_owner_id%5D=5e3c276901d43-5650&KlassSearch%5Bpackage_type_code%5D=&KlassSearch%5Bfilter_ss_except%5D=&KlassSearch%5Btubular%5D=&KlassSearch%5Bpromo%5D=&KlassSearch%5Btiny_name%5D=&KlassSearch%5Bmin_threshold%5D=&KlassSearch%5Bcount_boxes_1_start%5D=&KlassSearch%5Bcount_boxes_1_end%5D=&KlassSearch%5Bcount_boxes_2_start%5D=&KlassSearch%5Bcount_boxes_2_end%5D=&page="



    main()

