import asyncio
import aiohttp
from bs4 import BeautifulSoup
import urllib

"""
Currently Broken:
related - currently shows html as well as some extra
artist - shows as N/A
English publisher - gets html tags
"""


class Raitonoberu:

    def __init__(self):
        """The base url that we'll be ripping information from"""
        self.baseurl = 'http://www.novelupdates.com/'
        self.session = aiohttp.ClientSession()

    async def search_novel_updates(self, term: str):
        """
        This function will get the first link from the search term we do on term and then it will return the link we want to parse from.


        :param term: Light Novel to Search For
        """
        to_encode = {'s': term, 'post_type': 'seriesplan'}
        params = urllib.parse.urlencode(to_encode)
        async with self.session.get(self.baseurl, params=params) as response:
            if response.status == 200:
                search = BeautifulSoup(await response.text(), 'lxml')
                parsedsearch = search.find(
                    'a', class_='w-blog-entry-link').get('href')
                return parsedsearch
            else:
                raise aiohttp.ClientResponseError(response.status)

    async def page_info_parser(self, term: str):
        """
        This function will parse the information from the link that search_novel_updates returns and then return it as a dictionary


        :param term: The novel to search for and parse
        """

        to_parse = await self.search_novel_updates(term)
        async with self.session.get(to_parse) as response:
            if response.status == 200:
                html = await response.text()
                parse_info = BeautifulSoup(html, 'lxml')
                data = {'title': parse_info.find('h4', class_='seriestitle new').string,
                        'cover': parse_info.find('img').get('src'),
                        'type': parse_info.find('a', class_='genre type').string,
                        'genre': list(set([x.string for x in list(parse_info.find_all('div', id='seriesgenre')[0].children) if len(x.string.strip()) > 0])),
                        'tags': list(set([x.string for x in list(parse_info.find_all('div', id='showtags')[0].children) if len(x.string.strip()) > 0])),
                        'language': parse_info.find('a', class_='genre lang').string,
                        'authors': list(set([x.string for x in parse_info.find_all('a', id='authtag')])),
                        'artists': list(set([x.string for x in parse_info.find_all('span', class_='seriesna')])),
                        'year': parse_info.find('div', id='edityear').string.strip(),
                        'novel_status': parse_info.find('div', id='editstatus').string.strip(),
                        'licensed': True if parse_info.find('div', id='showlicensed').string.strip() == 'Yes' else False,
                        'completely_translated': True if len(list(parse_info.find('div', id='showtranslated').descendants)) > 1 else False,
                        'publisher': parse_info.find('a', class_='genre', id='myopub').string,
                        'english publisher': parse_info.find('a', class_='genre', id='myepub'),
                        'description': ''.join([x.string.strip() for x in list(parse_info.find('div', id='editdescription').children) if x.string.strip()]),
                        'aliases': list(set([x.string for x in parse_info.find('div', id='editassociated') if x.string is not None])),
                        'related': list(set(parse_info.find_all('a', class_='genre'))),
                        'link': to_parse}
                return data
            else:
                raise aiohttp.ClientResponseError(response.status)

if __name__ == '__main__':
    n = NovelUpdatesAPI()
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(n.page_info_parser(
        'Curing incurable diseases with semen')))
    print(loop.run_until_complete(n.page_info_parser('ISSTH')))
    print(loop.run_until_complete(n.page_info_parser('Sword art online')))
