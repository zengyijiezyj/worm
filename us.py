# -*- coding: utf-8 -*-
"""
-------------------
Description:
File Name:us
Author:YJ
Date:2018/9/1
Time:15:50
-------------------
"""
import os,shutil
from time import sleep

usb_path = "E:"
flag = os.path.exists(usb_path)

while not flag:
    flag = os.path.exists(usb_path)
    sleep(10)

shutil.copytree(usb_path, "D:\D")
