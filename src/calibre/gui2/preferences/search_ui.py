# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/preferences/search.ui'
#
# Created: Sun Jul  8 22:44:31 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(670, 663)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.opt_search_as_you_type = QtGui.QCheckBox(Form)
        self.opt_search_as_you_type.setObjectName(_fromUtf8("opt_search_as_you_type"))
        self.gridLayout.addWidget(self.opt_search_as_you_type, 0, 0, 1, 1)
        self.opt_use_primary_find_in_search = QtGui.QCheckBox(Form)
        self.opt_use_primary_find_in_search.setObjectName(_fromUtf8("opt_use_primary_find_in_search"))
        self.gridLayout.addWidget(self.opt_use_primary_find_in_search, 0, 1, 1, 1)
        self.opt_highlight_search_matches = QtGui.QCheckBox(Form)
        self.opt_highlight_search_matches.setObjectName(_fromUtf8("opt_highlight_search_matches"))
        self.gridLayout.addWidget(self.opt_highlight_search_matches, 1, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.opt_limit_search_columns = QtGui.QCheckBox(self.groupBox)
        self.opt_limit_search_columns.setObjectName(_fromUtf8("opt_limit_search_columns"))
        self.gridLayout_2.addWidget(self.opt_limit_search_columns, 1, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.opt_limit_search_columns_to = EditWithComplete(self.groupBox)
        self.opt_limit_search_columns_to.setObjectName(_fromUtf8("opt_limit_search_columns_to"))
        self.gridLayout_2.addWidget(self.opt_limit_search_columns_to, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.l12 = QtGui.QHBoxLayout()
        self.l12.setObjectName(_fromUtf8("l12"))
        self.la10 = QtGui.QLabel(self.groupBox_2)
        self.la10.setObjectName(_fromUtf8("la10"))
        self.l12.addWidget(self.la10)
        self.gst_names = QtGui.QComboBox(self.groupBox_2)
        self.gst_names.setEditable(True)
        self.gst_names.setMinimumContentsLength(10)
        self.gst_names.setObjectName(_fromUtf8("gst_names"))
        self.l12.addWidget(self.gst_names)
        self.gst_delete_button = QtGui.QToolButton(self.groupBox_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("trash.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gst_delete_button.setIcon(icon)
        self.gst_delete_button.setObjectName(_fromUtf8("gst_delete_button"))
        self.l12.addWidget(self.gst_delete_button)
        self.gst_value = EditWithComplete(self.groupBox_2)
        self.gst_value.setObjectName(_fromUtf8("gst_value"))
        self.l12.addWidget(self.gst_value)
        self.gst_save_button = QtGui.QToolButton(self.groupBox_2)
        self.gst_save_button.setObjectName(_fromUtf8("gst_save_button"))
        self.l12.addWidget(self.gst_save_button)
        self.gridLayout_3.addLayout(self.l12, 0, 0, 1, 1)
        self.gst_explanation = QtGui.QTextBrowser(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.gst_explanation.sizePolicy().hasHeightForWidth())
        self.gst_explanation.setSizePolicy(sizePolicy)
        self.gst_explanation.setObjectName(_fromUtf8("gst_explanation"))
        self.gridLayout_3.addWidget(self.gst_explanation, 0, 1, 3, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.l11 = QtGui.QLabel(self.groupBox_2)
        self.l11.setObjectName(_fromUtf8("l11"))
        self.hboxlayout.addWidget(self.l11)
        self.opt_grouped_search_make_user_categories = EditWithComplete(self.groupBox_2)
        self.opt_grouped_search_make_user_categories.setObjectName(_fromUtf8("opt_grouped_search_make_user_categories"))
        self.hboxlayout.addWidget(self.opt_grouped_search_make_user_categories)
        self.gridLayout_3.addLayout(self.hboxlayout, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 6, 0, 1, 2)
        self.clear_history_button = QtGui.QPushButton(Form)
        self.clear_history_button.setObjectName(_fromUtf8("clear_history_button"))
        self.gridLayout.addWidget(self.clear_history_button, 5, 0, 1, 2)
        self.groupBox22 = QtGui.QGroupBox(Form)
        self.groupBox22.setObjectName(_fromUtf8("groupBox22"))
        self.gridLayout_22 = QtGui.QGridLayout(self.groupBox22)
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        self.label1 = QtGui.QLabel(self.groupBox22)
        self.label1.setWordWrap(True)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.gridLayout_22.addWidget(self.label1, 0, 0, 1, 6)
        self.label_221 = QtGui.QLabel(self.groupBox22)
        self.label_221.setObjectName(_fromUtf8("label_221"))
        self.gridLayout_22.addWidget(self.label_221, 1, 0, 1, 1)
        self.similar_authors_search_key = QtGui.QComboBox(self.groupBox22)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.similar_authors_search_key.sizePolicy().hasHeightForWidth())
        self.similar_authors_search_key.setSizePolicy(sizePolicy)
        self.similar_authors_search_key.setObjectName(_fromUtf8("similar_authors_search_key"))
        self.gridLayout_22.addWidget(self.similar_authors_search_key, 1, 1, 1, 1)
        self.opt_similar_authors_match_kind = QtGui.QComboBox(self.groupBox22)
        self.opt_similar_authors_match_kind.setObjectName(_fromUtf8("opt_similar_authors_match_kind"))
        self.gridLayout_22.addWidget(self.opt_similar_authors_match_kind, 1, 2, 1, 1)
        self.label_222 = QtGui.QLabel(self.groupBox22)
        self.label_222.setObjectName(_fromUtf8("label_222"))
        self.gridLayout_22.addWidget(self.label_222, 1, 3, 1, 1)
        self.similar_series_search_key = QtGui.QComboBox(self.groupBox22)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.similar_series_search_key.sizePolicy().hasHeightForWidth())
        self.similar_series_search_key.setSizePolicy(sizePolicy)
        self.similar_series_search_key.setObjectName(_fromUtf8("similar_series_search_key"))
        self.gridLayout_22.addWidget(self.similar_series_search_key, 1, 4, 1, 1)
        self.opt_similar_series_match_kind = QtGui.QComboBox(self.groupBox22)
        self.opt_similar_series_match_kind.setObjectName(_fromUtf8("opt_similar_series_match_kind"))
        self.gridLayout_22.addWidget(self.opt_similar_series_match_kind, 1, 5, 1, 1)
        self.label_223 = QtGui.QLabel(self.groupBox22)
        self.label_223.setObjectName(_fromUtf8("label_223"))
        self.gridLayout_22.addWidget(self.label_223, 2, 0, 1, 1)
        self.similar_tags_search_key = QtGui.QComboBox(self.groupBox22)
        self.similar_tags_search_key.setObjectName(_fromUtf8("similar_tags_search_key"))
        self.gridLayout_22.addWidget(self.similar_tags_search_key, 2, 1, 1, 1)
        self.opt_similar_tags_match_kind = QtGui.QComboBox(self.groupBox22)
        self.opt_similar_tags_match_kind.setObjectName(_fromUtf8("opt_similar_tags_match_kind"))
        self.gridLayout_22.addWidget(self.opt_similar_tags_match_kind, 2, 2, 1, 1)
        self.label_224 = QtGui.QLabel(self.groupBox22)
        self.label_224.setObjectName(_fromUtf8("label_224"))
        self.gridLayout_22.addWidget(self.label_224, 2, 3, 1, 1)
        self.similar_publisher_search_key = QtGui.QComboBox(self.groupBox22)
        self.similar_publisher_search_key.setObjectName(_fromUtf8("similar_publisher_search_key"))
        self.gridLayout_22.addWidget(self.similar_publisher_search_key, 2, 4, 1, 1)
        self.opt_similar_publisher_match_kind = QtGui.QComboBox(self.groupBox22)
        self.opt_similar_publisher_match_kind.setObjectName(_fromUtf8("opt_similar_publisher_match_kind"))
        self.gridLayout_22.addWidget(self.opt_similar_publisher_match_kind, 2, 5, 1, 1)
        self.gridLayout.addWidget(self.groupBox22, 7, 0, 1, 2)
        self.label_2.setBuddy(self.opt_limit_search_columns_to)
        self.la10.setBuddy(self.gst_names)
        self.l11.setBuddy(self.opt_grouped_search_make_user_categories)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.opt_search_as_you_type.setText(_("Search as you &type"))
        self.opt_use_primary_find_in_search.setText(_("Unaccented characters match accented characters"))
        self.opt_highlight_search_matches.setText(_("&Highlight search results instead of restricting the book list to the results"))
        self.groupBox.setTitle(_("What to search by default"))
        self.label.setText(_("When you enter a search term without a prefix, by default calibre will search all metadata for matches. For example, entering, \"asimov\" will search not just authors but title/tags/series/comments/etc. Use these options if you would like to change this behavior."))
        self.opt_limit_search_columns.setText(_("&Limit the searched metadata"))
        self.label_2.setText(_("&Columns that non-prefixed searches are limited to:"))
        self.label_3.setText(_("Note that this option affects all searches, including saved searches and restrictions. Therefore, if you use this option, it is best to ensure that you always use prefixes in your saved searches. For example, use \"series:Foundation\" rather than just \"Foundation\" in  a saved search"))
        self.groupBox_2.setTitle(_("Grouped Search Terms"))
        self.la10.setText(_("&Names:"))
        self.gst_names.setToolTip(_("Contains the names of the currently-defined group search terms.\n"
"Create a new name by entering it into the empty box, then\n"
"pressing Save. Rename a search term by selecting it then\n"
"changing the name and pressing Save. Change the value of\n"
"a search term by changing the value box then pressing Save."))
        self.gst_delete_button.setToolTip(_("Delete the current search term"))
        self.gst_delete_button.setText(_("..."))
        self.gst_save_button.setToolTip(_("Save the current search term. You can rename a search term by\n"
"changing the name then pressing Save. You can change the value\n"
"of a search term by changing the value box then pressing Save."))
        self.gst_save_button.setText(_("&Save"))
        self.l11.setText(_("Make &user categories from:"))
        self.opt_grouped_search_make_user_categories.setToolTip(_("Enter the names of any grouped search terms you wish\n"
"to be shown as user categories"))
        self.clear_history_button.setToolTip(_("Clear search histories from all over calibre. Including the book list, e-book viewer, fetch news dialog, etc."))
        self.clear_history_button.setText(_("Clear search &histories"))
        self.groupBox22.setTitle(_("What to search when searching similar books"))
        self.label1.setText(_("<p>When you search for similar books by right clicking the\n"
"         book and selecting \"Similar books...\",\n"
"         calibre constructs a search using the column lookup names specified below.\n"
"         By changing the lookup name to a grouped search term you can\n"
"         search multiple columns at once.</p>"))
        self.label_221.setText(_("Similar authors: "))
        self.label_222.setText(_("Similar series: "))
        self.label_223.setText(_("Similar tags: "))
        self.label_224.setText(_("Similar publishers: "))

from calibre.gui2.complete2 import EditWithComplete

