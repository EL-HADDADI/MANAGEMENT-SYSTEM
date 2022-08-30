from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUi
import db
import sqlite3

class LOGIN(QMainWindow):
    def __init__(self):
        super().__init__()
        self.l = None
        loadUi("log.ui",self)
        self.clear_btn.clicked.connect(self.clear)
        self.login_btn.clicked.connect(self.logfcn)
        self.message = QMessageBox()

    def logfcn(self):
        self.uname = self.username.text()
        self.pword = self.password.text()

        if self.uname == "" and self.pword == "":
            self.l =StudentManagement()
            self.l.show()
            self.hide()

            
        else:
            self.message.information(self,"info","invalid login")


    #def anotherWindow(self):
        #if self.l is None:
            #self.l = StudentManagement()
            #self.l.show()
        #else:
            #self.l = None


    def clear(self):
        self.username.setText("")
        self.password.setText("")




class StudentManagement(QWidget):
    def __init__(self):
        super().__init__()
        print("okayyy")
        loadUi("sms.ui", self)
        self.message = QMessageBox()
        self.check.hide()
        self.updt.hide()
        self.check2.hide()
        self.delete_btn.hide()
        self.logout.clicked.connect(self.logoutfcn)
        self.message = QMessageBox()
        self.registration.setStyleSheet("color:white;background:black")
        db.connect()
        print("we here")

        self.fields()
        self.rowcheck = 1
        self.add.clicked.connect(self.insert)
        self.check.clicked.connect(self.searchRecord)
        self.registration.clicked.connect(self.reg)
        self.search.clicked.connect(self.sch)
        self.clear_btn.clicked.connect(self.clear)
        self.update.clicked.connect(self.updateRecord)
        self.showall.clicked.connect(self.all)
        self.delete_2.clicked.connect(self.delt)
        self.updt.clicked.connect(self.updatefcn)
        self.check2.clicked.connect(self.checkupdt)
        self.delete_btn.clicked.connect(self.deletefcn)

        self.display.setColumnWidth(0, 300)
        self.display.setColumnWidth(1, 200)
        self.display.setColumnWidth(2, 200)
        self.display.setColumnWidth(3, 100)
        self.display.setColumnWidth(4, 150)
        self.display.setColumnWidth(5, 300)

    def insert(self):
        reg = self.regno.text()
        fname = self.firstname.text()
        lname = self.lastname.text()
        gender = self.gender.text()
        dob = self.dob.text()
        course = self.course.text()
        self.check2.hide()
        self.delete_btn.hide()

        db.insertRecord(reg, fname, lname, gender, dob, course)
        data = [reg, fname, lname, gender, dob, course]
        self.fields()

        self.display.setItem(1, 0, QTableWidgetItem(reg))
        self.display.setItem(1, 1, QTableWidgetItem(fname))
        self.display.setItem(1, 2, QTableWidgetItem(lname))
        self.display.setItem(1, 3, QTableWidgetItem(gender))
        self.display.setItem(1, 4, QTableWidgetItem(dob))
        self.display.setItem(1, 5, QTableWidgetItem(course))

        self.message.information(self, "info", "Record Added")

    def sch(self):
        self.search.setStyleSheet("color:white;background:black")
        self.add.hide()
        self.check.show()
        self.updt.hide()
        self.regno.setText("")
        self.firstname.setText("")
        self.lastname.setText("")
        self.gender.setText("")
        self.dob.setText("")
        self.course.setText("")
        self.display.clear()
        self.search.setStyleSheet("color:white;background:black")
        self.showall.setStyleSheet("background: rgb(68, 45, 34);")
        self.update.setStyleSheet("background: rgb(68, 45, 34);")
        self.delete_2.setStyleSheet("background: rgb(68, 45, 34);")
        self.registration.setStyleSheet("background: rgb(68, 45, 34);")
        self.firstname.setText("")
        self.lastname.setText("")
        self.gender.setText("")
        self.dob.setText("")
        self.course.setText("")
        self.regno.setText("")
        self.fields()
        self.check2.hide()
        self.delete_btn.hide()

    def reg(self):
        self.add.show()
        self.check.hide()
        self.display.clear()
        self.updt.hide()
        self.registration.setStyleSheet("color:white;background:black")
        self.update.setStyleSheet("background: rgb(68, 45, 34);")
        self.delete_2.setStyleSheet("background: rgb(68, 45, 34);")
        self.showall.setStyleSheet("background: rgb(68, 45, 34);")
        self.search.setStyleSheet("background: rgb(68, 45, 34);")
        self.check2.hide()
        self.fields()
        self.firstname.setText("")
        self.lastname.setText("")
        self.gender.setText("")
        self.dob.setText("")
        self.course.setText("")
        self.regno.setText("")
        self.delete_btn.hide()

    def all(self):
        self.add.hide()
        self.check.hide()
        self.display.clear()
        self.updt.hide()
        self.registration.setStyleSheet("background: rgb(68, 45, 34);")
        self.showall.setStyleSheet("color:white;background:black")
        self.update.setStyleSheet("background: rgb(68, 45, 34);")
        self.delete_2.setStyleSheet("background: rgb(68, 45, 34);")
        self.search.setStyleSheet("background: rgb(68, 45, 34);")
        self.check2.hide()
        self.fields()
        self.firstname.setText("")
        self.lastname.setText("")
        self.gender.setText("")
        self.dob.setText("")
        self.course.setText("")
        self.regno.setText("")
        self.delete_btn.hide()

        try:
            con = sqlite3.connect("data/student_records.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM student_data WHERE 1 ORDER BY REGNO Asc")
            row = cur.fetchall()

            checking = len(row)
            # print(checking)

            self.display.setRowCount(checking + 1)
            self.display.setColumnCount(6)

            for r in row:
                self.display.setItem(self.rowcheck, 0, QTableWidgetItem(r[0]))
                self.display.setItem(self.rowcheck, 1, QTableWidgetItem(r[1]))
                self.display.setItem(self.rowcheck, 2, QTableWidgetItem(r[2]))
                self.display.setItem(self.rowcheck, 3, QTableWidgetItem(r[3]))
                self.display.setItem(self.rowcheck, 4, QTableWidgetItem(r[4]))
                self.display.setItem(self.rowcheck, 5, QTableWidgetItem(r[5]))
                self.rowcheck += 1

            self.rowcheck = 1
            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

    def searchRecord(self):
        reg = self.regno.text()
        try:
            con = sqlite3.connect("data/student_records.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM student_data WHERE REGNO = '" + reg + "'")
            row = cur.fetchall()

            for r in row:
                self.firstname.setText(r[1])
                self.lastname.setText(r[2])
                self.gender.setText(r[3])
                self.dob.setText(r[4])
                self.course.setText(r[5])
                for final in r:
                    self.display.setItem(1, 0, QTableWidgetItem(r[0]))
                    self.display.setItem(1, 1, QTableWidgetItem(r[1]))
                    self.display.setItem(1, 2, QTableWidgetItem(r[2]))
                    self.display.setItem(1, 3, QTableWidgetItem(r[3]))
                    self.display.setItem(1, 4, QTableWidgetItem(r[4]))
                    self.display.setItem(1, 5, QTableWidgetItem(r[5]))
                self.message.information(self, "info", "succesfully searched")

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

    def updateRecord(self):
        self.update.setStyleSheet("color:white;background:black")
        self.updt.show()
        self.add.hide()
        self.check.hide()
        self.update.setStyleSheet("color:white;background:black")
        self.registration.setStyleSheet("background: rgb(68, 45, 34);")
        self.delete_2.setStyleSheet("background-color: rgb(68, 45, 34);")
        self.search.setStyleSheet("background-color: rgb(68, 45, 34);")
        self.showall.setStyleSheet("background: rgb(68, 45, 34);")
        self.check2.show()
        self.display.clear()
        self.fields()
        self.delete_btn.hide()

    def clear(self):
        self.firstname.setText("")
        self.lastname.setText("")
        self.gender.setText("")
        self.dob.setText("")
        self.course.setText("")
        self.regno.setText("")
        self.display.clear()

    def delt(self):
        self.delete_2.setStyleSheet("color:white;background:black")
        self.update.setStyleSheet("background: rgb(68, 45, 34);")
        self.registration.setStyleSheet("background: rgb(68, 45, 34);")
        self.showall.setStyleSheet("background: rgb(68, 45, 34);")
        self.search.setStyleSheet("background: rgb(68, 45, 34);")
        self.delete_btn.show()
        self.updt.hide()
        self.add.hide()
        self.check2.hide()
        self.check.show()
        self.display.clear()
        self.fields()

    def fields(self):

        try:
            con = sqlite3.connect("data/student_records.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM student_data")
            row = cur.fetchall()

            checking = len(row)
            # print(checking)

            self.display.setRowCount(checking + 1)
            self.display.setColumnCount(6)

            self.display.setItem(0, 0, QTableWidgetItem("Reg No"))
            self.display.setItem(0, 1, QTableWidgetItem("First Name"))
            self.display.setItem(0, 2, QTableWidgetItem("Last Name"))
            self.display.setItem(0, 3, QTableWidgetItem("Gender"))
            self.display.setItem(0, 4, QTableWidgetItem("DOB"))
            self.display.setItem(0, 5, QTableWidgetItem("Course"))

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

    def checkupdt(self):
        reg = self.regno.text()
        try:
            con = sqlite3.connect("data/student_records.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM student_data WHERE REGNO = '" + reg + "'")
            row = cur.fetchall()

            for r in row:
                self.firstname.setText(r[1])
                self.lastname.setText(r[2])
                self.gender.setText(r[3])
                self.dob.setText(r[4])
                self.course.setText(r[5])

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

    def updatefcn(self):
        reg = self.regno.text()
        sfname = self.firstname.text()
        slname = self.lastname.text()
        sgender = self.gender.text()
        sdob = self.dob.text()
        scourse = self.course.text()
        self.display.clear()
        self.fields()

        try:
            con = sqlite3.connect("data/student_records.db")
            cur = con.cursor()
            cur.execute(
                "UPDATE student_data SET  FIRSTNAME ='" + sfname + "',LASTNAME ='" + slname + "',GENDER ='" + sgender + "',DOB ='" + sdob + "',COURSE ='" + scourse + "' WHERE REGNO ='" + reg + "'")

            self.message.information(self, "info", "Successfully Updated")

            con.commit()


        except Exception as e:
            self.message.information(self, "Error", e)

        try:
            con = sqlite3.connect("data/student_records.db")
            cur = con.cursor()

            cur.execute(
                "SELECT REGNO,FIRSTNAME,LASTNAME,GENDER,DOB,COURSE FROM student_data WHERE REGNO = '" + reg + "'")
            row = cur.fetchall()

            for r in row:
                self.display.setItem(1, 0, QTableWidgetItem(r[0]))
                self.display.setItem(1, 1, QTableWidgetItem(r[1]))
                self.display.setItem(1, 2, QTableWidgetItem(r[2]))
                self.display.setItem(1, 3, QTableWidgetItem(r[3]))
                self.display.setItem(1, 4, QTableWidgetItem(r[4]))
                self.display.setItem(1, 5, QTableWidgetItem(r[5]))
            self.message.information(self, "info", "succesfully loaded")

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

    def deletefcn(self):
        reg = self.regno.text()
        try:
            con = sqlite3.connect("data/student_records.db")
            cur = con.cursor()
            cur.execute("DELETE FROM student_data WHERE REGNO = '" + reg + "'")
            self.message.information(self, "info", "Record Deleted")
            print("deleted")

        except Exception as e:
            self.message.information(self, "Error", e)

        con.commit()

        self.clear()

    def logoutfcn(self):
        pass








app = QApplication(sys.argv)
l = LOGIN()
l.show()

app.exec_()
app.exit()

