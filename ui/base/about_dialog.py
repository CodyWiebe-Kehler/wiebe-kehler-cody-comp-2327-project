"""Defines the AboutDialog class."""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog,
                               QLayout,
                               QVBoxLayout,
                               QLabel,
                               QPushButton,)

class AboutDialog(QDialog):
    """Represents a dialog window that contains information about a program.
    """

    def __init__(self) -> None:
        """Initializes a new instance of the AboutDialog class."""

        super().__init__()

        self.setFixedWidth(300)
        self.setFixedHeight(140)
        self.setModal(True)
        self.setWindowTitle("About")

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.__initialize_widgets(main_layout)

    def __initialize_widgets(self, main_layout: QLayout) -> None:
        """Initializes the widgets on this dialog window."""

        #creates and stores reference to widgets
        self._title_lable = QLabel("About")
        title_font = self._title_lable.font()
        title_font.setBold(True)
        title_font.setPointSize(20)
        self._title_lable.setFont(title_font)

        self._version_label = QLabel("Version: x.x.x")
        self._pyside6_credit_label = QLabel("Built with PySide6")
        self._copyright_label = QLabel("© 20xx name email@domain.com")

        self._ok_button = QPushButton("Ok")
        self._ok_button.clicked.connect(self._ok_button_on_click)

        #adds widgets to layout
        main_layout.addWidget(self._title_lable,0,Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(self._version_label,0,Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(self._pyside6_credit_label,0,Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(self._copyright_label,0,Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(self._ok_button,0)

    def _ok_button_on_click(self) -> None:
        """Handles clicked functionality for ok button"""
        self.done(0)