# coding=utf-8

import os
from connectFtp import Myftp
from config.config import *

# filename = sys.argv[1]


if __name__ == '__main__':
    filename = ExeName

    ftp = Myftp(FtpIp)
    ftp.login(FtpLogin, FtpPwd)
    try:
        ftp.downloadfile('d:', target, filename)
    except:
        print("error: 下载失败")
    else:
        print('下载完成，开始安装：')
        os.system(filename)
    ftp.close()


