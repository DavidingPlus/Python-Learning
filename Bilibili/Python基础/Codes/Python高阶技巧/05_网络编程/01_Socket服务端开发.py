# 1.创建conn对象
import socket
socket_server = socket.socket()

# 2.绑定ip地址
socket_server.bind(("localhost", 8888))

# 3.监听端口
socket_server.listen(1)
# listen接受一个整数参数,表示接受的连接数量

# 4.等待客户端连接
# result: tuple = socket_server.accept()
# conn = result[0]  # 客户端和服务端链接对象
# address = result[1]  # 客户端的地址信息
conn, address = socket_server.accept()
# accept返回的是二元元组,
# 返回 客户端和服务端链接对象 和 客户端的地址信息
# 等待客户端的连接,如果没有客户端连接就等着连接

print(f"接收到了客户端的连接,客户端的信息是: {address}")

# 5.接受客户端信息 使用客户端和服务端的链接对象
data: str = conn.recv(1024).decode("UTF_8")
# recv接受缓存区大小 一般给1024
# 返回值是bytes对象 字节数组,通过UTF-8解码转换为字符串对象
print(f"客户端发来的消息是: {data}")

# 6.发送回复消息
msg = input("请输入您要回复的消息: ").encode("UTF-8")  # 可以将字符串编码为字节数组
conn.send()

# 7.关闭连接
conn.close()
socket_server.close()
