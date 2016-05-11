# -*- coding: utf-8 -*-
import os
import sys
import platform
import socket
from _winreg import OpenKey, QueryValue, QueryValueEx, SetValueEx, REG_SZ, KEY_ALL_ACCESS,\
        HKEY_LOCAL_MACHINE
from ConfigParser import SafeConfigParser
from PySide import QtCore, QtGui
from gui import Ui_MainWindow

def main(argv):
    app = QtGui.QApplication(argv)
    mainWindow = GUIMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

class GUIMainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, *args):
        QtGui.QMainWindow.__init__(self, *args)
        Ui_MainWindow.__init__(self, self)
        self.mode = QtGui.QApplication.arguments()[2]
        self.create_connects_for_proxy_editing()
        self.set_registry_path()
        if self.mode == "admin":
            if self.get_bitbox_install_path():
                self.set_bitbox_current_settings()
            else:
                self.set_default_policy()
            self.MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow",
            "Security Policy Manager - Administrator Mode", None, QtGui.QApplication.UnicodeUTF8))
            self.create_load_button()
            self.create_connects_admin_mode()
        else:
            if self.get_bitbox_install_path():
                self.MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow",
                    "Security Policy Manager - User Mode", None, QtGui.QApplication.UnicodeUTF8))
                self.create_reset_button()
                self.create_connects_user_mode()
                self.set_bitbox_current_settings()  
            else:
                sys.exit(0)

    def create_reset_button(self):
        self.pushButton_reset = QtGui.QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout_save_reset_buttons.addWidget(self.pushButton_reset)
        self.pushButton_reset.setText("Reset")

    def create_load_button(self):
        self.pushButton_load = QtGui.QPushButton(self.centralwidget)
        self.pushButton_load.setObjectName("pushButton_load")
        self.horizontalLayout_save_reset_buttons.addWidget(self.pushButton_load)
        self.pushButton_load.setText("Laden")

    def set_registry_path(self):
        if platform.machine() == "AMD64":
            self.bitboxreg_main = "SOFTWARE\Wow6432Node\Sirrix AG\BitBox"
        else:
            self.bitboxreg_main = "SOFTWARE\Sirrix AG\BitBox"

        self.bitboxreg_guesttohost_texttohost = "{}{}".format(self.bitboxreg_main, 
                    "\informationFlows\GuestToHost\permissions\\textToHost\\1")
        self.bitboxreg_guesttohost_download = "{}{}".format(self.bitboxreg_main,
                    "\informationFlows\GuestToHost\permissions\download\\1")
        self.bitboxreg_guesttohost_print = "{}{}".format(self.bitboxreg_main,
                    "\informationFlows\GuestToHost\permissions\print\\1")
        self.bitboxreg_hosttoguest_texttoguest = "{}{}".format(self.bitboxreg_main,
                    "\informationFlows\HostToGuest\permissions\\textToGuest\\1")
        self.bitboxreg_hosttoguest_upload = "{}{}".format(self.bitboxreg_main,
                    "\informationFlows\HostToGuest\permissions\upload\\1")
    
    def get_bitbox_install_path(self):
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, self.bitboxreg_main)
            return QueryValueEx(key, 'installDir')[0]
        except WindowsError as e:
            #TODO: Logging maybe??
            if self.mode == 'user':
                result = QtGui.QMessageBox.critical(self, "Registry Fehler",
                    "BitBox Installation wurde nicht gefunden:{}".format(e), QtGui.QMessageBox.Ok)
            else:
                return None

    def set_registry_value(self, subkey, value):
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, subkey,0, KEY_ALL_ACCESS)
            SetValueEx(key, "type", None, REG_SZ, value)
        except WindowsError as e:
            result = QtGui.QMessageBox.critical(self, "Registry Fehler",
                    u"Registry speichern fehgeschlagen für: {1}\n{0}".format(e, subkey),
                    QtGui.QMessageBox.Ok)

    def get_bitbox_setting_value(self, subkey):
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, subkey)
            return QueryValueEx(key, 'type')[0]
        except WindowsError as e:
            result = QtGui.QMessageBox.critical(self, "Registry Fehler",
                    u"Registry lesen fehgeschlagen für: {1}\n{0}".format(e, subkey),
                    QtGui.QMessageBox.Ok)

    def get_bitbox_tomini(self):
        parser = SafeConfigParser()
        bitboxinstalldir = self.get_bitbox_install_path() 
        parser.read("{}\\{}".format(bitboxinstalldir, 'BitBoxTOM.ini'))
        return parser

    def set_default_policy(self):
        self.comboBox_clipboard_guesttohost.setCurrentIndex(2)
        self.comboBox_clipboard_hosttoguest.setCurrentIndex(2)
        self.comboBox_upload.setCurrentIndex(2)
        self.comboBox_download.setCurrentIndex(3)
        self.checkBox_print.setChecked(True)
        self.radioButton_persistency_all.setChecked(True)

        self.radioButton_proxy_none.setChecked(True)
        self.radioButton_dns_windows.setChecked(True)

        self.change_automatic_proxy_inputfield_state()
        self.change_dns_servers_inputfield_state()
        self.change_static_proxy_inputfield_state()

    def set_bitbox_loaded_settings(self, filename):
        parser = SafeConfigParser()
        parser.read(filename)
        for section in parser.sections():
            for k,v in parser.items(section):
                if section == "network":
                    for k,v in parser.items(section):
                        if k == "proxy":
                            if v == "static":
                                self.radioButton_proxy_static.setChecked(True)
                                self.lineEdit_proxy_static_ip.setText(parser.get(section, "address"))
                                self.lineEdit_proxy_static_prefix.setText(parser.get(section, "port"))
                            elif v == "automatic":
                                self.radioButton_proxy_automatic.setChecked(True)
                                self.lineEdit_proxy_automatic_url.setText(parser.get(section, "url"))
                            else:
                                self.radioButton_proxy_none.setChecked(True)
                        elif k == "dns":
                            if v == "dhcp":
                                self.radioButton_dns_windows.setChecked(True)
                            elif v == "static":
                                self.radioButton_dns_static.setChecked(True)
                                self.lineEdit_dns_static_adress.setText(parser.get(section, "servers"))
                        elif k == "lock":
                            if v == "true":
                                self.checkBox_lockproxy.setChecked(True)
                            else:
                                self.checkBox_lockproxy.setChecked(False)
                else:
                    if k == "printing":
                        if v == "true":
                            self.checkBox_print.setChecked(True)
                        else:
                            self.checkBox_print.setChecked(False)
                    elif k == "download":
                        if v == "allow":
                            self.comboBox_download.setCurrentIndex(3)
                        elif v == "askUser":
                            self.comboBox_download.setCurrentIndex(1)
                        elif v == "checkVirus":
                            self.comboBox_download.setCurrentIndex(2)
                        else:
                            self.comboBox_download.setCurrentIndex(0)
                    elif k == "upload":
                        if v == "allow":
                            self.comboBox_upload.setCurrentIndex(2)
                        elif v == "askUser":
                            self.comboBox_upload.setCurrentIndex(1)
                        else:
                            self.comboBox_upload.setCurrentIndex(0)
                    elif k == "persistentdata":
                        if v == "all":
                            self.radioButton_persistency_all.setChecked(True)
                        elif v == "bookmarksonly":
                            self.radioButton_persistency_bookmarksonly.setChecked(True)
                        else:
                            self.radioButton_persistency_deny.setChecked(True)
                    elif k == "clipboard_guesttohost":
                        if v == "allow":
                            self.comboBox_clipboard_guesttohost.setCurrentIndex(2)
                        elif v == "askUser":
                            self.comboBox_clipboard_guesttohost.setCurrentIndex(1)
                        else:
                            self.comboBox_clipboard_guesttohost.setCurrentIndex(0)
                    elif k == "clipboard_hosttoguest":
                        if v == "allow":
                            self.comboBox_clipboard_hosttoguest.setCurrentIndex(2)
                        elif v == "askUser":
                            self.comboBox_clipboard_hosttoguest.setCurrentIndex(1)
                        else:
                            self.comboBox_clipboard_hosttoguest.setCurrentIndex(0)

    def set_bitbox_current_settings(self):
        bitboxsetting_guesttohost_texttohost = \
                self.get_bitbox_setting_value(self.bitboxreg_guesttohost_texttohost)
        bitboxsetting_guesttohost_download = \
                self.get_bitbox_setting_value(self.bitboxreg_guesttohost_download)
        bitboxsetting_guesttohost_print = \
                self.get_bitbox_setting_value(self.bitboxreg_guesttohost_print)
        bitboxsetting_hosttoguest_texttoguest = \
                self.get_bitbox_setting_value(self.bitboxreg_guesttohost_texttohost)
        bitboxsetting_hosttoguest_upload = \
                self.get_bitbox_setting_value(self.bitboxreg_hosttoguest_upload)

        parsed_bitbox_tomini = self.get_bitbox_tomini()

        """Policy: Persitent Data"""
        if parsed_bitbox_tomini.get('user', 'persistentdata') == 'all':
            self.radioButton_persistency_all.setChecked(True)
        elif parsed_bitbox_tomini.get('user', 'persistentdata') == 'bookmarksonly':
            self.radioButton_persistency_bookmarksonly.setChecked(True)
        else:
            self.radioButton_proxy_none.setChecked(True)

        """Policy: Host to Guest"""
        #Clipboard host to guest
        if bitboxsetting_hosttoguest_texttoguest == "allow":
            self.comboBox_clipboard_hosttoguest.setCurrentIndex(2)
        elif bitboxsetting_hosttoguest_texttoguest == "askUser":
            self.comboBox_clipboard_hosttoguest.setCurrentIndex(1)
        else:
            self.comboBox_clipboard_hosttoguest.setCurrentIndex(0)

        #Upload host to guest
        if bitboxsetting_hosttoguest_upload == "allow":
            self.comboBox_upload.setCurrentIndex(2)
        elif bitboxsetting_hosttoguest_upload == "askUser":
            self.comboBox_upload.setCurrentIndex(1)
        else:
            self.comboBox_upload.setCurrentIndex(0)
        
        """Policy: Guest to Host"""
        #Clipboard guest to host
        if bitboxsetting_guesttohost_texttohost == "allow":
            self.comboBox_clipboard_guesttohost.setCurrentIndex(2)
        elif bitboxsetting_hosttoguest_texttoguest == "askUser":
            self.comboBox_clipboard_guesttohost.setCurrentIndex(1)
        else:
            self.comboBox_clipboard_guesttohost.setCurrentIndex(0)

        #Guest to host Download
        if bitboxsetting_guesttohost_download == "allow":
            self.comboBox_download.setCurrentIndex(3)
        elif bitboxsetting_guesttohost_download == "askUser":
            self.comboBox_download.setCurrentIndex(1)
        elif bitboxsetting_guesttohost_download == "checkVirus":
            self.comboBox_download.setCurrentIndex(2)
        else:
            self.comboBox_download.setCurrentIndex(0)

        #Guest to host Printing
        if bitboxsetting_guesttohost_print == "allow":
            self.checkBox_print.setChecked(True)
        else:
            self.checkBox_print.setChecked(False)

        """Network Policy"""
        #Policy: Proxy
        if parsed_bitbox_tomini.get("proxy", "proxy") == "automatic":
            self.radioButton_proxy_automatic.setChecked(True)
            self.lineEdit_proxy_automatic_url.setText(parsed_bitbox_tomini.get("proxy", "url"))
            self.lineEdit_proxy_static_ip.setDisabled(True)
            self.lineEdit_proxy_static_prefix.setDisabled(True)
        elif parsed_bitbox_tomini.get("proxy", "proxy") == "manual":
            self.radioButton_proxy_static.setChecked(True)
            self.lineEdit_proxy_static_ip.setText(parsed_bitbox_tomini.get("proxy", "address"))
            self.lineEdit_proxy_static_prefix.setText(parsed_bitbox_tomini.get("proxy", "port"))
            self.lineEdit_proxy_automatic_url.setDisabled(True)
        else:
            self.radioButton_proxy_none.setChecked(True)
            self.lineEdit_proxy_static_ip.setDisabled(True)
            self.lineEdit_proxy_static_prefix.setDisabled(True)
            self.lineEdit_proxy_automatic_url.setDisabled(True)

        if parsed_bitbox_tomini.get("proxy", "lock") == "true":
            self.checkBox_lockproxy.setCheckState(QtCore.Qt.CheckState.Checked)

        #Policy: DNS
        if parsed_bitbox_tomini.get("dns", "type") == "static":
            self.radioButton_dns_static.setChecked(True)
            self.lineEdit_dns_static_adress.setText(parsed_bitbox_tomini.get("dns", "servers"))
        else:
            self.radioButton_dns_windows.setChecked(True)
            self.lineEdit_dns_static_adress.setDisabled(True)
         
    
    def write_bitbox_config_to_registry(self):
        if self.checkBox_print.isChecked():
            self.set_registry_value(self.bitboxreg_guesttohost_print, "allow")
        else:
            self.set_registry_value(self.bitboxreg_guesttohost_print, "deny")

        if self.comboBox_download.currentIndex() == 0:
            self.set_registry_value(self.bitboxreg_guesttohost_download, "deny")
        elif self.comboBox_download.currentIndex() == 1:
            self.set_registry_value(self.bitboxreg_guesttohost_download, "askUser")
        elif self.comboBox_download.currentIndex() == 2:
            self.set_registry_value(self.bitboxreg_guesttohost_download, "checkVirus")
        else:
            self.set_registry_value(self.bitboxreg_guesttohost_download, "allow")

        if self.comboBox_upload.currentIndex() == 0:
            self.set_registry_value(self.bitboxreg_hosttoguest_upload, "deny")
        elif self.comboBox_upload.currentIndex() == 1:
            self.set_registry_value(self.bitboxreg_hosttoguest_upload, "askUser")
        else:
            self.set_registry_value(self.bitboxreg_hosttoguest_upload, "allow")

        if self.comboBox_clipboard_guesttohost.currentIndex() == 0:
            self.set_registry_value(self.bitboxreg_guesttohost_texttohost, "deny")
        elif self.comboBox_clipboard_guesttohost.currentIndex() == 1:
            self.set_registry_value(self.bitboxreg_guesttohost_texttohost, "askUser")
        else:
            self.set_registry_value(self.bitboxreg_guesttohost_texttohost, "allow")

        if self.comboBox_clipboard_hosttoguest.currentIndex() == 0:
            self.set_registry_value(self.bitboxreg_hosttoguest_texttoguest, "deny")
        elif self.comboBox_clipboard_hosttoguest.currentIndex() == 1:
            self.set_registry_value(self.bitboxreg_hosttoguest_texttoguest, "askUser")
        else:
            self.set_registry_value(self.bitboxreg_hosttoguest_texttoguest, "allow")

    def write_bitbox_config_to_tomini(self):
        parser = self.get_bitbox_tomini()
        parser.sections()
        
        if self.radioButton_proxy_static.isChecked():
            parser.set("proxy", "proxy", "manual")
            parser.set("proxy", "address", self.lineEdit_proxy_static_ip.text())
            parser.set("proxy", "port", self.lineEdit_proxy_static_prefix.text())
            parser.set("proxy", "url", "")
        elif self.radioButton_proxy_automatic.isChecked():
            parser.set("proxy", "proxy", "automatic")
            parser.set("proxy", "url", self.lineEdit_proxy_automatic_url.text())
            parser.set("proxy", "address", "")
            parser.set("proxy", "port", "")
        elif self.radioButton_proxy_none.isChecked():
            parser.set("proxy", "proxy", "none")
            parser.set("proxy", "address", "")
            parser.set("proxy", "port", "")
            parser.set("proxy", "url", "")
        if self.radioButton_dns_windows.isChecked():
            parser.set("dns", "type", "dhcp")
            parser.set("dns", "servers", "8.8.8.8,8.8.4.4")
        elif self.radioButton_dns_static.isChecked():
            parser.set("dns", "type", "static")
            parser.set("dns", "servers", self.lineEdit_dns_static_adress.text())
        
        if self.checkBox_lockproxy.isChecked():
            parser.set("proxy", "lock", "true")
        else:
            parser.set("proxy", "lock", "false")

        bitboxtomini_path = "{}\\{}".format(self.get_bitbox_install_path(), "BitBoxTOM.ini")
        with open(bitboxtomini_path, "w") as tomini:
            parser.write(tomini)
            

    def save_bitbox_config_to_registry_and_tomini(self):
        result = QtGui.QMessageBox.question(self, "Speichern",\
                u"Sind Sie sicher, dass Sie speichern möchten?",\
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if result is QtGui.QMessageBox.Yes:
            try:
                self.write_bitbox_config_to_registry()
                if self.verify_ip(self.lineEdit_proxy_static_ip.text()):
                    self.write_bitbox_config_to_tomini()
                    QtGui.QMessageBox.information(self, "Speichern",
                        "Konfiguration wurde gespeichert!", QtGui.QMessageBox.Ok)
                else:
                    result = QtGui.QMessageBox.question(self, "Statischer Proxy",\
                    u"Die eingegebene IP Addresse ist ungültig, möchten Sie dennoch speichern?",\
                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                    if result is QtGui.QMessageBox.No:
                        self.lineEdit_proxy_static_ip.setFocus()
                    else:
                        self.write_bitbox_config_to_tomini()
                        QtGui.QMessageBox.information(self, "Speichern",\
                                "Konfiguration wurde gespeichert!", QtGui.QMessageBox.Ok)

            except (WindowsError, IOError) as e:
                QtGui.QMessageBox.critical(self, "Speichern fehlgeschlagen", "{}".format(e),
                        QtGui.QMessageBox.Ok)

    def save_bitbox_config_to_ini(self):
        parser = SafeConfigParser()
        parser.add_section('informationflow')
        if self.radioButton_persistency_all.isChecked():
            parser.set('informationflow', 'persistentdata', 'all')
        elif self.radioButton_persistency_bookmarksonly.isChecked():
            parser.set('informationflow', 'persistentdata', 'bookmarksonly')
        else:
            parser.set('informationflow', 'persistentdata', 'none')
        
        if self.checkBox_print.isChecked():
            parser.set('informationflow', 'printing', 'true')
        else:
            parser.set('informationflow', 'printing', 'false')

        if self.comboBox_download.currentIndex() == 0:
            parser.set('informationflow', 'download', 'deny')
        elif self.comboBox_download.currentIndex() == 1:
            parser.set('informationflow', 'download', 'askUser')
        elif self.comboBox_download.currentIndex() == 2:
            parser.set('informationflow', 'download', 'checkVirus')
        else:
            parser.set('informationflow', 'download', 'allow')

        if self.comboBox_upload.currentIndex() == 0:
            parser.set('informationflow', 'upload', 'deny')
        elif self.comboBox_upload.currentIndex() == 1:
            parser.set('informationflow', 'upload', 'askUser')
        else:
            parser.set('informationflow', 'upload', 'allow')

        if self.comboBox_clipboard_guesttohost.currentIndex() == 0:
            parser.set('informationflow', 'clipboard_guesttohost', 'deny')
        elif self.comboBox_clipboard_guesttohost.currentIndex() == 1:
            parser.set('informationflow', 'clipboard_guesttohost', 'askUser')
        else:
            parser.set('informationflow', 'clipboard_guesttohost', 'allow')

        if self.comboBox_clipboard_hosttoguest.currentIndex() == 0:
            parser.set('informationflow', 'clipboard_hosttoguest', 'deny')
        elif self.comboBox_clipboard_hosttoguest.currentIndex() == 1:
            parser.set('informationflow', 'clipboard_hosttoguest', 'askUser')
        else:
            parser.set('informationflow', 'clipboard_hosttoguest', 'allow')

        parser.add_section('network')
        
        if self.radioButton_proxy_automatic.isChecked():
            parser.set('network', 'proxy', 'automatic')
            parser.set('network', 'url', self.lineEdit_proxy_automatic_url.text())
        elif self.radioButton_proxy_static.isChecked():
            if self.verify_ip(self.lineEdit_proxy_static_ip.text()):
                parser.set('network', 'proxy', 'static')
                parser.set('network', 'address', self.lineEdit_proxy_static_ip.text())
                parser.set('network', 'port', self.lineEdit_proxy_static_prefix.text())
            else:
                result = QtGui.QMessageBox.question(self, "Statischer Proxy",\
                u"Die eingegebene IP Addresse ist ungültig, möchten Sie dennoch speichern?",\
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                if result is QtGui.QMessageBox.Yes:
                    parser.set('network', 'proxy', 'static')
                    parser.set('network', 'address', self.lineEdit_proxy_static_ip.text())
                    parser.set('network', 'port', self.lineEdit_proxy_static_prefix.text())
                else:
                    return
        else:
            parser.set('network', 'proxy', 'none')
        parser.set('network', 'lock', str(self.checkBox_lockproxy.isChecked()).lower())

        if self.radioButton_dns_static.isChecked():
            parser.set('network', 'dns', 'static')
            parser.set('network', 'servers', self.lineEdit_dns_static_adress.text())
        else:
            parser.set('network', 'dns', 'dhcp')

        self.save_policy_file(parser)
                    
    def save_policy_file(self, parser):
        try:
            dest = QtGui.QFileDialog.getSaveFileName(self, u"Datei Speichern", None,\
                    u"Policies (*.policy)")
            if all(dest):
                filename = unicode(dest[0])
                policy_file = open(filename, 'w')
                parser.write(policy_file)
                policy_file.close()
                QtGui.QMessageBox.information(self, "Speichern", "Konfiguration wurde gespeichert!",
                    QtGui.QMessageBox.StandardButton)
        except IOError as e:
            print e
            result = QtGui.QMessageBox.critical(self, "Fehler",
                    "{}".format(e), QtGui.QMessageBox.Ok)
            if result == QtGui.QMessageBox.Ok:
                self.set_bitbox_current_settings()

    def change_static_proxy_inputfield_state(self):
        if self.radioButton_proxy_static.isChecked():
            self.lineEdit_proxy_static_ip.setDisabled(False)
            self.lineEdit_proxy_static_prefix.setDisabled(False)
        else:
            self.lineEdit_proxy_static_ip.setDisabled(True)
            self.lineEdit_proxy_static_prefix.setDisabled(True)

    def change_automatic_proxy_inputfield_state(self):
        if self.radioButton_proxy_automatic.isChecked():
            self.lineEdit_proxy_automatic_url.setDisabled(False)
        else:
            self.lineEdit_proxy_automatic_url.setDisabled(True)

    def change_dns_servers_inputfield_state(self):
        if self.radioButton_dns_windows.isChecked():
            self.lineEdit_dns_static_adress.setDisabled(True)
        else:
            self.lineEdit_dns_static_adress.setDisabled(False)
    
    def verify_ip(self, ip):
        try:
            socket.inet_aton(ip)
            return True
        except:
            return False

    def verify_proxy_static_ip(self):
        if not self.verify_ip(self.lineEdit_proxy_static_ip.text()):
            result = QtGui.QMessageBox.question(self, "Statischer Proxy",\
                u"Die eingegebene IP Addresse ist ungültig, möchten Sie dennoch speichern?",\
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if result is QtGui.QMessageBox.No:
                self.lineEdit_proxy_static_ip.setFocus()
        
    def create_connects_for_proxy_editing(self):
        self.radioButton_proxy_static.toggled.connect(self.change_static_proxy_inputfield_state)
        self.radioButton_proxy_automatic.toggled.connect(self.change_automatic_proxy_inputfield_state) 
        self.radioButton_dns_windows.toggled.connect(self.change_dns_servers_inputfield_state)

    def create_connects_user_mode(self):
        self.pushButton_save.clicked.connect(self.save_config)
        self.pushButton_reset.clicked.connect(self.reset_options)
    
    def create_connects_admin_mode(self):
        self.pushButton_save.clicked.connect(self.save_config)
        self.pushButton_load.clicked.connect(self.load_config)

    """
    Slots optimieren die Speichverwaltung von Qt und beschleunigt somit
    die Ausführung der Slots.
    """
    @QtCore.Slot()
    def save_config(self):
        if self.mode == "user":
            self.save_bitbox_config_to_registry_and_tomini()
        else:
            self.save_bitbox_config_to_ini()

    @QtCore.Slot()
    def load_config(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, u"Policy öffnen", None,\
                u"Policy(*.policy)")
        if all(filename):
            filename = unicode(filename[0])
            self.set_bitbox_loaded_settings(filename)

    @QtCore.Slot()
    def reset_options(self):
        self.set_bitbox_current_settings()


if __name__ == '__main__':
    main(sys.argv)
