# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoggerWindwoRDaASC.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(643, 443)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_plottingView = QGroupBox(self.centralwidget)
        self.groupBox_plottingView.setObjectName(u"groupBox_plottingView")
        self.groupBox_plottingView.setGeometry(QRect(180, 10, 451, 251))
        self.label_imagePlot = QLabel(self.groupBox_plottingView)
        self.label_imagePlot.setObjectName(u"label_imagePlot")
        self.label_imagePlot.setGeometry(QRect(10, 20, 431, 221))
        self.label_imagePlot.setAlignment(Qt.AlignCenter)
        self.groupBox_control = QGroupBox(self.centralwidget)
        self.groupBox_control.setObjectName(u"groupBox_control")
        self.groupBox_control.setGeometry(QRect(10, 10, 161, 251))
        self.verticalLayoutWidget = QWidget(self.groupBox_control)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 141, 221))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_getInfo = QPushButton(self.verticalLayoutWidget)
        self.pushButton_getInfo.setObjectName(u"pushButton_getInfo")
        self.pushButton_getInfo.setMinimumSize(QSize(0, 48))

        self.verticalLayout.addWidget(self.pushButton_getInfo)

        self.pushButton_SparkSim = QPushButton(self.verticalLayoutWidget)
        self.pushButton_SparkSim.setObjectName(u"pushButton_SparkSim")
        self.pushButton_SparkSim.setMinimumSize(QSize(0, 48))

        self.verticalLayout.addWidget(self.pushButton_SparkSim)

        self.pushButton_ConnectToSerial = QPushButton(self.verticalLayoutWidget)
        self.pushButton_ConnectToSerial.setObjectName(u"pushButton_ConnectToSerial")
        self.pushButton_ConnectToSerial.setMinimumSize(QSize(0, 48))

        self.verticalLayout.addWidget(self.pushButton_ConnectToSerial)

        self.pushButton_startStopLogging = QPushButton(self.verticalLayoutWidget)
        self.pushButton_startStopLogging.setObjectName(u"pushButton_startStopLogging")
        self.pushButton_startStopLogging.setMinimumSize(QSize(0, 48))

        self.verticalLayout.addWidget(self.pushButton_startStopLogging)

        self.groupBox_logging = QGroupBox(self.centralwidget)
        self.groupBox_logging.setObjectName(u"groupBox_logging")
        self.groupBox_logging.setGeometry(QRect(190, 290, 441, 80))
        self.horizontalLayoutWidget = QWidget(self.groupBox_logging)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 421, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_logFileName = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_logFileName.setObjectName(u"lineEdit_logFileName")

        self.horizontalLayout.addWidget(self.lineEdit_logFileName)

        self.pushButton_selectFile = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_selectFile.setObjectName(u"pushButton_selectFile")

        self.horizontalLayout.addWidget(self.pushButton_selectFile)

        self.groupBox_Data = QGroupBox(self.centralwidget)
        self.groupBox_Data.setObjectName(u"groupBox_Data")
        self.groupBox_Data.setGeometry(QRect(10, 270, 161, 121))
        self.formLayoutWidget = QWidget(self.groupBox_Data)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 141, 91))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(49, 24))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(49, 24))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(49, 24))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_xValue = QLineEdit(self.formLayoutWidget)
        self.lineEdit_xValue.setObjectName(u"lineEdit_xValue")
        self.lineEdit_xValue.setMinimumSize(QSize(0, 24))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_xValue)

        self.lineEdit_yValue = QLineEdit(self.formLayoutWidget)
        self.lineEdit_yValue.setObjectName(u"lineEdit_yValue")
        self.lineEdit_yValue.setMinimumSize(QSize(0, 24))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_yValue)

        self.lineEdit_xValue_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_xValue_2.setObjectName(u"lineEdit_xValue_2")
        self.lineEdit_xValue_2.setMinimumSize(QSize(0, 24))
        self.lineEdit_xValue_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_xValue_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 643, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_plottingView.setTitle(QCoreApplication.translate("MainWindow", u"Plotting", None))
        self.label_imagePlot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_control.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.pushButton_getInfo.setText(QCoreApplication.translate("MainWindow", u"Get Info", None))
        self.pushButton_SparkSim.setText(QCoreApplication.translate("MainWindow", u"Spark Sim", None))
        self.pushButton_ConnectToSerial.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButton_startStopLogging.setText(QCoreApplication.translate("MainWindow", u"Start Logging", None))
        self.groupBox_logging.setTitle(QCoreApplication.translate("MainWindow", u"Log File Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_selectFile.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_Data.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"z", None))
    # retranslateUi

