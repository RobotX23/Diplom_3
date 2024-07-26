from selenium.webdriver.common.by import By

class MainPageLocator:
    COME = By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    CABINET = By.XPATH, ".//p[(@class='AppHeader_header__linkText__3q_va ml-2') and (text()='Личный Кабинет')]"
    FLAG = By.XPATH, ".//p[(@class='BurgerIngredient_ingredient__text__yp3dH') and (text()='Краторная булка N-200i')]"