import random as rn
import datetime

GROUP_SIZE = 23

def main():
    result = 0
    for i in range(100000):
        if check():
            result+=1
    return result


def group():
    listt = []
    i = 0
    while i <= GROUP_SIZE:
        try:
            listt.append(datetime.date(2020, rn.randint(1, 12), rn.randint(1, 31)))
            i+=1
        except:
            continue
    return listt

def check():
    listt = group()
    for i in range(GROUP_SIZE):
        for j in range(i+1, GROUP_SIZE):
            if listt[i] == listt[j]:
                return True

print(main())