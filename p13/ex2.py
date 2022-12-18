# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def sr_geom(*args):
    if args:
        g = 1
        for arg in args:
            g = g * arg
        n = len(args)
        return pow(g, 1/n)
    else:
        return None


if __name__ == "__main__":
    arguments = list(map(float, input('Введите аргументы: ').split()))
    print(f'Среднее геометрическое: {sr_geom(*arguments)}')
