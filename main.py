#!/usr/bin/python
# -*- coding: utf-8 -*-
# Pro-Environment 2019
import pymysql
import configparser
import time
import serial


def print_info(info):
    print("[" + time.strftime("%H:%M:%S", time.localtime()) + " INFO] " + info+"\033[0m")


print_info("Pro Environment Group © 2019")

# 读取配置文件
print("")
print_info("The followings is the information of MySQL Connection:")
# 生成config对象
conf = configparser.ConfigParser()
# 用config对象读取配置文件
conf.read("settings.conf")
# 以列表形式返回所有的section
sections = conf.sections()
print('Sections:', sections)
# 得到指定section的所有option
options = conf.options("MySQL")
print('Options:', options)
# 得到指定section的所有键值对
kvs = conf.items("MySQL")
print("Key-Value Pair List:", kvs)
print_info("End of information.")
print("")

print_info("********** Value List **********")
# 指定section，option读取值
conf_host = conf.get("MySQL", "host")
print_info("Value of MySQL-host = "+conf_host)
conf_port = conf.getint("MySQL", "port")
conf_portstr = conf.get("MySQL", "port")
print_info("Value of MySQL-port = "+conf_portstr+"  \033[7m(Require type: int)\033[0m")
conf_user = conf.get("MySQL", "user")
print_info("Value of MySQL-user = "+conf_user)
conf_passwd = conf.get("MySQL", "passwd")
print_info("Value of MySQL-passwd = "+conf_passwd)
conf_db = conf.get("MySQL", "db")
print_info("Value of MySQL-db = "+conf_db)
conf_table = conf.get("MySQL", "table")
print_info("Value of MySQL-table = "+conf_table)
print_info("************* END *************")

# Arduino串口通信
# 读取配置文件
print("")
print_info("The followings is the information of Arduino Serial Connection:")
# 生成config对象
conf = configparser.ConfigParser()
# 用config对象读取配置文件
conf.read("settings.conf")
# 以列表形式返回所有的section
sections = conf.sections()
print('Sections:', sections)
# 得到指定section的所有option
options = conf.options("Arduino")
print('Options:', options)
# 得到指定section的所有键值对
kvs = conf.items("Arduino")
print("Key-Value Pair List:", kvs)
print_info("End of information.")
print("")

print_info("********** Value List **********")
# 指定section，option读取值
conf_COM = conf.get("Arduino", "COM")
print_info("Value of Arduino-COM = "+conf_COM)
conf_baudRate = conf.getint("Arduino", "baudRate")
conf_baudRatestr = conf.get("Arduino", "baudRate")
print_info("Value of Arduino-baudRate = "+conf_baudRatestr+"  \033[7m(Require type: int)\033[0m")
print_info("************* END *************")

# ser = serial.Serial(conf_COM, conf_baudRate, timeout=0.5)
print_info("Arduino Serial Settings:")
print_info("COM = \033[7m"+conf_COM+"\033[0m; BaudRate = \033[7m"+conf_baudRatestr+
           "\033[0m; Timeout = \033[7m0.5\033[0m")

# 查询远程MySQL数据库
# 创建一个连接对象，再使用创建游标
con = pymysql.connect(host=conf_host, port=conf_port, user=conf_user, passwd=conf_passwd,
                      db=conf_db)
cursor = con.cursor()
print_info("MySQL Server has been connected.")

barcode = input("Type EAN-13 Code > \033[7m ")
print("\033[0m")
# 执行一个SQL语句
sql = "SELECT name,type FROM test WHERE code='" + barcode + "';"
cursor.execute(sql)

# 从游标中取出所有记录放到一个序列中并关闭游标
result = cursor.fetchall()
# print("初步返回值为  "+result)

for dbreturn in result:
    # 注意int类型需要使用str函数转义
    print_info("Original Type = \033[7m"+dbreturn[1])
    print("")
    if dbreturn[1] == "T":
        ResultType = "TEST"
        arduino = 0
    elif dbreturn[1] == "A":
        ResultType = "Plastic"
        arduino = 1
    elif dbreturn[1] == "B":
        ResultType = "Papery"
        arduino = 2
    elif dbreturn[1] == "C":
        ResultType = "Metallic"
        arduino = 3
    print_info("Bar Code = \033[7m"+barcode+"\033[0m; Name = \033[7m"+dbreturn[0]+"\033[0m; Type = \033[7m"+ResultType)
cursor.close()
con.close()
