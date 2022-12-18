# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def mult_after_max(*args):
    """
    Произведение аргументов, расположенных после
    максимальногопо модулю аргумента.
    """
    if args:
        mult = 1
        values = [float(arg) for arg in args]
        max_item = 0
        max_ind = 0
        for i, item in enumerate(values):
            if math.fabs(item) > max_item:
                max_ind = i
                max_item = math.fabs(item)
        values = values[max_ind:]
        for arg in values:
            mult = mult * arg
        return mult
    else:
        return None


if __name__ == "__main__":
    print(f'Произведение: {mult_after_max()}')
    print(f'Произведение: {mult_after_max(1, 3, 6, 4, 5)}')
    print(f'Произведение: {mult_after_max(7, 8, 12, 76, 34, 7, 34)}')
