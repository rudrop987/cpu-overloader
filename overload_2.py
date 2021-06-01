import time
def Overload_2():
    a = 2
    while True:
        print(a)
        a = a ** a
        time.sleep(0.2)
Overload_2()