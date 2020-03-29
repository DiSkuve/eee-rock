from math import *
from random import *

def numbering(A):
    S1 = int(A%10)
    S2 = int(A/10%10)
    S3 = int(A/100%10)
    S = S1 + S2 + S3

    return S

def exercise1():
    print("exercise1")
    #speed of the first trin (km/h)
    print("enter speed of the first train")
    V1 = int(input())
    #speed of the second trin (km/h)
    print("enter speed of the second train")
    V2 = int(input())

    #distance between the trains(km)
    S=10
    #distance to the sidetrack
    S1 = 4

    t1 = S1/V1
    t2 = (S-S1)/V2

    if t2<t1:
        k = True
    else:
        k = False

    print(k)
def exercise2():
    #statr point of catapult
    x0 = 0
    #acceleration of gravity on Earth
    g = 9.81
    #start speed of shell
    print("enter the start speed")
    V0 = int(input())
    #angle between the vector of start speed and horizon
    print("enter the angle to horizon in degree")
    alpha = int(input())
    #alpha from degree to radian
    alpha = alpha*pi/180
    #calculate of distance of fly
    S = V0**2*sin(2*alpha)/g
    x = x0 + S
    print("distance is equal: " , x)


def numbering(A):
    S1 = int(A % 10)
    S2 = int(A / 10 % 10)
    S3 = int(A / 100 % 10)
    S = S1 + S2 + S3

    return S

def exercise3():
    A = randrange(1,9) * 100 + randrange(1,9) * 10 + randrange(1,9)
    print(A)
    numbering(A)
    S = numbering(A)
    print(S)

exercise1()
exercise2()
exercise3()