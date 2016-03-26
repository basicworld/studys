#!/usr/bin/python
#-*- encoding:utf-8 -*-
import os
import xlrd
import xlwt
import docx
from xlutils.copy import copy as xlcopy
import subprocess
import time

def init_env():
    #need to used after job down
    #file to read docx
    count=0

    #file to output result
    dir_output=r'/var/ftpadmin/forwenjie/file_output'
    try :
        os.chdir(dir_output)
        count+=1
    except OSError:
        subprocess.call(r'mkdir -p /var/ftpadmin/forwenjie/file_ouput',shell=True)
        timestamp=time.time()
        f=open('/var/ftpadmin/forwenjie/file_output/run.log','a')
        f.write('warning:dir_output be inited @ %s'%timestamp)
        f.close()

    #file to read docx
    dir_input=r'/var/ftpadmin/forwenjie/file_input'
    try:
        os.chdir(dir_input)
        count+=1
    except OSError,oser:
        subprocess.call(r'mkdir -p /var/ftpadmin/forwenjie/file_input',shell=True)
        timestamp=time.time()
        f=open('/root/SHELL/word_to_excel_for_wenjie/run.log','a')
        f.write('warning:dir_input be inited @ %s'%timestamp)
        f.close()

    #init readme
    #copy readme from @backfile

    return count

def read_all_docx_in():
    #read all docx and return(docx_lists[])
    docx_lists=[]
    dir_input=r'/var/ftpadmin/forwenjie/file_input'
    #try:
    for parent,dirnames,filenames in os.walk(dir_input):
        docx_lists+=(filenames)
    return docx_lists
    #except:
    #    timestamp=time.time()
    #    f=open('/root/SHELL/word_to_excel_for_wenjie/run.log','a')
    #    f.write('error:readlists error! @ %s'%timestamp)
    #    f.close()
    #return []
def read_one_docx(filename):
    #return write_list[],write_dict{}
    #tables[0]
    #0,1:<name>:0;0,3:<birth>:2;
    #1,1:<sex>:1;1,3:<city>
    #2,1:<birth_city>;2,3:<hobby>
    #7,0:<tel><phone>:7<email>:8
    dir_input=r'/var/ftpadmin/forwenjie/file_input'
    if not os.chdir(dir_input):os.chdir(dir_input)
    read_list=[(0,1),(0,3),(1,1),(1,3),(2,1),(2,3),(7,0)]
    #0<name>,1<sex>,2<birth>,7<phont>,8<email>
    write_list=['name','birth','sex','city','birth_city','hobby','tel','phone','email',]
    write_values=[]
    write_dict={}
    #filename='伏英娜.docx'
    document=docx.Document(filename)
    table=document.tables[0]
    for i in read_list:
        write_values.append(table.cell(i[0],i[1]).text)
    uni=write_values[len(write_values)-1]
    write_values.pop()
    tel_left_index=uni.index('联系电话'.decode('utf8'))
    tel_right_index=uni.index('手机'.decode('utf8'))
    tel=uni[tel_left_index+5:tel_right_index].strip()

    phone_right_index=uni.index('mail')
    phone=uni[tel_right_index+3:phone_right_index-1].strip()
    '''right_index1=uni.index('.com')+4
    right_index2=uni.index('.cn')+3
    if right_index1>=right_index2: email_right_index=right_index1
    else:email_right_index=right_index2'''
    email_right_index=uni.index('通讯'.decode('utf8'))
    email=uni[phone_right_index+5:email_right_index].strip()

    #write_values=write_values+split_cell_0700(uni)
    write_values.append(tel)
    write_values.append(phone)
    write_values.append(email)
    for i,key in enumerate(write_values):
        write_dict[i]=key

    return write_dict
    '''
    name=return_cell_text(0,1)
    sex=return_cell_text(1,1)
    birth=return_cell_text(0,3)
    city=return_cell_text(1,3)
    (tel,phone,email)=return_cell_text(7,0)

    temp_list=[]
    temp_list.append(name)
    tem'''

def write_one_docx(row,write_dict):
    write_list=['name','birth','sex','city','birth_city','hobby','tel','phone','email']
    template_file='/var/ftpadmin/forwenjie/template/template.xlsx'
    rb=xlrd.open_workbook(template_file)
    wb=xlcopy(rb)
    sheet=wb.get_sheet(0)
    sheet.write(row,0,write_dict[0])
    sheet.write(row,2,write_dict[2])
    sheet.write(row,1,write_dict[1])
    sheet.write(row,7,write_dict[7])
    sheet.write(row,8,write_dict[8])
    wb.save('/var/ftpadmin/forwenjie/file_output/output.xls')
    #name,sex,birth,phone,email


def read_docx_and_write():
    #use read_all_docx_in,and write to excel one by one
    #write logs if error
    files=read_all_docx_in()

    if files==[]:
        return 404
    else:
        template_file='/var/ftpadmin/forwenjie/template/template.xlsx'
        rb=xlrd.open_workbook(template_file)
        wb=xlcopy(rb)
        sheet=wb.get_sheet(0)
        #row=0
        for index,file in enumerate(files):
            write_dict=read_one_docx(file)
            #write_one_docx(index+1,write_dict)
            sheet.write(index+1,0,write_dict[0])
            sheet.write(index+1,2,write_dict[2])
            sheet.write(index+1,1,write_dict[1])
            sheet.write(index+1,7,write_dict[7])
            sheet.write(index+1,8,write_dict[8])
        wb.save('/var/ftpadmin/forwenjie/file_output/output.xls')

    #return (row+1,)

if __name__=='__main__':
    init_env()
    count_error=read_docx_and_write()

