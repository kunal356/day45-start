from bs4 import BeautifulSoup
with open('website.html', mode='r') as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name) # Prints the name of the tag
# print(soup.title.string) # Prints the string inside the tag
# print(soup.a) # Prints first anchor tag in the document
