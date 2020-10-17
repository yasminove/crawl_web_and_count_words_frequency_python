
import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    for link in soup.findAll('a', {'class': 'css-vh7bxp-PromoLink e1f5wbog3'}):
        words = []
        title = link.string
        lower_words = title.lower().split()
        # print(lower_words)
        for word in lower_words:
            words.append(word)
    clean_list(words)


def clean_list(words):
    clean_list = []
    for word in words:
        symbols = "~!@#$%^&*()_+|}{\":?/>.<,"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
            if len(word) > 0 :
                clean_list.append(word)
    count_frequency(clean_list)


def count_frequency(clean_list):
    frequency_counter = {}
    for word in clean_list:
        if word in frequency_counter:
            frequency_counter[word] += 1
        else:
            frequency_counter[word] = 1
    for key, value in sorted(frequency_counter.items(), key=operator.itemgetter(1)):
        print(key, value)

        
start('https://www.bbc.co.uk/search?q=covid&page=1')
