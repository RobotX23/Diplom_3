import allure
from pages.base_page import BasePage
from locators.person_area_page_locators import PesronAreaPageLocators



class PersonArea(BasePage):

    @allure.step("Проверка перехода в личный кабинет")
    def get_profile(self):
        return self.find_element_with_wait(PesronAreaPageLocators.PROFILE)


    @allure.step("Нажатие на кнопку истории заказов")
    def get_ckick_history(self):
        self.clik_to_element(PesronAreaPageLocators.HISTORY_ORDERS)


    @allure.step("Нажатие на кнопку истории заказов")
    def get_history_good(self):
        self.find_element_good(PesronAreaPageLocators.ORDER_GOOD)



    @allure.step("Нажатие на кнопку выход")
    def get_exit(self):
        self.clik_to_element(PesronAreaPageLocators.EXIT)

    @allure.step("Выход по кнопке успешен")
    def get_order_good(self):
        return self.find_element_good(PesronAreaPageLocators.ORDER_GOOD)


    @allure.step("получение последнего номера заказа")
    def get_num(self):
        return self.find_element_one(PesronAreaPageLocators.ORDER)