from PyQt5.QtWidgets import QMessageBox


class ShowMessage(QMessageBox):
    def __init__(self):
        super().__init__()