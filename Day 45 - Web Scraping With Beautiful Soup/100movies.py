from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

lines = soup.find_all(name="h3")
titles = []
for line in lines:
    title_line = line.get_text()
    print(title_line)
    titles.append(title_line)

titles.reverse()

file = open("list.txt", "w")
for title in titles:
    print(title)
    file.write(title+"\n")


