import pytest
import unittest
from pages.homepage.login_page import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures('oneTimeSetUp')
class LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        result = self.lp.successfulLogin('test@email.com', 'abcabc')
        self.ts.markFinal(result, "Loggedin successfully", "test_validLogin")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        result = self.lp.failureLogin("est@email.com", "acbbc")
        self.ts.mark(result, "Login failed")
