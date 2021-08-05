import requests
from bs4 import BeautifulSoup

frsah_domain = 'http://frsah.ro'

if __name__ == '__main__':
    page = requests.get(f'{frsah_domain}')

    soup = BeautifulSoup(page.content, features='html.parser')

    table = soup.find(class_='td-ss-main-content td_block_template_1').find(class_='td_module_16 td_module_wrap td-animation-stack')
    print(table)