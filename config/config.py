# coding=utf-8

import sys

if len(sys.argv) < 2:
    raise Exception("please input 2 args")

ProFile = sys.argv[1]
ExeName = 'D5_Render_installer-pre-%s.exe' % ProFile[31:41]
print(ExeName)

Launcher = ProFile[-10:]
print(Launcher)

FtpIp = '10.40.1.182'
FtpLogin = 'd5ftp'
FtpPwd = '111111'

target = '/build/installer/'
tokenFolder = r'E:\D5 Render Preview ' + ProFile[38:41]
print(tokenFolder)
