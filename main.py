# import sys
# from PyQt5.QtWidgets import QApplication
# from apscheduler.schedulers.background import BackgroundScheduler

# def start():
#     print("start")

# if __name__ == '__main__':
#     try:
#         app = QApplication(sys.argv)
#         global me
#         # me = Monitor(cf)
#         # sched = QtScheduler()
#         sched = BackgroundScheduler()
#         # m = Main()
#         # sched.add_job(start, 'cron', id='first', day_of_week ='0-4', hour = 9, minute = 11)
#         # sched.add_job(stop, 'cron', id='second', day_of_week ='0-4', hour = 15, minute = 20)
#         sched.add_job(start, 'cron', second = 5)    
#         # sched.add_job(start, "cron", id="first", second=10)
#         # sched.add_job(stop, "cron", id="second", hour=21, minute=10)
#         sched.start()
#         app.exec_()
#     except BaseException as e:
#     # except BaseException, e:
#         print(e)
#         # logger.exception(e)

from subprocess import call

import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print("In job")
    # call(['python', 'scheduler/main.py'])


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=1)
    # scheduler.add
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        # print("except")