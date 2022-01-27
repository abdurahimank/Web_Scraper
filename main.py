import requests
from bs4 import BeautifulSoup
import string


r = requests.get('https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3')
soup = BeautifulSoup(r.content, 'html.parser')
article_list = soup.find_all('article')
# news_article_list = []
links = []
for p1 in article_list:
    article_type = p1.find('span', "c-meta__type").text
    if article_type == "News":
        # news_article_list.append(p1)
        links.append(p1.find('a').get('href'))
# print(news_article_list)
# print(links)
saved_articles = []
url = "https://nature.com"
for i in range(len(links)):
    new_url = url + links[i]
    r = requests.get(new_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    body = soup.find('div', "c-article-body u-clearfix").text
    title = soup.find('title').text
    title = title.replace(" ", "_").strip()
    for j in string.punctuation.replace("_", ""):
        title = title.replace(j, "")
    title = title + '.txt'
    saved_articles.append(title)
    body = bytes(body, encoding="utf-8")
    with open(title, 'wb') as file:
        file.write(body)
    # print(title)
    # print(body)
    # break
print(saved_articles)
