import numpy as np
import imageio
import os
import random
import matplotlib.pyplot as plt

# 道路长度v，根据题目为500m，单位：元胞（每个元胞长度为5m）
v = 500 // 5

# 运行时间T，设置为1000步
T = 1000

# 生成概率prob_create，根据题目为0.4，以模拟密度为80辆车/km
# prob_create = 车辆密度 * 元胞长度 / 1000
prob_create = 0.4

# 减速概率prob_slowdown，这里设置为生成概率的一半，为0.2
prob_slowdown = 0.2

# 最大速度maxspeed，这里设置为30km/h，即6个元胞/步
maxspeed = 30

# 车辆状态color
color = np.zeros(v)

# 初始化车辆速度，-1表示无车，初始状态无车
speed = np.ones(v) * (-1)


# 状态更新过程
def update(color, speed):
    i = 0
    while i < v and speed[i] == -1:
        i = i + 1
    while i < v:
        p = random.random()
        if p <= prob_slowdown and speed[i] > 0:
            speed[i] = speed[i] - 1
        elif speed[i] < maxspeed:
            speed[i] = speed[i] + 1
        inext = i + 1
        while inext < v and speed[inext] == -1:
            inext = inext + 1
        if inext < v:
            if speed[i] >= inext - i:
                speed[i] = inext - i - 1
        if speed[i] > 0:
            if i + speed[i] < v:
                ni = int(i + speed[i])
                speed[ni] = speed[i]
                color[ni] = color[i]
            speed[i] = -1
            color[i] = 0
        i = inext
    p = random.random()
    if p <= prob_create and speed[0] == -1:
        speed[0] = random.randint(1, maxspeed)
        color[0] = 1
    return color, speed


# 将每步的交通图合并为GIF动图
def create_gif(img_dir, image_list, gif_name, duration):
    frames = []
    for image_name in image_list:
        print("image_name={0} img_dir={1}".format(image_name, img_dir))
        frames.append(imageio.imread(img_dir + '/' + image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


# 仿真循环
for i in range(T):
    nc = np.zeros((121, v, 3))
    for j in range(3):
        nc[59, :, j] = color
        nc[60, :, j] = color
        nc[61, :, j] = color
    color, speed = update(color, speed)
    plt.imsave("images\\" + str(i) + '.png', nc)

img_dir = './images'
duration = 0.05
image_list = os.listdir(img_dir + '/')
gif_name = img_dir + '.gif'
create_gif(img_dir, image_list, gif_name, duration)
