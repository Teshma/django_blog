from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class CVPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_updating_a_cv_and_save_it(self):
        ## enter cv page
        self.browser.get("http://127.0.0.1:8000")
        ## click on cv button
        cv_button = self.browser.find_element_by_tag_name("cv_button")
        cv_button.click()
        ## click on update
        ## enter some text
        ## save
        ## page redirects to the updated cv
        

if __name__ == "__main__":
    unittest.main()