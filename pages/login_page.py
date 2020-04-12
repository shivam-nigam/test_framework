import logging
from time import sleep

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.xpathHeading = "//strong[contains(text(),'Sign in to continue')]"
        self.userName = "//label[contains(text(),'Username')]//following::input"
        self.password = "//label[contains(text(),'Password')]//following::input"
        self.signIn = "//input[contains(@value, 'Sign in')]"
        self.dashboard = "//a[contains(text(), 'Dashboard')]"

    def login(self, user_name, password):
        """
        This method is to login into page.

        return: instance of index page
        rtype: indexPage instance
        """

        logging.info("## Verifying login page ##")
        self.services.wait_for_element(self.xpathHeading)
        self.driver.find_element_by_xpath(self.userName).send_keys(user_name)
        self.driver.find_element_by_xpath(self.password).send_keys(password)
        self.services.assert_and_click_by_xpath(self.signIn)
        self.services.wait_for_element(self.dashboard)