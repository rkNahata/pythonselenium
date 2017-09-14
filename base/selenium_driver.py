from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_stack
import utilities.logging_utility as cl
import logging
import time
import os


class SeleniumDriver:
    log = cl.customLoger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " is incorrect")
            return False

    def getElement(self, locator, locatorType):

        element = None

        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found")
        except:
            self.log.info("Element not found")
        return element

    def getElementList(self, locator, locatorType="id"):

        elements = None

        try:
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Element found")
        except:
            self.log.info("Element not found")
        return elements

    def elementClick(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked the element with Locator: " + locator + "and LocatorType: " + locatorType)

        except:
            self.log.info("Unable to click the element with Locator: " + locator + "and LocatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("sent data to the element with Locator: " + locator + "and LocatorType: " + locatorType)

        except:
            self.log.info(
                "Unable to send the data to element with Locator: " + locator + "and LocatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                return True
            else:
                return False
        except:
            self.log.info("Element Not found")
            return False

    def waitForElement(self, locator, locatorType, timeout=10, pollFrequency=.5):
        element = None

        try:
            byType = self.getByType(locatorType)
            wait = WebDriverWait(self.driver, timeout, pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
        except:
            self.log.error("### Exception occured")
            print_stack()

        return element

    def screenShot(self, resultMessage):
        fileName = resultMessage + "_" + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occured")
            print_stack()

    def isElementVisible(self, locator, locatorType):

        element = self.getElement(locator, locatorType)
        isDisplayed = element.is_displayed()

        return isDisplayed

    def isElementPresent(self, locator, byType):

        elements = self.driver.find_elements(byType, locator)

        if len(elements) > 0:
            self.log.info("Element is present with Locator id:" + locator)
            return True
        else:
            self.log.info("Element not present with Locator id:" + locator)
            return False

    def webScroll(self, direction='up'):

        if direction == 'up':
            self.driver.execute_script("window.scrollBy(0, -1000);")

        else:
            self.driver.execute_script("window.scrollBy(0, 1000);")
