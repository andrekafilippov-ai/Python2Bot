#Парсить данные. Программа ищет данные за вас

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://quotes.toscrape.com/")
print("зашли на сайт")

#ждём пока загрузится блок quote
quote_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "quote"))
                                            )
#внутри блока quote ищем текст класса text

quote_text = quote_box.find_element(By.CLASS_NAME, "text").text

print(quote_text)

driver.quit()

# By.CLASS_NAME, "quote" — «найди кусок страницы, у которого имя = quote».
#
# WebDriverWait(..., 10).until(...) — «подожди до 10 секунд, пока он появится».
#
# find_element(..., "text") — «внутри найденного куска найди текстовую часть».
#
# .text — заберём текст и покажем в консоли.