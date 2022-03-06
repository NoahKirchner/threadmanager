######################
#  THIS DOESN'T WORK
#  BUT IT MIGHT BE USEFUL IN THE FUTURE IF YOU TRY TO WRITE IN THE FUNCTIONALITY
#  Basically here is the gist.
'''
This was attempting to create a subclass of Thread which allowed you to pause and resume a thread. The problem with
this is that it required you to rewrite the run method of the Thread class, which while it is all great and beautiful,
also did not exactly allow you to pause the thread using the executor because the execution of the main thread still
seems to wait until all other threads are joined. This is really not that big of an issue with the intended use of
this program, and should not be that much of a problem, but I am leaving this unused code here to potentially add
this functionality in the future using this work as reference.
'''
######################


# from threading import Thread, Event
# from time import sleep
#
#
# class Job(Thread):
#     def __init__(self, target, args=None):
#         super(Job, self).__init__()
#
#         self.target = target
#         self.args = args
#
#         self.running = Event()  # Flag for whether or not the thread is suspended.
#         self.running.set()
#
#         self.alive = Event()  # Flag for whether or not the thread is alive.
#         self.alive.set()
#
#     def run(self):  # This really needs some logging.
#         if self.alive.isSet():
#             self.running.wait()  # Returns when the flag is true and thread is resumed, else waits.
#             try:
#                 if self.target:
#                     self.target(*self.args)
#                     sleep(1)
#             finally:
#                 sleep(1)
#                 del self.target, self.args
#
#
#     def stop(self):
#         self.running.set()  # Resumes the thread if it is paused.
#         self.alive.clear()  # Unsets alive flag.
#
#     def pause(self):
#         self.running.clear()
#
#     def resume(self):
#         self.running.set()
#
