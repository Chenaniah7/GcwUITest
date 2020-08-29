from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from testcases.pages.basePage import BasePage


class CategoryPage(BasePage):

    def __init__(self, login):
        BasePage.__init__(self, login.driver)

    # 文章loc
    click_article_loc = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]')
    # 分类loc
    click_category_loc = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a')
    # 分类名称loc
    category_name_loc = (By.NAME, 'category.title')
    # 父分类loc
    parent_category_loc = (By.NAME, 'category.pid')

    # slug loc
    slug_loc = (By.NAME, 'category.slug')

    # 添加按钮
    add_btn_loc = (By.XPATH, '//button')

    # 点击文章
    def click_article(self):
        self.click(*self.click_article_loc)
        sleep(1)

    # 点击分类
    def click_category(self):
        self.click(*self.click_category_loc)
        sleep(1)

    # 输入分类名称
    def input_category_name(self, name):
        self.type_text(name, *self.category_name_loc)
        sleep(1)

    # 选择父分类
    def select_parent_category(self, parent_name):
        parent_category_elem = self.find_element(*self.parent_category_loc)
        Select(parent_category_elem).select_by_visible_text(parent_name)


    # 输入slug
    def input_slug(self, slug):
        self.type_text(slug, *self.slug_loc)

    # 点击添加
    def click_add_btn(self):
        self.click(*self.add_btn_loc)
