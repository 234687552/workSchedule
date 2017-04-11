# -*- coding: utf-8 -*-

import time

from  utils  import  ComputeDueTime
# print ComputeDueTime.getDueTime('123','','','','')
# print ComputeDueTime.testDueTime('123')



def getDueTime(am_start, am_end, pm_start, pm_end, period):
    day = time.strftime("%Y-%m-%d ")
    am_start = day + '8:30'
    am_start1 = day + '08:30:01'
    am_end = day + '12:00'
    pm_start = day + '13:30'
    pm_end = day + pm_end
    period = day + period
    print  am_start, am_start1
    # 将其转换为时间数组
    timeArray = time.strptime(am_start, "%Y-%m-%d %H:%M")
    timeArray1 = time.strptime(am_start1, "%Y-%m-%d %H:%M:%S")
    # 转换为时间戳:
    timeStamp = int(time.mktime(timeArray))
    timeStamp1 = int(time.mktime(timeArray1))
    print timeStamp
    print timeStamp1
    return 'am_start'


if __name__ == '__main__':
    am_start = '08:30'
    am_end = '12:00'
    pm_start = '13:30'
    pm_end = '18:00'
    period = '60'

    getDueTime(am_start, am_end, pm_start, pm_end, pm_start)


