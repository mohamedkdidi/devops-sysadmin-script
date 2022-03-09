
#!/usr/bin/env python
# Author: mohamedkdidi@gmail.com 
# A simple multi-threading port scanner Python program using socket

import socket, threading, time
from queue import Queue


therad_locked = threading.Lock()

# URL to scan
target = 'www.coolfounders.com'

# Input the target 
target = input('\nEnter the target domain name or ip address: ')

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
        # Gets an worker from the queue
        worker = my_queue.get()

        # Run port scanner job with the avail worker in queue (thread)
        port_scanner(worker)

        # Completed with the job
        my_queue.task_done()



def main():
    # how many threads are we going to allow for
    for thread in range(100):
        my_thread = threading.Thread(target=multi_threading)

        # Classifying as a daemon, so they will die when the main dies
        my_thread.daemon = True

        # Begins, must come after daemon definition
        my_thread.start()


    seconds = time.time()
    local_time = time.ctime(seconds)
    print(local_time, '#', target)

    # Exampe scan the most commonly used ports.
    # HTTP – Port 80
    # HTTPS – 443
    # FTP – 21
    # FTPS / SSH – 22
    # POP3 – 110
    # POP3 SSL – 995
    # IMAP – 143
    # IMAP SSL – 993
    # SMTP – 25 (Alternate: 26)
    # SMTP SSL – 587
    # MySQL – 3306
    # cPanel – 2082
    # cPanel SSL – 2083
    # WHM (Webhost Manager) – 2086
    # WHM (Webhost Manager) SSL – 2087
    # Webmail – 2095
    # Webmail SSL – 2096
    # WebDAV/WebDisk – 2077
    # WebDAV/WebDisk SSL – 2078
    for worker in [80, 443, 22]:
        my_queue.put(worker)

    # Wait until the thread terminates.
    my_queue.join()


if __name__ == "__main__":
   main()
