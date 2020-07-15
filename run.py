# coding=utf-8

import os
from connectFtp import Myftp
from config.config import *
import process
import calculate_md5
import time

# filename = sys.argv[1]

ftp = Myftp(FtpIp)
ftp.login(FtpLogin, FtpPwd)

if __name__ == '__main__':

    try:
        ftp.downloadfile('d:', target, ExeName)
        ftp.close()
        print('开始安装：')
        print(ExeName)
        os.system(ExeName)
        time.sleep(7)
        print(55)
        while process.process_search(ExeName) is True:
            calculate_md5.calculate(tokenFolder)
            print("token完成")
    except IOError:
        print("error: 失败")

