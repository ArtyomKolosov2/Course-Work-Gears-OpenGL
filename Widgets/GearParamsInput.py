from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout, QPushButton, QVBoxLayout


class GearParamsInput(QWidget):
    def __init__(self):
        super().__init__()

        toothAmount_hbox = QHBoxLayout()

        self.toothAmount_label = QLabel("Tooths: ")
        self.toothAmount_lineEdit = QLineEdit("20")

        toothAmount_hbox.addWidget(self.toothAmount_label)
        toothAmount_hbox.addWidget(self.toothAmount_lineEdit)

        self.width_label = QLabel("Width: ")
        self.width_lineEdit = QLineEdit("1.0")

        width_hbox = QHBoxLayout()
        width_hbox.addWidget(self.width_label)
        width_hbox.addWidget(self.width_lineEdit)

        self.innerRadius_label = QLabel("Inner Radius: ")
        self.innerRadius_lineEdit = QLineEdit("1.0")

        innerRadius_hbox = QHBoxLayout()
        innerRadius_hbox.addWidget(self.innerRadius_label)
        innerRadius_hbox.addWidget(self.innerRadius_lineEdit)

        self.outerRadius_label = QLabel("Outer Radius: ")
        self.outerRadius_lineEdit = QLineEdit("5.0")

        outerRadius_hbox = QHBoxLayout()
        outerRadius_hbox.addWidget(self.outerRadius_label)
        outerRadius_hbox.addWidget(self.outerRadius_lineEdit)

        self.dx_label = QLabel("Dx: ")
        self.dx_lineEdit = QLineEdit("0.0")

        dx_hbox = QHBoxLayout()
        dx_hbox.addWidget(self.dx_label)
        dx_hbox.addWidget(self.dx_lineEdit)

        self.dy_label = QLabel("Dy: ")
        self.dy_lineEdit = QLineEdit("0.0")

        dy_hbox = QHBoxLayout()
        dy_hbox.addWidget(self.dy_label)
        dy_hbox.addWidget(self.dy_lineEdit)

        self.dz_label = QLabel("Dz: ")
        self.dz_lineEdit = QLineEdit("0.0")

        dz_hbox = QHBoxLayout()
        dz_hbox.addWidget(self.dz_label)
        dz_hbox.addWidget(self.dz_lineEdit)

        self.angle_label = QLabel("Angle: ")
        self.angle_lineEdit = QLineEdit("0")

        angle_hbox = QHBoxLayout()
        angle_hbox.addWidget(self.angle_label)
        angle_hbox.addWidget(self.angle_lineEdit)

        secondLevelHbox = QHBoxLayout()
        secondLevelHbox.addLayout(dx_hbox)
        secondLevelHbox.addLayout(dy_hbox)
        secondLevelHbox.addLayout(dz_hbox)
        secondLevelHbox.addLayout(angle_hbox)

        firstLevelHbox = QHBoxLayout()
        firstLevelHbox.addLayout(toothAmount_hbox)
        firstLevelHbox.addLayout(width_hbox)
        firstLevelHbox.addLayout(innerRadius_hbox)
        firstLevelHbox.addLayout(outerRadius_hbox)



        self.createPushButton = QPushButton("Create new gear!")
        self.deleteLastGearPushButton = QPushButton("DeleteLastGear")

        buttonsHbox = QHBoxLayout()

        buttonsHbox.addWidget(self.createPushButton)
        buttonsHbox.addWidget(self.deleteLastGearPushButton)

        mainVerticalLayout = QVBoxLayout()
        mainVerticalLayout.addLayout(secondLevelHbox)
        mainVerticalLayout.addLayout(firstLevelHbox)
        mainVerticalLayout.addLayout(buttonsHbox)

        self.setLayout(mainVerticalLayout)
