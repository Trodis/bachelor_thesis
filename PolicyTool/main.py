# -*- coding: utf-8 -*-
import sys
import platform
from _winreg import OpenKey, QueryValue, QueryValueEx, SetValueEx, REG_SZ, HKEY_LOCAL_MACHINE
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
        self.set_registry_path()
        self.set_bitbox_current_settings()
        self.create_connects()

    def set_registry_path(self):
        if platform.machine() == "AMD64":
            self.bitboxreg_main = "SOFTWARE\Wow6432Node\Sirrix AG\BitBox"
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
        else:
            #TODO: Need to check on x86 Windows how the reg path is
            pass
    
    def get_bitbox_install_path(self):
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, self.bitboxreg_main)
            return QueryValueEx(key, 'installDir')[0]
        except WindowsError as e:
            #TODO: Logger would be better!
            result = QtGui.QMessageBox.critical(self, "Registry Fehler",
                    "{}".format(e), QtGui.QMessageBox.Ok)
            if result == QtGui.QMessageBox.Ok:
                sys.exit(0)

    def set_registry_value(self, subkey, value):
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, subkey)
            SetValueEx(key, "type", None, REG_SZ, value)
        except WindowsError as e:
            result = QtGui.QMessageBox.critical(self, "Registry Fehler",
                    "{}".format(e), QtGui.QMessageBox.Ok)
            if result == QtGui.QMessageBox.Ok:
                sys.exit(0)

    def get_bitbox_setting_value(self, subkey):
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, subkey)
            return QueryValueEx(key, 'type')[0]
        except WindowsError as e:
            result = QtGui.QMessageBox.critical(self, "Registry Fehler",
                    "Auf die Registry konnte nicht zugegriffen werden", QtGui.QMessageBox.Ok)
            if result == QtGui.QMessageBox.Ok:
                sys.exit(0)

    def get_bitbox_tomini_settings(self):
        parser = SafeConfigParser()
        bitboxinstalldir = self.get_bitbox_install_path() 
        parser.read("{}\\{}".format(bitboxinstalldir, 'BitBoxTOM.ini'))
        return parser

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

        parsed_bitbox_tomini = self.get_bitbox_tomini_settings()

        """Policy: Persitent Data"""
        if parsed_bitbox_tomini.get('user', 'persistentdata') == 'all':
            self.radioButton_persistency_all.toggle()
        elif parsed_bitbox_tomini.get('user', 'persistentdata') == 'bookmarksonly':
            self.radioButton_persistency_bookmarksonly.toggle()
        else:
            self.radioButton_proxy_none.toggle()

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
            self.checkBox_print.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.checkBox_print.setCheckState(QtCore.Qt.CheckState.Checked)

        #Policy: Proxy
        if parsed_bitbox_tomini.get("proxy", "proxy") == "automatic":
            self.radioButton_proxy_automatic.toggle()
            self.lineEdit_proxy_automatic_url.setText(parsed_bitbox_tomini.get("proxy", "url"))
        elif parsed_bitbox_tomini.get("proxy", "proxy") == "manual":
            self.radioButton_proxy_static.toggle()
            self.lineEdit_proxy_static_ip.setText(parsed_bitbox_tomini.get("proxy", "address"))
            self.lineEdit_proxy_static_prefix.setText(parsed_bitbox_tomini.get("proxy", "port"))
        else:
            self.radioButton_proxy_none.toggle()

        if parsed_bitbox_tomini.get("proxy", "lock") == "true":
            self.checkBox_lockproxy.setCheckState(QtCore.Qt.CheckState.Checked)

        #Policy: DNS
        if parsed_bitbox_tomini.get("dns", "type") == "static":
            self.radioButton_dns_static.toggle()
            self.lineEdit_dns_static_adress.setText(parsed_bitbox_tomini.get("dns", "servers"))
        else:
            self.radioButton_dns_windows.toggle()
         
    def create_connects(self):
        self.pushButton_save.clicked.connect(self.save_configfile)
        self.pushButton_reset.clicked.connect(self.reset_options)
    
    """
    Slots optimieren die Speichverwaltung von Qt und beschleunigt somit
    die Ausführung der Slots.
    """
    @QtCore.Slot()
    def write_bitbox_registry_config(self):
        if self.radioButton_persistency_all.isChecked():
            pass


    @QtCore.Slot()
    def save_configfile(self):
        bitboxinstalldir = self.get_bitbox_install_path()
        
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
            parser.set('network', 'proxy', self.lineEdit_proxy_automatic_url.text())
        elif self.radioButton_proxy_static.isChecked():
            parser.set('network', 'proxy', 'static')
            parser.set('network', 'address', self.lineEdit_proxy_static_ip.text())
            parser.set('network', 'port', self.lineEdit_proxy_static_prefix.text())
        else:
            parser.set('network', 'proxy', 'none')
        parser.set('network', 'lock', str(self.checkBox_lockproxy.isChecked()))

        if self.radioButton_dns_static.isChecked():
            parser.set('network', 'dns', 'static')
            parser.set('network', 'servers', self.lineEdit_dns_static_adress.text())
        else:
            parser.set('network', 'dns', 'dhcp')

        try:
            result = QtGui.QMessageBox.question(self, "Speichern",\
                        "Sind Sie sicher, dass Sie speichern möchten?",\
                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if result == QtGui.QMessageBox.Yes:
                bitbox_cfgfile = open("{}\\{}\\{}".format(bitboxinstalldir,
                    'SetupData', 'UserConfig.policy'), 'w')
                parser.write(bitbox_cfgfile)
                bitbox_cfgfile.close()
                QtGui.QMessageBox.information(self, "Speichern", "Konfiguration wurde gespeichert!",
                        QtGui.QMessageBox.StandardButton)
        except IOError as e:
            print e
            result = QtGui.QMessageBox.critical(self, "Fehler",
                    "{}".format(e), QtGui.QMessageBox.Ok)
            if result == QtGui.QMessageBox.Ok:
                self.set_bitbox_current_settings()



    @QtCore.Slot()
    def reset_options(self):
        self.set_bitbox_current_settings()


if __name__ == '__main__':
    main(sys.argv)
