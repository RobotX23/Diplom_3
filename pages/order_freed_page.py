import allure
from pages.base_page import BasePage
from locators.order_feed_locator import OrderFreedLocator



class OrderFreed(BasePage):

    @allure.step("Проверка нахождения в ленте заказа")
    def get_in_order(self):
        return self.find_element_with_wait(OrderFreedLocator.FREED_LOCATOR)