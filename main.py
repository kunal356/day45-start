from bs4 import BeautifulSoup

with open('website.html', mode='r') as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
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
