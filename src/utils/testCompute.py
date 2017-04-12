# -*- coding: utf-8 -*-

import time

from  src.utils import ComputeDueTime





if __name__ == '__main__':
    am_start = '08:30'
    am_end = '12:00'
    pm_start = '13:30'
    pm_end = '18:00'
    period = 60
    aheadTime = 5

    result = ComputeDueTime.getDueTime(am_start, am_end, pm_start, pm_end, period, aheadTime)

    for item in result:
        print ComputeDueTime.TimeStamp2Str(item)
