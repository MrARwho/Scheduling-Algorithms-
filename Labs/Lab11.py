import os
from multiprocessing import Process, Pipe


# def child(conn):
#     a = conn.recv()
#     a = a + " 052-CS"
#     conn.send(a)
#     conn.close()
#
#
# def parent(conn):
#     name = input("enter your name : ")
#     conn.send(name)
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p1 = Process(target=child, args=(child_conn,))
#     p2 = Process(target=parent, args=(parent_conn,))
#     p2.start()
#     print("child recv : ", child_conn.recv())
#     print("parent recv : ", parent_conn.recv())
#     p2.join()
#     p1.start()
#     print("parent recv : ", parent_conn.recv())
#     p1.join()

# TASK 2:
from multiprocessing import Process, Pipe
def f(conn):
    for i in range(6):
        conn.send(i**2)
    conn.close()
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    p.join()
    while parent_conn.recv:
        print(parent_conn.recv())


