import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QAction, QApplication, QLabel,
                             QMainWindow, QMessageBox, QScrollArea,
                             QSizePolicy, QSlider, QWidget, QHBoxLayout)

from Widgets.GlSimulationWidget import GLWidget


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

        xSlider = self.createSlider(self.glWidget.xRotationChanged,
                                    self.glWidget.setXRotation)
        ySlider = self.createSlider(self.glWidget.yRotationChanged,
                                    self.glWidget.setYRotation)
        zSlider = self.createSlider(self.glWidget.zRotationChanged,
                                    self.glWidget.setZRotation)

        self.createActions()
        self.createMenus()

        centralLayout = QHBoxLayout()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.glWidgetArea)

        hbox2 = QHBoxLayout()
        # centralLayout.addWidget(self.pixmapLabelArea, 0, 1)

        hbox2.addSpacing(2)
        hbox2.addWidget(xSlider)
        hbox2.addSpacing(2)
        hbox2.addWidget(ySlider)
        hbox2.addSpacing(2)
        hbox2.addWidget(zSlider)
        hbox2.addSpacing(2)

        centralLayout.addLayout(hbox1)
        centralLayout.addLayout(hbox2)

        centralWidget.setLayout(centralLayout)

        xSlider.setValue(15 * 16)
        ySlider.setValue(345 * 16)
        zSlider.setValue(0 * 16)

        self.setWindowTitle("Grabber")
        self.resize(800, 700)

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

    def createSlider(self, changedSignal, setterSlot):
        slider = QSlider(Qt.Vertical)
        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QSlider.TicksRight)
        slider.setStyleSheet("margin: 5px; border: 2px solid black; ")
        slider.valueChanged.connect(setterSlot)
        changedSignal.connect(slider.setValue)

        return slider

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
