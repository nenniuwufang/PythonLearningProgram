a = "helloworld123"
# print(a) 输出字符串a
# for i in a:
#     print(i,end=' ') 逐个输出字符串a中的字符并使用空格隔开
# for i in range(10):
#     print(i) 逐行输出0-9共10个数字
# while True:
#     print(a) 死循环 重复打印a

a = 789
b = 1.23
c = b*b
# print("{:.2f}".format(c)) # print->1.51
# print("{1:.1f},{0:.2f}".format(c,b)) # 先输出b 再输出c（按照人为给定的打印顺序）
# print("{:.1f},{:.2f}".format(c,b))
print("{:}".format(a)) # print(a)
print("{:f}".format(a)) # print(float(a))此处的float为数值类型 单精度浮点数
