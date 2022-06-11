# Form implementation generated from reading ui file 'resources/main_view.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PyClick1.0")
        MainWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.controlButton = QtWidgets.QPushButton(self.centralwidget)
        self.controlButton.setGeometry(QtCore.QRect(20, 140, 361, 34))
        self.controlButton.setObjectName("controlButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 351, 61))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.totalClicksLabel = QtWidgets.QLabel(self.widget)
        self.totalClicksLabel.setObjectName("totalClicksLabel")
        self.gridLayout.addWidget(self.totalClicksLabel, 0, 0, 1, 1)
        self.timeLabel = QtWidgets.QLabel(self.widget)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout.addWidget(self.timeLabel, 0, 1, 1, 1)
        self.counterClicks = QtWidgets.QLCDNumber(self.widget)
        self.counterClicks.setSmallDecimalPoint(False)
        self.counterClicks.setObjectName("counterClicks")
        self.gridLayout.addWidget(self.counterClicks, 1, 0, 1, 1)
        self.counterTime = QtWidgets.QLCDNumber(self.widget)
        self.counterTime.setSmallDecimalPoint(False)
        self.counterTime.setObjectName("counterTime")
        self.gridLayout.addWidget(self.counterTime, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.controlButton.setText(_translate("MainWindow", "start | stop (F2)"))
        self.totalClicksLabel.setText(_translate("MainWindow", "Total Clicks"))
        self.timeLabel.setText(_translate("MainWindow", "Time"))
        self.counterClicks.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.counterTime.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())