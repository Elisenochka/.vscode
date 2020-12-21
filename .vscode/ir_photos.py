import requests
from lxml import html
import urllib
from bs4 import BeautifulSoup
import io

USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

LOGIN_URL = "https://bonduelle.intrtl.com/site/login"
IR_URL ="https://iqtools-grocery-prod.intrtl.com"
BASE_URL = "https://bonduelle.intrtl.com/photos"

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

    i = list(range(1))

    for item in i:
        URL = BASE_URL# + str(item) + "&per-page=50"
        input-group date
        r = s.get(URL, headers = dict(referer = URL)).content
        soup = BeautifulSoup(r, 'lxml')

        table = soup.find("table", attrs={'table table-bordered'})

        imgs= table.findAll('img')
        img_links = []
        path = r"C:\Users\elili\Documents\Python\class"

        for img in imgs:
            print("page:" + str(item), "image:" + img.get('src'))
            img_links.append(img.get('src'))

        for img_link in img_links:
            f = io.open('parsed_data.html', 'a', encoding='utf8')
            #write to html file
            f.write("<a href='"+ IR_URL + str(img_link)+"'></a>")
            f.close()
            #save to folder
            
            urllib.request.urlretrieve(IR_URL + str(img_link), path + str(img_link)[str(img_link).rfind("/"):])

if __name__ == '__main__':
    main()

