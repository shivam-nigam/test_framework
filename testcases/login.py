from pages.login_page import LoginPage
from utility.drivermanager import DriverManager

import time

class LoginTest(DriverManager):
    
    def login_test(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login(user_name="QA_traininguser13", password="Empirix!")
        time.sleep(10)
