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

    i = list(range(1,5))

    for item in i:
        URL = BASE_URL + str(item) + "&proposal=false&limit=0"
        r = s.get(URL, headers = dict(referer = URL)).content
        soup = BeautifulSoup(r, 'lxml')

        klss = soup.find("div", {"class": "panel-body klasses"})
        print(klss)
    
      
        img_ids = []
        imgs = []

        for kls in klss:
            #print(code)
            img = kls.find_next('img')
            imgs.append(img)


        img_links = []
        path = os.getcwd()

        for img in imgs:
            print("image:" + img.get('src'))
            img_links.append(img.get('src'))


        for img_link in img_links:
            f = io.open('parsed_data.html', 'a', encoding='utf8')
            #write to html file
            f.write("<a href='"+ IR_URL + str(img_link[:-str(img_link).rfind("?")+len(str(img_link))])+"'></a>")
            f.close()
            #save to folder
            urllib.request.urlretrieve(IR_URL + str(img_link), path + '\\' + str(img_link)[str(img_link).rfind("/"):-str(img_link).rfind("?")+len(str(img_link))])

if __name__ == '__main__':
    
    iqname = str(input("Enter iqtools name: "))
    classid = str(input("Enter class id: "))

    LOGIN_URL = f"https://iqtools-{iqname}.intrtl.com/site/login"
    IR_URL = f"https://iqtools-{iqname}.intrtl.com"
    BASE_URL = f"https://iqtools-{iqname}.intrtl.com/validate?klass_id={classid}&lots_id&size_id&confirm=&page="



    main()

