#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    t = s[:2]
    t2 = s[3:5]
    t3 = s[6:8]
    ival = int(t)
    #ival2 = int(t2)
    #ival3 = int(t3)
    print(ival, t2, t3)

    zone = s[8:]
    print(zone)

    if ival == 12 and zone == 'AM':
        ival = '00'
        #ival2 = str(ival2)
        #ival3 = str(ival3)
        sol = ival+':'+t2+':'+t3
        return sol
    elif ival == 12 and zone == 'PM':
        ival = '12'
        #ival2 = str(ival2)
        #ival3 = str(ival3)
        sol2 = ival+':'+t2+':'+t3
        return sol2
    elif zone == 'AM':
        sol3 = t+':'+t2+':'+t3
        return sol3
    else:
        oval = ival + 12
        str_val = str(oval)
        #ival2 = str(ival2)
        #ival3 = str(ival3)
        sol4 = str_val+':'+t2+':'+t3
        return sol4
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
