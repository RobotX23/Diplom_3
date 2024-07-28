from selenium.webdriver.common.by import By


class LoginPageLocator:
    RESTORE_LOGIN = By.XPATH, ".//p[@class='undefined text text_type_main-default text_color_inactive']/a[@class='Auth_link__1fOlj']"
    CLICK_PASWORD = By.XPATH, ".//label[@class='input__placeholder text noselect text_type_main-default input__placeholder-focused']"
    SLEEP_PASWORD = By.XPATH, ".//div[@class='input__icon input__icon-action']"
    EMAIL = By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']/input[@class='text input__textfield text_type_main-default']"
    PASSWORD = By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_password input_size_default']/input[@class='text input__textfield text_type_main-default']"
    ENTRANCE = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    ENT = By.XPATH, ".//h2[text()='Вход']"
    KONST = By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"






