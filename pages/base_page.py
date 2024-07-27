from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    def clik_to_element(self, locator):
        WebDriverWait(self.driver, 100).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def sleep(self, locator):
        WebDriverWait(self.driver, 100).until(
            expected_conditions.presence_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def add_text_to_element(self, locator, text):
        text_area = self.driver.find_element(*locator)
        text_area.clear()
        text_area.click()
        text_area.send_keys(text)


    def get_text_fo_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_lokators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    def url(self):
        return self.driver.current_url

    def window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()