import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from data_provider import CRUDService
from add_window import AddWindow
from edit_window import EditWindow


class QuotesWindowPresenter(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('QuotesWindow.ui', self)
        self.setWindowTitle('Quotes')
        self.setWindowIcon(QIcon('icon.png'))
        self.addButton.clicked.connect(self.on_addButton_click)
        self.editButton.clicked.connect(self.on_editButton_click)
        self.deleteButton.clicked.connect(self.on_deleteButton_click)
        self.updateButton.clicked.connect(self.on_updateButton_click)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Author', 'Quote'])
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon('icon.png'))
        self.msg.setWindowTitle("!")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.update_table()

    def on_addButton_click(self):
        self.add = AddWindow(self)
        self.add .show()

    def on_editButton_click(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            self.msg.setText("You didn't select a single line!")
            self.msg.exec_()
        elif len(selected_rows) > 1:
            self.msg.setText("You should only select one line!")
            self.msg.exec_()
        else:
            self.edit = EditWindow(self)
            self.edit.show()

    def on_deleteButton_click(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            self.msg.setText("You didn't select a single line!")
            self.msg.exec_()
        else:
            for row in selected_rows:
                row_number = row.row()
                self.service.delete(self.tableWidget.item(row_number, 0).text(),
                                    self.tableWidget.item(row_number, 1).text())
            self.update_table()
            self.msg.setText("{0} row(s) deleted!".format(len(selected_rows)))
            self.msg.exec_()

    def on_updateButton_click(self):
        self.update_table()
        self.msg.setText("Data updated!")
        self.msg.exec_()

    def update_table(self):
        self.service = CRUDService()
        data = self.service.get_all()
        self.tableWidget.setRowCount(len(data))
        row = 0
        for tup in data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                self.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QuotesWindowPresenter()
    widget.show()
    sys.exit(app.exec_())

