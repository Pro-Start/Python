import requests
from bs4 import BeautifulSoup
import lxml

with open("archive/045/index.html") as webpage:
    contents = webpage.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.body)
# print(soup.prettify())

print(soup.h1)
heading = soup.find(name="h1", id="1")
print(heading)


# --------------------------- LIVE PAGE ------------------------------------ #

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup2 = BeautifulSoup(yc_webpage, "html.parser")
article_tag = soup2.find(name="a", class_="storylink")
article_text = soup2.getText()
article_link = soup2.get("href").getText()
article_upvote = soup2.find(name="span", class_="score").getText()
