import pytest
from selenium import webdriver




@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://stellarburgers.nomoreparties.site/")


    elif request.param == 'firefox':
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


