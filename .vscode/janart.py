import requests
from lxml import html
import urllib
from bs4 import BeautifulSoup
import io


URL = 'http://janarat.ru/marinades_janarat'
path = r"C:\Users\elili\Documents\Python\janart"


def main():
    s = requests.session()

    # Get login csrf token
    r = s.get(URL).content


    soup = BeautifulSoup(r, 'lxml')

    images = soup.findAll('div', {'class': 't-slds__bgimg t-bgimg js-product-img'})
    names = soup.findAll('div',{'class': 't778__title t-name t-name_xs js-product-name'})
    
    for name in names:
        print(name.text)

    img_links = []

    for img in images:
        print("image:" + img.get('data-original'))
        img_links.append(img.get('data-original'))

    #names_text = []

    #for name in names:
    #    print("name" + name.get(''))
    i = 0
    for img_link in img_links:
            f = io.open('parsed_data.html', 'a', encoding='utf8')
            #write to html file
            f.write("<a href='"+ str(img_link)+"'></a>")
            f.close()
            #save to folder
            urllib.request.urlretrieve(str(img_link), path + "\\" + str(names[i].text).replace('"','') + ".jpg")
            i = i + 1



if __name__ == '__main__':
    main()