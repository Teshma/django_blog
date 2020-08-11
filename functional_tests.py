from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class CVPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("http://127.0.0.1:8000/admin")


    def tearDown(self):
        self.browser.quit()

    def test_can_create_a_cv_and_save_it(self):
        ## enter cv page
        self.browser.get("http://127.0.0.1:8000")
        ## click on cv button
        cv_button = self.browser.find_element_by_id("cv_button")
        cv_button.click()
        ## on cv page
        self.assertIn("cv", self.browser.current_url)
        ## check if cv already exists
        delete_cv_button = self.browser.find_element_by_id("delete_cv_button")
        if delete_cv_button:
            delete_cv_button.click()
        ## click on new
        new_cv_button = self.browser.find_element_by_id("new_cv_button")
        new_cv_button.click()
        ## landed on new cv page
        self.assertIn("cv/new", self.browser.current_url)
        ## enter some text
        first_section_text_box = self.browser.find_element_by_id("id_first_section_text")
        first_section_text_box.send_keys("Personal Profile Text")
        ## save
        save_button = self.browser.find_element_by_id("id_save_button")
        save_button.click()
        ## page redirects to the updated cv
        self.assertIn("cv", self.browser.current_url)
        ## cv has been saved and is viewable
        title = self.browser.find_element_by_id("title").text
        self.assertIn("My CV", title)

        

if __name__ == "__main__":
    unittest.main()