# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def sr_geom(*args):
    if args:
        values = [float(arg) for arg in args]
        g = 1
        for arg in values:
            g = g * arg
        n = len(args)
        return pow(g, 1/n)
    else:
        return None


if __name__ == "__main__":
    print(f'Среднее геометрическое 1: {sr_geom(1, 2, 3, 4, 5)}')
    print(f'Среднее геометрическое 1: {sr_geom()}')
    print(f'Среднее геометрическое 1: {sr_geom(1.3, 7.9, 8.3)}')
