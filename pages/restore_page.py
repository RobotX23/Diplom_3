import allure
from pages.base_page import BasePage
from locators.restore_page_locator import RestorePageLocator


class RestorePage(BasePage):

    @allure.step("Ввод email")
    def get_email(self, email):
        self.add_text_to_element(RestorePageLocator.RESTORE, email)

    @allure.step("Нажатие кнопки восстановить")
    def get_restore_button(self):
        self.clik_to_element(RestorePageLocator.BUTTON)

    @allure.step("Нахождение на странице восстановления пароля")
    def get_restore(self):
        return self.find_element_with_wait(RestorePageLocator.RESTOR)