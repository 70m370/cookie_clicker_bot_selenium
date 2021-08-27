import threading
import engine
import functions
from engine import *
from functions import *

def bot_loop1():
    while True:
        cookie_upgrade()
        time.sleep(4)

def bot_loop2():
    while True:
        cookie_workers()
        time.sleep(5)

def bot_loop3():
    while True:
        cookie_click()
        time.sleep(1)

thread1 = threading.Thread(target=bot_loop1)
thread1.start()

thread2 = threading.Thread(target=bot_loop2)
thread2.start()

thread3 = threading.Thread(target=bot_loop3)
thread3.start()