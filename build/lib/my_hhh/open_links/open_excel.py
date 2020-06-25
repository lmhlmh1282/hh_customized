import os
import io
import sys
import subprocess
import pandas as pd


#筛选处理，并用命令行打开网页链接
def _get_to_links(sheet,description,browser_filepath):
    ################################################################################
    # apply筛选
    # def is_equal(x,str):
    #     return (x==str)
    # sheet=sheet.loc[sheet['A'].apply(is_equal,args=(description,))].reset_index(drop=True)
    #
    ######################################################################### 
    #筛选，reset_index是为了将索引从0开始。默认筛选后没有变化
    sheet=sheet.loc[(sheet["A"]==description)].reset_index(drop=True)
    # print(sheet)

    #判断dataframe是否为空
    is_empty=(len(sheet.index)==0)
    #print(is_empty)
    #########################################################################
    if(is_empty==True):
        #当前表没有该值，查询为空，啥都不做
        return
    # print(sheet)
    ##########################################################################
    #打开链接
    #运行命令,第0行第B列,注意索引要从0开始
    web_link=sheet["B"][0]
    main_str="{} {}".format(browser_filepath,web_link)
    # print(main_str)
    ##################################################################################
    subprocess.Popen(main_str,shell=True)

#.def


######################
# 给一个excel 文件，然后给某一行的描述，打开对应的链接
# 给一个browser_filepath，用这个来打开链接，一般是浏览器快捷方式地址
# ###########################################################
def open_in_browser(excel_filepath,description,browser_filepath):
    excel_file=pd.ExcelFile(excel_filepath)
    for sheet_name in excel_file.sheet_names:
        #pandas读取数据esheet_name
        sheet=pd.read_excel(excel_filepath,sheet_name=sheet_name,header=None)
        #添加表头 A B C ...     ,'A' is 65
        sheet.columns=[chr(65+i) for i in range(0,sheet.shape[1])]
        #进行处理
        _get_to_links(sheet,description,browser_filepath)
        #释放内存
        del sheet
    del excel_file