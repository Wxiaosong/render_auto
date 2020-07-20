
import re

#  其他路径
# filepath = r'E:\D5 Render test 798\d5_immerse\Saved\Logs\d5_immerse.log'

#  pre、cn2路径
filepath = r'C:\Users\WXS\AppData\Local\d5_immerse\Saved\Logs\d5_immerse.log'

#  test路径
# filepath = r''

keyword_importfile = []
keyword_exportphoto = []
with open(filepath, 'r', encoding='UTF-8') as file:
    for line in file.readlines():
        if re.search('CMessageGoFusionProcess', line):  # 导入时间
            keyword_importfile.append(str(line)[15:24])
        if re.search('Request: percent:', line):  # 出图时间
            keyword_exportphoto.append(str(line)[15:24])


def time_convert(keyword_list):
    timeklist = []
    if len(keyword_list):
        for i in keyword_list:
            print(i)
            minute = int(i[:2])
            second = int(i[3:5])
            millisecond = int(i[-3:])
            time = (minute * 60 + second) * 1000 + millisecond
            # print(time)
            timeklist.append(time)

        use_time = timeklist[-1] - timeklist[0]
        # print(use_time)
        try:
            use_time = use_time / 1000
            # print(use_time)
            if use_time >= 60:
                use_time = use_time / 60
                print(use_time)
                print('用时：' + str(use_time) + ' 分钟')
            else:
                print('用时：' + str(use_time) + ' 秒')
        except:
            print('wrong')
    else:
        print('不存在操作')


if __name__ == '__main__':
    print('导入')
    time_convert(keyword_importfile)
    print('出图/视频')
    time_convert(keyword_exportphoto)
    # print(keyword_exportphoto)
    # print(keyword_importfile)
