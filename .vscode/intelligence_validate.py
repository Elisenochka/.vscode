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

    classid = str(input("Enter class id: "))

    payload = {
        "confirm": "",
        "klass_id": classid
    }
    
    r = s.post(base_url, data = payload, headers = dict(referer = base_url))
    
    # Scrape url
    soup = BeautifulSoup(r, 'lxml')

    panel = soup.find("class", attrs={'panel-body klasses'})
    #print(table)
    wrappers = panel.findAll("class", attrs={'klass-wrapper'})
      
    markup_links = []
    img_links = []
    imgs = []

    for wrapper in wrappers:
        #print(tr.get('data-key'))
        img_links.append(wrapper.get('src'))
        markup_links.append(wrapper.get('href'))

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

    login_url = f"https://iqtools-{iqname}.intrtl.com/site/login"
    ir_url = f"https://iqtools-{iqname}.intrtl.com"
    base_url = f"https://iqtools-{iqname}.intrtl.com/validate?confirm=&page=1&proposal=false&limit=0"

    main()

