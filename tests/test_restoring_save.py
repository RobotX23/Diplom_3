import pytest

from pages.restore_page import RestorePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import *
import allure


class TestRestoreSave:

    @allure.title('Переход по кнопке восстановление пароля через главное окно')
    @pytest.mark.parametrize('url', [url_restore])
    def test_click_restore(self, driver, url):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_entrance()
        login_page = LoginPage(driver)
        login_page.get_click_restore()
        assert login_page.get_url_log() == url


    @allure.title('Переход по кнопке восстановление пароля через личный кабинет')
    @pytest.mark.parametrize('url', [url_restore])
    def test_click_restore_1(self, driver, url):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_cabinet()
        login_page = LoginPage(driver)
        login_page.get_click_restore()
        assert login_page.get_url_log() == url

    @allure.title('Ввод email и восстановленипароля')
    @pytest.mark.parametrize('email', [email])
    def test_email_to_ckick(self, driver, email):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_cabinet()
        login_page = LoginPage(driver)
        login_page.get_click_restore()
        restore_page = RestorePage(driver)
        restore_page.get_email(email=email)
        restore_page.get_restore_button()
        assert restore_page.url() != url_restore


    @allure.title('Скрытие пароля')
    def test_password_sleep(self, driver):
        main_page = MainPage(driver)
        main_page.get_sleep()
        main_page.get_click_cabinet()
        login_page = LoginPage(driver)
        login_page.get_click_sleep()
        a = login_page.get_aktiv_paswoord()
        assert a.get_attribute('class')== class_sleep


