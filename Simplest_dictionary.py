import requests
from bs4 import BeautifulSoup as bs
import lxml.etree as xml
import lxml

word = input('enter the word: ')
url = f'https://www.dictionary.com/browse/{word}?s=t'
web_page = bs(requests.get(url, {}).text, "lxml")
meanings = web_page.find_all('div', attrs={'class': 'css-1ghs5zt e1q3nk1v2'})
print('\nThe meaning(s) of the word is: ')
# for all the meanings
# for meaning in meanings:
#   print('* '+ meaning.text)
#   print('\n')

# for most common meaning 
print(meanings[0].text)