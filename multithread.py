import threading
from time import sleep


def square(array):
        for num in array:
            print(pow(num,2))
            sleep(1)



def cube(array):
        for num in array:
            print(pow(num,3))
            sleep(1)



array = [2,3,4,5,6]

t1= threading.Thread(target=square, args=(array,))
t2= threading.Thread(target=cube, args=(array,))


t1.start()
t2.start()


