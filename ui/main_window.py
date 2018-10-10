# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created: Thu Oct 15 23:23:51 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ui_main_window(object):
    def setupUi(self, ui_main_window):
        ui_main_window.setObjectName(_fromUtf8("ui_main_window"))
        ui_main_window.setWindowModality(QtCore.Qt.WindowModal)
        ui_main_window.resize(820, 620)
        ui_main_window.setWindowTitle(_fromUtf8("QuickOSM"))
        self.horizontalLayout = QtGui.QHBoxLayout(ui_main_window)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidget = QtGui.QListWidget(ui_main_window)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(100, 200))
        self.listWidget.setMaximumSize(QtCore.QSize(153, 16777215))
        self.listWidget.setStyleSheet(_fromUtf8("QListWidget{\n"
"    background-color: rgb(69, 69, 69, 220);\n"
"    outline: 0;\n"
"}\n"
"QListWidget::item {\n"
"    color: white;\n"
"    padding: 3px;\n"
"}\n"
"QListWidget::item::selected {\n"
"    color: black;\n"
"    background-color:palette(Window);\n"
"    padding-right: 0px;\n"
"}"))
        self.listWidget.setFrameShape(QtGui.QFrame.Box)
        self.listWidget.setLineWidth(0)
        self.listWidget.setIconSize(QtCore.QSize(32, 32))
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/QuickOSM/resources/quick.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/QuickOSM/resources/favorites.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/QuickOSM/resources/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/QuickOSM/resources/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/QuickOSM/resources/general.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/QuickOSM/resources/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/QuickOSM/resources/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.messageBar = gui.QgsMessageBar(ui_main_window)
        self.messageBar.setObjectName(_fromUtf8("messageBar"))
        self.verticalLayout_13.addWidget(self.messageBar)
        self.stackedWidget = QtGui.QStackedWidget(ui_main_window)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(300, 200))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.quick_query = QuickQueryWidget()
        self.quick_query.setObjectName(_fromUtf8("quick_query"))
        self.stackedWidget.addWidget(self.quick_query)
        self.my_queries = MyQueriesWidget()
        self.my_queries.setObjectName(_fromUtf8("my_queries"))
        self.stackedWidget.addWidget(self.my_queries)
        self.query = QueryWidget()
        self.query.setObjectName(_fromUtf8("query"))
        self.stackedWidget.addWidget(self.query)
        self.osm_file = OsmFileWidget()
        self.osm_file.setObjectName(_fromUtf8("osm_file"))
        self.stackedWidget.addWidget(self.osm_file)
        self.parameters = QtGui.QWidget()
        self.parameters.setObjectName(_fromUtf8("parameters"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.parameters)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.parameters)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.comboBox_default_OAPI = QtGui.QComboBox(self.groupBox)
        self.comboBox_default_OAPI.setObjectName(_fromUtf8("comboBox_default_OAPI"))
        self.horizontalLayout_8.addWidget(self.comboBox_default_OAPI)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_OAPI_timestamp = QtGui.QPushButton(self.groupBox)
        self.pushButton_OAPI_timestamp.setObjectName(_fromUtf8("pushButton_OAPI_timestamp"))
        self.horizontalLayout_2.addWidget(self.pushButton_OAPI_timestamp)
        self.label_timestamp_oapi = QtGui.QLabel(self.groupBox)
        self.label_timestamp_oapi.setObjectName(_fromUtf8("label_timestamp_oapi"))
        self.horizontalLayout_2.addWidget(self.label_timestamp_oapi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.parameters)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pushButton_restoreQueries = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_restoreQueries.setObjectName(_fromUtf8("pushButton_restoreQueries"))
        self.horizontalLayout_7.addWidget(self.pushButton_restoreQueries)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_7 = QtGui.QGroupBox(self.parameters)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.radioButton_outputJson = QtGui.QRadioButton(self.groupBox_7)
        self.radioButton_outputJson.setObjectName(_fromUtf8("radioButton_outputJson"))
        self.verticalLayout_11.addWidget(self.radioButton_outputJson)
        self.radioButton_outputShape = QtGui.QRadioButton(self.groupBox_7)
        self.radioButton_outputShape.setObjectName(_fromUtf8("radioButton_outputShape"))
        self.verticalLayout_11.addWidget(self.radioButton_outputShape)
        self.verticalLayout_2.addWidget(self.groupBox_7)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.parameters)
        self.help = QtGui.QWidget()
        self.help.setObjectName(_fromUtf8("help"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.help)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(self.help)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 89, 58))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_homeHelp = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_homeHelp.setObjectName(_fromUtf8("pushButton_homeHelp"))
        self.horizontalLayout_3.addWidget(self.pushButton_homeHelp)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.webBrowser = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.webBrowser.setObjectName(_fromUtf8("webBrowser"))
        self.verticalLayout_5.addWidget(self.webBrowser)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.help)
        self.about = QtGui.QWidget()
        self.about.setObjectName(_fromUtf8("about"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.about)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scrollArea_2 = QtGui.QScrollArea(self.about)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -39, 636, 845))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_13.setText(_fromUtf8("<html><head/><body><p>Etienne Trimaille</p></body></html>"))
        self.label_13.setScaledContents(False)
        self.label_13.setOpenExternalLinks(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_5.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setText(_fromUtf8("<a href=\"mailto:etienne@trimaille.eu?subject=Plugin QuickOSM - About\" style=\"color:#7BA11A;text-decoration:none;\">etienne@trimaille.eu</a>"))
        self.label_14.setOpenExternalLinks(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_5.addWidget(self.label_14)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.groupBox_5 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_10 = QtGui.QLabel(self.groupBox_5)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_7.addWidget(self.label_10)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_12.setText(_fromUtf8("<html><head/><body><p><a href=\"http://www.3liz.com/\"><img src=\":/plugins/QuickOSM/resources/3liz.png\"/></a></p></body></html>\n"
""))
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setOpenExternalLinks(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.label_11 = QtGui.QLabel(self.groupBox_5)
        self.label_11.setText(_fromUtf8("<a href=\"http://www.3liz.com\" style=\"color:#7BA11A;text-decoration:none;\">Libérez vos SIG !</a>"))
        self.label_11.setOpenExternalLinks(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addWidget(self.groupBox_5)
        self.groupBox_8 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_18 = QtGui.QLabel(self.groupBox_8)
        self.label_18.setScaledContents(True)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_12.addWidget(self.label_18)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_21 = QtGui.QLabel(self.groupBox_8)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_14.addWidget(self.label_21)
        self.label_22 = QtGui.QLabel(self.groupBox_8)
        self.label_22.setText(_fromUtf8("Antony Bartolo"))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_14.addWidget(self.label_22)
        self.verticalLayout_12.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_23 = QtGui.QLabel(self.groupBox_8)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_15.addWidget(self.label_23)
        self.label_24 = QtGui.QLabel(self.groupBox_8)
        self.label_24.setText(_fromUtf8("Kari Salovaara"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_15.addWidget(self.label_24)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_17 = QtGui.QLabel(self.groupBox_8)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_13.addWidget(self.label_17)
        self.label_9 = QtGui.QLabel(self.groupBox_8)
        self.label_9.setText(_fromUtf8("Etienne Trimaille"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_13.addWidget(self.label_9)
        self.verticalLayout_12.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_6 = QtGui.QLabel(self.groupBox_8)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_12.addWidget(self.label_6)
        self.label_5 = QtGui.QLabel(self.groupBox_8)
        self.label_5.setText(_fromUtf8("Thomas Moenkemeier"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_12.addWidget(self.label_5)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_8 = QtGui.QLabel(self.groupBox_8)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_11.addWidget(self.label_8)
        self.label_7 = QtGui.QLabel(self.groupBox_8)
        self.label_7.setText(_fromUtf8("Francesco Bisantis"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_11.addWidget(self.label_7)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_4 = QtGui.QLabel(self.groupBox_8)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_10.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.groupBox_8)
        self.label_3.setText(_fromUtf8("<a href=\"https://github.com/freeExec\" style=\"color:#7BA11A;text-decoration:none;\">freeExec</a>"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_10.addWidget(self.label_3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9.addLayout(self.verticalLayout_12)
        self.verticalLayout_9.addWidget(self.groupBox_8)
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_19 = QtGui.QLabel(self.groupBox_6)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_6)
        self.label_20.setText(_fromUtf8("<a href=\"https://github.com/3liz/QgisQuickOSMPlugin\" style=\"color:#7BA11A;text-decoration:none;\">https://github.com/3liz/QgisQuickOSMPlugin</a>"))
        self.label_20.setOpenExternalLinks(True)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_4.addWidget(self.label_20, 0, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_4)
        self.verticalLayout_9.addWidget(self.groupBox_6)
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setText(_fromUtf8("OpenStreetMap"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_4)
        self.label_16.setText(_fromUtf8("<html><head/><body><p><a href=\"https://www.gnu.org/licenses/gpl-2.0.html\"><img src=\":/plugins/QuickOSM/resources/gnu.png\"/></a></p></body></html>"))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setOpenExternalLinks(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 1, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_4)
        self.label_15.setText(_fromUtf8("Plugin : Licence GPL Version 2"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setText(_fromUtf8("<html><head/><body><p>ODBL : © OpenStreetMap\'s contributors </p><p><a href=\"http://www.openstreetmap.org/copyright\"><span style=\" text-decoration: underline; color:#0057ae;\">http://www.openstreetmap.org/copyright</span></a></p></body></html>"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.verticalLayout_9.addWidget(self.groupBox_4)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.about)
        self.verticalLayout_13.addWidget(self.stackedWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_13)

        self.retranslateUi(ui_main_window)
        self.listWidget.setCurrentRow(-1)
        self.stackedWidget.setCurrentIndex(6)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("currentRowChanged(int)")), self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(ui_main_window)
        ui_main_window.setTabOrder(self.pushButton_OAPI_timestamp, self.listWidget)

    def retranslateUi(self, ui_main_window):
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("ui_main_window", "Quick query", None))
        item = self.listWidget.item(1)
        item.setText(_translate("ui_main_window", "My queries", None))
        item = self.listWidget.item(2)
        item.setText(_translate("ui_main_window", "Query", None))
        item = self.listWidget.item(3)
        item.setText(_translate("ui_main_window", "OSM File", None))
        item = self.listWidget.item(4)
        item.setText(_translate("ui_main_window", "Parameters", None))
        item = self.listWidget.item(5)
        item.setText(_translate("ui_main_window", "Help", None))
        item = self.listWidget.item(6)
        item.setText(_translate("ui_main_window", "About", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("ui_main_window", "Overpass API", None))
        self.pushButton_OAPI_timestamp.setText(_translate("ui_main_window", "Get timestamp", None))
        self.label_timestamp_oapi.setText(_translate("ui_main_window", "unknow", None))
        self.groupBox_3.setTitle(_translate("ui_main_window", "Queries", None))
        self.pushButton_restoreQueries.setText(_translate("ui_main_window", "Restore queries", None))
        self.groupBox_7.setTitle(_translate("ui_main_window", "Outputs", None))
        self.radioButton_outputJson.setText(_translate("ui_main_window", "GeoJSON (not editable, column\'s name longer)", None))
        self.radioButton_outputShape.setText(_translate("ui_main_window", "Shapefile (editable, column\'s name shorter)", None))
        self.pushButton_homeHelp.setText(_translate("ui_main_window", "Home", None))
        self.groupBox_2.setTitle(_translate("ui_main_window", "Realization", None))
        self.groupBox_5.setTitle(_translate("ui_main_window", "Supervision", None))
        self.label_10.setText(_translate("ui_main_window", "This intership was supervised by 3Liz", None))
        self.groupBox_8.setTitle(_translate("ui_main_window", "Translators", None))
        self.label_18.setText(_translate("ui_main_window", "<html><head/><body><p>The web-based translating platform <a href=\"https://www.transifex.com/projects/p/gui/\"><span style=\" text-decoration: underline; color:#0057ae;\">Transifex</span></a> is used. It\'s easier for translators.</p></body></html>", None))
        self.label_21.setText(_translate("ui_main_window", "Dutch", None))
        self.label_23.setText(_translate("ui_main_window", "Finnish", None))
        self.label_17.setText(_translate("ui_main_window", "French", None))
        self.label_6.setText(_translate("ui_main_window", "German", None))
        self.label_8.setText(_translate("ui_main_window", "Italian", None))
        self.label_4.setText(_translate("ui_main_window", "Russian", None))
        self.groupBox_6.setTitle(_translate("ui_main_window", "Sources", None))
        self.label_19.setText(_translate("ui_main_window", "Github\'s repository", None))
        self.groupBox_4.setTitle(_translate("ui_main_window", "Licence", None))

from qgis import gui
from query_dialog import QueryWidget
from osm_file_dialog import OsmFileWidget
from quick_query_dialog import QuickQueryWidget
from my_queries_dialog import MyQueriesWidget
from QuickOSM import resources_rc
