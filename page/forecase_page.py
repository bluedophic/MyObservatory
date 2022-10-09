# -*- coding:utf-8 -*-
# @Time : 2022/10/4 16:58
# @Author: 彭小钗
# @File : forecase_page.py

from selenium.webdriver.common.by import By
from common.common_fun import Common

class ForecasePage(Common):
    # the title of forecase
    forecase_title = (By.XPATH, '//*[@text="天氣預報"]')

    #get the value of forecase title
    def get_text_of_forecase_title(self):
        return self.get_text(self.forecase_title)