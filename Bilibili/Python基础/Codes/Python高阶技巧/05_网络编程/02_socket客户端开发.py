# 创建socket对象
import socket
socket_client = socket.socket()
# 连接到服务器
socket_client.connect(("localhost", 8888))
# 发送消息
socket_client.send("你好呀".encode("UTF-8"))
# 接受返回消息
recv_data = socket_client.recv(1024)  # 1024是缓冲区的大小 一般1024即可,同样recv方法是阻塞的
print(f"服务端回复的消息是: {recv_data.decode('UTF-8')}")
# 关闭连接
socket_client.close()
