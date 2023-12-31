from allure_commons.types import AttachmentType
import unittest
from selenium import webdriver
from base_page import buyme_site
import json
import allure
from selenium.webdriver.chrome.options import Options
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
        chrome_options = Options()
        chrome_options.add_argument("--headless")
    def test_sign_in(self):
        try:
            buyme_site.sign_page(self)
            buyme_site.assert_name(self)
        except:
            screenshot(self)
    def test_choose_gift(self):
        try:
            buyme_site.choose_gift(self)
        except:
            screenshot(self)
    def test_send_info(self):
        try:
            data =json_setup(self)
            self.driver.get(data['url2'])
            buyme_site.send_info(self)
        except:
            screenshot(self)
    def tearDown(self):
        self.driver.quit()
