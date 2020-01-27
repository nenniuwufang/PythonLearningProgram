ls = []
dict = {"name": "小明", "age": 20, "sex": "male"}

# file = open("./Test.txt",'r',encoding='utf-8')
# 只读文件 若文件不存在 则程序会报错
file = open("readfile.txt", 'w', encoding='utf-8')
# 写文件 若文件不存在 则创建一个文件到当前目录下
# file = open("readfile.txt",'r+',encoding='utf-8')
# 读+写文件，在读文件的前提下对于文件进行追加写操作

# 将列表中的元素逐个写入文件中
ls = ['1', '2', '3', '4', '5']
for i in ls:
    fileopen = file.write(i + "\n")  # 向文件中逐个写入列表名为ls的列表变量
else:
    # 此处else当且仅当for语句执行完毕时才会执行else中的内容
    # 若for循环没有执行完毕 则else中的语句将不会执行
    print("数据写入成功！")
# writelines write三者中有本质上的区别 注意！！！
file.close()
