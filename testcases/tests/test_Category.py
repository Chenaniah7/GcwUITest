
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from testcases.pages.categoryPage import CategoryPage
from selenium.webdriver.support import expected_conditions as EC
from testcases.tests.test_AdminLogin import TestAdminLogin
from time import sleep

class TestCategory(object):

    category_data = [
        ('','python', 'test', '分类名称不能为空'),
        ('test','python', 'test', ''),
    ]

    def setup_class(self) -> None:
        self.login = TestAdminLogin()
        self.categoryPage = CategoryPage(self.login)

    # 测试文章分类
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    @pytest.mark.parametrize('name,parent,slug,expected', category_data)
    def test_add_category(self, name, parent, slug, expected):

        if name == '':
            # 点击文章
            self.categoryPage.click_article()
            # 点击分类
            self.categoryPage.click_category()

        # 输入分类名称
        self.categoryPage.input_category_name(name)

        # 选择父分类
        self.categoryPage.select_parent_category(parent)

        # 输入slug
        self.categoryPage.input_slug(slug)

        # 点击添加
        self.categoryPage.click_add_btn()

        if name == '':
            loc = (By.CLASS_NAME, 'toast-message')
            WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))
            msg = self.login.driver.find_element(*loc).text
            assert msg == expected
            sleep(5)
        else:
            assert 1 == 1

# if __name__ == '__main__':
#     # 这里可以跳过登录错误
#     pytest.main(['test_Category.py'])
