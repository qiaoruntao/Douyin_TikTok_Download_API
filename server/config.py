# 配置文件路径
import os

import yaml

path = os.path.abspath(os.path.dirname(__file__))
config_file_path = f"{path}/config.yaml"
# 读取配置文件
with open(config_file_path, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)