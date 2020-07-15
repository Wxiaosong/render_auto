# -*- coding: utf-8 -*-
# 根据launcher版本号生成token.ini文件，方便pre测试
#   输入launcher版本号，在路径：C:\Users\WXS\Desktop\Test_files\auto_drs下生成token.ini

import sys
import hashlib
import os
from config.config import *

magic = 'Magic' + str(Launcher)


def calculate(target):
    md5hash = hashlib.md5(magic.encode('utf-8'))
    md5 = md5hash.hexdigest()
    print(md5)

    with open(r'e:\Test_files\auto_drs\token.ini', 'w') as f:
        f.writelines('[Preview]' + '\n')
        f.writelines('Key=' + md5)
    os.system("copy E:\Test_files\\auto_drs\\token.ini \"%s\"" % target)
    # print("copy E:\Test_files\\auto_drs\\token.ini \"%s\"" % taget)