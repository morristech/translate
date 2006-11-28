# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Tue Nov 28 17:32:44 2006
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,800,492).size()).expandedTo(MainWindow.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400,300))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowIcon(QtGui.QIcon("./images/icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,800,30))
        self.menubar.setObjectName("menubar")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuOpen_Recent = QtGui.QMenu(self.menuFile)
        self.menuOpen_Recent.setIcon(QtGui.QIcon("./images/open.png"))
        self.menuOpen_Recent.setObjectName("menuOpen_Recent")

        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuGo = QtGui.QMenu(self.menubar)
        self.menuGo.setObjectName("menuGo")

        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")

        self.menuToolBars = QtGui.QMenu(self.menuView)
        self.menuToolBars.setObjectName("menuToolBars")

        self.menuWindows = QtGui.QMenu(self.menuView)
        self.menuWindows.setObjectName("menuWindows")

        self.menuMessages = QtGui.QMenu(self.menuView)
        self.menuMessages.setObjectName("menuMessages")

        self.menuToolbars = QtGui.QMenu(self.menuView)
        self.menuToolbars.setObjectName("menuToolbars")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setGeometry(QtCore.QRect(0,469,800,23))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolStandard = QtGui.QToolBar(MainWindow)
        self.toolStandard.setEnabled(True)
        self.toolStandard.setOrientation(QtCore.Qt.Horizontal)
        self.toolStandard.setObjectName("toolStandard")
        MainWindow.addToolBar(self.toolStandard)

        self.toolNavigation = QtGui.QToolBar(MainWindow)
        self.toolNavigation.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolNavigation.setAcceptDrops(False)
        self.toolNavigation.setOrientation(QtCore.Qt.Horizontal)
        self.toolNavigation.setObjectName("toolNavigation")
        MainWindow.addToolBar(self.toolNavigation)

        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setIcon(QtGui.QIcon("./images/new.png"))
        self.actionNew.setObjectName("actionNew")

        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setIcon(QtGui.QIcon("./images/open.png"))
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        self.actionSave.setIcon(QtGui.QIcon("./images/save.png"))
        self.actionSave.setObjectName("actionSave")

        self.actionSaveas = QtGui.QAction(MainWindow)
        self.actionSaveas.setEnabled(False)
        self.actionSaveas.setIcon(QtGui.QIcon("./images/saveAs.png"))
        self.actionSaveas.setObjectName("actionSaveas")

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setIcon(QtGui.QIcon("./images/stop.png"))
        self.actionExit.setObjectName("actionExit")

        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        self.actionUndo.setIcon(QtGui.QIcon("./images/undo.png"))
        self.actionUndo.setObjectName("actionUndo")

        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setEnabled(False)
        self.actionRedo.setIcon(QtGui.QIcon("./images/redo.png"))
        self.actionRedo.setObjectName("actionRedo")

        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setEnabled(False)
        self.actionCut.setIcon(QtGui.QIcon("./images/cut.png"))
        self.actionCut.setObjectName("actionCut")

        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setCheckable(False)
        self.actionCopy.setEnabled(False)
        self.actionCopy.setIcon(QtGui.QIcon("./images/copy.png"))
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setEnabled(False)
        self.actionPaste.setIcon(QtGui.QIcon("./images/paste.png"))
        self.actionPaste.setObjectName("actionPaste")

        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setEnabled(False)
        self.actionFind.setIcon(QtGui.QIcon("./images/find.png"))
        self.actionFind.setObjectName("actionFind")

        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionShowMenuBar = QtGui.QAction(MainWindow)
        self.actionShowMenuBar.setObjectName("actionShowMenuBar")

        self.actionShowTUview = QtGui.QAction(MainWindow)
        self.actionShowTUview.setObjectName("actionShowTUview")

        self.actionAboutQT = QtGui.QAction(MainWindow)
        self.actionAboutQT.setObjectName("actionAboutQT")

        self.actionShow_MenuBar = QtGui.QAction(MainWindow)
        self.actionShow_MenuBar.setObjectName("actionShow_MenuBar")

        self.actionShow_TUview = QtGui.QAction(MainWindow)
        self.actionShow_TUview.setObjectName("actionShow_TUview")

        self.actionFirst = QtGui.QAction(MainWindow)
        self.actionFirst.setEnabled(False)
        self.actionFirst.setIcon(QtGui.QIcon("./images/first.png"))
        self.actionFirst.setObjectName("actionFirst")

        self.actionPrevious = QtGui.QAction(MainWindow)
        self.actionPrevious.setEnabled(False)
        self.actionPrevious.setIcon(QtGui.QIcon("./images/previous.png"))
        self.actionPrevious.setObjectName("actionPrevious")

        self.actionNext = QtGui.QAction(MainWindow)
        self.actionNext.setEnabled(False)
        self.actionNext.setIcon(QtGui.QIcon("./images/next.png"))
        self.actionNext.setObjectName("actionNext")

        self.actionLast = QtGui.QAction(MainWindow)
        self.actionLast.setEnabled(False)
        self.actionLast.setIcon(QtGui.QIcon("./images/last.png"))
        self.actionLast.setObjectName("actionLast")

        self.actionShowDetail = QtGui.QAction(MainWindow)
        self.actionShowDetail.setObjectName("actionShowDetail")

        self.actionShowComment = QtGui.QAction(MainWindow)
        self.actionShowComment.setObjectName("actionShowComment")

        self.actionShowOverview = QtGui.QAction(MainWindow)
        self.actionShowOverview.setObjectName("actionShowOverview")

        self.actionCopySource2Target = QtGui.QAction(MainWindow)
        self.actionCopySource2Target.setEnabled(True)
        self.actionCopySource2Target.setObjectName("actionCopySource2Target")

        self.actionToggleFuzzy = QtGui.QAction(MainWindow)
        self.actionToggleFuzzy.setEnabled(False)
        self.actionToggleFuzzy.setObjectName("actionToggleFuzzy")

        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")

        self.actionFind_Previous = QtGui.QAction(MainWindow)
        self.actionFind_Previous.setEnabled(False)
        self.actionFind_Previous.setObjectName("actionFind_Previous")

        self.actionFind_Next = QtGui.QAction(MainWindow)
        self.actionFind_Next.setEnabled(False)
        self.actionFind_Next.setObjectName("actionFind_Next")

        self.actionReplace = QtGui.QAction(MainWindow)
        self.actionReplace.setEnabled(False)
        self.actionReplace.setObjectName("actionReplace")

        self.actionFindNext = QtGui.QAction(MainWindow)
        self.actionFindNext.setEnabled(False)
        self.actionFindNext.setObjectName("actionFindNext")

        self.actionOpenInNewWindow = QtGui.QAction(MainWindow)
        self.actionOpenInNewWindow.setIcon(QtGui.QIcon("./images/window_new.png"))
        self.actionOpenInNewWindow.setObjectName("actionOpenInNewWindow")

        self.actionFilterFuzzy = QtGui.QAction(MainWindow)
        self.actionFilterFuzzy.setCheckable(True)
        self.actionFilterFuzzy.setChecked(True)
        self.actionFilterFuzzy.setEnabled(False)
        self.actionFilterFuzzy.setObjectName("actionFilterFuzzy")

        self.actionFilterTranslated = QtGui.QAction(MainWindow)
        self.actionFilterTranslated.setCheckable(True)
        self.actionFilterTranslated.setChecked(True)
        self.actionFilterTranslated.setEnabled(False)
        self.actionFilterTranslated.setObjectName("actionFilterTranslated")

        self.actionFindPrevious = QtGui.QAction(MainWindow)
        self.actionFindPrevious.setEnabled(False)
        self.actionFindPrevious.setObjectName("actionFindPrevious")

        self.actionSelectAll = QtGui.QAction(MainWindow)
        self.actionSelectAll.setEnabled(False)
        self.actionSelectAll.setObjectName("actionSelectAll")

        self.actionEdit_Header = QtGui.QAction(MainWindow)
        self.actionEdit_Header.setEnabled(False)
        self.actionEdit_Header.setObjectName("actionEdit_Header")

        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")

        self.actionFilterUntranslated = QtGui.QAction(MainWindow)
        self.actionFilterUntranslated.setCheckable(True)
        self.actionFilterUntranslated.setChecked(True)
        self.actionFilterUntranslated.setEnabled(False)
        self.actionFilterUntranslated.setObjectName("actionFilterUntranslated")

        self.actionAsf = QtGui.QAction(MainWindow)
        self.actionAsf.setObjectName("actionAsf")

        self.actionStandard_Tools = QtGui.QAction(MainWindow)
        self.actionStandard_Tools.setCheckable(True)
        self.actionStandard_Tools.setChecked(False)
        self.actionStandard_Tools.setObjectName("actionStandard_Tools")

        self.actionNavigation_Tools = QtGui.QAction(MainWindow)
        self.actionNavigation_Tools.setCheckable(True)
        self.actionNavigation_Tools.setObjectName("actionNavigation_Tools")

        self.actionHide_View = QtGui.QAction(MainWindow)
        self.actionHide_View.setCheckable(True)
        self.actionHide_View.setChecked(True)
        self.actionHide_View.setObjectName("actionHide_View")

        self.actionHide_Detail = QtGui.QAction(MainWindow)
        self.actionHide_Detail.setCheckable(True)
        self.actionHide_Detail.setChecked(True)
        self.actionHide_Detail.setObjectName("actionHide_Detail")

        self.actionHide_Comment = QtGui.QAction(MainWindow)
        self.actionHide_Comment.setCheckable(True)
        self.actionHide_Comment.setChecked(True)
        self.actionHide_Comment.setObjectName("actionHide_Comment")

        self.actionStandard_Tools1 = QtGui.QAction(MainWindow)
        self.actionStandard_Tools1.setCheckable(True)
        self.actionStandard_Tools1.setChecked(False)
        self.actionStandard_Tools1.setObjectName("actionStandard_Tools1")

        self.actionNavigation_Tools1 = QtGui.QAction(MainWindow)
        self.actionNavigation_Tools1.setCheckable(True)
        self.actionNavigation_Tools1.setChecked(False)
        self.actionNavigation_Tools1.setObjectName("actionNavigation_Tools1")

        self.actionHello = QtGui.QAction(MainWindow)
        self.actionHello.setCheckable(True)
        self.actionHello.setObjectName("actionHello")

        self.actionComment = QtGui.QAction(MainWindow)
        self.actionComment.setCheckable(True)
        self.actionComment.setObjectName("actionComment")

        self.actionHello_2 = QtGui.QAction(MainWindow)
        self.actionHello_2.setCheckable(True)
        self.actionHello_2.setObjectName("actionHello_2")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQT)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionOpenInNewWindow)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuOpen_Recent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveas)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFindPrevious)
        self.menuEdit.addAction(self.actionFindNext)
        self.menuEdit.addAction(self.actionReplace)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopySource2Target)
        self.menuEdit.addAction(self.actionToggleFuzzy)
        self.menuEdit.addAction(self.actionEdit_Header)
        self.menuGo.addAction(self.actionFirst)
        self.menuGo.addAction(self.actionPrevious)
        self.menuGo.addAction(self.actionNext)
        self.menuGo.addAction(self.actionLast)
        self.menuToolBars.addAction(self.actionStandard_Tools)
        self.menuToolBars.addAction(self.actionNavigation_Tools)
        self.menuMessages.addAction(self.actionFilterFuzzy)
        self.menuMessages.addAction(self.actionFilterTranslated)
        self.menuMessages.addAction(self.actionFilterUntranslated)
        self.menuToolbars.addAction(self.actionStandard_Tools)
        self.menuToolbars.addAction(self.actionNavigation_Tools)
        self.menuView.addAction(self.menuMessages.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuToolbars.menuAction())
        self.menuView.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuGo.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolStandard.addAction(self.actionOpen)
        self.toolStandard.addAction(self.actionSave)
        self.toolStandard.addSeparator()
        self.toolStandard.addAction(self.actionCut)
        self.toolStandard.addAction(self.actionCopy)
        self.toolStandard.addAction(self.actionPaste)
        self.toolStandard.addSeparator()
        self.toolStandard.addAction(self.actionUndo)
        self.toolStandard.addAction(self.actionRedo)
        self.toolNavigation.addAction(self.actionFirst)
        self.toolNavigation.addAction(self.actionPrevious)
        self.toolNavigation.addAction(self.actionNext)
        self.toolNavigation.addAction(self.actionLast)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def tr(self, string):
        return QtGui.QApplication.translate("MainWindow", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(self.tr("Form"))
        self.menuHelp.setTitle(self.tr("&Help"))
        self.menuSettings.setTitle(self.tr("&Settings"))
        self.menuFile.setTitle(self.tr("&File"))
        self.menuOpen_Recent.setTitle(self.tr("Open &Recent"))
        self.menuEdit.setTitle(self.tr("&Edit"))
        self.menuGo.setTitle(self.tr("&Go"))
        self.menuView.setTitle(self.tr("&View"))
        self.menuToolBars.setTitle(self.tr("ToolBars"))
        self.menuWindows.setTitle(self.tr("Tools"))
        self.menuMessages.setTitle(self.tr("Messages"))
        self.menuToolbars.setTitle(self.tr("Toolbars"))
        self.toolStandard.setWindowTitle(self.tr("Standard Toolbar"))
        self.toolNavigation.setWindowTitle(self.tr("Navigation Toolbar"))
        self.actionNew.setText(self.tr("&New"))
        self.actionNew.setShortcut(self.tr("Ctrl+N"))
        self.actionOpen.setText(self.tr("&Open"))
        self.actionOpen.setShortcut(self.tr("Ctrl+O"))
        self.actionSave.setText(self.tr("&Save"))
        self.actionSave.setShortcut(self.tr("Ctrl+S"))
        self.actionSaveas.setText(self.tr("Save &As"))
        self.actionExit.setText(self.tr("&Quit"))
        self.actionExit.setShortcut(self.tr("Ctrl+Q"))
        self.actionUndo.setText(self.tr("Undo"))
        self.actionUndo.setShortcut(self.tr("Ctrl+Z"))
        self.actionRedo.setText(self.tr("Redo"))
        self.actionRedo.setShortcut(self.tr("Ctrl+Shift+Z"))
        self.actionCut.setText(self.tr("Cut"))
        self.actionCut.setShortcut(self.tr("Ctrl+X"))
        self.actionCopy.setText(self.tr("Copy"))
        self.actionCopy.setShortcut(self.tr("Ctrl+C"))
        self.actionPaste.setText(self.tr("Paste"))
        self.actionPaste.setIconText(self.tr("Paste"))
        self.actionPaste.setToolTip(self.tr("Paste"))
        self.actionPaste.setShortcut(self.tr("Ctrl+V"))
        self.actionFind.setText(self.tr("Find"))
        self.actionFind.setShortcut(self.tr("Ctrl+F"))
        self.actionAbout.setText(self.tr("About"))
        self.actionShowMenuBar.setText(self.tr("Show MenuBar"))
        self.actionShowMenuBar.setShortcut(self.tr("Ctrl+M"))
        self.actionShowTUview.setText(self.tr("Show TUview"))
        self.actionShowTUview.setShortcut(self.tr("Ctrl+T"))
        self.actionAboutQT.setText(self.tr("About QT"))
        self.actionShow_MenuBar.setText(self.tr("Show MenuBar"))
        self.actionShow_TUview.setText(self.tr("Show TUview"))
        self.actionFirst.setText(self.tr("&First"))
        self.actionFirst.setShortcut(self.tr("Ctrl+PgUp"))
        self.actionPrevious.setText(self.tr("&Previous"))
        self.actionPrevious.setShortcut(self.tr("PgUp"))
        self.actionNext.setText(self.tr("&Next"))
        self.actionNext.setShortcut(self.tr("PgDown"))
        self.actionLast.setText(self.tr("&Last"))
        self.actionLast.setShortcut(self.tr("Ctrl+PgDown"))
        self.actionShowDetail.setText(self.tr("Show Detail"))
        self.actionShowComment.setText(self.tr("Show Comment"))
        self.actionShowOverview.setText(self.tr("Show Overview"))
        self.actionCopySource2Target.setText(self.tr("Copy Source to Target"))
        self.actionCopySource2Target.setShortcut(self.tr("F2"))
        self.actionToggleFuzzy.setText(self.tr("Toggle fuzzy"))
        self.actionToggleFuzzy.setShortcut(self.tr("Ctrl+U"))
        self.actionFile.setText(self.tr("file"))
        self.actionFind_Previous.setText(self.tr("Find Previous"))
        self.actionFind_Next.setText(self.tr("Find Next"))
        self.actionReplace.setText(self.tr("&Replace"))
        self.actionReplace.setShortcut(self.tr("Ctrl+R"))
        self.actionFindNext.setText(self.tr("Find Next"))
        self.actionFindNext.setIconText(self.tr("Find Next"))
        self.actionFindNext.setToolTip(self.tr("Find Next"))
        self.actionFindNext.setShortcut(self.tr("F3"))
        self.actionOpenInNewWindow.setText(self.tr("Open in New Window"))
        self.actionFilterFuzzy.setText(self.tr("Fuzzy"))
        self.actionFilterTranslated.setText(self.tr("Translated"))
        self.actionFindPrevious.setText(self.tr("Find Previous"))
        self.actionFindPrevious.setShortcut(self.tr("Shift+F3"))
        self.actionSelectAll.setText(self.tr("Select &All"))
        self.actionSelectAll.setShortcut(self.tr("Ctrl+A"))
        self.actionEdit_Header.setText(self.tr("Edit Header.."))
        self.actionPreferences.setText(self.tr("Preferences"))
        self.actionFilterUntranslated.setText(self.tr("Untranslated"))
        self.actionFilterUntranslated.setIconText(self.tr("Untranslated"))
        self.actionFilterUntranslated.setToolTip(self.tr("Untranslated"))
        self.actionAsf.setText(self.tr("asf"))
        self.actionStandard_Tools.setText(self.tr("Standard Tools"))
        self.actionNavigation_Tools.setText(self.tr("Navigation Tools"))
        self.actionHide_View.setText(self.tr("Hide Overview"))
        self.actionHide_Detail.setText(self.tr("Hide Detail"))
        self.actionHide_Comment.setText(self.tr("Hide Comment"))
        self.actionStandard_Tools1.setText(self.tr("Standard Tools"))
        self.actionNavigation_Tools1.setText(self.tr("Navigation Tools"))
        self.actionHello.setText(self.tr("Hello"))
        self.actionComment.setText(self.tr("Comment"))
        self.actionHello_2.setText(self.tr("Hello"))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
