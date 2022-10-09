# -*- coding:utf-8 -*-
# @Time : 2022/10/1 22:28
# @Author: 彭小钗
# @File : common_fun.py

from base.base_page import Base

class Common(Base):

    def size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    #swipe up the screen
    #n:times of swipe up
    #t:during time of swipe up
    def swipeUp(self, n, t):
        x1 = self.size()[0] * 0.3
        y1 = self.size()[1] * 0.75
        y2 = self.size()[1] * 0.5
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)