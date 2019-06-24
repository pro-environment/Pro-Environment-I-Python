#!/usr/bin/python
# -*- coding: utf-8 -*-
# Pro-Environment 2019
import pymysql
import configparser
import time


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
conf_db = conf.get("MySQL", "db")
print_info("Value of MySQL-db = "+conf_db)
conf_table = conf.get("MySQL", "table")
print_info("Value of MySQL-table = "+conf_table)
print_info("************* END *************")

# 先输入个密码再说好不好？
print("")
passwd = input("Insect Password >>")
# 打开数据库连接
db = pymysql.connect(host=conf_host, port=conf_port, user="insect", passwd=passwd, db=conf_db)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 手动输入一堆东西，以后改自动读串口
inputcode = input("Code >>")
inputname = input("Name >>")
inputtype = input("Type >>")

# SQL 插入语句
sql = "INSERT INTO "+conf_table+" (code, name, type) VALUES ('"+inputcode+"', '"+inputname+"', '"+inputtype+"');"
# 打印一下语句方便查BUG
print_info("Your SQL sentence is: "+sql)
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()
print_info("It seems to have succeeded!")
# 关闭数据库连接
db.close()
# 这下面还能写啥？没啦！！
