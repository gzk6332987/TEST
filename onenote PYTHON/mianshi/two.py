import time
import threading
def p_1():
    for i in range(15):
        print("我是p_1",i)
        time.sleep(0.3)

def p_2():
    for i in range(15):
        print("我是p_2",i)
        time.sleep(0.3)

t1 = threading.Thread(target=p_1)
time.sleep(0.2)
t2 = threading.Thread(target=p_2)

t1.start()
t2.start()