import os
from ftplib import FTP

ftp = FTP()
ftp.connect('10.40.1.182', port=21)
ftp.login(user='d5ftp', passwd='111111')
print(ftp.welcome)


def downloadfile( localpath, remotepath, filename):
    os.chdir(localpath)
    ftp.cwd(remotepath)
    ftp.nlst()
    file_handle = open(filename, 'wb').write
    ftp.retrbinary('RETR %s' % os.path.basename(filename), file_handle, blocksize=1024)


try:
    downloadfile('d:', '/build/installer/', 'D5_Render_installer-pre-1.6.1.0937.exe')
    print('下载完成，开始安装：')
    os.system('d:/D5_Render_installer-pre-1.6.1.0937.exe')
except IOError:
    print(IOError)