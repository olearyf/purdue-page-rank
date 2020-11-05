import httplib2
from bs4 import BeautifulSoup, SoupStrainer


def getLinks(url):
    http = httplib2.Http()
    try:
        status, response = http.request(url)
    except:
        print('Error')
        return []
    links = []
    m = 0
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            if 'https' in link['href']:
                print(m, end='')
                print(' ', end='')
                print(link['href'])
                m = m+1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    getLinks('https://www.purdue.edu/disabilityresources/')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
