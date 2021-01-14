#!/usr/bin/python
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    delay = 5          #in seconds
    time.sleep(delay)
    logging.info("Thread %s: finishing (%s seconds delay)", name, delay)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    # daemon = True -> dont wait for process, kill it
    # deamon = False -> wait for process to end the task
    x = threading.Thread(target=thread_function, args=(1,), daemon=False)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")