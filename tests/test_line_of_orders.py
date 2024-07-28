import pytest
import time
from pages.restore_page import RestorePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_freed_page import OrderFreed
from pages.person_area_page import PersonArea
from data import *
import allure


class TestLineOfOrders:


    @allure.title('Открытие окна детали заказа')
    @pytest.mark.parametrize('classe', [(class_order)])
    def test_order_open(self, driver, classe):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_order()
        order_page=OrderFreed(driver)
        order_page.get_order_good()
        order_page.get_in_order()
        order_page.get_order_open()
        a = order_page.get_order_open_class()
        assert a.get_attribute('class') == classe


    @allure.title('Проверка нахождения заказа пользователя в ленте заказов')
    @pytest.mark.parametrize('email, password', [(email,password)])
    def test_zakaz_person(self, driver, email, password):
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
        main_page.get_ing_order_ok()
        main_page.get_close_order()
        main_page.get_close_order_good()
        main_page.get_click_cabinet()
        person_page = PersonArea(driver)
        person_page.get_ckick_history()
        person_page.get_order_good()
        a = person_page.get_num()
        numer = a.text
        main_page.get_click_order()
        order_page = OrderFreed(driver)
        order_page.get_order_good()
        a = order_page.get_order_vile()
        b = []
        for i in range(len(a)):
            b.append(str(a[i].text))
        if str(numer) in b:
            c = True
        else:
            c = False
        assert c == True

    @allure.title('Проверка увеличение счетчика заказов')
    @pytest.mark.parametrize('email, password', [(email,password)])
    def test_zakaz_total(self, driver, email, password):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_order()
        order_page = OrderFreed(driver)
        order_page.get_order_good()
        a = order_page.get_total_order()[0]
        numb = a.text
        main_page.get_click_cabinet()
        login_page = LoginPage(driver)
        login_page.get_email(email=email)
        login_page.get_password(password=password)
        login_page.get_click_entrance()
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_add_ing()
        main_page.get_ing_order()
        main_page.get_ing_order_ok()
        main_page.get_close_order()
        main_page.get_close_order_good()
        main_page.get_click_order()
        order_page = OrderFreed(driver)
        order_page.get_order_good()
        a = order_page.get_total_order()[0]
        numbe = a.text
        assert int(numbe) > int(numb)


    @allure.title('Проверка увеличение счетчика заказов за сегодня')
    @pytest.mark.parametrize('email, password', [(email,password)])
    def test_zakaz_total_event(self, driver, email, password):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_order()
        order_page = OrderFreed(driver)
        order_page.get_order_good()
        a = order_page.get_total_order()[1]
        numb = a.text
        main_page.get_click_cabinet()
        login_page = LoginPage(driver)
        login_page.get_email(email=email)
        login_page.get_password(password=password)
        login_page.get_click_entrance()
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_add_ing()
        main_page.get_ing_order()
        main_page.get_ing_order_ok()
        main_page.get_close_order()
        main_page.get_close_order_good()
        main_page.get_click_order()
        order_page = OrderFreed(driver)
        order_page.get_order_good()
        a = order_page.get_total_order()[1]
        numbe = a.text
        assert int(numbe) > int(numb)

    @allure.title('Проверка увеличение счетчика заказов за сегодня')
    @pytest.mark.parametrize('email, password', [(email,password)])
    def test_zakaz_at_work(self, driver, email, password):
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
        main_page.get_ing_order_ok()
        main_page.get_close_order()
        main_page.get_close_order_good()
        main_page.get_click_cabinet()
        person_page = PersonArea(driver)
        person_page.get_ckick_history()
        person_page.get_order_good()
        a = person_page.get_num()
        numer = a.text
        main_page.get_click_order()
        order_page = OrderFreed(driver)
        order_page.get_order_good()
        a = order_page.get_at_work()
        assert str(a.text) == str(numer).replace("#","")
