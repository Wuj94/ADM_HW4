import requests
from bs4 import BeautifulSoup
import pandas as pd


class Scraper:

    def __init__(self):
        self.__link_templ__ = "https://www.immobiliare.it/vendita-case/roma/?criterio=rilevanza&pag={}"
        self.__main_page__ = 'https://www.immobiliare.it'
        self.__res_columns_name__ = ['title', 'link', 'price', 'locali', 'superficie', 'bagni', 'piano', 'description']

    def start(self):
        content = requests.get(self.__link_templ__.format(1))
        df = self.__scrape__(content)
        for i in range(1720, 1730):
            content = requests.get(self.__link_templ__.format(i))
            df = pd.concat([df, self.__scrape__(content)], ignore_index=True)
        return df

    def __scrape__(self, content):
        soup = BeautifulSoup(content.text, "lxml")
        # find all the announcements
        announcements = soup.find_all('li', class_='listing-item vetrina js-row-detail')
        if len(announcements) == 0:
            announcements = soup.find_all('li', class_='listing-item js-row-detail')

        res = []
        for ann in announcements:
            try:
                res.append(self.__scrape_announcement__(ann))
            except:
                print('exception')

        return pd.DataFrame(res, columns=self.__res_columns_name__)

    def __scrape_announcement__(self, ann):
        # result contains [title, link, price, locali, superficie,
        # bagni, piani, description]
        result = ['NA','NA','NA','NA','NA','NA','NA','NA']

        result[0] = ann.find('p', class_='titolo text-primary').a['title']
        result[1] = ann.find('p', class_='titolo text-primary').a['href']

        link = result[1]
        if not link.startswith(self.__main_page__):
            link = self.__main_page__ + link

        # get the page of the announcement
        subcontent = requests.get(link)
        subsoup = BeautifulSoup(subcontent.text, 'html.parser')

        # select infos (price, locali, superficie, piano)
        infos = subsoup.find('div', class_='im-property__features')

        price = infos.find('span', class_='features__price--double')
        if price is None:
            price = infos.find('ul', class_='features__price-block').find('li', class_='features__price').span
        result[2] = price.getText()

        subinfos = infos.find('ul', class_='list-inline list-piped features__list')

        for list_item in subinfos.find_all('li'):
            feature = list_item.find('div', class_='features__label')
            if feature is not None:
                if feature.getText() == 'locali':
                    result[3] = list_item.find('div').find('span').getText()
                elif feature.getText() == 'superficie':
                    result[4] = list_item.find('div').find('span').getText()
                elif feature.getText() == 'bagni':
                    result[5] = list_item.find('div').find('span').getText()
                elif feature.getText() == 'piano':
                    piano = list_item.find('div').find('span')
                    if piano is None:
                        piano = list_item.find('div').find('abbr')
                    result[6] = piano.getText()

        # scrape description
        description = subsoup.find('div', class_='left-side')
        description = description.find('div', class_='col-xs-12 description-text text-compressed').div.getText()
        result[7] = description
        return result


s = Scraper()
df = s.start()
print(df)
