from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def add_to_basket_page_asserts(self):
        self.should_be_success_message()
        self.should_be_basket_total()
    def add_product_to_basket(self):
        busket = self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON)
        busket.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == success_message, "Product name is not in the success message"

    def should_be_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Basket total is not presented"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, "Product price is not in the basket total"