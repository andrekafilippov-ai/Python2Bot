from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def dns_search_selenium(query: str, limit: int = 5, timeout: int = 25):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(f"https://www.dns-shop.ru/search/?q={query}")
        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".catalog-product, .product"))
        )

        cards = driver.find_elements(By.CSS_SELECTOR, ".catalog-product, .product")
        results = []

        for card in cards:
            # Заголовок + ссылка
            title_el = None
            for sel in ["a.catalog-product__name", ".product-info__title-link a", "a.ui-link"]:
                try:
                    title_el = card.find_element(By.CSS_SELECTOR, sel)
                    if title_el.text.strip():
                        break
                except:
                    pass
            if not title_el:
                continue

            title = title_el.text.strip()
            url = title_el.get_attribute("href")

            # Цена
            price = "цена не найдена"
            for sel in [".product-buy__price", ".product-buy__cur-price", ".product-card__price", "[class*='price']"]:
                try:
                    t = card.find_element(By.CSS_SELECTOR, sel).text.strip()
                    if t:
                        price = t
                        break
                except:
                    pass

            results.append((title, price, url))
            if len(results) >= limit:
                break

        return results
    finally:
        driver.quit()


dns_search_selenium("iphone")