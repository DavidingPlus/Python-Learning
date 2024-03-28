from pymysql import Connection

# 构建到mysql数据库的链接
conn = Connection(
    host="localhost",  # 主机名 IP
    port=3306,  # 端口
    user="root",  # 账户
    password="05121428"  # 密码
)
# print(conn.get_server_info())

cursor = conn.cursor()  # 获取游标对象
conn.select_db("sys")  # 选择数据库
# # 1.执行非查询性质SQL
# cursor.execute("create table test_pymysql(id int)")
# 2.执行查询性质SQL
cursor.execute("select * from student")
results: tuple[tuple] = cursor.fetchall()
for r in results:
    print(r)

# 关闭连接
conn.close()
