__author__ = 'Vishal'

import requests
from bs4 import BeautifulSoup as Soup
from fake_useragent import UserAgent

def scrape_membean_words(url):

    user_agent = UserAgent()

    page = requests.get(url=url, headers={'user-agent': user_agent.chrome})

    soup = Soup(page.content, 'html.parser')

    return {li.a.string:li.div.string for li in soup.find_all('li', class_='entry learnable')}


def extract_words():
    level_1_words = scrape_membean_words("https://www.vocabulary.com/lists/305775")
    level_2_words = scrape_membean_words("https://www.vocabulary.com/lists/305892")
    level_3_words = scrape_membean_words("https://www.vocabulary.com/lists/306097")
    level_4_words = scrape_membean_words("https://www.vocabulary.com/lists/306624")
    level_5_words = scrape_membean_words("https://www.vocabulary.com/lists/306630")

    filename = 'Membean_words.csv'

    with open(filename, mode="w+") as f:

        for word, meaning in level_1_words.items():
            f.write(f"Level 1, {word}, {meaning}\n")

        for word, meaning in level_2_words.items():
            f.write(f"Level 2, {word}, {meaning}\n")

        for word, meaning in level_3_words.items():
            f.write(f"Level 3, {word}, {meaning}\n")

        for word, meaning in level_4_words.items():
            f.write(f"Level 4, {word}, {meaning}\n")

        for word, meaning in level_5_words.items():
            f.write(f"Level 5, {word}, {meaning}\n")


if __name__ == '__main__':
    extract_words()