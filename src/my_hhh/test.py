import os
from hh_customized.open_links import open_excel




if __name__ == "__main__":
    browser_filepath="D:\\应用\\chrome.lnk"   #用什么打开链接
    excel_file_basename="课程链接.xlsx" #什么excel文件 
    description="数字图像处理【伦斯勒理工学院】（冈萨雷斯第三版）- Introduction to Digita"   #要打开的链接对应的description
    #excel文件夹
    excel_filepath_dir="D:\\临时作业\\temp\\homehomehome\\课程连接"
    #excel地址
    excel_filepath=os.path.join(excel_filepath_dir,excel_file_basename)

    #打开链接
    open_excel.open_in_browser(excel_filepath,description,browser_filepath)