# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/load_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadDialog(object):
    def setupUi(self, LoadDialog):
        LoadDialog.setObjectName("LoadDialog")
        LoadDialog.resize(714, 121)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadDialog.sizePolicy().hasHeightForWidth())
        LoadDialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(LoadDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(LoadDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.select_original_video_button = QtWidgets.QPushButton(LoadDialog)
        self.select_original_video_button.setObjectName("select_original_video_button")
        self.gridLayout.addWidget(self.select_original_video_button, 1, 2, 1, 1)
        self.original_image_line_edit = QtWidgets.QLineEdit(LoadDialog)
        self.original_image_line_edit.setText("")
        self.original_image_line_edit.setObjectName("original_image_line_edit")
        self.gridLayout.addWidget(self.original_image_line_edit, 0, 1, 1, 1)
        self.select_original_image_button = QtWidgets.QPushButton(LoadDialog)
        self.select_original_image_button.setObjectName("select_original_image_button")
        self.gridLayout.addWidget(self.select_original_image_button, 0, 2, 1, 1)
        self.label_original_image = QtWidgets.QLabel(LoadDialog)
        self.label_original_image.setObjectName("label_original_image")
        self.gridLayout.addWidget(self.label_original_image, 0, 0, 1, 1)
        self.original_video_line_edit = QtWidgets.QLineEdit(LoadDialog)
        self.original_video_line_edit.setObjectName("original_video_line_edit")
        self.gridLayout.addWidget(self.original_video_line_edit, 1, 1, 1, 1)
        self.label_original_video = QtWidgets.QLabel(LoadDialog)
        self.label_original_video.setObjectName("label_original_video")
        self.gridLayout.addWidget(self.label_original_video, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(LoadDialog)
        self.buttonBox.accepted.connect(LoadDialog.accept)
        self.buttonBox.rejected.connect(LoadDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadDialog)

    def retranslateUi(self, LoadDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadDialog.setWindowTitle(_translate("LoadDialog", "Dialog"))
        self.select_original_video_button.setText(_translate("LoadDialog", "select"))
        self.select_original_image_button.setText(_translate("LoadDialog", "select"))
        self.label_original_image.setText(_translate("LoadDialog", "Original Image:"))
        self.label_original_video.setText(_translate("LoadDialog", "Original Video:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadDialog = QtWidgets.QDialog()
    ui = Ui_LoadDialog()
    ui.setupUi(LoadDialog)
    LoadDialog.show()
    sys.exit(app.exec_())
