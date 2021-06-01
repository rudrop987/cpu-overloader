import time
def Overload_1():
    a = 2
    while True:
        print(a)
        a = a ** a
        time.sleep(0.2)
Overload_1()