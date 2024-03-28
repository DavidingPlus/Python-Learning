from pymysql import Connection

# 构建到mysql数据库的链接
conn = Connection(
    host="localhost",  # 主机名 IP
    port=3306,  # 端口
    user="root",  # 账户
    password="05121428",  # 密码
    autocommit=True  # 设置自动确认!!!!!!
)
# print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("sys")
# 执行SQL
cursor.execute("insert into student values(10001,'林俊杰',31,'男')")
# conn.commit()  # 需要确认才能改变数据!!!!

# 关闭连接
conn.close()
