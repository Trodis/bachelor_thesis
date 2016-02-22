# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'security_policy_tool.ui'
#
# Created: Thu Feb 18 13:10:44 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(726, 605)
        self.createComponents()
        self.createLayout()
        self.retranslateUi()
        self.MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Sirrix AG - \
            Browser in the Box | Security Policy Manager", None, QtGui.QApplication.UnicodeUTF8))

    def createLayout(self):
        
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")        

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")

        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.addWidget(self.label_7)

        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_guesttohost_download)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.addWidget(self.radio_guesttohost_download_allow)
        self.verticalLayout_7.addWidget(self.radio_guesttohost_download_askuser)
        self.verticalLayout_7.addWidget(self.radio_guesttohost_download_deny)
        self.verticalLayout.addWidget(self.groupBox_guesttohost_download)
        
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_guesttohost_print)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.addWidget(self.radio_guesttohost_print_allow)
        self.verticalLayout_6.addWidget(self.radio_guesttohost_print_askuser)
        self.verticalLayout_6.addWidget(self.radio_guesttohost_print_deny)
        self.verticalLayout.addWidget(self.groupBox_guesttohost_print)
        
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_guesttohost_clipboard)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.addWidget(self.radio_guesttohost_clipboard_allow)
        self.verticalLayout_5.addWidget(self.radio_guesttohost_clipboard_askuser)
        self.verticalLayout_5.addWidget(self.radio_guesttohost_clipboard_deny)
        self.verticalLayout.addWidget(self.groupBox_guesttohost_clipboard)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
                
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_hosttoguest_upload)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.addWidget(self.radio_hosttoguest_upload_allow)
        self.verticalLayout_8.addWidget(self.radio_hosttoguest_upload_askuser)
        self.verticalLayout_8.addWidget(self.radio_hosttoguest_upload_deny)
        self.verticalLayout_3.addWidget(self.groupBox_hosttoguest_upload)
        
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_hosttoguest_clipboard)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.addWidget(self.radio_hosttoguest_clipboard_allow)
        self.verticalLayout_9.addWidget(self.radio_hosttoguest_clipboard_askuser)
        self.verticalLayout_9.addWidget(self.radio_hosttoguest_clipboard_deny)
        self.verticalLayout_3.addWidget(self.groupBox_hosttoguest_clipboard)

        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)

        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.pushButton_anwenden)
        self.horizontalLayout.addWidget(self.pushButton_reset)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 19))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
    
    def createComponents(self):
        self.centralwidget = QtGui.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_guesttohost_download = QtGui.QGroupBox(self.tab)
        self.groupBox_guesttohost_download.setObjectName("groupBox_guesttohost_download")
        self.radio_guesttohost_download_allow = QtGui.QRadioButton(self.groupBox_guesttohost_download)
        self.radio_guesttohost_download_allow.setObjectName("radio_guesttohost_download_allow")
        self.radio_guesttohost_download_askuser = QtGui.QRadioButton(self.groupBox_guesttohost_download)
        self.radio_guesttohost_download_askuser.setObjectName("radio_guesttohost_download_askuser")
        self.radio_guesttohost_download_deny = QtGui.QRadioButton(self.groupBox_guesttohost_download)
        self.radio_guesttohost_download_deny.setObjectName("radio_guesttohost_download_deny")

        self.groupBox_guesttohost_print = QtGui.QGroupBox(self.tab)
        self.groupBox_guesttohost_print.setObjectName("groupBox_guesttohost_print")
        self.groupBox_guesttohost_clipboard = QtGui.QGroupBox(self.tab)
        self.groupBox_guesttohost_clipboard.setObjectName("groupBox_guesttohost_clipboard")
        self.groupBox_hosttoguest_upload = QtGui.QGroupBox(self.tab)
        self.groupBox_hosttoguest_upload.setObjectName("groupBox_hosttoguest_upload")

        self.groupBox_hosttoguest_clipboard = QtGui.QGroupBox(self.tab)
        self.groupBox_hosttoguest_clipboard.setObjectName("groupBox_hosttoguest_clipboard")

        
        self.radio_guesttohost_print_allow = QtGui.QRadioButton(self.groupBox_guesttohost_print)
        self.radio_guesttohost_print_allow.setObjectName("radio_guesttohost_print_allow")
        self.radio_guesttohost_print_askuser = QtGui.QRadioButton(self.groupBox_guesttohost_print)
        self.radio_guesttohost_print_askuser.setObjectName("radio_guesttohost_print_askuser")
        self.radio_guesttohost_print_deny = QtGui.QRadioButton(self.groupBox_guesttohost_print)
        self.radio_guesttohost_print_deny.setObjectName("radio_guesttohost_print_deny")
        self.radio_guesttohost_clipboard_allow = QtGui.QRadioButton(self.groupBox_guesttohost_clipboard)
        self.radio_guesttohost_clipboard_allow.setObjectName("radio_guesttohost_clipboard_allow")
        self.radio_guesttohost_clipboard_askuser = QtGui.QRadioButton(self.groupBox_guesttohost_clipboard)
        self.radio_guesttohost_clipboard_askuser.setObjectName("radio_guesttohost_clipboard_askuser")
        self.radio_guesttohost_clipboard_deny = QtGui.QRadioButton(self.groupBox_guesttohost_clipboard)
        self.radio_guesttohost_clipboard_deny.setObjectName("radio_guesttohost_clipboard_deny")
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.radio_hosttoguest_upload_allow = QtGui.QRadioButton(self.groupBox_hosttoguest_upload)
        self.radio_hosttoguest_upload_allow.setObjectName("radio_hosttoguest_upload_allow")
        self.radio_hosttoguest_upload_askuser = QtGui.QRadioButton(self.groupBox_hosttoguest_upload)
        self.radio_hosttoguest_upload_askuser.setObjectName("radio_hosttoguest_upload_askuser")
        self.radio_hosttoguest_upload_deny = QtGui.QRadioButton(self.groupBox_hosttoguest_upload)
        self.radio_hosttoguest_upload_deny.setObjectName("radio_hosttoguest_upload_deny")
        self.radio_hosttoguest_clipboard_allow = QtGui.QRadioButton(self.groupBox_hosttoguest_clipboard)
        self.radio_hosttoguest_clipboard_allow.setObjectName("radio_hosttoguest_clipboard_allow")
        self.radio_hosttoguest_clipboard_askuser = QtGui.QRadioButton(self.groupBox_hosttoguest_clipboard)
        self.radio_hosttoguest_clipboard_askuser.setObjectName("radio_hosttoguest_clipboard_askuser")
        self.radio_hosttoguest_clipboard_deny = QtGui.QRadioButton(self.groupBox_hosttoguest_clipboard)
        self.radio_hosttoguest_clipboard_deny.setObjectName("radio_hosttoguest_clipboard_deny")
        self.pushButton_anwenden = QtGui.QPushButton(self.centralwidget)
        self.pushButton_anwenden.setObjectName("pushButton_save")
        self.pushButton_reset = QtGui.QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName("pushButton_reset")

    def retranslateUi(self):
        self.label.setText(QtGui.QApplication.translate("MainWindow", "BitBox to Desktop", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_guesttohost_download.setTitle(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_guesttohost_download_allow.setText(QtGui.QApplication.translate("MainWindow", "Allow", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_guesttohost_download_askuser.setText(QtGui.QApplication.translate("MainWindow", "Ask User", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_guesttohost_download_deny.setText(QtGui.QApplication.translate("MainWindow", "Deny", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_guesttohost_print.setTitle(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_guesttohost_print_allow.setText(QtGui.QApplication.translate("MainWindow", "Allow", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_guesttohost_print_askuser.setText(QtGui.QApplication.translate("MainWindow", "Ask User", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_guesttohost_print_deny.setText(QtGui.QApplication.translate("MainWindow", "Deny", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_guesttohost_clipboard.setTitle(QtGui.QApplication.translate("MainWindow", "Clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_guesttohost_clipboard_allow.setText(QtGui.QApplication.translate("MainWindow", "Allow", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_guesttohost_clipboard_askuser.setText(QtGui.QApplication.translate("MainWindow", "Ask User", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_guesttohost_clipboard_deny.setText(QtGui.QApplication.translate("MainWindow", "Deny", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Desktop to BitBox", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_hosttoguest_upload.setTitle(QtGui.QApplication.translate("MainWindow", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_hosttoguest_upload_allow.setText(QtGui.QApplication.translate("MainWindow", "Allow", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_hosttoguest_upload_askuser.setText(QtGui.QApplication.translate("MainWindow", "Ask User", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_hosttoguest_upload_deny.setText(QtGui.QApplication.translate("MainWindow", "Deny", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_hosttoguest_clipboard.setTitle(QtGui.QApplication.translate("MainWindow", "Clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_hosttoguest_clipboard_allow.setText(QtGui.QApplication.translate("MainWindow", "Allow", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_hosttoguest_clipboard_askuser.setText(QtGui.QApplication.translate("MainWindow", "Ask User", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_hosttoguest_clipboard_deny.setText(QtGui.QApplication.translate("MainWindow", "Deny", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Information flow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Network", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_anwenden.setText(QtGui.QApplication.translate("MainWindow", "Speichern", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))

