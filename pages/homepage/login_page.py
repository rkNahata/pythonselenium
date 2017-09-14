from base.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = ".//*[@id='navbar']//a[contains(text(),'Login')]"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = ".btn.btn-primary.btn-md.login-button"
    _user_icon = " "
    _login_error_message = "//div[contains(text(),'Invalid email or password')]"

    # Actions
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType='xpath')

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="css")

    def successfulLogin(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        return not self.isElementPresent(self._login_error_message, "xpath")

    def failureLogin(self, email=" ", password=" "):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        #return self.isElementPresent(self._login_error_message, "xpath")
        return False
