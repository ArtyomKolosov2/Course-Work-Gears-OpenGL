from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSlider, QLabel, QHBoxLayout, QVBoxLayout, QWidget


class QString(object):
    pass


class AxisSlider(QWidget):

    def __init__(self, axisName: str):
        super().__init__()

        self.textLabel = QLabel()
        self.setFont(QFont("Arial", 15, 1))
        self.textLabel.setText('0')

        self.slider = QSlider(Qt.Vertical)

        text = QLabel()
        text.setText(axisName)

        textHbox = QHBoxLayout()

        textHbox.addWidget(text)
        textHbox.addWidget(self.textLabel)

        vbox = QVBoxLayout()
        vbox.addLayout(textHbox)
        vbox.addWidget(self.slider)

        self.setMaximumWidth(100)
        self.setLayout(vbox)

    def valueChangedEvent(self, value):
        self.textLabel.setText(str(value))
        self.update()

    @staticmethod
    def createSlider(changedSignal, setterSlot, axisName):
        axisSlider = AxisSlider(axisName)
        axisSlider.slider.setRange(0, 360 * 16)
        axisSlider.slider.setSingleStep(16)
        axisSlider.slider.setPageStep(15 * 16)
        axisSlider.slider.setTickInterval(15 * 16)
        axisSlider.slider.setTickPosition(QSlider.TicksRight)
        axisSlider.slider.valueChanged.connect(setterSlot)
        axisSlider.slider.valueChanged.connect(axisSlider.valueChangedEvent)
        changedSignal.connect(axisSlider.slider.setValue)

        return axisSlider
