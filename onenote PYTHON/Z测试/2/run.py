import threading
import time


class A_class(threading.Thread):
    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 80
    def j(self):
        print("You are a stupid man!")
    def run(self):
        for i in range(50):
            print(self.x + self.y + i)


a = A_class()
a.start()
a.j()
