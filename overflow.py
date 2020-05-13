from datetime import datetime, timedelta
import signal
import sys

from apscheduler.schedulers.qt import QtScheduler
from PyQt5.QtWidgets import QApplication, QLabel


def tick():
    label.setText('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # This enables processing of Ctrl+C keypresses
    signal.signal(signal.SIGINT, lambda *args: QApplication.quit())

    label = QLabel('The timer text will appear here in a moment!')
    label.setWindowTitle('QtScheduler example')
    label.setFixedSize(280, 50)
    label.show()

    scheduler = QtScheduler()

    # any trigger, so long as next fire time causes overflow
    scheduler.add_job(tick, 'interval', seconds=3, start_date=datetime.now() + timedelta(days=3000))
    scheduler.start()

    # Execution will block here until the user closes the windows or Ctrl+C is pressed.
    app.exec_()