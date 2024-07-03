# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.15.2 and modified by later code editing
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# Developed by: Ligdamis A. Gutiérrez E. PhD.
# Shannon Entropy estimator for Characterization of Volcanic Seismic Signals

# Andalusian Institute of Geophysics
# Department of Theoretical Physics and the Cosmos,
# Science Faculty,
# Granada University, (Ugr), Spain, 2023

# FEMALE (PID2019-106260GB-I00) and PROOF334 FOREVER (EUR2022.134044) Spanish projects)
# Spanish Project PID2022-143083NB-100 founded by MCIN/AEI/10.13039/501100011033
# and by FEDER (EU) "Unam manera de hacer Europa".

''' WARNING: Do not modify or edit the code without permission of the author.
    In case of using this software, indicate and refer to the author and the institution he represents.
    The University of Granada, Ugr '''

# Program: Menu1.py -> Main menu to Entropy System

# Load libraries to use

# Load libraries to use
import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

# Load and see the operating system
import platform
System1 = platform.system()

# Main Class

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 430)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/Ugr.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 551, 321))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 191, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/Signal1.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(45, 45))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 220, 191, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/FilterSize1.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 130, 191, 61))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/Entropy1.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 55))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 240, 181, 61))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/Exit.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")

        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(250, 10, 21, 311))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(34, 10, 545, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(34, 56, 545, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(25, 18, 20, 46))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(570, 18, 20, 46))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 20, 534, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 236, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 236, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 236, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 236, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(9, 10, 514, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(420, 20, 111, 95))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/IAG.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(280, 20, 111, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/Ugr.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(350, 120, 111, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Images/LogoTSTC.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Command Button Format
        self.pushButton.setStyleSheet("background-color: honeydew; color: blue")   # Button color and text color  (Records Reading)
        self.pushButton_2.setStyleSheet("background-color: bisque; color: blue")   # Button color and text color  (Entropy smoothing)
        self.pushButton_3.setStyleSheet("background-color: silver; color: blue")   # Button color and text color  (Entropy_estimator)
        self.pushButton_4.setStyleSheet("background-color: CornflowerBlue; color: white")   # Button color and text color  (Exit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Menu - Granada University (Ugr)"))
        self.groupBox.setTitle(_translate("MainWindow", "Available Modules"))

        self.pushButton.setText(_translate("MainWindow", " Records Reading Module"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">Records Reading </span></p></body></html>"))

        self.pushButton_2.setText(_translate("MainWindow", " Envelope Filters module"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">Envelope Filters</span></p></body></html>"))

        self.pushButton_3.setText(_translate("MainWindow", " Entropy Calculation Module"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">Entropy Calculation </span></p></body></html>"))

        self.pushButton_4.setText(_translate("MainWindow", " Exit system"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#94181e;\">Exit system </span></p></body></html>"))

        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; color:#00007f;\">Shannon Entropy estimator for Characterization of Volcanic Seismic Signals</span></p></body></html>"))


    # Command buttons, Call to functions

        self.pushButton.clicked.connect(self.Read_records)                                  # Call the function to read records (readSignals)

        self.pushButton_2.clicked.connect(self.Smoothing1)                                  # Call the function to read records (smoothing1)

        self.pushButton_3.clicked.connect(self.Entropy_estimator)                           # Call the function to run Entropy_estimator (Entropy1)

        self.pushButton_4.clicked.connect(self.Exit)                                        # Call the function to exit system (Exit)



    """ ------------- Start of Program Functions  ------------ """

    def Entropy_estimator(self):   # Call function to Analysis_System_1 program.
        if System1 == "Windows":                                                    # In case it's Windows
            subprocess.Popen(["python", "Entropy1.py"])
            app.quit()

        else:                                                                       # In case it's Linux
            subprocess.Popen(["python3", "Entropy1.py"])
            app.quit()

    def Smoothing1(self):   # Call function to EnvelopeFilter program.
        if System1 == "Windows":                                                    # In case it's Windows
            subprocess.Popen(["python", "EnvelopeFilter.py"])
            app.quit()

        else:                                                                       # In case it's Linux
            subprocess.Popen(["python3", "EnvelopeFilter.py"])
            app.quit()


    def Read_records(self):   # Call function to Analysis_System_1 program.
        if System1 == "Windows":                                                    # In case it's Windows
            subprocess.Popen(["python", "ReadSignals1.py"])
            app.quit()

        else:                                                                       # In case it's Linux
            subprocess.Popen(["python3", "ReadSignals1.py"])
            app.quit()


    """  Fuction to exit system  """

    def Exit(self):    # Function to show exit dialog box
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Exit System")
        msg.setText("Are you sure to exit the System?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)                                        # By default, the focus is on the OK button
        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:                                           # If the answer is OK
            app.closeAllWindows()                                                   # Close all windows
            app.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    # Developed by: Ligdamis A. Gutiérrez E. PhD.