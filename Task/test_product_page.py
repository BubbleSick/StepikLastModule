from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import math
import time
import pytest

@pytest.mark.parametrize('promo', ["/?promo=offer0", "/?promo=offer1", "/?promo=offer2", "/?promo=offer3", "/?promo=offer4", "/?promo=offer5", "/?promo=offer6", pytest.param("/?promo=offer7", marks=pytest.mark.xfail(reason="Bug in offer7")), "/?promo=offer8", "/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.should_be_basket_total()
    page.should_be_success_message()