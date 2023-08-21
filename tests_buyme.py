from allure_commons.types import AttachmentType
import unittest
from selenium import webdriver
from base_page import Buyme_site
import json
import allure
def json_setup(self):
    json_file = open('C:/Users/nadav2022/PycharmProjects/pythonBuyMeProject/json_setup.json', 'r')
    data = json.load(json_file)
    return data
def screenshot(self):
    allure.attach(
        name="NoSuchElementScreenshot",
        body=self.driver.get_screenshot_as_png(),
        attachment_type=AttachmentType.PNG)
class basePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        data = json_setup(self)
        self.driver.get(data['url'])
    def test_sign_in(self):
        try:
            Buyme_site.sign_page(self)
            Buyme_site.assert_name(self)
        except:
            screenshot(self)
    def test_choose_gift(self):
        try:
            Buyme_site.choose_gift(self)
        except:
            screenshot(self)
    def test_send_info(self):
        try:
            data =json_setup(self)
            self.driver.get(data['url2'])
            Buyme_site.send_info(self)
        except:
            screenshot(self)
    def tearDown(self):
        self.driver.quit()
