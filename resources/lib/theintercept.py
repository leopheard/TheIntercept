import requests
import re
from bs4 import BeautifulSoup

#DECONSTRUCTED#
def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
#INTERCEPTED#
def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
#MURDER,GA#
def get_soup3(url3):
    page = requests.get(url3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup3))
    return soup3
#SOMEBODY#
def get_soup4(url4):
    page = requests.get(url4)
    soup4 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup4))
    return soup4

def get_playable_deconstructed(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:
            link = content.find('enclosure').get('url')
            title = content.find('title').get_text()
            thumbnail = content.find('itunes:image').get('href')
            desc = content.find('itunes:subtitle').get_text()  # Extract the subtitle
        except AttributeError:
            continue
        
        item = {
            'url': link,
            'title': title,
            'thumbnail': thumbnail,
            'description': desc,
        }
        subjects.append(item)
    
    return subjects

def compile_playable_deconstructed(playable_deconstructed):
    items = []
    for podcast in playable_deconstructed:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
            'info': {
                'plot': podcast.get('description', ''),
            }
        })
    return items

def get_playable_intercepted(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('itunes:title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_intercepted(playable_intercepted):
    items = []
    for podcast in playable_intercepted:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_murderGA(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_murderGA(playable_murderGA):
    items = []
    for podcast in playable_murderGA:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_somebody(soup4):
    subjects = []
    for content in soup4.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item)
    return subjects
def compile_playable_somebody(playable_somebody):
    items = []
    for podcast in playable_somebody:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items