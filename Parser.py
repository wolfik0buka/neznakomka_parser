import json
import os
from unicodedata import category

from requests import get
from bs4 import BeautifulSoup

from Category import Category


class Parser:
    def __init__(self):
        self.baseLink = 'https://neznakomka.spb.ru/23-katalog-zhenskoy-odezhdy'
        self.categoryList = []

    def run(self):
        self.get_category_list()


    def get_category_list(self):
        if os.path.isfile('category_list.txt'):
            with open('category_list.txt', 'r') as f:
                print(f.read())
        else:
            page = self.get_page(self.baseLink)
            link_block = page.find('div', id='categories_block_left')
            first_level = link_block.find('ul', class_='dhtml')
            for item in first_level.find_all('li', recursive=False):
                link = item.find('a')
                cat = Category(link.text.strip(), link['href'])
                submenu = item.find('ul')
                if submenu is not None:
                    for sub_item in submenu.find_all('a'):
                        sub_cat = Category(sub_item.text.strip(), sub_item['href'])
                        cat.add_child(sub_cat)
                self.categoryList.append(cat)
            self.save_category_list()

            

    def save_category_list(self):
        category_dict_list = [cat.to_dict() for cat in self.categoryList]

        # Сохраняем в файл
        with open('category_list.txt', 'w') as file:
            file.write(json.dumps(category_dict_list, indent=4, ensure_ascii=False))

    def get_page(self, baseLink):
        page = get(baseLink)
        parsed_html = BeautifulSoup(page.text, 'html.parser')
        return parsed_html

if __name__ == '__main__':
    parser = Parser()
    parser.run()
