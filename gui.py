
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
    
    def addTeacher(self):
        self.addWindow = QtWidgets.QMainWindow()
        self.ui = Ui_AddTeacher()
        self.ui.setupUi(self.addWindow)
        self.addWindow.show()

    def clickPictures(self):
        self.clickWindow = QtWidgets.QMainWindow()
        self.ui = Ui_clickpic()
        self.ui.setupUi(self.clickWindow)
        self.clickWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 284)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(30, 30, 111, 31))
        self.addButton.setObjectName("addButton")
        self.queryButton = QtWidgets.QPushButton(self.centralwidget)
        self.queryButton.setGeometry(QtCore.QRect(30, 190, 111, 31))
        self.queryButton.setObjectName("queryButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(280, 230, 81, 31))
        self.cancelButton.setObjectName("cancelButton")
        self.clickBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clickBtn.setGeometry(QtCore.QRect(30, 70, 111, 31))
        self.clickBtn.setObjectName("clickBtn")
        self.trainBtn = QtWidgets.QPushButton(self.centralwidget)
        self.trainBtn.setGeometry(QtCore.QRect(30, 110, 111, 31))
        self.trainBtn.setObjectName("trainBtn")
        self.testBtn = QtWidgets.QPushButton(self.centralwidget)
        self.testBtn.setGeometry(QtCore.QRect(30, 150, 111, 31))
        self.testBtn.setObjectName("testBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.addButton.clicked.connect(self.addTeacher)
        self.clickBtn.clicked.connect(self.clickPictures)
        self.cancelButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Privileged Mode"))
        self.addButton.setText(_translate("MainWindow", "Add New Teacher"))
        self.queryButton.setText(_translate("MainWindow", "Query"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.clickBtn.setText(_translate("MainWindow", "Click Pictures"))
        self.trainBtn.setText(_translate("MainWindow", "Train"))
        self.testBtn.setText(_translate("MainWindow", "Test"))

class Ui_Login(object):

    ###### Method to handle login Button #####
    def accept(self):
        if self.gen_radioButton.isChecked():
            self.generalWindow = QtWidgets.QMainWindow()
            self.ui = Ui_General()
            self.ui.setupUi(self.generalWindow)
            self.generalWindow.show()
        if self.pri_radioButton.isChecked():
            self.priv = QtWidgets.QMainWindow()
            self.ui = Ui_PrePrev()
            self.ui.setupUi(self.priv)
            self.priv.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(337, 157)
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(130, 100, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(220, 100, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.gen_radioButton = QtWidgets.QRadioButton(Dialog)
        self.gen_radioButton.setGeometry(QtCore.QRect(140, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.gen_radioButton.setFont(font)
        self.gen_radioButton.setObjectName("gen_radioButton")
        self.pri_radioButton = QtWidgets.QRadioButton(Dialog)
        self.pri_radioButton.setGeometry(QtCore.QRect(140, 60, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pri_radioButton.setFont(font)
        self.pri_radioButton.setObjectName("pri_radioButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        ### Accept Button ###
        self.loginButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Faculty Attendance using Facial Recognition"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.gen_radioButton.setText(_translate("Dialog", "General Mode"))
        self.pri_radioButton.setText(_translate("Dialog", "Privileged Mode"))
        self.label.setText(_translate("Dialog", "Select Mode:"))

class Ui_PrePrev(object):
    def OK(self):
        if self.passField.text() == 'mytechworld':
            self.privilegedWindow = QtWidgets.QMainWindow()
            self.ui = Ui_Privileged()
            self.ui.setupUi(self.privilegedWindow)
            self.privilegedWindow.show()
        else:
            pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 144)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.passField = QtWidgets.QLineEdit(self.centralwidget)
        self.passField.setGeometry(QtCore.QRect(140, 40, 161, 20))
        self.passField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passField.setClearButtonEnabled(True)
        self.passField.setObjectName("passField")
        self.okBtn = QtWidgets.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(140, 90, 75, 23))
        self.okBtn.setObjectName("okBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(230, 90, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        
        ### Ok Button ###
        self.okBtn.clicked.connect(self.OK)
        self.cancelBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Previleged Mode"))
        self.label.setText(_translate("MainWindow", "Enter Password:"))
        self.passField.setPlaceholderText(_translate("MainWindow", "Password"))
        self.okBtn.setText(_translate("MainWindow", "OK"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))


class Ui_AddTeacher(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 229)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 90, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 47, 13))
        self.label_5.setObjectName("label_5")
        self.titleDrop = QtWidgets.QComboBox(self.centralwidget)
        self.titleDrop.setGeometry(QtCore.QRect(90, 50, 41, 22))
        self.titleDrop.setObjectName("titleDrop")
        self.titleDrop.addItem("")
        self.titleDrop.addItem("")
        self.titleDrop.addItem("")
        self.titleDrop.addItem("")
        self.firstName = QtWidgets.QLineEdit(self.centralwidget)
        self.firstName.setGeometry(QtCore.QRect(90, 90, 131, 20))
        self.firstName.setText("")
        self.firstName.setObjectName("firstName")
        self.lastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lastName.setGeometry(QtCore.QRect(320, 90, 131, 20))
        self.lastName.setText("")
        self.lastName.setObjectName("lastName")
        self.designationDrop = QtWidgets.QComboBox(self.centralwidget)
        self.designationDrop.setGeometry(QtCore.QRect(90, 120, 101, 22))
        self.designationDrop.setObjectName("designationDrop")
        self.designationDrop.addItem("")
        self.designationDrop.addItem("")
        self.designationDrop.addItem("")
        self.mGender = QtWidgets.QRadioButton(self.centralwidget)
        self.mGender.setGeometry(QtCore.QRect(90, 160, 82, 17))
        self.mGender.setObjectName("mGender")
        self.fGender = QtWidgets.QRadioButton(self.centralwidget)
        self.fGender.setGeometry(QtCore.QRect(130, 160, 82, 17))
        self.fGender.setObjectName("fGender")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(200, 180, 75, 23))
        self.resetBtn.setObjectName("resetBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(290, 180, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(380, 180, 75, 23))
        self.addBtn.setObjectName("addBtn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 20, 61, 16))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cancelBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Teacher"))
        self.label.setText(_translate("MainWindow", "Title:"))
        self.label_2.setText(_translate("MainWindow", "First Name:"))
        self.label_3.setText(_translate("MainWindow", "Last Name:"))
        self.label_4.setText(_translate("MainWindow", "Designation:"))
        self.label_5.setText(_translate("MainWindow", "Gender:"))
        self.titleDrop.setItemText(0, _translate("MainWindow", "Dr."))
        self.titleDrop.setItemText(1, _translate("MainWindow", "Mr."))
        self.titleDrop.setItemText(2, _translate("MainWindow", "Mrs."))
        self.titleDrop.setItemText(3, _translate("MainWindow", "Ms."))
        self.firstName.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.lastName.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.designationDrop.setItemText(0, _translate("MainWindow", "Asst. Professor"))
        self.designationDrop.setItemText(1, _translate("MainWindow", "Professor"))
        self.designationDrop.setItemText(2, _translate("MainWindow", "Acct. Professor"))
        self.mGender.setText(_translate("MainWindow", "M"))
        self.fGender.setText(_translate("MainWindow", "F"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
        self.label_6.setText(_translate("MainWindow", "Teacher Id:"))
        self.label_7.setText(_translate("MainWindow", "Number"))


class Ui_clickpic(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 136)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 61, 16))
        self.label.setObjectName("label")
        self.okBtn = QtWidgets.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.okBtn.setObjectName("okBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(180, 90, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.idEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.idEdit.setGeometry(QtCore.QRect(100, 40, 41, 20))
        self.idEdit.setObjectName("idEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cancelBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Click Pictures"))
        self.label.setText(_translate("MainWindow", "Teacher Id:"))
        self.okBtn.setText(_translate("MainWindow", "OK"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))