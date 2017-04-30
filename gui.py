
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_General(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 194)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.markButton = QtWidgets.QPushButton(self.centralwidget)
        self.markButton.setGeometry(QtCore.QRect(40, 30, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.markButton.setFont(font)
        self.markButton.setObjectName("markButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(40, 120, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cancelButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "General Mode"))
        self.markButton.setText(_translate("MainWindow", "Mark Attendance"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))

class Ui_Privileged(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 195)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(30, 40, 111, 31))
        self.addButton.setObjectName("addButton")
        self.queryButton = QtWidgets.QPushButton(self.centralwidget)
        self.queryButton.setGeometry(QtCore.QRect(30, 80, 111, 31))
        self.queryButton.setObjectName("queryButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(240, 140, 81, 31))
        self.cancelButton.setObjectName("cancelButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cancelButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Privileged Mode"))
        self.addButton.setText(_translate("MainWindow", "Add New Teacher"))
        self.queryButton.setText(_translate("MainWindow", "Query"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))

class Ui_Login(object):

    ###### Method to handle login Button #####
    def accept(self):
        if self.pass_lineEdit.text() == 'mytechworld':
            if self.gen_radioButton.isChecked():
                self.generalWindow = QtWidgets.QMainWindow()
                self.ui = Ui_General()
                self.ui.setupUi(self.generalWindow)
                self.generalWindow.show()
            if self.pri_radioButton.isChecked():
                self.privilegedwindow = QtWidgets.QMainWindow()
                self.ui = Ui_Privileged()
                self.ui.setupUi(self.privilegedwindow)
                self.privilegedwindow.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 202)
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(140, 140, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(230, 140, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.gen_radioButton = QtWidgets.QRadioButton(Dialog)
        self.gen_radioButton.setGeometry(QtCore.QRect(140, 80, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.gen_radioButton.setFont(font)
        self.gen_radioButton.setObjectName("gen_radioButton")
        self.pri_radioButton = QtWidgets.QRadioButton(Dialog)
        self.pri_radioButton.setGeometry(QtCore.QRect(140, 100, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pri_radioButton.setFont(font)
        self.pri_radioButton.setObjectName("pri_radioButton")
        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(140, 40, 151, 20))
        self.pass_lineEdit.setText("")
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setClearButtonEnabled(True)
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)

        ###################LoginButton###################
        self.loginButton.clicked.connect(self.accept)

        self.cancelButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.gen_radioButton.setText(_translate("Dialog", "General Mode"))
        self.pri_radioButton.setText(_translate("Dialog", "Privileged Mode"))
        self.pass_lineEdit.setPlaceholderText(_translate("Dialog", "Password"))
        self.label.setText(_translate("Dialog", "Enter Password:"))