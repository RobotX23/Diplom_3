import allure
from pages.base_page import BasePage
from locators.order_feed_locator import OrderFreedLocator



class OrderFreed(BasePage):

    @allure.step("Проверка нахождения в ленте заказа")
    def get_in_order(self):
        return self.find_element_with_wait(OrderFreedLocator.FREED_LOCATOR)

    @allure.step("Нажатие на открытие заказа на открытие окна заказа")
    def get_order_open(self):
        return self.clik_to_one_element(OrderFreedLocator.ORDER)

    @allure.step("Открыто окно детали заказа")
    def get_order_open_class(self):
        return self.find_element_with_wait(OrderFreedLocator.DETALS)

    @allure.step("Страница заказа прогружена")
    def get_order_good(self):
        return self.find_element_good(OrderFreedLocator.ORDER_GOOD)

    @allure.step("получение всех заказов")
    def get_order_vile(self):
        return self.find_element_vile(OrderFreedLocator.ORDERES)

    @allure.step("Получение количества всего заказов")
    def get_total_order(self):
        return self.find_element_vile(OrderFreedLocator.TOTAL_ORDER)

    @allure.step("Заказы в работе")
    def get_at_work(self):
        return self.find_element_with_wait(OrderFreedLocator.AT_WORK)