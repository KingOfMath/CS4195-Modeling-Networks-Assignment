# coding=utf-8

import xlsxParser
res = xlsxParser.parser()

# compute N
def N():
    count = []
    for each in res:
        if each[0] not in count:
            count.append(each[0])
        if each[1] not in count:
            count.append(each[1])
    return len(count)

# compute L
def L():
    pair = []
    for each in res:
        if [each[0],each[1]] not in pair:
            pair.append([each[0],each[1]])
    return len(pair)

# compute p


# compute E[D]


# compute Var[D]

