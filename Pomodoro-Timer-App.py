import time
import os

def convert(t):
    return t * 60

def countdown(t,label):
    while t:
        min ,sec = divmod(t,60)
        print(f"{label}: {min:02d}: {sec:02d}", end="\r")
        time.sleep(1)
        t-=1

def pomodoro(workTime, breakTime):
    counter1=0
    while True:
        w = convert(workTime)
        b = convert(breakTime)
        countdown(w,"Work")
        os.system("clear||cls")
        counter1+=1
        if counter1 ==4:
            newb=b*4
            countdown(newb,"Break")
            os.system("clear||cls")
           
            counter1=0
        else:
            countdown(b,"Break")
            os.system("clear||cls")


workTime = int(input("Enter work time(min): "))
breakTime = int(input("Enter break tim(min): "))

pomodoro(workTime,breakTime)
