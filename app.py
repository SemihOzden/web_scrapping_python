#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re

def run():
    #url = "https://pcichecklist.com/"
    url = input('please enter url:')

    userText = input('What would like to search in '+url+":")

    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    results = soup.body.find_all(string=re.compile('.*{0}.*'.format(userText)), recursive=True)
    
    print('Found the word "{0}" {1} times\n'.format(userText, len(results)))
