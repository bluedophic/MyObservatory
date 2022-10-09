# -*- coding:utf-8 -*-
# @Time : 2022/10/1 22:33
# @Author: 彭小钗
# @File : path_read.py

import os

#get the path of cs_caps.yaml
class Config:
    config_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    yaml_path = config_dir + r'\cs_caps.yaml'
    print(yaml_path)