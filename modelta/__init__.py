# -*- coding: utf-8 -*- 
from ReadFile import *
from mytest import *
from mymath import *
import itertools
import random
import pandas as pd
from tqdm import tqdm

class MultiTree:
    def __init__(self, nodeobj, level:'int'=0, label:str="root"):
        self.nodeobj = nodeobj
        self.left = None
        self.right = None
        self.level = level
        self.label = label
    # 前序遍历,获取按照层级排序的全节点序列�? [node:level]
    def nodes(self,ll={}):
        lll= ll 
        if self.nodeobj is not None:
            lll[self]=self.level
            #print(self.nodeobj,' Level:',self.level,' Label:',self.label)
        if self.left is not None:
            self.left.nodes(lll)
        if self.right is not None:
            self.right.nodes(lll)
        
        lll = sorted(lll.items(), key=lambda item:item[1])
        llist = [[] for i in range(lll[-1][1]+1)]
        for i in lll: 
            llist[i[1]].append(i[0])
        return llist
    # 后序遍历_得到nodeobj:level�?
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.nodeobj is not None:
            print(self.nodeobj,' Level:',self.level,' Label:',self.label)
    # 前序遍历_得到nodeobj:level�?
    def preorder(self):
        if self.nodeobj is not None:
            print(self.nodeobj,' Level:',self.level,' Label:',self.label)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
    # 层序遍历
    def levelorder(self):
        # 返回某个节点的左孩子
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None
        # 返回某个节点的右孩子
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None
        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的数�?
        if self.nodeobj is not None:
            level_order.append([self])
        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操�?, 在level_order中添加节点而不是数�?
            for _ in range(2, height + 1):
                level = []  # 该层的节�?
                for node in level_order[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 如果右孩子非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 如果该层非空，则添加该层
                if level:
                    level_order.append(level)

            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].nodeobj
        return level_order
    # 二叉树的高度
    def height(self):
        # 空的树高度为0, 只有root节点的树高度�?1
        if self.nodeobj is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())
    # 原来的多叉树的叶子节�?
    def leaves(self,ll=[]):
        lll = ll
        if self.nodeobj is None:
            return None
        elif self.left is None and self.right is None:
            #print(self.nodeobj, end=' ')
            lll.append(self)
        elif self.left is None and self.right is not None:
            #print(self.nodeobj, end=' ')
            lll.append(self)
            self.right.leaves(lll)
        elif self.right is None and self.left is not None:
            self.left.leaves(lll)
        else:
            self.left.leaves(lll)
            self.right.leaves(lll)
        return lll
    #生成�?
    def CreatTree(self):
        if(self.nodeobj[0] == '('): #存在括号意味着还没达到叶子结点
            node_list = []
            brackets_num = 0 #括号个数
            node_num = 0 #节点序号
            node_tmp = ''
            for i in self.nodeobj[1:-1]:
                if i == '(':
                    brackets_num +=1
                    node_tmp += i
                elif i == ')':
                    brackets_num -=1
                    node_tmp += i
                elif i == ',' and brackets_num == 0:
                    node_list.append(node_tmp)
                    node_num +=1
                    node_tmp = ''
                else:
                    node_tmp += i
            node_list.append(node_tmp)   
            #print(node_list)    #查看拆分后的节点序列
            self_tmp = self
            for index,item in enumerate(node_list):
                if index == 0:
                #第一个子节点都是父节点的左节�?
                #后续子节点就是上一个子节点的右节点 
                #赋予label
                    label = str(index) if self.label == 'root' else self_tmp.label+','+str(index)    
                    self.left = MultiTree(item,label=label)
                    self = self.left
                    self.CreatTree()
                else:
                    label = str(index) if not ',' in self.label else self_tmp.label+','+str(index)    
                    self.right = MultiTree(item,label=label)
                    self = self.right
                    self.CreatTree()
    #赋层左子树后序遍历找出最大层级d
    def Posorder_Max_Level(self):
        level = self.level;
        while self.right:
            #有右子树就是有兄弟结�?
            level = max(level, self.right.level)
            self = self.right
        return level
    #赋予层级level
    def Level(self):
        if self.left == None: #叶子节点
            self.level = 0
        else:
            self.level = self.left.Posorder_Max_Level()+1
    def Postorder_Level(self):
        if self.left is not None:
            self.left.Postorder_Level()
        if self.right is not None:
            self.right.Postorder_Level()
        if self.nodeobj is not None:
            self.Level()
    #叶子节点个数,需要的是节点下的左节点才正�?
    def leaf_count(self,flag=1):
        if self is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        if flag == 1:
            self = self.left
        if self is None:
            return 1
        if self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.leaf_count(0)
        elif self.right is None and self.left is not None:
            return self.left.leaf_count(0)
        else:
            return self.left.leaf_count(0) + self.right.leaf_count(0)
        
    #总节点个�?
    def node_count(self):
        if self is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is not None and self.right is not None:
            return 1 + self.left.node_count() + self.right.node_count()
        elif self.left is None and self.right is not None:
            return 1 + self.right.node_count()
        elif self.right is None and self.left is not None:
            return 1 + self.left.node_count()
        #else:
            #return self.left.node_count()+ self.right.node_count()
    #获取当前节点一级子节点个数
    def son_count(self):
        self_tmp = self
        son_num = 0
        if self_tmp is None:
            return son_num
        elif self_tmp.left is None:
            return son_num
        elif self_tmp.left is not None:
            son_num += 1
            self_tmp = self_tmp.left
            while self_tmp.right:
                self_tmp = self_tmp.right
                son_num += 1
        return son_num    
    #获取当前节点一级子节点self
    def son(self):
        self_tmp = self
        son_tmp = []
        if self_tmp is None:
            return None
        elif self_tmp.left is None:
            son_tmp.append(self_tmp)
            return son_tmp
        elif self_tmp.left is not None:
            self_tmp = self_tmp.left
            son_tmp.append(self_tmp)
            while self_tmp.right:
                self_tmp = self_tmp.right
                son_tmp.append(self_tmp)
        return son_tmp
    # 中序遍历，得到生成树数据
    def inorder(self,data=[]):
        if self.left is not None:
            self.left.inorder(data)
        if self.nodeobj is not None:
            data.append(self)
        if self.right is not None:
            self.right.inorder(data)
        return data

def Scoredict(lllleaf, llllleaf):
    #������Զ����ɵĻ�
    #�����õ��ѿ�����
    score_dict = {}
    for i in itertools.product(set(lllleaf), set(llllleaf)):
        score_dict[i[0].nodeobj+'_'+i[1].nodeobj] = float(random.randint(-2,2))
    #score_dict[i[0].nodeobj+'_'+i[1].nodeobj] = random.random()/10
    #print(score_dict)

    #�����õ���ͬ�ڵ��ƥ��
    #score_dict = {}
    for i in lllleaf + llllleaf:
        score_dict[i.nodeobj+'_'+i.nodeobj] = 4.
    return score_dict

def loopindex(row,col):
    ll = []
    min_ = min(row,col)
    for i in range(min_):
        for j in range(i):
            ll.append([j,i])
            ll.append([i,j])
        ll.append([i,i])
    if row>col:
        for i in range(col):
            ll.append([row-1,i])
    elif col > row:
        for i in range(row):
            ll.append([i,col-1])
    return ll


def scoremat(TreeSeqFilePath,Name2TypeFilePath,TreeSeqFilePath2,Name2TypeFilePath2):
    TreeSeqType = ReadTreeSeq_Name2Type(TreeSeqFilePath,Name2TypeFilePath)
    TreeSeqType2 = ReadTreeSeq_Name2Type(TreeSeqFilePath2,Name2TypeFilePath2)
    root1 = MultiTree(TreeSeqType)
    root2 = MultiTree(TreeSeqType2)
    root1.CreatTree()
    root1.Postorder_Level()
    lll = root1.nodes({}) #��ά��ʾ
    lllnode = [j for i in lll for j in i]
    lllloop = []
    for i in lll:
        lllloop.append(len(i))
    llldict = {}
    for index,iter in enumerate(lllnode):
        llldict[index] = [lllnode.index(i) for i in iter.son()]

    root2.CreatTree()
    root2.Postorder_Level()
    llll = root2.nodes({}) #��ά��ʾ
    llllnode = [j for i in llll for j in i]
    llllloop = []
    for i in llll:
        llllloop.append(len(i))
    lllldict = {}
    for index,iter in enumerate(llllnode):
        lllldict[index] = [llllnode.index(i) for i in iter.son()]

    score_dict = Scoredict(root1.leaves([]),root2.leaves([]))

    mmatrix = pd.DataFrame([[0.0 for i in range(len(llllnode))] for j in range(len(lllnode))],
                        index=[i.label for i in lllnode],
                        columns=[j.label for j in llllnode])
    mmatrix.index.name = 'Root1' 
    mmatrix.columns.name = 'Root2'
    matrix_values = mmatrix.values

    ttrace = pd.DataFrame([[[] for i in range(len(llllnode))] for j in range(len(lllnode))],
                        index=[i.label for i in lllnode],
                        columns=[j.label for j in llllnode])
    ttrace.index.name = 'Root1' 
    ttrace.columns.name = 'Root2'
    trace_value = ttrace.values
    with tqdm(total=(root1.node_count()*root2.node_count()),desc='Matrix Node') as pbar:
        #ִ��ѭ�й��ɾ���(0,0)(0,1)(1,0)(1,1)(0,2)(2,0)(1,2)(2,1)(2,2)(0,3)(3,0)...(n,m)
        for loop_index in loopindex(root1.level+1,root2.level+1):
            #print(loop_index)
            for i in range(lllloop[loop_index[0]]):
                for j in range(llllloop[loop_index[1]]): 
                    i_index = 0
                    j_index = 0
                    for i_tmp in range(loop_index[0]):
                        i_index += lllloop[i_tmp]
                    i_index+=i
                    for j_tmp in range(loop_index[1]):
                        j_index += llllloop[j_tmp]
                    j_index+=j
                    matrix_tmp = matrix_values[llldict[i_index],:]
                    matrix_tmp = matrix_tmp[:,lllldict[j_index]]

                    matrix_values[i_index][j_index] = GetMaxScore(trace=trace_value,
                                                                    root1=lll[loop_index[0]][i],
                                                                    root2=llll[loop_index[1]][j],
                                                                    allmatrix = matrix_values,
                                                                    root1_index=i_index, 
                                                                    root2_index=j_index, 
                                                                    local_matrix=matrix_tmp,
                                                                    local_matrix_root1_index = llldict[i_index],
                                                                    local_matrix_root2_index = lllldict[j_index], 
                                                                    dict_score=score_dict,
                                                                    Algorithm='')
                    pbar.update(1)
    return(mmatrix)
    #print(ttrace)
    #print(matrix_values[len(lllnode)-1][len(llllnode)-1])
    #self.mp_lst.append(matrix_values[-1][-1])