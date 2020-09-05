
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from testcases.pages.userLoginPage import UserLoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep

class TestUserLogin(object):

    login_data=[
        ('','123456','账号不能为空'),
        ('admin', 'gcw60777', '用户中心'),
    ]

    def setup_class(self) -> None:
        self.driver = webdriver.Chrome()
        self.loginPage = UserLoginPage(self.driver)
        self.loginPage.goto_login_page()

    # 测试用户登录
    @pytest.mark.parametrize('username, pwd, expected', login_data)
    def test_user_login(self, username, pwd, expected):

        # 输入用户名
        self.loginPage.input_username(username)
        # 输入密码
        self.loginPage.input_pwd(pwd)
        # 点击登录
        self.loginPage.click_login_btn()

        sleep(3)
        # 验证
        if username != '':
            # 等待提示框
            WebDriverWait(self.driver, 5).until(EC.title_is(expected))
            sleep(3)
            # 验证
            assert self.driver.title == expected
        else:
            # 等待提示框
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == expected
            alert.accept()


# if __name__ == '__main__':
#     pytest.main(['-sv', 'test_UserLogin.py'])

    # jpxjopylueizbggg
