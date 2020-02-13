#!/usr/bin/env python3
import sys

def Hours(Time):
    if Time < 0:
        raise ValueError("Parameter Error")
    else:
        Hour = int(Time // 60)
        Minut = int(Time % 60)
        print("{} H, {} M".format(Hour, Minut))


if __name__ == '__main__':
    try:
        Hours(int(sys.argv[1]))
    except:
        print("Parameter Error")
