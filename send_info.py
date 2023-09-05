
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from basepage2 import BasePage
class def_send_info(BasePage):
    def send_info(self):
        self.driver.implicitly_wait(10)
        self.enter_text(By.XPATH, value="//input[@class='ember-view ember-text-field']").send_keys('tom')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'selected-text'))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                               '//li[@class="ember-view bm-select-option"]'))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,
                                                                               'textarea-clear-all'))).click()
        self.driver.find_element(By.CLASS_NAME, value="parsley-success"). \
            send_keys('מי יתן ותלך בדרך השושנים ולא בדרך הקוצים')
        image_path = 'C:/Users/nadav2022/OneDrive/שולחן העבודה/photos to python/photoBuyme.jpg'
        self.driver.find_element(By.XPATH, value='//input[@type="file"]').send_keys(image_path)
        self.click_element(By.XPATH, "//span[@class='label']")
        icon_list = self.driver.find_elements(By.CLASS_NAME, value='method-icon')
        icon_list[1].click()
        self.enter_text(By.ID, value='email').send_keys('tom@gmail.com')
        self.enter_text(By.XPATH, value="//input[@placeholder='שם שולח המתנה']").send_keys('tom')
        element2 = self.driver.find_element(By.XPATH, value="//input[@placeholder='שם שולח המתנה']")
        name = element2.get_attribute('value')
        assert name == 'tom'