# -*- coding:utf-8 -*-
# @Time : 2022/10/4 11:08
# @Author: 彭小钗
# @File : menu_page.py

from selenium.webdriver.common.by import By
from common.common_fun import Common

class MenuPage(Common):
    # 9 - Day Forecast button
    nine_day_forecase_btn = (By.XPATH, '//*[@text="九天預報"]')

    #click nine day forecase button
    def click_nine_day_forecase_button(self):
        self.click(self.nine_day_forecase_btn)

