# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QWidget, QMessageBox


class EditWindow(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('Edit')
        self.setWindowIcon(QIcon('icon.png'))
        self.setObjectName("Dialog")
        self.resize(555, 213)
        self.parent = parent
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon('icon.png'))
        self.msg.setWindowTitle("!")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText(self.parent.tableWidget.item(self.parent.tableWidget.selectionModel().selectedRows()[0].row(), 0).text())
        self.gridLayout_3.addWidget(self.textEdit, 1, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setText(self.parent.tableWidget.item(self.parent.tableWidget.selectionModel().selectedRows()[0].row(), 1).text())
        self.gridLayout_3.addWidget(self.textEdit_2, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(11, 11, 11, -1)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.okButton = QtWidgets.QPushButton(self.frame)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 0, 0, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.okButton.clicked.connect(self.on_okButton_click)
        self.cancelButton.clicked.connect(self.on_cancelButton_click)

    def on_okButton_click(self):
        answer = self.parent.service.put(
            self.textEdit.toPlainText(),
            self.textEdit_2.toPlainText(),
            self.parent.tableWidget.item(self.parent.tableWidget.selectionModel().selectedRows()[0].row(), 0).text(),
            self.parent.tableWidget.item(self.parent.tableWidget.selectionModel().selectedRows()[0].row(), 1).text())
        if answer == 0:
            self.parent.update_table()
            self.hide()
            self.msg.setText("The line was edited successfully!")
            self.msg.exec_()
        else:
            self.msg.setText("This record already exists!")
            self.msg.exec_()

    def on_cancelButton_click(self):
        self.hide()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "Edit the author:"))
        self.label_2.setText(_translate("Dialog", "Edit the quote:"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = EditWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
