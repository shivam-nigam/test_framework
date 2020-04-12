# coding:utf-8
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class IndexPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.dropDown = "//a[contains(text(), 'QA_traininguser13(Empirix_QA_Training)')]"
        self.languageJav = "//a[contains(text(), 'Japanese')]"
        self.languageJavAl = "//div[contains(text(), 'Japanese')]"
        self.languageEng = "//a[contains(text(), 'English')]"
        self.languageEngAl = "//div[contains(text(), 'English')]"
        self.verifyJav = "//a[contains(text(), 'ダッシュボード')]"
        self.verifyEng = "//a[contains(text(), 'Dashboard')]"

    def switch_language(self, language):
        """
        This method is to login into page.

        return: instance of index page
        rtype: indexPage instance
        """

        logging.info("## Verifying login page ##")
        self.services.assert_and_click_by_xpath(self.dropDown)
        if language == "Japanese":
            if self.services.is_element_present(self.languageJavAl):
                logging.info("Already language is Japanese.")
            else:
                if self.services.is_element_present(self.languageJav):
                    self.services.assert_and_click_by_xpath(self.languageJav)
                    obj = self.driver.switch_to.alert
                    obj.accept()
                    self.services.wait_for_element(self.verifyJav)
                else:
                    raise Exception("Element is not present")
        else:
            if self.services.is_element_present(self.languageEngAl):
                logging.info("Already language is English")
            else:
                if self.services.is_element_present(self.languageEng):
                    self.services.assert_and_click_by_xpath(self.languageEng)
                    obj = self.driver.switch_to.alert
                    obj.accept()
                    self.services.wait_for_element(self.verifyEng)
                else:
                    raise Exception("Element is not present")

