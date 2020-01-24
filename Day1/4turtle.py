import turtle
# 调用turtle库

# 对画笔的位置、大小、颜色进行限定

turtle.penup()# 乌龟把尾巴抬起 在纸面上不留下任何痕迹
turtle.goto(0,20) # 命令乌龟前往坐标为（0，20）的位置等待命令
turtle.pendown()# 让乌龟放下尾巴 准备开始作画
turtle.pensize(10)# 对乌龟的尾巴粗细进行调整
turtle.pencolor('green')# 对乌龟尾巴上的颜料进行调整

# 绘画8边形（转角角度为45°）360/8=45
for i in range(8):# 0-7
    turtle.fd(100) # fd->forward 前进 fd(100)就是前进100个单位
    turtle.right(45)# 向右转45°
# 上八边形
for i in range(8):# 0-7
    turtle.fd(100)
    turtle.left(45) # 向左转45°
# 下八边形

# # 绘画三角形（转角的角度为120°）360/3=120
# for i in range(3):
#     turtle.fd(100)
#     turtle.right(120)
# # 上三角
#
# for i in range(3):
#     turtle.fd(100)
#     turtle.left(120)
# # 下三角
