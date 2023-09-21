# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 19:07:42 2023

@author: User
"""

import os
import shutil
import time

if not os.path.exists('CS/homework'):
    os.makedirs('CS/homework')

with open('homework.txt','w') as file:
    file.write('4112029010_陳澤宇')

shutil.copy('homework.txt','homework')

size = os.path.getsize('homework.txt')
print(f'檔案大小:{size}字節')

m_time = os.path.getmtime('homework.txt')
print(f'最後修改時間:{m_time}')

f_time = time.ctime(m_time)
print(f'最後修改時間(人類可讀格式):{f_time}')

with open('homework.txt','r') as file:
    content = file.read()
    print(f'檔案內容:{content}')

shutil.rmtree('CS/homework')
