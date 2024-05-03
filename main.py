from bs4 import BeautifulSoup
import requests
# Scrapping website: https://news.ycombinator.com/
response = requests.get("https://news.ycombinator.com/")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.select("span.titleline > a")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.text)
    article_links.append(article.get("href"))

article_upvotes = [int((upvote.getText()).split(" ")[0]) for upvote in soup.select(".score")]

max_upvote_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_upvote_index])
print(article_links[max_upvote_index])
print(article_upvotes[max_upvote_index])

# with open('website.html', mode='r') as file:
#     contents = file.read()
#     # print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name) # Prints the name of the tag
# print(soup.title.string) # Prints the string inside the tag
# print(soup.a) # Prints first anchor tag in the document
# print(soup.prettify())  # Prints in indented format
# all_anchors = soup.find_all(name="a")  # Prints list of all anchor tags
# for anchor in all_anchors:
# print(anchor.getText()) # Prints the text inside the tags
# print(anchor.get("href"))  # get() gets all the tags by there attributes

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")  # Not to clash with class keyword we use  class_
# print(section_heading)

# name = soup.select_one(selector="#name")  # Finds single required tag using syntax of css selectors
# print(name)
#
# headings = soup.select(selector=".heading")  # Finds all tags using css selectors
# print(headings)
