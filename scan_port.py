
#!/usr/bin/env python
# Author: mohamedkdidi@gmail.com 
# A simple multi-threading port scanner Python program using socket

import socket, threading, time
from queue import Queue


therad_locked = threading.Lock()

# URL to scan
target = 'www.python.org'

# Create the queue and threader 
my_queue = Queue()

def port_scanner(port):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connexion = my_socket.connect((target,port))
        with therad_locked:
            print('port open: ',port)
        connexion.close()
    except:
        pass


# The multithreading thread pulls an worker from the queue and processes it
def multi_threading():
    while True:
        # gets an worker from the queue
        worker = my_queue.get()

        # Run port scanner job with the avail worker in queue (thread)
        port_scanner(worker)

        # completed with the job
        my_queue.task_done()


def main():
    # how many threads are we going to allow for
    for thread in range(100):
        my_thread = threading.Thread(target=multi_threading)

        # classifying as a daemon, so they will die when the main dies
        my_thread.daemon = True

        # begins, must come after daemon definition
        my_thread.start()


    seconds = time.time()
    local_time = time.ctime(seconds)
    print(local_time)

    # scan port 70 to 90.
    for worker in range(70,90):
        my_queue.put(worker)

    # wait until the thread terminates.
    my_queue.join()

if __name__ == "__main__":
   main()