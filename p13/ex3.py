# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def sr_harm(*args):
    if args:
        values = [float(arg) for arg in args]
        h = 0
        for arg in values:
            h += 1 / arg
        n = len(args)
        return n / h
    else:
        return None


if __name__ == "__main__":
    print(f'Среднее гармоническое: {sr_harm(1, 2, 3, 4, 5, 6)}')
    print(f'Среднее гармоническое: {sr_harm()}')
    print(f'Среднее гармоническое: {sr_harm(3.3, 6.5, 9.7, 8.0)}')
