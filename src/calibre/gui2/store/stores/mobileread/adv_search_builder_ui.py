# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/store/stores/mobileread/adv_search_builder.ui'
#
# Created: Fri May 11 09:13:11 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(752, 472)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("search.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.matchkind = QtGui.QComboBox(Dialog)
        self.matchkind.setObjectName(_fromUtf8("matchkind"))
        self.matchkind.addItem(_fromUtf8(""))
        self.matchkind.addItem(_fromUtf8(""))
        self.matchkind.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.matchkind, 0, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.all = QtGui.QLineEdit(self.groupBox)
        self.all.setObjectName(_fromUtf8("all"))
        self.horizontalLayout.addWidget(self.all)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.phrase = QtGui.QLineEdit(self.groupBox)
        self.phrase.setObjectName(_fromUtf8("phrase"))
        self.horizontalLayout_2.addWidget(self.phrase)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.any = QtGui.QLineEdit(self.groupBox)
        self.any.setObjectName(_fromUtf8("any"))
        self.horizontalLayout_3.addWidget(self.any)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.none = QtGui.QLineEdit(self.groupBox_2)
        self.none.setObjectName(_fromUtf8("none"))
        self.horizontalLayout_4.addWidget(self.none)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.tab)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.title_box = EnLineEdit(self.tab_2)
        self.title_box.setObjectName(_fromUtf8("title_box"))
        self.gridLayout.addWidget(self.title_box, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.clear_button = QtGui.QPushButton(self.tab_2)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.horizontalLayout_6.addWidget(self.clear_button)
        self.tab_2_button_box = QtGui.QDialogButtonBox(self.tab_2)
        self.tab_2_button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.tab_2_button_box.setObjectName(_fromUtf8("tab_2_button_box"))
        self.horizontalLayout_6.addWidget(self.tab_2_button_box)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 2)
        self.author_box = EnLineEdit(self.tab_2)
        self.author_box.setObjectName(_fromUtf8("author_box"))
        self.gridLayout.addWidget(self.author_box, 2, 1, 1, 1)
        self.format_box = QtGui.QLineEdit(self.tab_2)
        self.format_box.setObjectName(_fromUtf8("format_box"))
        self.gridLayout.addWidget(self.format_box, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.label_5.setBuddy(self.matchkind)
        self.label.setBuddy(self.all)
        self.label_2.setBuddy(self.all)
        self.label_3.setBuddy(self.all)
        self.label_4.setBuddy(self.all)
        self.label_7.setBuddy(self.title_box)
        self.label_8.setBuddy(self.author_box)
        self.label_10.setBuddy(self.format_box)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.all, self.phrase)
        Dialog.setTabOrder(self.phrase, self.any)
        Dialog.setTabOrder(self.any, self.none)
        Dialog.setTabOrder(self.none, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.title_box)
        Dialog.setTabOrder(self.title_box, self.author_box)
        Dialog.setTabOrder(self.author_box, self.format_box)
        Dialog.setTabOrder(self.format_box, self.clear_button)
        Dialog.setTabOrder(self.clear_button, self.tab_2_button_box)
        Dialog.setTabOrder(self.tab_2_button_box, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.matchkind)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Advanced Search"))
        self.label_5.setText(_("&What kind of match to use:"))
        self.matchkind.setItemText(0, _("Contains: the word or phrase matches anywhere in the metadata field"))
        self.matchkind.setItemText(1, _("Equals: the word or phrase must match the entire metadata field"))
        self.matchkind.setItemText(2, _("Regular expression: the expression must match anywhere in the metadata field"))
        self.groupBox.setTitle(_("Find entries that have..."))
        self.label.setText(_("&All these words:"))
        self.label_2.setText(_("This exact &phrase:"))
        self.label_3.setText(_("&One or more of these words:"))
        self.groupBox_2.setTitle(_("But dont show entries that have..."))
        self.label_4.setText(_("Any of these &unwanted words:"))
        self.label_6.setText(_("See the <a href=\"http://calibre-ebook.com/user_manual/gui.html#the-search-interface\">User Manual</a> for more help"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("A&dvanced Search"))
        self.label_7.setText(_("&Title:"))
        self.title_box.setToolTip(_("Enter the title."))
        self.label_8.setText(_("&Author:"))
        self.clear_button.setText(_("&Clear"))
        self.label_11.setText(_("Search only in specific fields:"))
        self.label_10.setText(_("&Format:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("Titl&e/Author/Price ..."))

from calibre.gui2.widgets import EnLineEdit

