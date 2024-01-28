from bs4 import BeautifulSoup


with open("website.html",encoding="utf8") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.a)
# print(soup.p)

# all_tags = soup.find_all(name="a")
# for tag in all_tags:
#    # print(tag.text)
#    # print(tag.getText())
#    print(tag.get("href"))
#
# print(soup.find(name="h1", id="name"))
# print(soup.find(name="h3",class_="heading"))

# Using CSS Selectors
compurl = soup.select_one(selector="ul li")
print(compurl)
