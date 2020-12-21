import requests
from lxml import html
import urllib
from bs4 import BeautifulSoup
import io

USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

LOGIN_URL = "https://nestlear.intrtl.com/site/login"
CITY_CR_URL ="https://nestlear.intrtl.com/city/create?CitySearch%5Bname%5D=&CitySearch%5Bcountry_id%5D=7716095&CitySearch%5Bregion_id%5D=15789406"
BASE_URL = "https://iqtools-grocery-prod.intrtl.com/klass?page="

parsed_pages=[]

def main():
    s = requests.session()

    # Get login csrf token
    r = s.get(LOGIN_URL)
    tree = html.fromstring(r.text)
    authenticity_token = list(set(tree.xpath("//input[@name='_csrf-frontend']/@value")))[0]

    # Create payload
    payload = {
        "LoginForm[name]": "elina.duchinskaya", 
        "LoginForm[password]": "8KGGpg14", 
        "_csrf-frontend": authenticity_token
    }

    # Perform login
    r = s.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    
    print(r.status_code)
    
    # go to another page
    r = s.get(CITY_CR_URL)
    print(r.status_code)
    print(r.text)
    
    # Create payload
    payload = {
        "_csrf-frontend":	"MNKQe4tpplINevGRxvk33vDIppSm0LKR3eu05jnONIhBsKAO6FrCEUIAyPa2q2i7u6SX4t-z86eXxvaDAZxduw==",
        "City[country_id]":	"7716095",
        "City[region_id]":	"15789406",
        "City[name]":	"Beccar"
    }

    r = s.post(CITY_CR_URL, data = payload, headers = dict(referer = CITY_CR_URL))

if __name__ == '__main__':
    main()

'''
app_id	"be14gutn"
v	"3"
g	"55c62db293cbc8dddfa2c46c2f84854420831fa0"
s	"19e95717-e204-451e-a804-1ae4f4faec57"
r	"https://nestlear.intrtl.com/site/login"
platform	"web"
Idempotency-Key	"b3fb2f65c112ba7e"
user_data	"{\"email\":\"elina.duchinskaya@intrtl.com\",\"anonymous_id\":\"927f27f1-938c-42ad-b284-6fed5cd60648\",\"name\":\"elina.duchinskaya\",\"User ID\":36671,\"Company\":null,\"Portal\":\"https://nestlear.intrtl.com\",\"Role\":\"senioreditor\",\"Login\":\"elina.duchinskaya\"}"
internal	"{}"
page_title	"Создать город - NestleAR Portal"
user_active_company_id	"undefined"
source	"apiBoot"
sampling	"false"
referer	"https://nestlear.intrtl.com/city/create"
anonymous_session	"QUl5NEthaGlNc3Y2S1I2UzliWXh3bmZ2ZzRzcVkxalJHQndoMFFBTXlKeXk1a2pZekFZUm1OL3h5MDd2RVFnaC0tTjVJck1tcnJzQThCTVQ0K2pabE1Ldz09--15e9273c4d23d0b5c1f60cbe6c1cd09664a5b255"

app_id=be14gutn&v=3&g=55c62db293cbc8dddfa2c46c2f84854420831fa0&s=19e95717-e204-451e-a804-1ae4f4faec57&r=https%3A%2F%2Fnestlear.intrtl.com%2Fsite%2Flogin&platform=web&Idempotency-Key=b3fb2f65c112ba7e&user_data=%7B%22email%22%3A%22elina.duchinskaya%40intrtl.com%22%2C%22anonymous_id%22%3A%22927f27f1-938c-42ad-b284-6fed5cd60648%22%2C%22name%22%3A%22elina.duchinskaya%22%2C%22User%20ID%22%3A36671%2C%22Company%22%3Anull%2C%22Portal%22%3A%22https%3A%2F%2Fnestlear.intrtl.com%22%2C%22Role%22%3A%22senioreditor%22%2C%22Login%22%3A%22elina.duchinskaya%22%7D&internal=%7B%7D&page_title=%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C%20%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%20-%20NestleAR%20Portal&user_active_company_id=undefined&source=apiBoot&sampling=false&referer=https%3A%2F%2Fnestlear.intrtl.com%2Fcity%2Fcreate&anonymous_session=QUl5NEthaGlNc3Y2S1I2UzliWXh3bmZ2ZzRzcVkxalJHQndoMFFBTXlKeXk1a2pZekFZUm1OL3h5MDd2RVFnaC0tTjVJck1tcnJzQThCTVQ0K2pabE1Ldz09--15e9273c4d23d0b5c1f60cbe6c1cd09664a5b255




_csrf-frontend	"MNKQe4tpplINevGRxvk33vDIppSm0LKR3eu05jnONIhBsKAO6FrCEUIAyPa2q2i7u6SX4t-z86eXxvaDAZxduw=="
City[country_id]	"7716095"
City[region_id]	"15789406"
City[name]	"Adrogué"

'''