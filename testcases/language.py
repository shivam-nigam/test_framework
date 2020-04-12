from pages.index_page import IndexPage
from pages.login_page import LoginPage
from utility.drivermanager import DriverManager

import time


class LanguageTest(DriverManager):

    def language_test(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login(user_name="QA_traininguser13", password="Empirix!")
        self.index_page = IndexPage(self.driver)
        self.index_page.switch_language(language="Japanese")
        self.index_page.switch_language(language="English")
        time.sleep(10)
