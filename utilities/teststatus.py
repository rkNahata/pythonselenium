from base.selenium_driver import SeleniumDriver
import utilities.logging_utility as cl
import logging
from traceback import print_stack


class TestStatus(SeleniumDriver):
    log = cl.customLoger(logging.DEBUG)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setTestResultStatus(self, result, resultMessage):

        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### Verification successful::" + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### Verification failed::" + resultMessage)
                    self.screenShot(resultMessage)

            else:
                self.resultList.append("FAIL")
                self.log.error("### Verification failed::" + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception occurred::" + resultMessage)
            self.screenShot(resultMessage)
            print_stack()

    def mark(self,result,resultMessage):
        self.setTestResultStatus(result, resultMessage)

    def markFinal(self, result, resultMessage, testName):

        self.setTestResultStatus(result, resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName+" ### Test failed")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName+ "### Test successful")
            self.resultList.clear()
            assert True == True

