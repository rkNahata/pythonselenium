from base.selenium_driver import SeleniumDriver
from utilities.utils import Utils
import logging
import utilities.logging_utility as cl
from traceback import print_stack


class BasePage(SeleniumDriver):
    log = cl.customLoger(logging.DEBUG)

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver

    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return Utils.verifyTextMatch(self.actualText, titleToVerify)
        except:
            self.log.error('### Cannot find title')
            print_stack()
            return False
