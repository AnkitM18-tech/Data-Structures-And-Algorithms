#Queue allows loose coupling
#FIFO(First In First Out) Structure

"""from collections import deque
q=deque()
q.appendleft("-------")
q.appendleft("-------")
q.pop()                          #FIFO structure"""
import time
import threading

from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
    def front(self):
        return self.buffer[-1]

"""food_order_queue=Queue()

def place_orders(orders):
    for order in orders:
        print("Placing order for: ",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)

def serve_orders():
    time.sleep(1)
    while (food_order_queue.size())!=0:
        order=food_order_queue.dequeue()
        print("Now serving: ",order)
        time.sleep(2)

if __name__=="__main__":
    orders=["pizza","samosa","pasta","biryani","burger"]
    t1=threading.Thread(target=place_orders,args=(orders,))
    t2= threading.Thread(target=serve_orders)

    t1.start()
    t2.start()"""                                   #Food Order Multithreading Using Queue

"""def produce_binary_nos(n):
    numbers_queue=Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front=numbers_queue.front()
        print(" ",front)
        numbers_queue.enqueue(front+"0")
        numbers_queue.enqueue(front+"1")

        numbers_queue.dequeue()

if __name__=="__main__":
    produce_binary_nos(10)"""                     #Binary Number Printing using queue