from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time
import pytest

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/')
        self.page.open()
        self.page.go_to_login_page()
        self.page.register_new_user(str(time.time()) + "@pythonmail.ru", str(time.time()) + "Password123!!!")
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # открытие страницы
        self.link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = MainPage(browser, self.link)
        page.open()

        # проверка на наличие промокода
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_promo()

        # добавление товара в корзину.
        browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form [type='submit']").click()
        page.solve_quiz_and_get_code()
        time.sleep(5)
        # проверка соответствия названия добавленного элемента с имеющимся в инфологе
        product_page.product_in_basket_match_added(browser)

        # проверка соответствия цены добавленного элемента с суммой корзины
        product_page.price_in_basket_match_added(browser)

        # проверка наличия сообщения об успешности добавленного товара
        product_page.should_be_success_message()
        browser.close()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):

    #открытие страницы
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)
    page.open()

    # проверка на наличие промокода
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_promo()

    # добавление товара в корзину.
    browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form [type='submit']").click()
    page.solve_quiz_and_get_code()
    time.sleep(5)

    # проверка соответствия названия добавленного элемента с имеющимся в инфологе
    product_page.product_in_basket_match_added(browser)

    # проверка соответствия цены добавленного элемента с суммой корзины
    product_page.price_in_basket_match_added(browser)

    # проверка наличия сообщения об успешности добавленного товара
    product_page.should_be_success_message()
    browser.close()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    # Открываем страницу товара
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)
    page.open()

    # Добавляем товар в корзину
    browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form [type='submit']").click()
    page.solve_quiz_and_get_code()
    time.sleep(5)

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()
    browser.close()



def test_guest_cant_see_success_message(browser):

    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()
    browser.close()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):


    # Открываем страницу товара
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form [type='submit']").click()
    page.solve_quiz_and_get_code()
    time.sleep(5)

    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_message_of_is_disappeared()
    browser.close()

def test_guest_should_see_login_link_on_product_page(browser):

    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    # Проверяем, что гость видит ссылку на страницу логина
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):

    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    # Переходит на страницу логина
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    # Переходит в корзину по кнопке в шапке
    time.sleep(3)
    page.go_to_basket_page()

    # Ожидаем, что в корзине нет товаров
    basketPage = BasketPage(browser, link)
    basketPage.empty_basket_check()

    # Ожидаем, что есть текст о том что корзина пуста
    basketPage.should_be_text_basket_is_empty()

@pytest.mark.skip
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):

    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    # Переходит в корзину по кнопке в шапке
    time.sleep(3)
    page.go_to_basket_page()

    # Ожидаем, что в корзине есть товары
    basketPage = BasketPage(browser, link)
    basketPage.not_empty_basket_check()

    # Ожидаем, что нет текста о том что корзина пуста
    basketPage.not_should_be_text_basket_is_empty()


