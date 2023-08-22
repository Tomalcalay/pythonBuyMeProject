import time
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class buyme_site:
    def _init_(self, driver):
        self.driver = driver

    def sign_page(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CLASS_NAME, value='notSigned').click()
        self.driver.find_element(By.XPATH, '//span[@aria-label="להרשמה"]').click()
        self.driver.find_element(By.ID, 'ember1917').send_keys('tom')
        self.driver.find_element(By.ID, 'ember1924').send_keys('tom@gmail.com')
        self.driver.find_element(By.ID, 'valPass').send_keys('Atom1234')
        self.driver.find_element(By.ID, 'ember1938').send_keys('Atom1234')
        self.driver.find_element(By.CLASS_NAME, 'fill').click()
        self.driver.find_element(By.ID, 'ember1948').click()

    def assert_name(self):
        element = self.driver.find_element(By.ID, value="ember1917")
        name_text = element.get_attribute('value')
        assert name_text == 'tom'

    def choose_gift(self):
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//span[@title="סכום"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'ember1075'))).click()
        self.driver.find_element(By.XPATH, '//span[@title="אזור"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'ember1110'))).click()
        self.driver.find_element(By.XPATH, '//span[@title="קטגוריה"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'ember1172'))).click()
        self.driver.find_element(By.ID, value='ember1199').click()
        self.driver.set_page_load_timeout(10)
        assert self.driver.current_url == 'https://buyme.co.il/search?budget=1&category=419&region=11'
        self.driver.find_element(By.LINK_TEXT, value='BUYME CHEF - מגוון מסעדות שף').click()
        self.driver.find_element(By.XPATH, value="//input[@data-parsley-max='1500']").send_keys('100')
        self.driver.find_element(By.XPATH, value="//input[@data-parsley-max='1500']").send_keys(Keys.ENTER)

    def send_info(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, value="//input[@class='ember-view ember-text-field']").send_keys('tom')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'selected-text'))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                '//li[@class="ember-view bm-select-option"]'))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,
                                                                               'textarea-clear-all'))).click()
        self.driver.find_element(By.CLASS_NAME,value="parsley-success"). \
            send_keys('מי יתן ותלך בדרך השושנים ולא בדרך הקוצים')
        image_path = 'C:/Users/nadav2022/OneDrive/שולחן העבודה/photos to python/photoBuyme.jpg'
        self.driver.find_element(By.XPATH, value='//input[@type="file"]').send_keys(image_path)
        self.driver.find_element(By.XPATH, "//span[@class='label']").click()
        icon_list = self.driver.find_elements(By.CLASS_NAME, value='method-icon')
        icon_list[1].click()
        self.driver.find_element(By.ID,value='email').send_keys('tom@gmail.com')
        self.driver.find_element(By.XPATH,value="//input[@placeholder='שם שולח המתנה']").send_keys('tom')
        element2 = self.driver.find_element(By.XPATH,value="//input[@placeholder='שם שולח המתנה']")
        name = element2.get_attribute('value')
        assert name == 'tom'