# Pro-Environment
import pymysql, time

# 创建一个连接对象，再使用创建游标
con = pymysql.connect(host='45.119.209.222', port=3306, user='RaspPI', passwd='RaspPI',
                      db='Pro_Environment')
cursor = con.cursor()
print("["+time.strftime("%H:%M:%S", time.localtime())+" INFO] "+"已连接至MySQL数据库！")

code = input("输入键值code --> ")
# 执行一个SQL语句
sql = "SELECT name,type FROM test WHERE code='" + code + "';"
cursor.execute(sql)

# 从游标中取出所有记录放到一个序列中并关闭游标
result = cursor.fetchall()
# print("初步返回值为  "+result)

for d in result :
    # 注意int类型需要使用str函数转义
    print("["+time.strftime("%H:%M:%S", time.localtime())+" INFO] "+"获取到的Type代号为  "+d[1])
    if d[1] == "T":
        ResultType = "测试"
    elif d[1] == "A":
        ResultType = "塑料"
    elif d[1] == "B":
        ResultType = "纸"
    elif d[1] == "C":
        ResultType = "金属"
    print("["+time.strftime("%H:%M:%S", time.localtime())+" INFO] "+"Code= "+code+' ; Name= '+d[0]+" ; Type= "+ResultType)
cursor.close()
con.close()
