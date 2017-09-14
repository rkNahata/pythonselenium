from base.base_page import BasePage
import utilities.logging_utility as cl
import logging

class RegisterCoursesPage(BasePage):
    log = cl.customLoger(logging.DEBUG)

    def __init__(self, driver):
        super(RegisterCoursesPage, self).__init__(self.driver)
        self.driver = driver

    #Locators


