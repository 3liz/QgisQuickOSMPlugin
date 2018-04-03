# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/query.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ui_query(object):
    def setupUi(self, ui_query):
        ui_query.setObjectName("ui_query")
        ui_query.resize(603, 871)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ui_query)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(ui_query)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 585, 853))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_9.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.textEdit_query = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_query.setAcceptRichText(False)
        self.textEdit_query.setObjectName("textEdit_query")
        self.verticalLayout.addWidget(self.textEdit_query)
        self.groupBox = QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setText("{{geocodeArea:}}")
        self.label_2.setObjectName("label_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_nominatim = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_nominatim.setObjectName("lineEdit_nominatim")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nominatim)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.radioButton_extentMapCanvas = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_extentMapCanvas.setChecked(True)
        self.radioButton_extentMapCanvas.setObjectName("radioButton_extentMapCanvas")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.radioButton_extentMapCanvas)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setText("Points")
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_points = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_points.setText("")
        self.checkBox_points.setChecked(True)
        self.checkBox_points.setObjectName("checkBox_points")
        self.horizontalLayout_4.addWidget(self.checkBox_points)
        self.lineEdit_csv_points = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_csv_points.setInputMask("")
        self.lineEdit_csv_points.setText("")
        self.lineEdit_csv_points.setPlaceholderText("col1,col2,col3")
        self.lineEdit_csv_points.setObjectName("lineEdit_csv_points")
        self.horizontalLayout_4.addWidget(self.lineEdit_csv_points)
        self.formLayout_4.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setText("Lines")
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_lines = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_lines.setText("")
        self.checkBox_lines.setChecked(True)
        self.checkBox_lines.setObjectName("checkBox_lines")
        self.horizontalLayout_6.addWidget(self.checkBox_lines)
        self.lineEdit_csv_lines = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_csv_lines.setObjectName("lineEdit_csv_lines")
        self.horizontalLayout_6.addWidget(self.lineEdit_csv_lines)
        self.formLayout_4.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setText("Multilinestrings")
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_multilinestrings = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_multilinestrings.setText("")
        self.checkBox_multilinestrings.setChecked(True)
        self.checkBox_multilinestrings.setObjectName("checkBox_multilinestrings")
        self.horizontalLayout_7.addWidget(self.checkBox_multilinestrings)
        self.lineEdit_csv_multilinestrings = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_csv_multilinestrings.setPlaceholderText("")
        self.lineEdit_csv_multilinestrings.setObjectName("lineEdit_csv_multilinestrings")
        self.horizontalLayout_7.addWidget(self.lineEdit_csv_multilinestrings)
        self.formLayout_4.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setText("Multipolygons")
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_multipolygons = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_multipolygons.setText("")
        self.checkBox_multipolygons.setChecked(True)
        self.checkBox_multipolygons.setObjectName("checkBox_multipolygons")
        self.horizontalLayout_8.addWidget(self.checkBox_multipolygons)
        self.lineEdit_csv_multipolygons = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_csv_multipolygons.setPlaceholderText("")
        self.lineEdit_csv_multipolygons.setObjectName("lineEdit_csv_multipolygons")
        self.horizontalLayout_8.addWidget(self.lineEdit_csv_multipolygons)
        self.formLayout_4.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_extentLayer = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_extentLayer.setObjectName("radioButton_extentLayer")
        self.horizontalLayout_3.addWidget(self.radioButton_extentLayer)
        self.comboBox_extentLayer = QgsMapLayerComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_extentLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_extentLayer.setSizePolicy(sizePolicy)
        self.comboBox_extentLayer.setObjectName("comboBox_extentLayer")
        self.horizontalLayout_3.addWidget(self.comboBox_extentLayer)
        self.formLayout_4.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.output_directory = QgsFileWidget(self.groupBox)
        self.output_directory.setObjectName("output_directory")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.output_directory)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_filePrefix = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_filePrefix.setObjectName("lineEdit_filePrefix")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_filePrefix)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_generateQuery = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_generateQuery.setObjectName("pushButton_generateQuery")
        self.horizontalLayout_2.addWidget(self.pushButton_generateQuery)
        self.pushButton_runQuery = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_runQuery.setDefault(True)
        self.pushButton_runQuery.setObjectName("pushButton_runQuery")
        self.horizontalLayout_2.addWidget(self.pushButton_runQuery)
        self.pushButton_saveQuery = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_saveQuery.setObjectName("pushButton_saveQuery")
        self.horizontalLayout_2.addWidget(self.pushButton_saveQuery)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_progress = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_progress.sizePolicy().hasHeightForWidth())
        self.label_progress.setSizePolicy(sizePolicy)
        self.label_progress.setText("progress text")
        self.label_progress.setObjectName("label_progress")
        self.verticalLayout.addWidget(self.label_progress)
        self.progressBar_execution = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_execution.setProperty("value", 0)
        self.progressBar_execution.setObjectName("progressBar_execution")
        self.verticalLayout.addWidget(self.progressBar_execution)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_overpassTurbo = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_overpassTurbo.setText("Overpass Turbo")
        self.pushButton_overpassTurbo.setObjectName("pushButton_overpassTurbo")
        self.horizontalLayout_5.addWidget(self.pushButton_overpassTurbo)
        self.pushButton_documentation = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_documentation.setObjectName("pushButton_documentation")
        self.horizontalLayout_5.addWidget(self.pushButton_documentation)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(ui_query)
        self.checkBox_points.toggled['bool'].connect(self.lineEdit_csv_points.setEnabled)
        self.checkBox_lines.toggled['bool'].connect(self.lineEdit_csv_lines.setEnabled)
        self.checkBox_multilinestrings.toggled['bool'].connect(self.lineEdit_csv_multilinestrings.setEnabled)
        self.checkBox_multipolygons.toggled['bool'].connect(self.lineEdit_csv_multipolygons.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ui_query)

    def retranslateUi(self, ui_query):
        _translate = QtCore.QCoreApplication.translate
        ui_query.setWindowTitle(_translate("ui_query", "QuickOSM - Query"))
        self.label.setText(_translate("ui_query", "Overpass query"))
        self.groupBox.setTitle(_translate("ui_query", "Advanced"))
        self.lineEdit_nominatim.setPlaceholderText(_translate("ui_query", "Can be overridden"))
        self.label_5.setText(_translate("ui_query", "{{bbox}} or {{center}}"))
        self.radioButton_extentMapCanvas.setText(_translate("ui_query", "Extent of the map canvas"))
        self.label_3.setText(_translate("ui_query", "Outputs"))
        self.lineEdit_csv_lines.setPlaceholderText(_translate("ui_query", "or let empty"))
        self.radioButton_extentLayer.setText(_translate("ui_query", "Extent of a layer"))
        self.label_4.setText(_translate("ui_query", "Directory"))
        self.label_6.setText(_translate("ui_query", "File prefix"))
        self.pushButton_generateQuery.setText(_translate("ui_query", "Generate query"))
        self.pushButton_runQuery.setText(_translate("ui_query", "Run query"))
        self.pushButton_saveQuery.setText(_translate("ui_query", "Save query"))
        self.pushButton_documentation.setText(_translate("ui_query", "Documentation"))

from qgis.gui import QgsCollapsibleGroupBox, QgsFileWidget, QgsMapLayerComboBox
