import requests
import argparse
import json

from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output_file')

args = parser.parse_args()

url = 'https://montrealgazette.com/category/news/'
r = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
# print(r.text)

s = BeautifulSoup(r.text, 'html.parser')
articles = s.find_all("div", class_="article-card__content")

trending = []

for i in range(len(articles)):
    children = articles[i].find_all('div',  class_="article-card-top-trending__label")
    if not children == []:
        trending.append(articles[i])

links = []

for i in range(len(trending)):
    children = trending[i].find('a', class_="article-card__link")
    # print(children)

    links.append(children['href'])

main_site_url = 'https://montrealgazette.com'
final_json = []

for i in range(len(links)):
    trending_url = main_site_url + links[i]
    r = requests.get(trending_url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

    soup = BeautifulSoup(r.text, 'html.parser')

    
    title = soup.find('h1', {"id": "articleTitle"}).contents[0]
    pub_date = soup.find('span', class_="published-date__since").contents[0]
    author = soup.find('span', class_="published-by__author").a.contents[0]
    blurb = soup.find('p', class_='article-subtitle').contents[0]

    info = {}

    info["title"] = title
    info["publication_date"] = pub_date
    info["author"] = author
    info["blurb"] = blurb

    final_json.append(info)

with open(args.output_file, 'w') as out:
    json.dump(final_json, out)

    



