from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import sys
import sqlite3

# Problems:
# No delete function to delete tasks
# When adding a new task, I don't even have to click save changes, fix it to where I have to click the save changes button after adding new task.
class MainUI(QWidget):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('main.ui', self)
        # When the date selection has been changed, connect to the function.
        # similar with button "self.button_name.clicked.connect(func). (Signal -> Slot)
        self.calendarWidget.selectionChanged.connect(self.calenderDateChanged)
        self.savebutton.clicked.connect(self.save_Changes)
        self.addButton.clicked.connect(self.addNewTask)


    def calenderDateChanged(self):
        print("The calender date was changed")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print(f"Date selected: {dateSelected}")
        self.updateTaskList(dateSelected)


    # Retrieving data from DB and updating to list widget
    def updateTaskList(self, date):
        self.taskListWidget.clear()

        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        row = (date,)
        cursor.execute("SELECT task, completed FROM data WHERE date = ?", row)
        tasks = cursor.fetchall()
        for task in tasks:
            item = QListWidgetItem(str(task[0]))  # Convert task to a list item
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable) # "|": Union Symbol
            item.setCheckState(QtCore.Qt.Unchecked)
            if task[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif task[1] == "NO":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.taskListWidget.addItem(item)


    def save_Changes(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate()

        # Updates each item in list widget (Completion only)
        for i in range(self.taskListWidget.count()):
            item = self.taskListWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE data SET completed = 'YES' WHERE task = ? AND date = ?"
            else:
                query = "UPDATE data SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task, date,)
            cursor.execute(query, row)
            db.commit()

        message_box = QMessageBox()
        message_box.setText("Changes saved.")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()


    def addNewTask(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        new_task = str(self.taskLineEdit.text())
        if not new_task:
            message_box = QMessageBox()
            message_box.setText("Task field can't be empty. Try again")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec_()
            return

        date = self.calendarWidget.selectedDate().toPyDate()

        query = "INSERT INTO data(task, completed, date) VALUES (?,?,?)"
        row = (new_task, "NO", date,)

        cursor.execute(query, row)
        db.commit()

        self.updateTaskList(date)
        self.taskLineEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainUI()
    win.show()
    sys.exit(app.exec_())

# for task in tasks:
#     # add task to the list widget
#     item = QListWidgetItem(task) # Convert task to a list item
#     item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable) # "|": Union Symbol
#     item.setCheckState(QtCore.Qt.Unchecked)
#     self.tasklistWidget.addItem(item)
