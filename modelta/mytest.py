# -*- coding: utf-8 -*- 
f = open("./core.py", encoding='utf-8')  # ����һ���ļ�����

line = f.readline()  # �����ļ��� readline()����

while line:
    # print(line,)  # ����� ',' �����Ի��з�

    print(line, end='')  # �� Python 3 ��ʹ��

    line = f.readline()

f.close()