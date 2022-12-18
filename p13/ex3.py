# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def sr_harm(*args):
    if args:
        h = 0
        for arg in args:
            h += 1 / arg
        n = len(args)
        return n / h
    else:
        return None


if __name__ == "__main__":
    arguments = list(map(float, input('Введите аргументы: ').split()))
    print(f'Среднее геометрическое: {sr_harm(*arguments)}')
