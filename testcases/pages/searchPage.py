from time import sleep

from selenium.webdriver.common.by import By

from testcases.pages.basePage import BasePage


class SearchPage(BasePage):
    search_input = (By.ID, u'kw')
    search_btn = (By.ID, u'su')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_baidu_home(self):
        self.driver.get('http://www.baidu.com')

    def input_kw(self):
        self.type_text('selenium', *self.search_input)

    def click_search_btn(self):
        self.click(*self.search_btn)
        sleep(2)


