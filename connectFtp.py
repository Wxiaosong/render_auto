from ftplib import FTP
import os

class Myftp:

    ftp = FTP()

    def __init__(self, host):
        self.ftp.connect(host, port=21)

    def login(self, username, pwd):
        # self.ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
        self.ftp.login(username, pwd)
        print(self.ftp.welcome)

    def downloadfile(self, localpath, remotepath, filename):
        os.chdir(localpath)
        self.ftp.cwd(remotepath)
        self.ftp.nlst()

        file_handle = open(filename, 'wb').write
        print("下载中：")
        self.ftp.retrbinary('RETR %s' % os.path.basename(filename), file_handle, blocksize=1024)
        print("下载完成")

    def close(self):
        self.ftp.set_debuglevel(0)
        self.ftp.quit()