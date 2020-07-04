import os
import sys
import subprocess
import pymysql
from configparser import ConfigParser

cp = ConfigParser()
cp.read('src\my_hhh\open_links\mysql.conf')
host = cp.get("mysql", "db_host")
port = cp.getint("mysql", "db_port")
user = cp.get("mysql", "db_user")
password = cp.get("mysql", "db_password")
database = cp.get("mysql", "db_database")

#在数据库查询并返回一个记录
def _get_data_from_mysql(description):
    data=None
    # 打开数据库连接
    db = pymysql.connect(host=host,
                        port=port,
                        user=user,
                        password=password,
                        db=database
                     )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT description,link,type FROM my_links where description=%s  limit 1"
    try:
        # 执行SQL语句
        cursor.execute(sql,description)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            description = row[0]
            link1 = row[1]
            type1 = row[2]
            print("description={},link1={},type1={}".format (description,link1,type1))
            data={"description":description,"link":link1,"type":type1}
    except Exception as e:
        print("查询出错：case %s"%e)

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()
    return data
#.def
#筛选处理，并用命令行打开网页链接
def _get_to_links(description,browser_filepath):
   

    data=_get_data_from_mysql(description)#这是要查找并利用的链接
    if(data == None):
        print("未找到结果!")
        return

    main_str="{} {}".format(browser_filepath,data["link"])
    # print(main_str)
    ##################################################################################
    subprocess.Popen(main_str,shell=True)

#.def


######################
# 给一个excel 文件，然后给某一行的描述，打开对应的链接
# 给一个browser_filepath，用这个来打开链接，一般是浏览器快捷方式地址
# ###########################################################
def open_in_browser(description,browser_filepath):
    _get_to_links(description,browser_filepath)


if __name__ == "__main__":
    browser_filepath="D:\\应用\\chrome.lnk"   #用什么打开链接
    excel_file_basename="课程链接.xlsx" #什么excel文件 
    description="数字图像处理【伦斯勒理工学院】（冈萨雷斯第三版）- Introduction to Digita"   #要打开的链接对应的description
    #excel文件夹
    excel_filepath_dir="D:\\临时作业\\temp\\homehomehome\\课程连接"
    #excel地址
    excel_filepath=os.path.join(excel_filepath_dir,excel_file_basename)

    #打开网页链接
    open_in_browser(description,browser_filepath)

   
