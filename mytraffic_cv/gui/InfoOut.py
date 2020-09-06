import os, sys
from os.path import split
import csv
from time import sleep,gmtime

import xlsxwriter
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import gui.PATH as PATH


class InfoOut:
    """信息导出gui功能实现类"""
    def __init__(self, wnd):
        self.wnd = wnd
        self.ui = wnd.ui
        self.ui.comboBox.addItems(['Excel文件', 'Txt文件'])
        self.ui.Out.clicked.connect(self.out)

    def out(self):  
        choic_item = self.ui.comboBox.currentText()
        dirpath = ''
        if PATH.bool_alltimes == True:                      #若为所有时间
            crutime = gmtime()
            VedioDate = str(crutime.tm_year) + "所有时间"
        else:                                               #若为特定时间段
            try:
                time = PATH.get_VedioDate()
                print(time)
                timelist = time.split('_')
                VedioDate = timelist[6]+'_'+timelist[2]+'_'+timelist[3]
            except:
                crutime = gmtime()
                VedioDate = str(crutime.tm_year) + "_" + str(crutime.tm_mon) + "_" + str(crutime.tm_mday)
           

        with open(PATH.run_a_red_lightpath(), 'r', encoding='UTF-8') as fp:
            data = []
            data_dict = {}
            data = fp.readlines()
            if '\n' in data:
                data.remove('\n')
            data_row = len(data)
            for i in range(data_row):
                plate_number, ilegal_type = data[i].split(' ')   
                ilegal_type = ilegal_type.replace('\n','')
                data_dict[plate_number] = ilegal_type

        if choic_item == 'Excel文件':
            dirpath = QFileDialog.getSaveFileName(self.wnd, '选择保存路径', PATH.DeskTop_path + PATH.get_roadname() + "_" + VedioDate + '.xlsx', 'xlsx(*.xlsx)')

            if dirpath[0] != '':
                row, col = 1, 0
                workbook = xlsxwriter.Workbook(dirpath[0])
                worksheet = workbook.add_worksheet('违法记录')
                title = ['车牌号码', '违法类型']
                worksheet.write(0, 0, title[0])
                worksheet.write(0, 1, title[1])
                for key in data_dict:
                    worksheet.write(row, col, key)
                    worksheet.write(row, col + 1, data_dict[key])
                    row = row + 1
                workbook.close()
            else:
                return
            #退出窗口
            self.ui.Quit.click()

        elif choic_item == 'Txt文件':   
            dirpath = QFileDialog.getSaveFileName(self.wnd, '选择保存路径', PATH.DeskTop_path + PATH.get_roadname() + "_" + VedioDate + '.txt', 'Text Files(*.txt)')
            if dirpath[0] != '':
                with open(dirpath[0], 'w', newline='', encoding='UTF-8') as txt_file:
                    title = ['车牌号码 ', '违法类型\n']
                    txt_file.writelines(title)
                    txt_file.writelines(data)
            else:
                return
            #退出窗口
            self.ui.Quit.click()
        try:
            os.system(dirpath[0])
        except:
            box = QMessageBox.information(self.wnd, "提示", "创建文件失败", QMessageBox.Yes)




        
        
        


