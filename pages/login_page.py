import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocator


class LoginPage(BasePage):

    @allure.step("Переход на страницу востановления пароля")
    def get_click_restore(self):
        self.clik_to_element(LoginPageLocator.RESTORE_LOGIN)

    @allure.step("Запрос URL")
    def get_url_log(self):
        return self.url()

    @allure.step("Нажатие на поле ввода пороля")
    def get_click_sleep(self):
        self.clik_to_element(LoginPageLocator.SLEEP_PASWORD)



    def get_aktiv_paswoord(self):
        return self.find_element_with_wait(LoginPageLocator.CLICK_PASWORD)