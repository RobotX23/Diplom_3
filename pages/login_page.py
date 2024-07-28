import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocator



class LoginPage(BasePage):

    @allure.step("Переход на страницу востановления пароля")
    def get_click_restore(self):
        self.clik_to_element(LoginPageLocator.RESTORE_LOGIN)


    @allure.step("Нажатие на поле ввода пороля")
    def get_click_sleep(self):
        self.clik_to_element(LoginPageLocator.SLEEP_PASWORD)

    @allure.step("Нажатие на кнопку входа")
    def get_click_entrance(self):
        self.clik_to_element(LoginPageLocator.ENTRANCE)

    @allure.step("Проверка нахождения на странице авторизации")
    def get_in_avtoriz(self):
        return self.find_element_with_wait(LoginPageLocator.ENT)

    @allure.step("Ввод почты")
    def get_email(self, email):
        self.add_text_to_element(LoginPageLocator.EMAIL, email)

    @allure.step("Ввод пароля")
    def get_password(self, password):
        self.add_text_to_element(LoginPageLocator.PASSWORD, password)

    @allure.step("Проверка подсветки поля ввода пароля")
    def get_aktiv_paswoord(self):
        return self.find_element_with_wait(LoginPageLocator.CLICK_PASWORD)


    @allure.step("Нажатие на кнопку конструктора")
    def get_click_konst(self):
        self.clik_to_element(LoginPageLocator.KONST)