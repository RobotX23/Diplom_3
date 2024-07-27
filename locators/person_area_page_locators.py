from selenium.webdriver.common.by import By

class PesronAreaPageLocators:
    PROFILE = By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"
    HISTORY_ORDERS = By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']"
    IN_HISTORY = By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and text()='История заказов']"
    EXIT = By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"