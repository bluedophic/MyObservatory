# -*- coding:utf-8 -*-
# @Time : 2022/10/1 22:02
# @Author: 彭小钗
# @File : base_page.py

from selenium.webdriver.support.wait import WebDriverWait

class Base():
    def __init__(self, driver):
        # initialize appium driver
        self.driver = driver

    #locate the element
    def locator(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    #input text
    def input_(self, loc, text):
        #clear the value of text
        el = self.locator(loc).clear()
        #input text
        el.send_keys(text)

    #click the element
    def click(self, loc):
        self.locator(loc).click()

    #get text
    def get_text(self, loc):
        return self.locator(loc).text
