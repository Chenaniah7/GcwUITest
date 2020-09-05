import pytest
from selenium.webdriver.support.wait import WebDriverWait

from testcases.pages.userRegisterPage import UserRegisterPage
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from util import util


class TestUserRegister(object):
    account = util.gen_random_str()
    login_data = [
        ('test001', 'test001@qq.com', '123456', '123456', '666', '验证码不正确'),
        (account, account + "@qq.com", '123456', '123456', '111', '注册成功，点击确定进行登录。'),
    ]

    def setup_class(self) -> None:
        self.driver = webdriver.Firefox()
        self.registerPage = UserRegisterPage(self.driver)
        self.registerPage.goto_register_page()

    # 测试登录验证码错误
    @pytest.mark.parametrize('username,email,pwd,confirmPwd,captcha,expected', login_data)
    def test1_register(self, username, email, pwd, confirmPwd, captcha, expected):

        self.registerPage.input_username(username)
        self.registerPage.input_email(email)

        self.registerPage.input_pwd(pwd)
        self.registerPage.input_confirmPwd(confirmPwd)

        if captcha != '666':
            captcha = util.get_code(self.driver, 'captchaimg')

        self.registerPage.input_captcha(captcha)
        self.registerPage.click_register_btn()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected

        alert.accept()
        sleep(5)
        self.driver.close()


# if __name__ == '__main__':
#     pytest.main(['-sv', 'test_UserRegister.py'])
