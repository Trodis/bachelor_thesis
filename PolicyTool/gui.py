# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'security_policy_tool.ui'
#
# Created: Wed Feb 24 10:40:31 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.createComponents()
        self.createLayout()
        self.retranslateUi()
    
    def createLayout(self):
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.addWidget(self.label_sirrixLogo)
        self.verticalLayout_4.addWidget(self.tabWidget)
        
        self.horizontalLayout_save_reset_buttons = QtGui.QHBoxLayout()
        self.horizontalLayout_save_reset_buttons.setObjectName("horizontalLayout_save_reset_buttons")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_informationflow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_description_informationflow = QtGui.QLabel(self.tab_informationflow)
        self.label_description_informationflow.setObjectName("label_description_informationflow")
        self.verticalLayout.addWidget(self.label_description_informationflow)
        self.groupBox_clipboard = QtGui.QGroupBox(self.tab_informationflow)
        self.groupBox_clipboard.setObjectName("groupBox_clipboard")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_clipboard)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_hosttoguest_description = QtGui.QLabel(self.groupBox_clipboard)
        self.label_hosttoguest_description.setObjectName("label_hosttoguest_description")
        self.verticalLayout_2.addWidget(self.label_hosttoguest_description)

        self.comboBox_clipboard_hosttoguest = QtGui.QComboBox(self.groupBox_clipboard)
        self.comboBox_clipboard_hosttoguest.setObjectName("comboBox_clipboard_hosttoguest")
        self.comboBox_clipboard_hosttoguest.addItem("")
        self.comboBox_clipboard_hosttoguest.addItem("")
        self.comboBox_clipboard_hosttoguest.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_clipboard_hosttoguest)
        self.label_guesttohost_description = QtGui.QLabel(self.groupBox_clipboard)
        self.label_guesttohost_description.setObjectName("label_guesttohost_description")
        self.verticalLayout_2.addWidget(self.label_guesttohost_description)

        self.comboBox_clipboard_guesttohost = QtGui.QComboBox(self.groupBox_clipboard)
        self.comboBox_clipboard_guesttohost.setObjectName("comboBox_clipboard_guesttohost")
        self.comboBox_clipboard_guesttohost.addItem("")
        self.comboBox_clipboard_guesttohost.addItem("")
        self.comboBox_clipboard_guesttohost.addItem("")

        self.verticalLayout_2.addWidget(self.comboBox_clipboard_guesttohost)
        self.verticalLayout.addWidget(self.groupBox_clipboard)
        self.groupBox_fileflow = QtGui.QGroupBox(self.tab_informationflow)
        self.groupBox_fileflow.setObjectName("groupBox_fileflow")
        
        self.label_upload_description = QtGui.QLabel(self.groupBox_fileflow)
        self.label_upload_description.setObjectName("label_upload_description")

        self.comboBox_upload = QtGui.QComboBox(self.groupBox_fileflow)
        self.comboBox_upload.setObjectName("comboBox_upload")
        self.comboBox_upload.addItem("")
        self.comboBox_upload.addItem("")
        self.comboBox_upload.addItem("")

        self.comboBox_download = QtGui.QComboBox(self.groupBox_fileflow)
        self.comboBox_download.setObjectName("comboBox_download")
        self.comboBox_download.addItem("")
        self.comboBox_download.addItem("")
        self.comboBox_download.addItem("")
        self.comboBox_download.addItem("")
        self.verticalLayout.addWidget(self.groupBox_fileflow)

        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_fileflow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.addWidget(self.label_upload_description)
        self.verticalLayout_3.addWidget(self.comboBox_upload)

        self.label_download_description = QtGui.QLabel(self.groupBox_fileflow)
        self.label_download_description.setObjectName("label_download_description")
        self.verticalLayout_3.addWidget(self.label_download_description)
        self.verticalLayout_3.addWidget(self.comboBox_download)
        self.verticalLayout_3.addWidget(self.checkBox_print)
        
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_persistency)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.addWidget(self.radioButton_persistency_bookmarksonly)
        self.radioButton_persistency_deny = QtGui.QRadioButton(self.groupBox_persistency)
        self.radioButton_persistency_deny.setObjectName("radioButton_persistency_deny")
        self.verticalLayout_5.addWidget(self.radioButton_persistency_deny)
        self.verticalLayout_5.addWidget(self.radioButton_persistency_all)
        self.verticalLayout.addWidget(self.groupBox_persistency)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
                
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_network)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.addWidget(self.groupBox_proxy)
        self.verticalLayout_6.addWidget(self.checkBox_lockproxy)
        self.verticalLayout_6.addWidget(self.groupBox_DNS)

        self.verticalLayout_static_dns = QtGui.QVBoxLayout()
        self.verticalLayout_static_dns.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_static_dns.setObjectName("verticalLayout_static_dns")
        self.verticalLayout_static_dns.addWidget(self.radioButton_dns_static)
        self.verticalLayout_static_dns.addWidget(self.lineEdit_dns_static_adress)

        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_DNS)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.addWidget(self.radioButton_dns_windows)
        self.verticalLayout_8.addLayout(self.verticalLayout_static_dns)
        
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_proxy)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.addWidget(self.radioButton_proxy_none)
        self.horizontalLayout_staticproxy = QtGui.QHBoxLayout()
        self.horizontalLayout_staticproxy.setObjectName("horizontalLayout_staticproxy")
        self.horizontalLayout_staticproxy.addWidget(self.radioButton_proxy_static)
        self.horizontalLayout_staticproxy.addWidget(self.lineEdit_proxy_static_ip)
        self.horizontalLayout_staticproxy.addWidget(self.label_slash_ip_prefix)
        self.horizontalLayout_staticproxy.addWidget(self.lineEdit_proxy_static_prefix)
        self.verticalLayout_10.addLayout(self.horizontalLayout_staticproxy)
        self.verticalLayout_proxy_automatic = QtGui.QVBoxLayout()
        self.verticalLayout_proxy_automatic.setObjectName("verticalLayout_proxy_automatic")
        self.verticalLayout_proxy_automatic.addWidget(self.radioButton_proxy_automatic)
        self.verticalLayout_proxy_automatic.addWidget(self.lineEdit_proxy_automatic_url)
        self.verticalLayout_10.addLayout(self.verticalLayout_proxy_automatic)
        
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum,
                QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Minimum)

        self.horizontalLayout_save_reset_buttons.addItem(spacerItem2)
        self.horizontalLayout_save_reset_buttons.addWidget(self.pushButton_save)
        self.horizontalLayout_save_reset_buttons.addWidget(self.pushButton_reset)
        self.verticalLayout_4.addLayout(self.horizontalLayout_save_reset_buttons)

    def createComponents(self):
        self.MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow",
            "Sirrix AG - Browser in the Box | Security Policy Manager", None,
            QtGui.QApplication.UnicodeUTF8))
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(531, 629)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindow.sizePolicy().hasHeightForWidth())
        self.MainWindow.setSizePolicy(sizePolicy)
        self.MainWindow.setMaximumSize(QtCore.QSize(531, 629))
        self.MainWindow.setBaseSize(QtCore.QSize(531, 520))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("BitBox.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.MainWindow.setWindowOpacity(1.0)
       
        self.centralwidget = QtGui.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_sirrixLogo = QtGui.QLabel(self.centralwidget)
        self.label_sirrixLogo.setText("")
        self.label_sirrixLogo.setPixmap(QtGui.QPixmap("sirrix_logo.png"))
        self.label_sirrixLogo.setScaledContents(True)
        self.label_sirrixLogo.setObjectName("label_sirrixLogo")

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_informationflow = QtGui.QWidget()
        self.tab_informationflow.setObjectName("tab_informationflow")
        self.tab_network = QtGui.QWidget()
        self.tab_network.setObjectName("tab_network")
        self.tabWidget.addTab(self.tab_informationflow, "")
        self.tabWidget.addTab(self.tab_network, "")
        self.tabWidget.setCurrentIndex(0)
        
        self.groupBox_proxy = QtGui.QGroupBox(self.tab_network)
        self.groupBox_proxy.setObjectName("groupBox_proxy")
        self.groupBox_persistency = QtGui.QGroupBox(self.tab_informationflow)
        self.groupBox_persistency.setObjectName("groupBox_persistency")
        self.radioButton_persistency_all = QtGui.QRadioButton(self.groupBox_persistency)
        self.radioButton_persistency_all.setObjectName("radioButton_persistency_all")
        self.radioButton_persistency_bookmarksonly = QtGui.QRadioButton(self.groupBox_persistency)
        self.radioButton_persistency_bookmarksonly.setObjectName("radioButton_persistency_bookmarksonly")
        
        self.checkBox_print = QtGui.QCheckBox(self.tab_informationflow)
        self.checkBox_print.setObjectName("checkBox_print")
        self.checkBox_print.setText('Drucken aus dem Browser erlauben')
        
        self.radioButton_proxy_none = QtGui.QRadioButton(self.groupBox_proxy)
        self.radioButton_proxy_none.setObjectName("radioButton_proxy_none")
        
        self.radioButton_proxy_static = QtGui.QRadioButton(self.groupBox_proxy)
        self.radioButton_proxy_static.setObjectName("radioButton_proxy_static")
        self.lineEdit_proxy_static_ip = QtGui.QLineEdit(self.groupBox_proxy)
        self.lineEdit_proxy_static_ip.setObjectName("lineEdit_proxy_static_ip")
        self.label_slash_ip_prefix = QtGui.QLabel(self.groupBox_proxy)
        self.label_slash_ip_prefix.setObjectName("label_slash_ip_prefix")
        self.lineEdit_proxy_static_prefix = QtGui.QLineEdit(self.groupBox_proxy)
        self.lineEdit_proxy_static_prefix.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_proxy_static_prefix.setObjectName("lineEdit_proxy_static_prefix")
        
        self.radioButton_proxy_automatic = QtGui.QRadioButton(self.groupBox_proxy)
        self.radioButton_proxy_automatic.setObjectName("radioButton_proxy_automatic")
        self.lineEdit_proxy_automatic_url = QtGui.QLineEdit(self.groupBox_proxy)
        self.lineEdit_proxy_automatic_url.setObjectName("lineEdit_proxy_automatic_url")
        
        self.checkBox_lockproxy = QtGui.QCheckBox(self.tab_network)
        self.checkBox_lockproxy.setObjectName("checkBox_lockproxy")

       
        self.groupBox_DNS = QtGui.QGroupBox(self.tab_network)
        self.groupBox_DNS.setObjectName("groupBox_DNS")
        self.radioButton_dns_windows = QtGui.QRadioButton(self.groupBox_DNS)
        self.radioButton_dns_windows.setObjectName("radioButton_dns_windows")
       
        self.radioButton_dns_static = QtGui.QRadioButton(self.groupBox_DNS)
        self.radioButton_dns_static.setObjectName("radioButton_dns_static")
        self.lineEdit_dns_static_adress = QtGui.QLineEdit(self.groupBox_DNS)
        self.lineEdit_dns_static_adress.setObjectName("lineEdit_dns_static_adress")
        
        
        self.pushButton_save = QtGui.QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_reset = QtGui.QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 19))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)

        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        self.label_description_informationflow.setText(QtGui.QApplication.translate("MainWindow", "Sicherheitseinstellungen für den Datentransfer zwischen Browser und Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_clipboard.setTitle(QtGui.QApplication.translate("MainWindow", "Zwischenablage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_hosttoguest_description.setText(QtGui.QApplication.translate("MainWindow", "Kopieren aus Windows und Einfügen in Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_clipboard_hosttoguest.setItemText(0, QtGui.QApplication.translate("MainWindow", "verbieten", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_clipboard_hosttoguest.setItemText(1, QtGui.QApplication.translate("MainWindow", "Bestätigung durch Benutzer", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_clipboard_hosttoguest.setItemText(2, QtGui.QApplication.translate("MainWindow", "erlauben", None, QtGui.QApplication.UnicodeUTF8))
        self.label_guesttohost_description.setText(QtGui.QApplication.translate("MainWindow", "Kopieren aus Browser und Einfügen in Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_clipboard_guesttohost.setItemText(0, QtGui.QApplication.translate("MainWindow", "verbieten", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_clipboard_guesttohost.setItemText(1, QtGui.QApplication.translate("MainWindow", "Bestätigung durch Benutzer", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_clipboard_guesttohost.setItemText(2, QtGui.QApplication.translate("MainWindow", "erlauben", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_fileflow.setTitle(QtGui.QApplication.translate("MainWindow", "Dateien", None, QtGui.QApplication.UnicodeUTF8))
        self.label_upload_description.setText(QtGui.QApplication.translate("MainWindow", "Hochladen ins Internet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_upload.setItemText(0, QtGui.QApplication.translate("MainWindow", "verbieten", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_upload.setItemText(1, QtGui.QApplication.translate("MainWindow", "Bestätigung durch Benutzer", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_upload.setItemText(2, QtGui.QApplication.translate("MainWindow", "erlauben", None, QtGui.QApplication.UnicodeUTF8))
        self.label_download_description.setText(QtGui.QApplication.translate("MainWindow", "Herunterladen aus dem Internet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_download.setItemText(0, QtGui.QApplication.translate("MainWindow", "verbieten", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_download.setItemText(1, QtGui.QApplication.translate("MainWindow", "Bestätigung durch Benutzer", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_download.setItemText(2, QtGui.QApplication.translate("MainWindow", "Virencheck", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_download.setItemText(3, QtGui.QApplication.translate("MainWindow", "erlauben", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_persistency.setTitle(QtGui.QApplication.translate("MainWindow", "Welche Dateien sollen dauerhaft gespeichert werden?", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_persistency_all.setText(QtGui.QApplication.translate("MainWindow", "Alle (Konfiguration, Lesezeichen)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_persistency_bookmarksonly.setText(QtGui.QApplication.translate("MainWindow", "Nur Lesezeichen", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_persistency_deny.setText(QtGui.QApplication.translate("MainWindow", "Keine", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_informationflow), QtGui.QApplication.translate("MainWindow", "Information flow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_proxy.setTitle(QtGui.QApplication.translate("MainWindow", "Proxy Einstellungen", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_proxy_none.setText(QtGui.QApplication.translate("MainWindow", "Kein Proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_proxy_static.setText(QtGui.QApplication.translate("MainWindow", "Statische Adresse/Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_slash_ip_prefix.setText(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_proxy_automatic.setText(QtGui.QApplication.translate("MainWindow", "Automatische Proxykonfigurations URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_lockproxy.setText(QtGui.QApplication.translate("MainWindow", "Proxy Einstellungen sperren", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_DNS.setTitle(QtGui.QApplication.translate("MainWindow", "DNS Einstellungen", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_dns_windows.setText(QtGui.QApplication.translate("MainWindow", "Einstellungen von Windows übernehmen", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_dns_static.setText(QtGui.QApplication.translate("MainWindow", "Statische Adressen (komma-getrennt)", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_dns_static_adress.setText(QtGui.QApplication.translate("MainWindow", None, None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_network), QtGui.QApplication.translate("MainWindow", "Network", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setText(QtGui.QApplication.translate("MainWindow", "Speichern", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))

