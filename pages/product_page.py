from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.base_pages import BasePage
from pages.locators import LocatorsOfProductPage


class ProductPage(BasePage):

    def add_product(self):
        button = self.browser.find_element(*LocatorsOfProductPage.ADD_PRODUCT)
        button.click()

    def should_be_button_add(self):
        assert self.browser.find_element(*LocatorsOfProductPage.ADD_PRODUCT), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def extract_text_book_from_adress(self):
        book_name = self.browser.find_element(*LocatorsOfProductPage.BOOK_NAME_FROM_ADDRESS)
        return book_name.text

    def extract_text_book(self):
        book_name = self.browser.find_element(*LocatorsOfProductPage.BOOK_NAME)
        return book_name.text

    def extract_text_price(self):
        book_name = self.browser.find_element(*LocatorsOfProductPage.BOOK_NAME)
        return book_name.text

    def should_correct_book_name(self, book_name_expected, book_name_actual, price_expected=None, price_actual=None):
        assert book_name_expected == book_name_actual, f'{book_name_actual} not equal {book_name_expected}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*LocatorsOfProductPage.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*LocatorsOfProductPage.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
