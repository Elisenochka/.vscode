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
    r = s.get(login_url)
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
    r = s.post(login_url, data = payload, headers = dict(referer = login_url))
    
    print(r.status_code)
    
    # Scrape url

    i = list(range(1,10))

    for item in i:
        url = base_url + str(item) + "&per-page=200"
        r = s.get(url, headers = dict(referer = url)).content
        soup = BeautifulSoup(r, 'lxml')

        table = soup.find("table", attrs={'table table-bordered'})
        #print(table)
        tbody = table.find('tbody')
        trs = tbody.findAll('tr')

        #for tr in trs:
        #    tds = tr.findAll('td')
        #    print(tds[3].text)
      
        class_id = []
        class_code = []
        imgs = []

        for tr in trs:
            #print(tr.get('data-key'))
            class_id.append(tr.get('data-key'))
            code = tr.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text
            #print(code)
            img = tr.find_next('img')
            class_code.append(code)
            imgs.append(img)

        img_links = []
        path = os.getcwd()

        for img in imgs:
            #print("page:" + str(item), "image:" + img.get('src'))
            img_links.append(img.get('src'))

        i = 0
        for img_link in img_links:
            f = io.open('parsed_data.html', 'a', encoding='utf8')
            #write to html file
            f.write("<a href='"+ ir_url + str(img_link)+"'></a>")
            f.close()
            #save to folder
            urllib.request.urlretrieve(ir_url + str(img_link), path + '\\' + str(class_code[i]) + "_" + str(class_id[i]) + str(img_link)[str(img_link).rfind("."):])
            i = i + 1

if __name__ == '__main__':
    
    iqname = str(input("Enter iqtools name: "))
    brandownerid = str(input("Enter brandowner id: "))

    login_url = f"https://iqtools-{iqname}.intrtl.com/site/login"
    ir_url = f"https://iqtools-{iqname}.intrtl.com"
    base_url = f"https://iqtools-{iqname}.intrtl.com/klass?KlassSearch%5BmyPageSize%5D=200&KlassSearch%5Bis_disabled%5D=&KlassSearch%5Bis_other%5D=&KlassSearch%5Bcode%5D=&KlassSearch%5Bname%5D=&KlassSearch%5Blocal_name%5D=&KlassSearch%5Bproduct_category_id%5D=&KlassSearch%5Bbrand_id%5D=&KlassSearch%5Bsubbrand_id%5D=&KlassSearch%5Bbrand_owner_id%5D={brandownerid}&KlassSearch%5Bpackage_type_code%5D=&KlassSearch%5Bfilter_ss_except%5D=&KlassSearch%5Btubular%5D=&KlassSearch%5Bpromo%5D=&KlassSearch%5Btiny_name%5D=&KlassSearch%5Bmin_threshold%5D=&KlassSearch%5Bcount_boxes_1_start%5D=&KlassSearch%5Bcount_boxes_1_end%5D=&KlassSearch%5Bcount_boxes_2_start%5D=&KlassSearch%5Bcount_boxes_2_end%5D=&page="



    main()

