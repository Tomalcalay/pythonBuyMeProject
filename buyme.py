import sign_in_page
import send_info
import choose_gift
class buyme_site():
    def _init_(self, driver):
        self.driver = driver
    def sign_in_page(self):
        sign_in_page.def_sign.sign_page(self)
    def assert_name(self):
        sign_in_page.def_sign.assert_name(self)

    def choose_gift(self):
        choose_gift.def_choose.choose_gift(self)
    def send_info(self):
        send_info.def_send_info.send_info(self)


