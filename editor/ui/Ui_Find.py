# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Tue Nov 28 10:06:19 2006
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_frmFind(object):
    def setupUi(self, frmFind):
        frmFind.setObjectName("frmFind")
        frmFind.setEnabled(True)
        frmFind.resize(QtCore.QSize(QtCore.QRect(0,0,767,81).size()).expandedTo(frmFind.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmFind.sizePolicy().hasHeightForWidth())
        frmFind.setSizePolicy(sizePolicy)
        frmFind.setMinimumSize(QtCore.QSize(600,20))
        frmFind.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        frmFind.setAutoFillBackground(True)

        self.gridlayout = QtGui.QGridLayout(frmFind)
        self.gridlayout.setMargin(1)
        self.gridlayout.setSpacing(1)
        self.gridlayout.setObjectName("gridlayout")

        self.lblReplace = QtGui.QLabel(frmFind)
        self.lblReplace.setSizeIncrement(QtCore.QSize(0,0))
        self.lblReplace.setObjectName("lblReplace")
        self.gridlayout.addWidget(self.lblReplace,1,0,1,1)

        self.replaceAll = QtGui.QPushButton(frmFind)
        self.replaceAll.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replaceAll.sizePolicy().hasHeightForWidth())
        self.replaceAll.setSizePolicy(sizePolicy)

        font = QtGui.QFont(self.replaceAll.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.replaceAll.setFont(font)
        self.replaceAll.setAutoDefault(True)
        self.replaceAll.setDefault(True)
        self.replaceAll.setFlat(False)
        self.replaceAll.setObjectName("replaceAll")
        self.gridlayout.addWidget(self.replaceAll,1,3,1,1)

        self.replace = QtGui.QPushButton(frmFind)
        self.replace.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replace.sizePolicy().hasHeightForWidth())
        self.replace.setSizePolicy(sizePolicy)

        font = QtGui.QFont(self.replace.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.replace.setFont(font)
        self.replace.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.replace.setAutoDefault(True)
        self.replace.setDefault(True)
        self.replace.setFlat(False)
        self.replace.setObjectName("replace")
        self.gridlayout.addWidget(self.replace,1,2,1,1)

        self.lineEdit_2 = QtGui.QLineEdit(frmFind)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0,26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridlayout.addWidget(self.lineEdit_2,1,1,1,1)

        self.groupBox = QtGui.QGroupBox(frmFind)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)

        font = QtGui.QFont(self.groupBox.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.hboxlayout = QtGui.QHBoxLayout(self.groupBox)
        self.hboxlayout.setMargin(1)
        self.hboxlayout.setSpacing(1)
        self.hboxlayout.setObjectName("hboxlayout")

        self.insource = QtGui.QCheckBox(self.groupBox)
        self.insource.setMinimumSize(QtCore.QSize(85,0))

        font = QtGui.QFont(self.insource.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.insource.setFont(font)
        self.insource.setCheckable(True)
        self.insource.setChecked(True)
        self.insource.setTristate(False)
        self.insource.setObjectName("insource")
        self.hboxlayout.addWidget(self.insource)

        self.intarget = QtGui.QCheckBox(self.groupBox)
        self.intarget.setMinimumSize(QtCore.QSize(85,0))

        font = QtGui.QFont(self.intarget.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.intarget.setFont(font)
        self.intarget.setObjectName("intarget")
        self.hboxlayout.addWidget(self.intarget)

        self.incomment = QtGui.QCheckBox(self.groupBox)
        self.incomment.setMinimumSize(QtCore.QSize(85,0))

        font = QtGui.QFont(self.incomment.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.incomment.setFont(font)
        self.incomment.setChecked(False)
        self.incomment.setObjectName("incomment")
        self.hboxlayout.addWidget(self.incomment)

        self.matchcase = QtGui.QCheckBox(self.groupBox)
        self.matchcase.setMinimumSize(QtCore.QSize(85,0))

        font = QtGui.QFont(self.matchcase.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.matchcase.setFont(font)
        self.matchcase.setObjectName("matchcase")
        self.hboxlayout.addWidget(self.matchcase)
        self.gridlayout.addWidget(self.groupBox,0,4,1,1)

        self.findNext = QtGui.QPushButton(frmFind)
        self.findNext.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findNext.sizePolicy().hasHeightForWidth())
        self.findNext.setSizePolicy(sizePolicy)

        font = QtGui.QFont(self.findNext.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.findNext.setFont(font)
        self.findNext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.findNext.setAutoDefault(True)
        self.findNext.setDefault(True)
        self.findNext.setFlat(False)
        self.findNext.setObjectName("findNext")
        self.gridlayout.addWidget(self.findNext,0,2,1,1)

        self.lineEdit = QtGui.QLineEdit(frmFind)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setMinimumSize(QtCore.QSize(0,26))
        self.lineEdit.setObjectName("lineEdit")
        self.gridlayout.addWidget(self.lineEdit,0,1,1,1)

        self.lblFind = QtGui.QLabel(frmFind)
        self.lblFind.setSizeIncrement(QtCore.QSize(0,0))
        self.lblFind.setObjectName("lblFind")
        self.gridlayout.addWidget(self.lblFind,0,0,1,1)

        self.findPrevious = QtGui.QPushButton(frmFind)
        self.findPrevious.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(17)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findPrevious.sizePolicy().hasHeightForWidth())
        self.findPrevious.setSizePolicy(sizePolicy)
        self.findPrevious.setMaximumSize(QtCore.QSize(16777215,16777215))

        font = QtGui.QFont(self.findPrevious.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.findPrevious.setFont(font)
        self.findPrevious.setAutoDefault(True)
        self.findPrevious.setDefault(True)
        self.findPrevious.setFlat(False)
        self.findPrevious.setObjectName("findPrevious")
        self.gridlayout.addWidget(self.findPrevious,0,3,1,1)

        self.retranslateUi(frmFind)
        QtCore.QMetaObject.connectSlotsByName(frmFind)
        frmFind.setTabOrder(self.lineEdit,self.findNext)
        frmFind.setTabOrder(self.findNext,self.findPrevious)
        frmFind.setTabOrder(self.findPrevious,self.lineEdit_2)
        frmFind.setTabOrder(self.lineEdit_2,self.replace)
        frmFind.setTabOrder(self.replace,self.replaceAll)

    def tr(self, string):
        return QtGui.QApplication.translate("frmFind", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, frmFind):
        frmFind.setWindowTitle(self.tr("Find & Replace"))
        self.lblReplace.setText(self.tr("Replace with:"))
        self.replaceAll.setText(self.tr("Replace &All"))
        self.replace.setText(self.tr("&Replace"))
        self.insource.setText(self.tr("&Source"))
        self.intarget.setText(self.tr("&Target"))
        self.incomment.setText(self.tr("&Comment"))
        self.matchcase.setText(self.tr("Matc&h case"))
        self.findNext.setText(self.tr("&Next"))
        self.lblFind.setText(self.tr("Search for:"))
        self.findPrevious.setText(self.tr("  &Previous  "))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmFind = QtGui.QWidget()
    ui = Ui_frmFind()
    ui.setupUi(frmFind)
    frmFind.show()
    sys.exit(app.exec_())
