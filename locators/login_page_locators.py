from selenium.webdriver.common.by import By


class LoginPageLocator:
    RESTORE_LOGIN = By.XPATH, ".//p[@class='undefined text text_type_main-default text_color_inactive']/a[@class='Auth_link__1fOlj']"
    CLICK_PASWORD = By.XPATH, ".//label[@class='input__placeholder text noselect text_type_main-default input__placeholder-focused']"
    SLEEP_PASWORD = By.XPATH, ".//div[@class='input__icon input__icon-action']"



