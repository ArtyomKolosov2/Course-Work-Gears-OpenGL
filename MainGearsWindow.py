import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QAction, QApplication, QLabel,
                             QMainWindow, QMessageBox, QScrollArea,
                             QSizePolicy, QSlider, QWidget, QHBoxLayout, QVBoxLayout, QErrorMessage)

from Modules.GearMaker import GearMaker
from Widgets.GearParamsInput import GearParamsInput
from Widgets.GlSimulationWidget import GLWidget
from Widgets.AxisSlider import AxisSlider


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.glWidget = GLWidget()
        self.pixmapLabel = QLabel()

        self.glWidgetArea = QScrollArea()
        self.glWidgetArea.setWidget(self.glWidget)
        self.glWidgetArea.setWidgetResizable(True)
        self.glWidgetArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setSizePolicy(QSizePolicy.Ignored,
                                        QSizePolicy.Ignored)
        self.glWidgetArea.setMinimumSize(50, 50)

        # self.pixmapLabelArea = QScrollArea()
        # self.pixmapLabelArea.setWidget(self.pixmapLabel)
        # self.pixmapLabelArea.setSizePolicy(QSizePolicy.Ignored,
        #      QSizePolicy.Ignored)
        # self.pixmapLabelArea.setMinimumSize(50, 50)

        xSlider = AxisSlider.createSlider(self.glWidget.xRotationChanged,
                                          self.glWidget.setXRotation, "x")
        ySlider = AxisSlider.createSlider(self.glWidget.yRotationChanged,
                                          self.glWidget.setYRotation, "y")
        zSlider = AxisSlider.createSlider(self.glWidget.zRotationChanged,
                                          self.glWidget.setZRotation, "z")

        self.createActions()
        self.createMenus()

        centralWidgetLayout = QHBoxLayout()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.glWidgetArea)

        hbox2 = QVBoxLayout()
        # centralLayout.addWidget(self.pixmapLabelArea, 0, 1)

        hbox2.addSpacing(2)
        hbox2.addWidget(xSlider)
        hbox2.addSpacing(2)
        hbox2.addWidget(ySlider)
        hbox2.addSpacing(2)
        hbox2.addWidget(zSlider)
        hbox2.addSpacing(2)

        centralWidgetLayout.addLayout(hbox1)
        centralWidgetLayout.addLayout(hbox2)

        verticalLayout = QVBoxLayout()
        verticalLayout.addLayout(centralWidgetLayout)

        self.paramsInput = GearParamsInput()
        self.paramsInput.createPushButton.clicked.connect(self.createNewGear)
        self.paramsInput.deleteLastGearPushButton.clicked.connect(self.deleteLastGear)

        verticalLayout.addWidget(self.paramsInput)

        centralWidget.setLayout(verticalLayout)

        xSlider.slider.setValue(15 * 16)
        ySlider.slider.setValue(345 * 16)
        zSlider.slider.setValue(0 * 16)

        self.setWindowTitle("Grabber")
        self.resize(800, 700)

    def createNewGear(self):
        reflectance1 = (0.8, 0.1, 0.0, 1.0)

        try:
            toothAmount = int(self.paramsInput.toothAmount_lineEdit.text())
            if toothAmount < 5:
                raise Exception("Tooth amount lower than 5!")

            gear = GearMaker.makeGear(
                    reflectance1,
                    float(self.paramsInput.innerRadius_lineEdit.text()),
                    float(self.paramsInput.outerRadius_lineEdit.text()),
                    float(self.paramsInput.width_lineEdit.text()),
                    1.0,
                    toothAmount)

            gear.dx = float(self.paramsInput.dx_lineEdit.text())
            gear.dy = float(self.paramsInput.dy_lineEdit.text())
            gear.dz = float(self.paramsInput.dz_lineEdit.text())
            gear.outputAngle = float(self.paramsInput.angle_lineEdit.text())

            self.glWidget.gears.append(gear)

            self.update()

        except Exception as ex:
            QMessageBox.critical(self, "Ошибка ", str(ex), QMessageBox.Ok)

    def deleteLastGear(self):
        if len(self.glWidget.gears) > 0:
            self.glWidget.gears.pop()
            self.update()

    def grabFrameBuffer(self):
        pass

    # image = self.glWidget.grabFramebuffer()
    # self.setPixmap(QPixmap.fromImage(image))

    def clearPixmap(self):
        pass

    # self.setPixmap(QPixmap())

    def about(self):
        QMessageBox.about(self, "About Grabber",
                          "The <b>Grabber</b> example demonstrates two approaches for "
                          "rendering OpenGL into a Qt pixmap.")

    def createActions(self):
        self.grabFrameBufferAct = QAction("&Grab Frame Buffer", self,
                                          shortcut="Ctrl+G", triggered=self.grabFrameBuffer)

        self.clearPixmapAct = QAction("&Clear Pixmap", self,
                                      shortcut="Ctrl+L", triggered=self.clearPixmap)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                               triggered=self.close)

        self.aboutAct = QAction("&About", self, triggered=self.about)

        self.aboutQtAct = QAction("About &Qt", self,
                                  triggered=QApplication.instance().aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.grabFrameBufferAct)
        self.fileMenu.addAction(self.clearPixmapAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def setPixmap(self, pixmap):
        self.pixmapLabel.setPixmap(pixmap)
        size = pixmap.size()

        if size - QSize(1, 0) == self.pixmapLabelArea.maximumViewportSize():
            size -= QSize(1, 0)

        self.pixmapLabel.resize(size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
