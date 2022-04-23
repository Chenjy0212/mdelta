# -*- coding: utf-8 -*- 
f = open("./core.py", encoding='utf-8')  # 返回一个文件对象

line = f.readline()  # 调用文件的 readline()方法

while line:
    # print(line,)  # 后面跟 ',' 将忽略换行符

    print(line, end='')  # 在 Python 3 中使用

    line = f.readline()

f.close()