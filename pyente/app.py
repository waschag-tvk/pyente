import sys

import pkg_resources

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QAction, QApplication, QDesktopWidget, QDialog, QFileDialog, QGroupBox,
                             QHBoxLayout, QLabel, QMainWindow, QToolBar, QVBoxLayout, QWidget)


class Ente(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""

    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(Ente, self).__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle('Ente')
        window_icon = pkg_resources.resource_filename('pyente.images',
                                                      'ic_insert_drive_file_black_48dp_1x.png')
        self.setWindowIcon(QIcon(window_icon))

        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)
        self.setCentralWidget(self.widget)

        self.layout.addWidget(self.about())

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready', 5000)

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


def main():
    application = QApplication(sys.argv)
    window = Ente()
    desktop = QDesktopWidget().availableGeometry()
    width = (desktop.width() - window.width()) / 2
    height = (desktop.height() - window.height()) / 2
    window.show()
    window.move(width, height)
    sys.exit(application.exec_())
