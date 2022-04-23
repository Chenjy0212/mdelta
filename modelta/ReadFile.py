# -*- coding: utf-8 -*- 
import os
import sys

# 读取 .nwk类文件并把谱系树中的节点名称转换为类型
# 例如   (a1,b7); ---> (a,b);
def ReadTreeSeq_Name2Type(TreeSeqFilePath, Name2TypeFilePath):
    if TreeSeqFilePath[-1] == '/' or Name2TypeFilePath[-1] == '/':
        print('文件夹路径末尾不能加/')
        return

    file1= open(TreeSeqFilePath,encoding='utf-8') #读取到文本的所有内容
    content=file1.read()
    #print(content)
    file2= open(Name2TypeFilePath,encoding='utf-8')
    file2.readline() #跳过第一行
    while True:
        text_line = file2.readline().replace('\n', '')
        if text_line:
            #print(len(text_line), text_line)
            name2type = text_line.split(',', 1 )
            #print(name2type)
            name = name2type[0]
            ctype = name2type[1]
            #print('name:',name,'\t','type:',type)
            content = content.replace(name, ctype)
            #print(content)
        else:
            break
    #print(content)
    return content.replace(';', '')





