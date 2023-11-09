from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
   LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
   REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUSKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    PRODUCT_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    BASKET_TOTAL = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p")

