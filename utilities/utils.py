import utilities.logging_utility as cl
import logging


class Utils(object):
    log = cl.customLoger(logging.DEBUG)

    def verifyTextMatch(self, actualText, expectedText):

        self.log.info("Actual text is ::" + actualText)
        self.log.info("Expected text is ::" + expectedText)

        if actualText.lower() == expectedText.lower():
            self.log.info("### Verification successful")
            return True
        else:
            self.log.error("### Verification failed")
            return False
