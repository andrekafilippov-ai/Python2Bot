from bs4 import BeautifulSoup


#открыть файл в нужной кодировке
file = open("сайт.html", encoding="utf-8")

#прочитываю файл
rfile = file.read()

#разобранный сайт
soup = BeautifulSoup(rfile, "lxml")

title = soup.select_one(".title")
price = soup.select_one(".price")

print(title.get.text())
print(price.get.text())


#from bs4 import BeautifulSoup
#from selenium.webdriver.support.expected_conditions import title_is

#file = open("sit.html", encoding="utf-8")

#rfile = file.read()

#soup = BeautifulSoup(rfile, "lxml")

#title = soup.select_one("title")
#price = soup.select_one("price")

#print(title)
#print(price)

#print(rfile)