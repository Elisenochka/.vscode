import requests
from lxml import html
import urllib
from bs4 import BeautifulSoup
import io
import pandas as pd

USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

LOGIN_URL = "https://iqtools-grocery-prod.intrtl.com/site/login"
IR_URL ="https://iqtools-grocery-prod.intrtl.com"
BASE_URL = "https://iqtools-grocery-prod.intrtl.com/klass?page="
NSTL_URL = "https://iqtools-grocery-prod.intrtl.com/klass?KlassSearch%5BmyPageSize%5D=200&KlassSearch%5Bis_disabled%5D=&KlassSearch%5Bis_other%5D=&KlassSearch%5Bcode%5D=&KlassSearch%5Bname%5D=&KlassSearch%5Blocal_name%5D=&KlassSearch%5Bproduct_category_id%5D=&KlassSearch%5Bbrand_id%5D=&KlassSearch%5Bsubbrand_id%5D=&KlassSearch%5Bbrand_owner_id%5D=5e3c276901d43-5650&KlassSearch%5Bpackage_type_code%5D=&KlassSearch%5Bfilter_ss_except%5D=&KlassSearch%5Btubular%5D=&KlassSearch%5Bpromo%5D=&KlassSearch%5Btiny_name%5D=&KlassSearch%5Bmin_threshold%5D=&KlassSearch%5Bcount_boxes_1_start%5D=&KlassSearch%5Bcount_boxes_1_end%5D=&KlassSearch%5Bcount_boxes_2_start%5D=&KlassSearch%5Bcount_boxes_2_end%5D=&page=38&per-page=200"
CHNGH_URL = "https://iqtools-grocery-prod.intrtl.com/master-data-history?MasterDataHistory%5Bdate%5D=&MasterDataHistory%5Buser_id%5D=duchinskaya&MasterDataHistory%5Baction_object_name%5D=&MasterDataHistory%5Baction_type%5D=update&type=products&page="

parsed_pages=[]

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
    
    # Scrape url

    i = list(range(1,100))
    l = []

    for item in i:
        URL = CHNGH_URL + str(item) #BASE_URL + str(item) + "&per-page=50"
        r = s.get(URL, headers = dict(referer = URL)).content
        soup = BeautifulSoup(r, 'lxml')

        table = soup.find("table", attrs={'table table-striped table-bordered'})
        #print(table)
        table_rows = table.find_all('tr')

        for tr in table_rows:
            td = tr.find_all('td')
            row = [tr.text for tr in td]
            l.append(row)
        
        
    df = pd.DataFrame(l, columns=["#", "Date", "User", "Entity name", "Action type", "Attribute name","Old value", "New value"])

    df.to_excel("output_08.12.2020.xlsx")

        #history = table.findAll('div', {'class': 'history-field'})
        #for h in history:
        #    print(h.get_text())

if __name__ == '__main__':
    main()
