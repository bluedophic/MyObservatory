# -*- coding:utf-8 -*-
# @Time : 2022/10/1 22:36
# @Author: 彭小钗
# @File : test_nine_day_forecase.py

import unittest
from time import sleep

from desired.desired_cap import desired_caps
from page.forecase_page import ForecasePage
from page.home_page import HomePage
from page.menu_page import MenuPage


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # initialize appium driver
        cls.driver = desired_caps()
        cls.hp = HomePage(cls.driver)
        cls.mu = MenuPage(cls.driver)
        cls.fc = ForecasePage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        # quit the app
        cls.driver.quit()

    def test_tomorrow_forecase(self):
        #expect value
        expect = "天氣預報"
        #click menu button on home page
        self.hp.click_menu_button()
        # sleep(2)
        #swipe up on the menu page
        self.mu.swipeUp(1, 100)
        #click nine day forecase button
        self.mu.click_nine_day_forecase_button()
        # actual value
        Actual = self.fc.get_text_of_forecase_title()
        #verify that we are at forecase page
        self.assertEqual(Actual, expect, msg="{0} is not equal to {1}".format(Actual, expect))

if __name__ == '__main__':
    unittest.main(['-sv', "test_nine_day_forecase.py"])