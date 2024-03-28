# threading模块
import time


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == "__main__":
    # sing()
    # dance()
    import threading
    # Thread参数列表 target线程名 args以元组形式传参 kargs以字典形式传参
    sing_thread = threading.Thread(target=sing, args=(
        "我要唱歌,哈哈哈",))  # 需要带上括号表示是元组!!! # 创建唱歌线程
    dance_thread = threading.Thread(
        target=dance, kwargs={"msg": "我在跳舞,啦啦啦"})  # 创建跳舞线程
    sing_thread.start()
    dance_thread.start()
