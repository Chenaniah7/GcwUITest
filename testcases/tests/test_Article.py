import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from testcases.pages.articlePage import ArticlePage
from selenium.webdriver.support import expected_conditions as EC
from testcases.tests.test_AdminLogin import TestAdminLogin
from time import sleep


class TestArticle(object):
    article_data = [
        ('我的文章', '我的文章内容', '文章保存成功。')
    ]

    def setup_class(self) -> None:
        self.login = TestAdminLogin()
        self.articlePage = ArticlePage(self.login)


    # 测试添加文章
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    @pytest.mark.parametrize('title, content, expected', article_data)
    def test_add_ok(self, title, content, expected):
        self.articlePage.click_article()
        self.articlePage.click_article_manage()
        self.articlePage.click_add_article()
        sleep(1)

        self.articlePage.input_article_title(title)
        self.articlePage.input_body(content)
        self.articlePage.click_add_btn()

        loc = (By.CLASS_NAME, 'toast-message')

        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        assert msg == expected

        sleep(2)

    # 测试删除单个文章
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_delete_one_article_ok(self):
        # 接上一个添加文章测试，不用再点击文章链接，直接点击文章管理
        # 点击文章管理
        self.articlePage.click_article_manage()
        # 删除文章
        self.articlePage.del_single_article()

        sleep(3)

    # 测试删除所有文章
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_delete_all_article_ok(self):
        self.articlePage.del_all_article()




# if __name__ == '__main__':
#     # 这里可以跳过登录错误
#     pytest.main(['test_Article.py'])
