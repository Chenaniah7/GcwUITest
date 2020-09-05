import pytest
from selenium.webdriver.support.wait import WebDriverWait

from testcases.pages.adminLoginPage import AdminLoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from util import util


class TestAdminLogin(object):
    admin_login_data = [
        ('admin', '123456', '666', '验证码不正确，请重新输入'),
        ('admin', 'gcw60777', '111', 'JPress后台'),
    ]

    def setup_class(self) -> None:
        self.driver = webdriver.Chrome()
        self.adminLoginPage = AdminLoginPage(self.driver)
        self.adminLoginPage.goto_admin_login_page()

    # 测试管理员登录验证码错误
    # @pytest.mark.skip()
    @pytest.mark.dependency(name='admin_login')
    @pytest.mark.parametrize('username,pwd,captcha,expected', admin_login_data)
    def test_admin_login(self, username, pwd, captcha, expected):

        self.adminLoginPage.input_username(username)
        self.adminLoginPage.input_pwd(pwd)
        if captcha != '666':  # 如果不是错误验证码就调用第三方接口去识别正确的验证码
            captcha = util.get_code(self.driver, '//form[@id="form"]/div[3]/img')
        self.adminLoginPage.input_captcha(captcha)
        self.adminLoginPage.click_admin_login_btn()

        if captcha != '666':
            WebDriverWait(self.driver, 10).until(EC.title_is(expected))
            assert expected == self.driver.title  # 断言登录成功
        else:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert

            assert alert.text == expected  # 断言登录失败
            alert.accept()

            sleep(5)
        # self.driver.close()

# if __name__ == '__main__':
#     pytest.main(['test_AdminLogin.py'])
