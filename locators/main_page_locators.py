from selenium.webdriver.common.by import By

class MainPageLocator:
    COME = By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    CABINET = By.XPATH, ".//p[(@class='AppHeader_header__linkText__3q_va ml-2') and (text()='Личный Кабинет')]"
    FLAG = By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']"
    ORDER_FREED = By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Лента Заказов']"
    ING = By.XPATH, ".//img[@class='BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4' and @alt='Флюоресцентная булка R2-D3']"
    INGRED = By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']"
    CLOSE_INGRED = By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/div/button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    ADD = By.XPATH, ".//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']"
    INGREDIENT_ONE = By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Флюоресцентная булка R2-D3']"
    COUNTER = By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Флюоресцентная булка R2-D3']/parent::a/div[@class='counter_counter__ZNLkj counter_default__28sqi']/p"
    ORDER = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    ORDER_OK = By.XPATH, ".//p[@class='undefined text text_type_main-small mb-2']"
    CLOSE_ORDER = By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    CLOSE_ORDER_GOOD = By.XPATH, ".//div[@class='Modal_modal__P3_V5']"