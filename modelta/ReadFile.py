# -*- coding: utf-8 -*- 
import itertools
import csv
from itertools import islice
import math

# 读取 .nwk类文件并把谱系树中的节点名称转换为类�?
# 例如   (a1,b7); ---> (a,b);
def ReadTreeSeq_Name2Type(TreeSeqFilePath, Name2TypeFilePath):
    file1= open(TreeSeqFilePath,encoding='utf-8') #读取到文本的所有内�?
    content=file1.read()
    #print(content)
    file2= open(Name2TypeFilePath,encoding='utf-8')
    file2.readline() #跳过第一�?
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

def ReadTreeSeq(TreeSeqFilePath):
    file1= open(TreeSeqFilePath,encoding='utf-8') #读取到文本的所有内�?
    content=file1.read()
    #print(content)
    return content.replace(';', '')

def Scoredict(lllleaf, llllleaf, mv:float):
    score_dict = {}
    #for i in itertools.product(set(lllleaf), set(llllleaf)):
    #    score_dict[i[0].nodeobj+'_'+i[1].nodeobj] = float(random.randint(-2,2))
    #score_dict[i[0].nodeobj+'_'+i[1].nodeobj] = random.random()/10
    #print(score_dict)

    #score_dict = {}
    for i in lllleaf:
        score_dict[i.nodeobj+'_'+i.nodeobj] = float(mv)
    for i in llllleaf:
        score_dict[i.nodeobj+'_'+i.nodeobj] = float(mv)
    return score_dict

def reverseScore(Score, matchScore:float):
    #Score =matchScore-log(Score+1,math.e)
    Score =matchScore-(Score**0.5)
    return Score

def QuantitativeScoreFile(lllleaf, llllleaf, mv, ScoreFile, matchScore = -999.):
    score_dict={}
    for i in lllleaf:
        score_dict[i.nodeobj+'_'+i.nodeobj] = float(mv)
    for i in llllleaf:
        score_dict[i.nodeobj+'_'+i.nodeobj] = float(mv)
    typeXn_dict = {}
    csv_reader=csv.reader(open(ScoreFile,encoding='utf-8'))
    for row in islice(csv_reader, 1, None): #跳过第一行名称信�?
        #print(row)
        if len(row) == 3:
            score_dict[row[0]+ '_' + row[1]] = float(row[2])
            score_dict[row[1]+ '_' + row[0]] = float(row[2])
        else:
            typeXn_dict[row[0]]=row[1:]
        #print(list(typeXn_dict.keys()))
        for i in itertools.product(list(typeXn_dict.keys()), list(typeXn_dict.keys())):
            #print(i[0]+ '_' + i[1])
            # cmath.sqrt() 返回的是complex复数形式，不利于计算
            score_dict[i[0]+ '_' + i[1]] = reverseScore(sum((abs(float(a)**2-float(b)**2)**0.5) for a,b in zip(typeXn_dict[i[0]],typeXn_dict[i[1]])),math.ceil(len(row)**0.5) if matchScore==-999. else matchScore)
    return score_dict

## ================== add by lzz ========================
def leafLable_to_celltype_info(node_list):
    # get root1 leaves' new label to celltype infos
    labels = []
    celltypes = []
    for each_node in node_list:
        if "(" not in each_node.nodeobj:
            labels.append(each_node.label)
            celltypes.append(each_node.nodeobj)
    ## conver to strings
    
    return ";".join(labels), ";".join(celltypes)