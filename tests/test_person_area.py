import pytest
from pages.person_area_page import PersonArea
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import *
import allure
import time

class TestPersonArea:

    @allure.title('Переход по кнопке "Войти в аккаунт"')
    @pytest.mark.parametrize('email, password', [(email,password)])
    def test_click_entrance(self, driver, email, password):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_entrance()
        login_page = LoginPage(driver)
        login_page.get_email(email=email)
        login_page.get_password(password=password)
        login_page.get_click_entrance()
        main_page.get_click_cabinet()
        person_page = PersonArea(driver)
        a = person_page.get_profile()
        assert a.text == 'Профиль'


    @allure.title('Переход по кнопке "Личный кабинет"')
    @pytest.mark.parametrize('email, password', [(email,password)])
    def test_click_cabinet(self, driver, email, password):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_cabinet()
        login_page = LoginPage(driver)
        login_page.get_email(email=email)
        login_page.get_password(password=password)
        login_page.get_click_entrance()
        main_page.get_click_cabinet()
        person_page = PersonArea(driver)
        a = person_page.get_profile()
        assert a.text == 'Профиль'

    @allure.title('Переход в историю заказа')
    @pytest.mark.parametrize('email, password, url', [(email,password,url_history)])
    def test_click_history(self, driver, email, password, url):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_cabinet()
        login_page = LoginPage(driver)
        login_page.get_email(email=email)
        login_page.get_password(password=password)
        login_page.get_click_entrance()
        main_page.get_click_cabinet()
        person_page = PersonArea(driver)
        person_page.get_ckick_history()
        assert person_page.url() == url

    @allure.title('Выход из профиля')
    @pytest.mark.parametrize('email, password, class_exit', [(email,password, class_exit)])
    def test_exit(self, driver, email, password, class_exit):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_cabinet()
        login_page = LoginPage(driver)
        login_page.get_email(email=email)
        login_page.get_password(password=password)
        login_page.get_click_entrance()
        main_page.get_click_cabinet()
        person_page = PersonArea(driver)
        person_page.get_exit()
        login_page_1 = LoginPage(driver)
        a = login_page_1.get_in_avtoriz()
        assert a.text == 'Вход'