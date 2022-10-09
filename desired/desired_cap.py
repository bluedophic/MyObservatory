# -*- coding:utf-8 -*-
# @Time : 2022/10/1 22:34
# @Author: 彭小钗
# @File : desired_cap.py

from config.config_read import Yaml_Load
from appium import webdriver

def desired_caps():
    #get the data of Desired Capabilities from yaml file
    data = Yaml_Load().read_yaml()
    info = {}
    info['platformName'] = data['platformName']
    info['platformVersion'] = data['platformVersion']
    info['deviceName'] = data['deviceName']
    # info['automationName'] = data['automationName']
    info['appPackage'] = data['appPackage']
    info['appActivity'] = data['appActivity']
    info['noReset'] = data['noReset']
    driver = webdriver.Remote("http://"+str(data['ip'])+":"+str(data['port'])+"/wd/hub", info)
    return driver

if __name__ == '__main__':
    desired_caps()
