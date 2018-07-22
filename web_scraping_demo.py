__author__ = 'Vishal'

from bs4 import BeautifulSoup
import requests


def beautiful_soup_demo():
    """
        Demo demonstrating the basics of the BeautifulSoup package.
    """

    url = "https://example.com"

    # Getting the web page, creating the Response object.
    response = requests.get(url)

    #Extracting the source code of the web page.
    data = response.text

    #Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
    soup = BeautifulSoup(data, 'html.parser')

    #Extracting all the <a> tags into a list.
    tags = soup.find_all('a')

    #Extracting URLs from the attribute <href> in the <a> tag.
    for tag in tags:
        print(tag.get('href'))


if __name__ == '__main__':
    beautiful_soup_demo()
