from selenium.webdriver.common.by import By


class OrderFreedLocator:
    FREED_LOCATOR = By.XPATH, ".//h1[@class='text text_type_main-large mt-10 mb-5']"
    ORDER = By.XPATH,".//p[@class='text text_type_digits-default']"
    DETALS = By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"
    ORDER_GOOD = By.XPATH, ".//div[@class='OrderFeed_orderFeed__2RO_j']"
    ORDERES = By.XPATH,  ".//p[@class='text text_type_digits-default']"
    TOTAL_ORDER = By.XPATH, ".//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    AT_WORK = By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']"
