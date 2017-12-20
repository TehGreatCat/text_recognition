# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys
from PIL import ImageGrab
from tesseract import get_string

def setMoveWindow(widget):
    """
    Позволяет перемещать окно ухватившись не только за заголовок, а за произвольный виджит (widget).
    """
    win = widget.window()
    cursorShape = widget.cursor().shape()
    moveSource = getattr(widget, "mouseMoveEvent")
    pressSource = getattr(widget, "mousePressEvent")
    releaseSource = getattr(widget, "mouseReleaseEvent")

    def move(event):
        if move.b_move:
            x = event.globalX() + move.x_korr - move.lastPoint.x()
            y = event.globalY() + move.y_korr - move.lastPoint.y()
            win.move(x, y)
            widget.setCursor(QtCore.Qt.SizeAllCursor)
        return moveSource(event)

    def press(event):
        if event.button() == QtCore.Qt.LeftButton:
            # Корекция геометрии окна: учитываем размеры рамки и заголовока
            x_korr = win.frameGeometry().x() - win.geometry().x()
            y_korr = win.frameGeometry().y() - win.geometry().y()
            # Корекция геометрии виджита: учитываем смещение относительно окна
            parent = widget
            while not parent == win:
                x_korr -= parent.x()
                y_korr -= parent.y()
                parent = parent.parent()
            move.__dict__.update({"lastPoint": event.pos(), "b_move": True, "x_korr": x_korr, "y_korr": y_korr})
        else:
            move.__dict__.update({"b_move": False})
            widget.setCursor(cursorShape)
        return pressSource(event)

    def release(event):
        move.__dict__.update({"b_move": False})
        widget.setCursor(cursorShape)
        return releaseSource(event)

    setattr(widget, "mouseMoveEvent", move)
    setattr(widget, "mousePressEvent", press)
    setattr(widget, "mouseReleaseEvent", release)
    move.__dict__.update({"b_move": False})
    return widget


class Ui_MainWindow(object):
    MainWindow = ""
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_NoSystemBackground, True)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("background-color: rgb(38, 44, 52);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setText("Tr")
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("Handwritten OCR_16px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pushButton_2.setIcon(icon)
        # self.pushButton_2.clicked.connect(self.shoot)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)



        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Handwritten OCR_16px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.clicked.connect(self.shoot)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)


        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Delete_16px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.closeIt)
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(21)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("border:3px solid rgb(62, 102, 141); opacity: 1;")


        self.widget_2.setObjectName("widget_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgb(38, 44, 52);")
        self.widget.setObjectName("widget")

        self.widget_2.resizeEvent = self.resiz
        self.sizegrip = QtWidgets.QSizeGrip(self.widget_2)
        self.sizegrip.setStyleSheet(
            "border:0px solid rgb(62, 102, 141); opacity: 1; alignment: 'AlignRight | AlignBottom';")
        width = self.widget_2.frameGeometry().width()
        height = self.widget_2.frameGeometry().height()
        self.label.setText(str(width) + "x" + str(height))

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setStyleSheet("background-color: rgb(38, 44, 52);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 65))
        self.textBrowser.setStyleSheet("background-color: rgb(38, 44, 52);\n""color: rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def resiz(self, event):
        width = self.widget_2.frameGeometry().width()
        height = self.widget_2.frameGeometry().height()
        self.label.setText("  " + str(width) + "x" + str(height))

    def shoot(self):
        try:
            name = "buff.jpg"

            x_buff = self.widget_2.x()
            y_buff = self.widget_2.y()
            x_b = self.widget_3.x()
            y_b = self.widget_3.y()
            x = self.MainWindow.x()
            y = self.MainWindow.y()
            width = self.widget_2.width()
            height = self.widget_2.height()

            path = name
            ImageGrab.grab(bbox=(x + x_buff, y + y_buff, x + x_buff + width, y + y_buff + height)).save(path, "JPEG")
            result = get_string(path)
            # print(result)
            self.textBrowser.setText(result)
        except Exception as e:
            print(e)


    def closeIt(self):
        self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    setMoveWindow(w)
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())