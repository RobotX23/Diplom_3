import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_freed_page import OrderFreed
from data import *
import allure


class TestMainFunctionality:


    @allure.title('Переход на старницу конструктора')
    def test_const(self, driver):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_entrance()
        login_page = LoginPage(driver)
        login_page.get_click_konst()
        main_page_1 = MainPage(driver)
        a = main_page_1.get_home()
        assert a.text== 'Соберите бургер'


    @allure.title('Переход на страницу ленты заказов')
    def test_lent(self, driver):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_order()
        order_page = OrderFreed(driver)
        a = order_page.get_in_order()
        assert a.text== 'Лента заказов'


    @allure.title('Нажатие на ингридиент')
    def test_ing(self, driver):
        main_page = MainPage(driver)
        main_page.get_sleep()
        a = main_page.get_ing()
        assert a.text == 'Детали ингредиента'

    @allure.title('Закрытие ингредиента')
    def test_ing_close(self, driver):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_ing()
        main_page.get_ing_close()
        a = main_page.get_home()
        assert a.text == 'Соберите бургер'

    @allure.title('Добаление ингредиента')
    def test_add_ing(self, driver):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_add_ing()
        a = main_page.get_add_counter()
        assert a.text == '2'

    @allure.title('Оформление заказа авторизованным пользователем')
    @pytest.mark.parametrize('email, password', [(email,password)])
    def test_zakaz(self, driver, email, password):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_entrance()
        login_page = LoginPage(driver)
        login_page.get_email(email=email)
        login_page.get_password(password=password)
        login_page.get_click_entrance()
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_add_ing()
        main_page.get_ing_order()
        a= main_page.get_ing_order_ok()
        assert a.text == 'Ваш заказ начали готовить'