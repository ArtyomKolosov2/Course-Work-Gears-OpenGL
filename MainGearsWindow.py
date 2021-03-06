import os
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QAction, QApplication, QLabel,
                             QMainWindow, QMessageBox, QScrollArea,
                             QSizePolicy, QWidget, QHBoxLayout, QVBoxLayout)

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

        self.setWindowTitle("GEARS")
        self.resize(800, 700)
        self.showInfo()

    def showInfo(self):
        text = """<p style="font-size:18px;"><b>?????????????????? ???????????????????????????? ???????????????????? ?? ??????????????????????????
                <br/>?????????????? ???????????????????????? ?????????????????????? ???????????????????????????? ???????????? ?? ????????????????????</b>
                <br/><br/><center>???????????????? ????????????</center><br/>
                ???? ???????????????????? ?????????????????????? ???????????????????? ?? ???????????????????? ??????????????
                <br/><b>????????: ???????????????????? ???????????????? ??????????????????</b><br/>                                                                                                     
                ??????????????????????: ?????????????? ????. 10701219 ?????????????? ??.??.</p>
                """

        QMessageBox.information(self, "Greetings!", text, QMessageBox.Ok)

    def createNewGear(self):
        reflectance1 = (0.8, 0.1, 0.0, 1.0)

        try:
            toothAmount = int(self.paramsInput.toothAmount_lineEdit.text())
            innerRadius = float(self.paramsInput.innerRadius_lineEdit.text())
            outerRadius = float(self.paramsInput.outerRadius_lineEdit.text())
            width = float(self.paramsInput.width_lineEdit.text())
            if toothAmount < 5:
                raise Exception("Tooth amount lower than 5!")

            if innerRadius <= 0:
                raise Exception("Inner radius must be greater than zero!")

            if outerRadius <= 0:
                raise Exception("Outer radius must be greater than zero!")

            if width <= 0:
                raise Exception("Width  must be greater than zero!")

            if innerRadius > outerRadius:
                raise Exception("Inner radius must be lower than outer!")



            gear = GearMaker.makeGear(
                    reflectance1,
                    innerRadius,
                    outerRadius,
                    width,
                    1.0,
                    toothAmount)

            gear.dx = float(self.paramsInput.dx_lineEdit.text())
            gear.dy = float(self.paramsInput.dy_lineEdit.text())
            gear.dz = float(self.paramsInput.dz_lineEdit.text())
            gear.outputAngle = float(self.paramsInput.angle_lineEdit.text())
            self.glWidget.gears.append(gear)

            self.update()

        except Exception as ex:
            QMessageBox.critical(self, "???????????? ", str(ex), QMessageBox.Ok)

    def deleteLastGear(self):
        if len(self.glWidget.gears) > 0:
            self.glWidget.gears.pop()
            self.update()

    def about(self):
        os.system("Helper.chm")

    def createActions(self):

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                               triggered=self.close)

        self.aboutAct = QAction("&Help", self, triggered=self.about)

        self.helpAct = QAction("&About", self, triggered=self.showInfo)

        self.aboutQtAct = QAction("About &Qt", self,
                                  triggered=QApplication.instance().aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.helpAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def setPixmap(self, pixmap):
        self.pixmapLabel.setPixmap(pixmap)
        size = pixmap.size()

        if size - QSize(1, 0) == self.pixmapLabelArea.maximumViewportSize():
            size -= QSize(1, 0)

        self.pixmapLabel.resize(size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    style = """ QLineEdit:hover{border-radius:4px;
                                border-color:rgb(0,128,0);
                                background-color:rgb(220,220,220);}
                                QLineEdit{background: white;
                                font:11px Arial;
                                border: 2px solid grey;
                                border-radius:4px;}
                                QMainWindow{background-color: rgb(235, 237, 235);}   
                QPushButton{
                                border-radius: 5px;
                                border: 2px solid black;
                                background: white;;
                                font: 13px Arial italic;
                                }
                                QPushButton:hover{
                                border-radius: 5px;
                                border-color: rgb(0,128,0);
                                background-color: rgb(210,210,210)}
                                QPushButton:pressed{
                                border-radius: 5px;
                                border-color: rgb(0,128,0);
                                background-color: rgb(240,240,240);
                                }
                        QGroupBox{
                        border: 2px solid green;
                        }
                        """

    mainWin = MainWindow()

    mainWin.setStyleSheet(style)
    mainWin.show()
    sys.exit(app.exec_())
