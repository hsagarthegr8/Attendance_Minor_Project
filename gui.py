
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import facerec,os,helper
import databasehelper as db
import mysql.connector
from mysql.connector import errorcode

class Ui_General(object):
    def mark(self,MainWindow):
        name,id = facerec.recognize(True)
        comment = "Attendance Marked for {}. Is this You???".format(name)
        buttonReply = QtWidgets.QMessageBox.question(MainWindow, 'Attendance Marked', comment, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                         QtWidgets.QMessageBox.Yes)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            cnx = db.connect()
            cnx.database = 'RJIT'
            db.mark_attendance(cnx,id)
        else:
            pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 194)
        MainWindow.setFixedSize(MainWindow.size())
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
        self.markButton.clicked.connect(lambda: self.mark(MainWindow))
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
        self.trainBtn.setEnabled(True)
    
    def test(self):
        facerec.recognize()
        

    def train(self):
        facerec.train()
        self.trainBtn.setEnabled(False)
    
    def query(self):
        self.queryWindow = QtWidgets.QMainWindow()
        self.ui = Ui_QueryWindow()
        self.ui.setupUi(self.queryWindow)
        self.queryWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 284)
        MainWindow.setFixedSize(MainWindow.size())
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
        self.testBtn.clicked.connect(self.test)
        self.trainBtn.clicked.connect(self.train)
        self.clickBtn.clicked.connect(self.clickPictures)
        self.cancelButton.clicked.connect(MainWindow.close)
        self.queryButton.clicked.connect(self.query)
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
        db.set_database()
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
        Dialog.setFixedSize(Dialog.size())
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
    def OK(self,MainWindow):
        if self.passField.text() == 'mytechworld':
            self.privilegedWindow = QtWidgets.QMainWindow()
            self.ui = Ui_Privileged()
            self.ui.setupUi(self.privilegedWindow)
            self.privilegedWindow.show()
            MainWindow.close()
        else:
            pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 144)
        MainWindow.setFixedSize(MainWindow.size())
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
        self.okBtn.clicked.connect(lambda: self.OK(MainWindow))
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
    def add(self, MainWindow):
        id = self.label_7.text()
        fname = self.firstName.text()
        lname = self.lastName.text()
        title = self.titleDrop.currentText()
        design = self.designationDrop.currentText()
        gender = None
        if self.fGender.isChecked():
            gender = 'F'
        elif self.mGender.isChecked():
            gender = 'M'
        result,comment = db.add_teacher(id,title,fname,lname,gender,design)
        if result:
            helper.ensure_dir('Training/'+id+'/')
            MainWindow.close()
            buttonReply = QtWidgets.QMessageBox.question(MainWindow, 'Teacher Added', comment, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            
        
            
    
    def reset(self):
        self.firstName.clear()
        self.lastName.clear()
        self.mGender.setChecked(True)
        self.titleDrop.setCurrentIndex(0)
        self.designationDrop.setCurrentIndex(0)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 229)
        MainWindow.setFixedSize(MainWindow.size())
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
        self.label_7.setGeometry(QtCore.QRect(90, 20, 80, 16))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.addBtn.clicked.connect(lambda: self.add(MainWindow))
        self.resetBtn.clicked.connect(self.reset)
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
        helper.ensure_dir('Training/')
        s = os.listdir('Training')
        if len(s)<9:
            id = 'RJITCSEIT0'+str(len(s)+1)
        else:
            id = 'RJITCSEIT'+str(len(s)+1)
        self.label_7.setText(_translate("MainWindow", id ))


class Ui_clickpic(object):
    def go(self):
        id = self.idBox.currentText()
        cnx = db.connect()
        cnx.database = 'RJIT'
        cursor = cnx.cursor()
        try:
            cursor.execute("SELECT `first_name`, `last_name`, `title` FROM `teachers` \
                       WHERE `teacher_id` = '{}'".format(id))
            s = cursor.fetchall()
            self.fName.setText(s[0][0])
            self.lName.setText(s[0][1])
            self.title.setText(s[0][2])
            self.okBtn.setEnabled(True)
        except mysql.connector.Error as err:
            print err.msg

    def click(self):
        id = self.idBox.currentText()
        facerec.create_dataset(id)
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 216)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 61, 16))
        self.label.setObjectName("label")
        self.okBtn = QtWidgets.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(230, 180, 75, 23))
        self.okBtn.setObjectName("okBtn")
        self.okBtn.setEnabled(False)
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(320, 180, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.idBox = QtWidgets.QComboBox(self.centralwidget)
        self.idBox.setGeometry(QtCore.QRect(100, 40, 121, 22))
        self.idBox.setObjectName("idBox")
        for i in range(len(os.listdir('Training'))):
            self.idBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 61, 16))
        self.label_3.setObjectName("label_3")
        self.goBtn = QtWidgets.QPushButton(self.centralwidget)
        self.goBtn.setGeometry(QtCore.QRect(240, 40, 51, 23))
        self.goBtn.setObjectName("goBtn")
        self.fName = QtWidgets.QLineEdit(self.centralwidget)
        self.fName.setEnabled(False)
        self.fName.setGeometry(QtCore.QRect(100, 120, 131, 20))
        self.fName.setObjectName("fName")
        self.lName = QtWidgets.QLineEdit(self.centralwidget)
        self.lName.setEnabled(False)
        self.lName.setGeometry(QtCore.QRect(100, 150, 131, 20))
        self.lName.setObjectName("lName")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 47, 13))
        self.label_4.setObjectName("label_4")
        self.title = QtWidgets.QLineEdit(self.centralwidget)
        self.title.setEnabled(False)
        self.title.setGeometry(QtCore.QRect(100, 90, 51, 20))
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.goBtn.clicked.connect(self.go)
        self.okBtn.clicked.connect(self.click)
        self.cancelBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Click Pictures"))
        self.label.setText(_translate("MainWindow", "Teacher Id:"))
        self.okBtn.setText(_translate("MainWindow", "OK"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.label_2.setText(_translate("MainWindow", "First Name:"))
        self.label_3.setText(_translate("MainWindow", "Last Name:"))
        self.goBtn.setText(_translate("MainWindow", "Go"))
        self.label_4.setText(_translate("MainWindow", "Title:"))
        i = 0
        print(os.listdir('Training'))
        for id in os.listdir('Training'):
            self.idBox.setItemText(i, _translate("MainWindow", id))
            i += 1

class Ui_QueryWindow(object):
    def query(self):
        tid = self.teacherId.text()
        title = self.titleBox.currentText()
        fName = self.fName.text()
        lName = self.lName.text()
        design = self.designBox.currentText()
        gender = self.genderBox.currentText()
        sDate = self.startDate.date().toPyDate()
        eDate = self.endDate.date().toPyDate()
        if not tid:
            tid = '%'
        if not fName:
            fName = '%'
        if not lName:
            lName = '%'
        if title =='All':
            title = '%'
        if design == 'All':
            design =='%'
        if gender == 'All':
            gender = '%'
        if design == 'All':
            design = '%'
        if not self.dateEnBox.isChecked():
            sDate = '%'
        if not self.betweenBox.isChecked():
            eDate = '%'
        result = db.query(tid,title,fName,lName,design,gender,sDate,eDate)
        self.numRecords.setText(str(len(result)) +' Record(s) found.')
        if len(result):
            self.printBtn.setEnabled(True)
        else:
            self.printBtn.setEnabled(False)
        self.numRecords.show()
        self.myTable.setRowCount(0)
        for i in range(len(result)):
            self.myTable.insertRow(i)
            for j in range(9):
                self.myTable.setItem(i,j,QtWidgets.QTableWidgetItem(str(result[i][j])))
        
    def dateToggle(self):
        if self.startDate.isEnabled():
            self.startDate.setEnabled(False)
            self.betweenBox.setEnabled(False)
            self.betweenBox.setChecked(False)
            self.endDate.setEnabled(False)
        else:
            self.startDate.setEnabled(True)
            self.betweenBox.setEnabled(True)
        
    def betweenToggle(self):
        if self.endDate.isEnabled():
            self.endDate.setEnabled(False)
        else:
            self.endDate.setEnabled(True)
    
    def reset(self):
        self.teacherId.setText('')
        self.fName.setText('')
        self.lName.setText('')
        self.titleBox.setCurrentIndex(0)
        self.designBox.setCurrentIndex(0)
        self.genderBox.setCurrentIndex(0)
        self.myTable.setRowCount(0)
        self.printBtn.setEnabled(False)
        self.dateEnBox.setChecked(False)
        self.numRecords.hide()

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            self.handlePaintRequest(dialog.printer())
    
    def handlePaintRequest(self, printer):
        document = self.makeTableDocument()
        document.print_(printer)

    def makeTableDocument(self):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        rows = self.myTable.rowCount()
        columns = self.myTable.columnCount()
        table = cursor.insertTable(rows + 1, columns)
        format = table.format()
        format.setHeaderRowCount(1)
        table.setFormat(format)
        format = cursor.blockCharFormat()
        format.setFontWeight(QtGui.QFont.Bold)
        for column in range(columns):
            cursor.setCharFormat(format)
            cursor.insertText(self.myTable.horizontalHeaderItem(column).text())
            cursor.movePosition(QtGui.QTextCursor.NextCell)
        
        for row in range(rows):
            for column in range(columns):
                cursor.insertText(
                    self.myTable.item(row, column).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        
        return document
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 647)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 80, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(454, 80, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 30, 41, 21))
        self.label_5.setObjectName("label_5")
        self.teacherId = QtWidgets.QLineEdit(self.centralwidget)
        self.teacherId.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.teacherId.setObjectName("teacherId")
        self.fName = QtWidgets.QLineEdit(self.centralwidget)
        self.fName.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.fName.setObjectName("fName")
        self.lName = QtWidgets.QLineEdit(self.centralwidget)
        self.lName.setGeometry(QtCore.QRect(310, 80, 113, 20))
        self.lName.setObjectName("lName")
        self.titleBox = QtWidgets.QComboBox(self.centralwidget)
        self.titleBox.setGeometry(QtCore.QRect(310, 30, 51, 21))
        self.titleBox.setObjectName("titleBox")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.designBox = QtWidgets.QComboBox(self.centralwidget)
        self.designBox.setGeometry(QtCore.QRect(524, 80, 111, 22))
        self.designBox.setObjectName("designBox")
        self.designBox.addItem("")
        self.designBox.addItem("")
        self.designBox.addItem("")
        self.designBox.addItem("")
        self.genderBox = QtWidgets.QComboBox(self.centralwidget)
        self.genderBox.setGeometry(QtCore.QRect(734, 80, 69, 22))
        self.genderBox.setObjectName("genderBox")
        self.genderBox.addItem("")
        self.genderBox.addItem("")
        self.genderBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(680, 80, 51, 20))
        self.label_6.setObjectName("label_6")
        self.startDate = QtWidgets.QDateEdit(self.centralwidget)
        self.startDate.setEnabled(False)
        self.startDate.setGeometry(QtCore.QRect(100, 130, 110, 21))
        self.startDate.setDate(QtCore.QDate(2017, 5, 19))
        self.startDate.setObjectName("startDate")
        self.endDate = QtWidgets.QDateEdit(self.centralwidget)
        self.endDate.setEnabled(False)
        self.endDate.setGeometry(QtCore.QRect(310, 130, 110, 22))
        self.endDate.setMaximumDate(QtCore.QDate(2117, 5, 19))
        self.endDate.setMinimumDate(QtCore.QDate(2017, 5, 19))
        self.endDate.setObjectName("endDate")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 47, 41))
        self.label_7.setObjectName("label_7")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(870, 600, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(690, 600, 75, 23))
        self.searchBtn.setObjectName("searchBtn")
        self.printBtn = QtWidgets.QPushButton(self.centralwidget)
        self.printBtn.setEnabled(False)
        self.printBtn.setGeometry(QtCore.QRect(780, 600, 75, 23))
        self.printBtn.setObjectName("printBtn")
        self.betweenBox = QtWidgets.QCheckBox(self.centralwidget)
        self.betweenBox.setEnabled(False)
        self.betweenBox.setGeometry(QtCore.QRect(240, 130, 81, 21))
        self.betweenBox.setObjectName("betweenBox")
        self.dateEnBox = QtWidgets.QCheckBox(self.centralwidget)
        self.dateEnBox.setGeometry(QtCore.QRect(70, 130, 70, 21))
        self.dateEnBox.setText("")
        self.dateEnBox.setObjectName("dateEnBox")
        self.myTable = QtWidgets.QTableWidget(self.centralwidget)
        self.myTable.setGeometry(QtCore.QRect(20, 170, 921, 401))
        self.myTable.setObjectName("myTable")
        self.myTable.setColumnCount(9)
        self.myTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.myTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.myTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.myTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.myTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.myTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.myTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.myTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.myTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.myTable.setHorizontalHeaderItem(8, item)
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(600, 600, 75, 23))
        self.resetBtn.setObjectName("resetBtn")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 600, 121, 16))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.numRecords = QtWidgets.QLabel(self.centralwidget)
        self.numRecords.setGeometry(QtCore.QRect(470, 600, 101, 16))
        self.numRecords.setObjectName("numRecords")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.dateEnBox.toggled.connect(self.dateToggle)
        self.betweenBox.toggled.connect(self.betweenToggle)
        self.searchBtn.clicked.connect(self.query)
        self.resetBtn.clicked.connect(self.reset)
        self.printBtn.clicked.connect(self.handlePrint)
        self.cancelBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Query"))
        self.label.setText(_translate("MainWindow", "Teacher ID:"))
        self.label_2.setText(_translate("MainWindow", "First Name:"))
        self.label_3.setText(_translate("MainWindow", "Last Name:"))
        self.label_4.setText(_translate("MainWindow", "Designation:"))
        self.label_5.setText(_translate("MainWindow", "Title:"))
        self.titleBox.setItemText(0, _translate("MainWindow", "All"))
        self.titleBox.setItemText(1, _translate("MainWindow", "Dr."))
        self.titleBox.setItemText(2, _translate("MainWindow", "Mr."))
        self.titleBox.setItemText(3, _translate("MainWindow", "Mrs."))
        self.titleBox.setItemText(4, _translate("MainWindow", "Ms."))
        self.designBox.setItemText(0, _translate("MainWindow", "All"))
        self.designBox.setItemText(1, _translate("MainWindow", "Asst. Professor"))
        self.designBox.setItemText(2, _translate("MainWindow", "Professor"))
        self.designBox.setItemText(3, _translate("MainWindow", "Acct. Professor"))
        self.genderBox.setItemText(0, _translate("MainWindow", "All"))
        self.genderBox.setItemText(1, _translate("MainWindow", "M"))
        self.genderBox.setItemText(2, _translate("MainWindow", "F"))
        self.label_6.setText(_translate("MainWindow", "Gender:"))
        self.label_7.setText(_translate("MainWindow", "Date:"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.printBtn.setText(_translate("MainWindow", "Print"))
        self.betweenBox.setText(_translate("MainWindow", "Between"))
        item = self.myTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Teacher ID"))
        item = self.myTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.myTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.myTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.myTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.myTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Designation"))
        item = self.myTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Date"))
        item = self.myTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Login Time"))
        item = self.myTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Logout Time"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.numRecords.setText(_translate("MainWindow", "0 Record(s) Found."))
        self.numRecords.hide()