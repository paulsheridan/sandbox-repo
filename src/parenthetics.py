# -*- coding: utf-8 -*-


def paren_check(string):
    count = 0
    for idx, l in enumerate(string):
        if l == '(':
            count += 1
        elif l == ')':
            count -= 1
        if count < 0:
            return -1
            break
    if count > 0:
        return 1
    else:
        return 0
