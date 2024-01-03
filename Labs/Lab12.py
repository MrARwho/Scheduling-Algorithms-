import random
from multiprocessing import Process, Value , Array

# TASK 1 :
# def first(n):
#     n.value = 1
#
#
# def second(n):
#     n.value = 2
#
#
# def third(n):
#     n.value = 3
#
#
# def fourth(n):
#     n.value = 4
#
#
# def fifth(n):
#     n.value = 5
#
#
# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     p1 = Process(target=first, args=(num,))
#     p2 = Process(target=second, args=(num,))
#     p3 = Process(target=third, args=(num,))
#     p4 = Process(target=fourth, args=(num,))
#     p5 = Process(target=fifth, args=(num,))
#
#     print("intial value : ", num.value)
#     p1.start()
#     p1.join()
#
#     p2.start()
#     p2.join()
#
#     p3.start()
#     p3.join()
#
#     p4.start()
#     p4.join()
#
#     p5.start()
#     p5.join()
#
#     print("final value : ", num.value)


# TASK 2 :

def start(n):
    for i in range(5):
        n[i] = n[i]**2
def end(n):
    for i in range(5,10):
        n[i] = n[i]**2
if __name__ == '__main__':
    arr = Array('i', range(10))
    p1 = Process(target=start, args=(arr,))
    p2 = Process(target=end, args=(arr,))
    print("initial array : ", arr[:])
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print("final", arr[:])



