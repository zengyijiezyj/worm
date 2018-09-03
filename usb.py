# -*- coding: utf-8 -*-
"""
-------------------
Description:
File Name:usb
Author:YJ
Date:2018/9/1
Time:9:33
-------------------
"""
from time import sleep
import os,shutil
usb_path = "E:"
content = os.listdir(usb_path)
while True:
    new_content=os.listdir(usb_path)
    if new_content != content:
        break
    sleep(3)

x=[item for item in new_content if item not in content]
shutil.copytree(os.path.join(usb_path, x[0]), 'D:\D')
