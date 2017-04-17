# -*- coding: utf-8 -*-
import time

'''
# 通过早上/下午工作时间 以及 周期 计算的通知的时间点
# 参数:
#         am_start      : 早上开始时间
#         am_end        : 早上结束时间
#         pm_start      : 下午开始时间
#         pm_end        : 下午结束时间 eg:
#         period        : 多长周期 min
#       aheadTime       ：提前时间 min
# 返回: List 时间戳

# 使用例子
# am_start = '8:30';
# am_end = '12:00';
# period = 60   单位：min
# aheadTime  提前时间 默认0 设置后单位 min
'''


def getDueTime(am_start, am_end, pm_start, pm_end, period, aheadTime=0):
    day = time.strftime("%Y-%m-%d ")
    am_start = day + '8:30'
    am_end = day + '12:00'
    pm_start = day + '13:30'
    pm_end = day + pm_end
    result = []
    # 获取早上提醒时间
    temp = Str2TimeStamp(am_start) + period * 60
    am_end_timeStamp = Str2TimeStamp(am_end)
    while temp < am_end_timeStamp:
        result.append(temp)
        temp += period * 60

    if (aheadTime > 0):  # 勾选了提前提示
        if result[-1] > am_end_timeStamp - aheadTime * 60:
            result[-1] = am_end_timeStamp - aheadTime * 60
        else:
            result.append(am_end_timeStamp - aheadTime * 60)
    else:  # 不勾选了提前提示 则 最后提醒时间为下班时间
        result.append(am_end_timeStamp)

    # 获取下午提醒时间
    temp = Str2TimeStamp(pm_start) + period * 60
    pm_end_timeStamp = Str2TimeStamp(pm_end)

    while temp < pm_end_timeStamp:
        result.append(temp)
        temp += period * 60

    if (aheadTime > 0):  # 勾选了提前提示
        if result[-1] > pm_end_timeStamp - aheadTime * 60:
            result[-1] = pm_end_timeStamp - aheadTime * 60
        else:
            result.append(pm_end_timeStamp - aheadTime * 60)
    else:  # 不勾选了提前提示 则 最后提醒时间为下班时间
        result.append(pm_end_timeStamp)

    return result


'''
# 字符时间格式转时间戳
# 2017-04-12 08:30:00 >>>> 1491957000
'''


def Str2TimeStamp(strTime):
    timeArray = time.strptime(strTime, "%Y-%m-%d %H:%M")
    # 转换为时间戳:
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


'''
# 时间戳转字符时间格式
# 1491957000 >>>>  2017-04-12 08:30:00
'''


def TimeStamp2Str(timeStamp):
    timeArray = time.localtime(float(timeStamp))
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return strTime


if __name__ == '__main__':
    am_start = '08:30'
    am_end = '12:00'
    pm_start = '13:30'
    pm_end = '18:00'
    period = 60
    aheadTime = 5

    result = getDueTime(am_start, am_end, pm_start, pm_end, period, aheadTime)

    for item in result:
        print TimeStamp2Str(item)
