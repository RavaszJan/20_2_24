
import threading
import time

def backround_task():
    while True:
        print("Deamond thread running..")
        time.sleep(2)


deamon_thread=threading.Thread(target=backround_task, args=(), daemon=True)
deamon_thread.start()

print("Zacni program")
time.sleep(11)
print("Ukonci program")
