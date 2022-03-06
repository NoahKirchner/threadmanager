from threading import Thread
from time import time_ns


class Executor:
    def __init__(self):
        self.threadlist = dict()

    def add(self, label: str, target, args: tuple = ()):  # Target: function to be called, args: arguments for function.
        thread = Thread(target=target, args=args)
        self.threadlist.update({label: thread})  # Adds a thread with a label to the threadlist but does not start it.

    def add_bulk(self, list_input: iter):  # Uses any type of iterable to bind a list of functions to threads.
        for item in list_input:
            try:
                self.add(item[0], item[1], item[2])
            except TypeError:
                raise Exception("Addbulk requires a list of lists (or equivalent). The format of the sublists should"
                                "be (thread label, target function, arguments)")

    def start(self, label: str):  # Starts one of the threads based on its label.
        print("Start {} @ {} \r\n".format(self.threadlist[label], time_ns()))
        self.threadlist[label].start()

    def start_all(self):  # Starts all threads in the threadlist.
        for item in self.threadlist.values():
            print("Start {} @ {} \r\n".format(item, time_ns()))
            item.start()

    def stop(self, label: str):  # Because threads cannot be suspended, the stop and stop_all methods are useless.
        print("Stop {} @ {} \r\n".format(self.threadlist[label], time_ns()))
        self.threadlist[label].join()

    def stop_all(self):
        for item in self.threadlist.values():
            print("Stop {} @ {} \r\n".format(item, time_ns()))
            item.join()

