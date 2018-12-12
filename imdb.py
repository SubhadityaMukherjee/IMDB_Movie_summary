import os
from bs4 import BeautifulSoup
import urllib.request
import re

def getLinks(name):
    c = 0
    link = b'https://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=all'.decode('ASCII').format('+'.join(name.split()))
    print(link)
    site = urllib.request.urlopen(link)
    soup = BeautifulSoup(site, 'html.parser')
    list_of_links = []
    for link in soup.find_all('a'):
        hre = link.get('href')
        if c!=2:
            try:
                if '/title/' in hre and 'fn_al_' in hre:
                    list_of_links.append('https://www.imdb.com'+hre)
                    c+=1
            except:
                pass
        
    return list_of_links

def getinfo(list_of_links):
    l = []
    for a in list_of_links:
        site = urllib.request.urlopen(a)
        soup = BeautifulSoup(site, 'html.parser')
        l.append(soup.text)
    return l


def summary(text):
    st = text.find('Storyline\n')
    wb = text.find('Written by')
    return text[st:wb]

def main():
    dirn = input('Enter dir: ')
    lis = os.listdir(dirn)
    for a in lis:
        if 'Store' not in a:
            f = open(dirn+'/'+a+'/'+a+'.txt','a+')
            l = getinfo(getLinks(a))
            for b in l:
                f.write(summary(b))
            f.close()
main()

