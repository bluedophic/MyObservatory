# -*- coding:utf-8 -*-
# @Time : 2022/10/1 22:35
# @Author: 彭小钗
# @File : home_page.py

from selenium.webdriver.common.by import By
from common.common_fun import Common

class HomePage(Common):
    #menu button
    menu_btn = (By.XPATH, "//*[@content-desc='转到上一层级']")

    #click menu button
    def click_menu_button(self):
        self.click(self.menu_btn)