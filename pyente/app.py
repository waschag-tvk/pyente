import sys

import datetime
import pkg_resources

from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
        QAction, QApplication, QDesktopWidget, QGroupBox, QHBoxLayout,
        QInputDialog, QLabel, QLineEdit, QMainWindow, QToolBar, QVBoxLayout,
        QWidget)

from .control import Control


class Ente(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""

    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(Ente, self).__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle('Ente')
        self.control = Control()
        window_icon = pkg_resources.resource_filename('pyente.images',
                                                      'ic_insert_drive_file_black_48dp_1x.png')
        self.setWindowIcon(QIcon(window_icon))

        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.setCentralWidget(self.widget)

        self.clock_timer = QTimer()

        self.layout.addWidget(self.clock(self.clock_timer))
        self.layout.addWidget(self.about())

        self.addToolBar(self.user_toolbar())

        self.status_bar = self.statusBar()
        self.notify('Ready')

    def user_toolbar(self):
        user_toolbar = QToolBar('User')
        user_toolbar.setIconSize(QSize(14, 14))

        activate_action = QAction('Activate machine(s) now (Space)', self)
        activate_action.setStatusTip('Activate machine(s) now')
        activate_action.setShortcut('SPACE')
        activate_action.triggered.connect(self.activate)

        user_toolbar.addAction(activate_action)

        return user_toolbar

    def about(self):
        """Create a group box that shows application information."""
        about = QGroupBox('About')
        about_layout = QVBoxLayout()
        about_layout.setAlignment(Qt.AlignVCenter)

        author = QLabel('TvK Wasch-AG')
        author.setAlignment(Qt.AlignCenter)

        icons = QLabel('Material design icons created by Google')
        icons.setAlignment(Qt.AlignCenter)

        github = QLabel('GitHub: waschag-tvk')
        github.setAlignment(Qt.AlignCenter)

        about_layout.addWidget(author)
        about_layout.addWidget(icons)
        about_layout.addWidget(github)

        about.setLayout(about_layout)
        return about

    def clock(self, timer):
        clock = QGroupBox('Clock')
        clock_layout = QHBoxLayout()
        display = QLabel('TIME')
        display.setAlignment(Qt.AlignCenter)
        display.setStyleSheet('font-size: 96pt; background-color: Gold')
        clock_layout.addWidget(display)
        clock.setLayout(clock_layout)

        def showtime():
            display.setText(
                    datetime.datetime.now().timetz().strftime('%H:%M:%S'))

        timer.timeout.connect(showtime)
        timer.start(1000)
        return clock

    def activate(self):
        username, _ = QInputDialog.getText(
                self, 'Login', 'Please enter your wasch username')
        password, _ = QInputDialog.getText(
                self, 'Password', 'Password for {}'.format(username),
                QLineEdit.Password)
        machines = [1]  # TODO determine which machines can be activated
        try:
            for machine in machines:
                self.control.activate(machine)
        except RuntimeError as e:
            self.notify(str(e))
            return
        print('activated by {}!'.format(username))  # TODO actually activate

    def notify(self, message):
        self.status_bar.showMessage(message, 5000)


def main():
    application = QApplication(sys.argv)
    window = Ente()
    desktop = QDesktopWidget().availableGeometry()
    width = (desktop.width() - window.width()) / 2
    height = (desktop.height() - window.height()) / 2
    window.show()
    window.move(width, height)
    sys.exit(application.exec_())
