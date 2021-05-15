from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout, QPushButton, QVBoxLayout


class GearParamsInput(QWidget):
    def __init__(self):
        super().__init__()

        toothAmount_hbox = QHBoxLayout()

        self.toothAmount_label = QLabel("Tooths: ")
        self.toothAmount_lineEdit = QLineEdit()

        toothAmount_hbox.addWidget(self.toothAmount_label)
        toothAmount_hbox.addWidget(self.toothAmount_lineEdit)

        self.createPushButton = QPushButton("Create new gear!")
        self.deleteLastGearPushButton = QPushButton("DeleteLastGear")

        buttonsHbox = QHBoxLayout()

        buttonsHbox.addWidget(self.createPushButton)
        buttonsHbox.addWidget(self.deleteLastGearPushButton)

        mainVerticalLayout = QVBoxLayout()
        mainVerticalLayout.addLayout(toothAmount_hbox)
        mainVerticalLayout.addLayout(buttonsHbox)

        self.setLayout(mainVerticalLayout)
