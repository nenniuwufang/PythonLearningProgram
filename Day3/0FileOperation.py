ls = []

# file = open("./Test.txt",'r',encoding='utf-8')
# 只读文件 若文件不存在 则程序会报错
file = open("readfile.txt",'w',encoding='utf-8')
# 写文件 若文件不存在 则创建一个文件到当前目录下
# file = open("readfile.txt",'r+',encoding='utf-8')
# 读+写文件，在读文件的前提下对于文件进行追加写操作

ls = [1,2,3,4,5]

fileopen = file.writelines(ls)# 向文件中写入列表名为ls的列表变量
#writelines writeline write三者中有本质上的区别 注意！！！

