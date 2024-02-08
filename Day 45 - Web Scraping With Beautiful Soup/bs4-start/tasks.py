import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")
lines = soup.find_all(name="span", class_="titleline")
article_texts =[]
article_links = []
for line in lines:
    text = line.find_next(name="a").string
    article_texts.append(text)
    link_line = line.find_next(name="a")
    link = link_line.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_vote_index = article_upvote.index(max(article_upvote))

print(article_texts[max_vote_index])
print(article_links[max_vote_index])
print(article_upvote[max_vote_index])













