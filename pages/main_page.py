import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocator


class MainPage(BasePage):

    @allure.step("Ожидание полной занрузки страницы")
    def get_sleep(self):
        self.sleep(MainPageLocator.FLAG)

    @allure.step("Переход на страницу входа в аккаунт")
    def get_click_entrance(self):
        self.clik_to_element(MainPageLocator.COME)

    @allure.step("Переход на страницу личного кабинета")
    def get_click_cabinet(self):
        self.clik_to_element(MainPageLocator.CABINET)


    @allure.step("Переход к странице заказа")
    def go_to_order_page(self, num):
        if num == 0:
            self.scroll_to_element(MainPageLocator.ORDER_1)
            self.clik_to_element(MainPageLocator.ORDER_1)
        else:
            self.scroll_to_element(MainPageLocator.ORDER_2)
            self.clik_to_element(MainPageLocator.ORDER_2)

    @allure.step("Переход на главную страницу")
    def scoter(self):
        self.clik_to_element(MainPageLocator.SCOTER)
        return self.url()

    @allure.step("Переход на страницу Яндекса")
    def yandex(self):
        self.clik_to_element(MainPageLocator.YANDEX)
        self.window()
        time.sleep(10)
        return self.url()