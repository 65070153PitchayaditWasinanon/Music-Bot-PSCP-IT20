"""Algorithm Analysis"""

from time import time
import random

# def summation(n):
#     """Summation"""
    # แบบที่ 1
    # total = 0
    # for i in range(0, n):
    #     total += i
    # return total

    #แบบที่ 2
    # return (n*(n+1))/2

def isIntersect(a,b,c):
    """Check Intersect"""
    #แบบที่ N^2
    # for i in a:
    #     if (i in b) and (i in c):
    #         return True
    # return False

    #แบบที่ N^3
    for i in a:
        for j in b:
            for k in c:
                if (i == j) and (i == k):
                    return True
    return False

def randomList(n):
    """Random List"""
    return random.sample(range(0, 999999999), n)


def analyze_algo(n=1000):
    """Algo analysis"""
    stime = time()
    # summation(n)
    print(isIntersect(randomList(n), randomList(n), randomList(n)))
    etime = time()
    elapsed = etime - stime
    print("execution time : " + str(elapsed))

analyze_algo()