"""Defines the ClientServicesAboutDialog class."""

__author__ = "Cody Wiebe-Kehler"
__version__ = "1.0.0"

from ui.base.about_dialog import AboutDialog

class ClientServicesAboutDialog(AboutDialog):
    """Represents the dialog for displaying information about the client services program"""

    def __init__(self) -> None:
        """Initializes and instance of the ClientServicesAboutDialog class"""
        super().__init__()

        self.setWindowTitle("About Client Services")

        self._title_lable.setText("About Client Services")
        self._version_label.setText("Version: 1.0.0")
        self._copyright_label.setText("©2026 Cody Wiebe-Kehler cwiebe-kehler@rrc.ca")

