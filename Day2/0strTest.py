"""
对于字符串进行的相关操作
注意：对于字符串进行一系列的无论截片等操作都不会对字符串本身造成任何影响
"""

hellopython = "hello" + "python3"
# hellopython = "hellopython3"
print(hellopython)  # hellopython3
'''
对于字符串进行连接操作
'''

hello = hellopython * 3
print(hello)  # hellopython3hellopython3hellopython3

print("hellopython1")
print("hello" + "python2")
print(hellopython)

'''
对于字符串进行分割
注意：
    字符串分割从0开始时，分割出来的子字符串包括头不包括尾部
    字符串从尾部开始分割时 所得的子字符串包括头尾
'''
print(hellopython[:-1])  # hellopython
print(hellopython[0:])  # hellopython3
print(hellopython[0:5])  # hello

# 进阶
# 对于字符串进行逐个输出

for i in hellopython:  # hellopython是一个变量
    print(i, end='')  # 对于hellopython变量进行逐个输出
    # end=''表示输出的每一个字符后不换行
