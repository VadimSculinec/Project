from selenium.webdriver.common.by import By


class LocatorsOfProductPage:
    ADD_PRODUCT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".price_color")
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BOOK_NAME_FROM_ADDRESS = (By.XPATH, '//*[@class="active"]')
