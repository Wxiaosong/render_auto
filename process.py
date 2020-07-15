# _*_ coding: utf-8 _*_
#  获取pc进程pid、name
import psutil


def process_search(name):
    for process in psutil.process_iter():
        try:
            # print(list(psutil.process_iter()))
            processions = process.as_dict(attrs=['name', 'pid'])  # 获取name
            # print(processions['name'])
            if processions['name'] == name:   # 判断进程是否存在
                print('进程存在')
                return True
        except psutil.NoSuchProcess:
            return False


if __name__ == '__main__':
    if process_search('chrome.exe') is True:
        print('exit')
    else:
        print('sorry')