'''
Created on 2018. 06. 07.
@author: Administrator
'''

# -*- coding: utf-8 -*-
#!/usr/bin/env python

from PyQt5 import QtCore, QtWidgets
import requests
import xml.etree.ElementTree as ET
import cmAxlConfig

CM_IP = cmAxlConfig.CM_IP
CM_ID = cmAxlConfig.CM_ID
CM_PW = cmAxlConfig.CM_PW
VER_LIST = cmAxlConfig.VER_LIST
MENU_LIST = cmAxlConfig.MENU_LIST
QUERY_DIC = cmAxlConfig.QUERY_DIC
HEADER_DIC = cmAxlConfig.HEADER_DIC
BODY_DIC = cmAxlConfig.BODY_DIC
     
def getSelectList(menu_text): 
    print('function >>>>> getSelectList() > menu_text : '+menu_text)
    query = QUERY_DIC[menu_text]
    column_header = HEADER_DIC[menu_text]
    column_body = BODY_DIC[menu_text]
    print('query >>>>> '+query)
    print('column_header >>>>> '+str(column_header))
    print('column_body >>>>> '+str(column_body))
    
    try:
        soapRequest, soapHeader = getSoapReqMessage(query)
        AXLResponse = requests.post('https://'+ui.lineEdit_ip.text()+'/axl/', data = soapRequest, headers = soapHeader, 
                                verify = False, auth=(ui.lineEdit_id.text(), ui.lineEdit_pw.text()))
    
        print(AXLResponse.text)
        root = ET.fromstring(AXLResponse.text)
        row_list = root.iter('row')           
        
    except:
        print('Except >>>>> ')
        print('Status: %s ' % AXLResponse.text)        
   
    return column_header, column_body, row_list

    
def getSoapReqMessage(query):
    version = ui.comboBox_ver.currentText()
    soapRequest = ' <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" '
    soapRequest += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
    soapRequest += 'xmlns:xsd="http://www.w3.org/2001/XMLSchema"> '
    soapRequest += '  <SOAP-ENV:Body>'
    soapRequest += '    <axlapi:executeSQLQuery xmlns:axlapi="http://www.cisco.com/AXL/API/'+version+'" sequence="1234">'
    soapRequest += '      <sql>'+query+'</sql>'
    soapRequest += '    </axlapi:executeSQLQuery>'
    soapRequest += '  </SOAP-ENV:Body>'
    soapRequest += '</SOAP-ENV:Envelope>'
    
    soapHeader = {
        'Content-type' : 'text/xml charset=UTF-8', 
        'SOAPAction' : 'CUCM:DB ver='+version+' executeSQLQuery'
    }
    
    return soapRequest, soapHeader



        
class Ui_CM_AXL(object):
    def setupUi(self, CM_AXL):
        CM_AXL.setObjectName('CM_AXL')
        CM_AXL.setWindowModality(QtCore.Qt.ApplicationModal)
        CM_AXL.setEnabled(True)
        CM_AXL.resize(1200, 600)
        self.groupBox = QtWidgets.QGroupBox(CM_AXL)
        self.groupBox.setGeometry(QtCore.QRect(9, 10, 1180, 580))
        self.groupBox.setObjectName('groupBox')
        
        self.tabWidget = QtWidgets.QTabWidget(CM_AXL)
        self.tabWidget.setGeometry(QtCore.QRect(310, 30, 865, 548))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)  
        self.tabWidget.setObjectName('tabWidget')
       
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 280, 150))
        self.formLayoutWidget.setObjectName('formLayoutWidget')
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName('formLayout')
        
        self.label_ip = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ip.setObjectName('label_ip')
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_ip)
        
        
        self.label_id = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id.setObjectName('label_id')
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_id)
        
        self.label_pw = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_pw.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pw.setObjectName('label_pw')
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_pw)
        
        self.label_ver = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_ver.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ver.setObjectName('label_ver')
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_ver)        
        
        self.label_menu = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_menu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_menu.setObjectName('label_menu')
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_menu)  
      
               
        #form input
        self.lineEdit_ip = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_ip.setObjectName('lineEdit_ip')
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ip)
        
        self.lineEdit_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_id.setObjectName('lineEdit_id')
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_id)
        
        self.lineEdit_pw = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pw.setObjectName('lineEdit_pw')
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_pw)
                
        self.comboBox_ver = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_ver.setObjectName('comboBox_ver')
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_ver)
        
        self.comboBox_menu = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_menu.setObjectName('comboBox_menu')
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_menu)
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(85, 170, 130, 30))
        self.horizontalLayoutWidget.setObjectName('horizontalLayoutWidget')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName('horizontalLayout')
        
        self.pushButton_submit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_submit.setObjectName('pushButton_submit')
        self.pushButton_submit.clicked.connect(self.clickSubmit)
        self.horizontalLayout.addWidget(self.pushButton_submit)
        
        
        self.formLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.lineEdit_pw.raise_()

        self.retranslateUi(CM_AXL)
        QtCore.QMetaObject.connectSlotsByName(CM_AXL)

    def retranslateUi(self, CM_AXL):
        _translate = QtCore.QCoreApplication.translate
        CM_AXL.setWindowTitle(_translate('CM_AXL', 'cmAxlPyQt'))
        self.groupBox.setTitle(_translate('CM_AXL', 'CM_AXL'))
        self.label_ip.setText(_translate('CM_AXL', 'IP'))
        self.label_id.setText(_translate('CM_AXL', 'ID'))
        self.label_pw.setText(_translate('CM_AXL', 'PW'))
        self.label_ver.setText(_translate('CM_AXL', 'Ver'))
        self.label_menu.setText(_translate('CM_AXL', 'MEMU'))
        self.lineEdit_ip.setText(CM_IP)
        self.lineEdit_id.setText(CM_ID)
        self.lineEdit_pw.setText(CM_PW)
        for ver in VER_LIST:
            self.comboBox_ver.addItem(ver)
            
        #self.comboBox_menu.addItem('Device', '1')
        for menu in MENU_LIST:
            self.comboBox_menu.addItem(menu)
            
        self.pushButton_submit.setText(_translate('CM_AXL', 'Submit'))
        #self.pushButton_clear.setText(_translate('CM_AXL', 'Clear'))

    
     
    def clickSubmit(self):
        #self.menu_id = self.comboBox_menu.itemData(self.comboBox_menu.currentIndex())
        self.menu_text = self.comboBox_menu.currentText()
        
        tab_count = self.tabWidget.count()
        print('tab_count : '+str(tab_count))
        self.tab = QtWidgets.QWidget()        
        
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(8, 10, 845, 500))
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setObjectName('tableWidget')
        
        
        #column_head, column_body, row_list = getSelectList(self.menu_id)
        column_head, column_body, row_list = getSelectList(self.menu_text)
        
        result_list = []
        for row in row_list:
            result_list.append(row)
        
        #column setting
        self.tableWidget.setColumnCount(len(column_head))
        self.tableWidget.setRowCount(len(result_list))
        for i, column in enumerate(column_head):            
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            self.tableWidget.horizontalHeaderItem(i).setText(column)
                
        for y, row in enumerate(result_list):
            #print(y)          
            for x, key in enumerate(column_body):
                item = QtWidgets.QTableWidgetItem()                
                self.tableWidget.setItem(y, x, item)
                self.tableWidget.item(y, x).setText(row.find(key).text)
                
                
        self.tabWidget.setCurrentWidget(self.tab)       
        self.tabWidget.addTab(self.tab, self.menu_text)
        self.tabWidget.setCurrentIndex(tab_count)       
        
        
    def closeTab(self, index):
        tab = self.tabWidget.widget(index)
        tab.deleteLater()
        self.tabWidget.removeTab(index)
   
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CM_AXL = QtWidgets.QWidget()
    ui = Ui_CM_AXL()
    ui.setupUi(CM_AXL)
    CM_AXL.show()
    sys.exit(app.exec_())
    