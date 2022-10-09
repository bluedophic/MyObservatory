# -*- coding:utf-8 -*-
# @Time : 2022/10/1 22:32
# @Author: 彭小钗
# @File : config_read.py

import yaml
from config.path_read import Config

#get the data form the yaml file
class Yaml_Load():
    def read_yaml(self):
        yaml_path = Config.yaml_path
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data