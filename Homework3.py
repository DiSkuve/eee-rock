from random import *

def OportunityOfCarryingTheBox(H , L , W , M):
    PlatformLengthAndWidth = float(1)
    PlatformCarryingCapacity = 1000
    if M<=PlatformCarryingCapacity and H<=PlatformLengthAndWidth and L<=PlatformLengthAndWidth:
        Oportunity = True
    elif M<=PlatformCarryingCapacity and H<=PlatformLengthAndWidth and W<=PlatformLengthAndWidth:
        Oportunity = True
    elif M<=PlatformCarryingCapacity and L<=PlatformLengthAndWidth and W<=PlatformLengthAndWidth:
        Oportunity = True
    else:
        Oportunity = False
    print(Oportunity)

def exercise1():
    BoxLength = float(input())
    BoxHeight = float(input())
    BoxWidth = float(input())
    BoxMass = float(input())
    OportunityOfCarryingTheBox(BoxHeight , BoxLength , BoxWidth , BoxMass)

def exercise2():
    RandomDigit = randrange(1,10)
    print("enter random number")
    UserDigit = int(input())
    while(UserDigit != RandomDigit):
        print("try again")
        if UserDigit<RandomDigit:
            print("it is bigger")
        else:
            print("it is smaller")
        UserDigit = int(input())
    print("Congards, Random number is" , RandomDigit)

def exercise3():
    model1 = "Квадрокоптер Ryze Tello Black-White, 98 мм, 41 мм, 1100 мА*ч, 13 минут, 2699"
    model2 = "Квадрокоптер DJI Mavic Mini Fly More Combo, 290 мм, 55 мм, 2400 мА*ч, 30 минут, 15470"
    model3 = "Квадрокоптер DJI Mavic Mini, 290 мм, 55 мм, 2400 мА*ч, 24 минуты, 12370"
    model4 = "Квадрокоптер DJI Mavic 2 Pro, 320 мм, 84 мм, 3850 мА*ч, 31 минута, 42750"
    model5 = "Квадрокоптер Hubsan X4 H107C, 160 мм, 35 мм, 520 мА*ч, 7 минут, 1999"

    print(model1)
    model1 = list(model1)
    print(model1)
    model1.remove(" ")
    model1.remove("К")
    model1.remove("в")
    model1.remove("а")
    model1.remove("д")
    model1.remove("р")
    model1.remove("о")
    model1.remove("к")
    model1.remove("о")
    model1.remove("п")
    model1.remove("т")
    model1.remove("е")
    model1.remove("р")
    model1.remove("м")
    model1.remove("м")
    model1.remove("м")
    model1.remove("м")
    model1.remove("м")
    model1.remove("А")
    model1.remove("*")
    model1.remove("ч")
    model1.remove("м")
    model1.remove("и")
    model1.remove("н")
    model1.remove("у")
    model1.remove("т")
    model1.remove(",")
    model1.remove(",")
    model1.remove(",")
    model1.remove(",")
    model1.remove(",")
    print(model1)

def exercise4():
    dostopremechatelnosti = {
        'Эйфелева башня' : "Франция",
        'Замок графа Дракулы' : "Румыния",
        'и тд' : 'Украина'
    }
    print(dostopremechatelnosti.keys())
    print(dostopremechatelnosti.items())

exercise1()
exercise2()
#exercise3()
exercise4()