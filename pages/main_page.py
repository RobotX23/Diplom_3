import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocator




class MainPage(BasePage):

    @allure.step("Ожидание полной загрузки страницы")
    def get_sleep(self):
        self.sleep(MainPageLocator.CLOSE_ORDER_GOOD)

    @allure.step("Нахождение на главной странице")
    def get_home(self):
       return self.find_element_with_wait(MainPageLocator.FLAG)

    @allure.step("Переход на страницу входа в аккаунт")
    def get_click_entrance(self):
        self.clik_to_element(MainPageLocator.COME)

    @allure.step("Переход на страницу ленты заказов")
    def get_click_order(self):
        self.clik_to_element(MainPageLocator.ORDER_FREED)

    @allure.step("Переход на страницу личного кабинета")
    def get_click_cabinet(self):
        self.clik_to_element(MainPageLocator.CABINET)


    @allure.step("Нажатие на ингредиент")
    def get_ing(self):
        self.clik_to_element(MainPageLocator.ING)
        return self.find_element_with_wait(MainPageLocator.INGRED)



    @allure.step("Закрытие ингредиента")
    def get_ing_close(self):
        self.clik_to_element(MainPageLocator.CLOSE_INGRED)

    @allure.step("Добавление ингредиента")
    def get_add_ing(self):
        self.drag_and_drop_on_element(MainPageLocator.INGREDIENT_ONE, MainPageLocator.ADD)


    @allure.step("Увеличение ингредиента")
    def get_add_counter(self):
        return self.find_element_with_wait(MainPageLocator.COUNTER)

    @allure.step("Нажатие на кнопку оформление заказа")
    def get_ing_order(self):
        self.clik_to_element(MainPageLocator.ORDER)

    @allure.step("Заказ оформлен")
    def get_ing_order_ok(self):
        return self.find_element_with_wait(MainPageLocator.ORDER_OK)

    @allure.step("Закрыть окно заказа")
    def get_close_order(self):
        self.clik_to_esc()

    @allure.step("Окно заказа закрыто")
    def get_close_order_good(self):
        self.find_element_good(MainPageLocator.CLOSE_ORDER_GOOD)