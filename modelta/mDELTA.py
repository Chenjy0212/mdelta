# -*- coding: utf-8 -*- 

from ReadFile import *
from mytest import *
from mymath import *
from auxi import *
import pandas as pd
import argparse
from copy import *
import random
from multiprocessing import *
import multiprocessing as mp
import psutil

parser = argparse.ArgumentParser(prog='MODELTA', description = ' Multi fork Development cell lineage tree alignment',epilog = 'Developer: Yang Lab(https://www.labxing.com/profile/10413), Details: https://github.com/Chenjy0212/modelta')
parser.add_argument('TreeSeqFile',type=str, help='[path/filename] Cell lineage tree file with branch length information removed.')
parser.add_argument('TreeSeqFile2',type=str, help='[path/filename] Cell lineage tree file with branch length information removed.')
parser.add_argument('-nt','--Name2TypeFile',type=str, default='', help='[path/filename] Convert tree node name to type.')
parser.add_argument('-nt2','--Name2TypeFile2',type=str, default='', help='[path/filename] Convert tree node name to type.')
parser.add_argument('-sd','--ScoreDictFile',type=str, default='', help='[path/filename] Defines the score of matches between nodes.')
parser.add_argument('-t','--top',type=int, default=0, help='[int > 0] Select the top few meaningful scores in the score matrix.')
parser.add_argument('-m','--mv',type=float, default=2., help=' [float] The matching score between the same nodes.')
parser.add_argument('-p','--pv',type=float, default=-1., help=' [float] The prune score between the different nodes.')
parser.add_argument('-T','--Tqdm',type=int, default=1, help=' [0(off) or 1(on)] Whether to display the operation progress bar.')
parser.add_argument('-n','--notebook',type=int, default=0, help='[0(off) or 1(on)] Is it written and run in the jupyter notebook environment.')
parser.add_argument('-P','--Pvalue',type=int, default=0, help='[int > 0] The number of times the original sequence needs to be disrupted.')
parser.add_argument('-a','--Alg',type=str, default='KM', help='[KM / GA] Represent KM algorithm and GA algorithm respectively to find the maximum value of each node of the score matrix')
parser.add_argument('-c','--CPUs',type=int, default=50, help='[int > 0] Multi process computing can greatly reduce the waiting time. The default process pool is 50, but limited by local computer resources, it can reach the maximum number of local CPU cores - 1.')

args = parser.parse_args() #开始解析参数 --对于可选参数来说

TreeSeqFile = args.TreeSeqFile
TreeSeqFile2 = args.TreeSeqFile2
Name2TypeFile = args.Name2TypeFile
Name2TypeFile2 = args.Name2TypeFile2
ScoreDictFile = args.ScoreDictFile
top = args.top
pv = args.pv
mv = args.mv
Tqdm = args.Tqdm
notebook = args.notebook
Alg = args.Alg
times = args.Pvalue
CPUs = args.CPUs

class MultiTree:
    def __init__(self, nodeobj:str, level:'int'=0, label:str="root"):
        self.nodeobj = nodeobj if nodeobj[-1] != ';' else nodeobj[:-1]
        self.left = None
        self.right = None
        self.level = level
        self.label = label
    # 前序遍历,获取按照层级排序的全节点序列对 [node:level]
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
    # 后序遍历_得到nodeobj:level对
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.nodeobj is not None:
            print(self.nodeobj,' Level:',self.level,' Label:',self.label)
    # 前序遍历_得到nodeobj:level对
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
        # 是否添加根节点中的数据
        if self.nodeobj is not None:
            level_order.append([self])
        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 璇ュ眰鐨勮妭鐐?
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
        # 空的树高度为0, 只有root节点的树高度为1
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
    # 原来的多叉树的叶子节点
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
    #生成树
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
                #第一个子节点都是父节点的左节点
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
            #有右子树就是有兄弟结点
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
    #叶子节点个数,需要的是节点下的左节点才正确
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
        
    #总节点个数
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

def scoremat(TreeSeqFile:str, 
            TreeSeqFile2:str, 
            Name2TypeFile:str = '',
            Name2TypeFile2:str = '', 
            ScoreDictFile:str = '', 
            top:int = 0,
            pv:float = -1.,
            mv:float = 2.,
            Alg:str = 'KM',
            Tqdm:int = 1,
            notebook:int = 0):
    if Name2TypeFile != '':
        TreeSeqType = ReadTreeSeq_Name2Type(TreeSeqFile,Name2TypeFile)
        TreeSeqOri = ReadTreeSeq(TreeSeqFile)
    else:
        TreeSeqType = ReadTreeSeq(TreeSeqFile)
        TreeSeqOri = ReadTreeSeq(TreeSeqFile)

    if Name2TypeFile2 != '':
        TreeSeqType2 = ReadTreeSeq_Name2Type(TreeSeqFile2,Name2TypeFile2)
        TreeSeqOri2 = ReadTreeSeq(TreeSeqFile2)
    else:
        TreeSeqType2 = ReadTreeSeq(TreeSeqFile2)
        TreeSeqOri2 = ReadTreeSeq(TreeSeqFile2)

    root1 = MultiTree(TreeSeqType)
    root2 = MultiTree(TreeSeqType2)
    oroot1 = MultiTree(TreeSeqOri)
    oroot2 = MultiTree(TreeSeqOri2)

    root1.CreatTree()
    root1.Postorder_Level()
    lll = root1.nodes({}) #二维表示
    lllnode = [j for i in lll for j in i]

    oroot1.CreatTree()
    oroot1.Postorder_Level()
    olll = oroot1.nodes({}) #二维表示
    olllnode = [j for i in olll for j in i]

    lllloop = []
    for i in lll:
        lllloop.append(len(i))
    llldict = {}
    for index,iter in enumerate(lllnode):
        llldict[index] = [lllnode.index(i) for i in iter.son()]

    root2.CreatTree()
    root2.Postorder_Level()
    llll = root2.nodes({}) #二维表示
    llllnode = [j for i in llll for j in i]

    oroot2.CreatTree()
    oroot2.Postorder_Level()
    ollll = oroot2.nodes({}) #二维表示
    ollllnode = [j for i in ollll for j in i]

    llllloop = []
    for i in llll:
        llllloop.append(len(i))
    lllldict = {}
    for index,iter in enumerate(llllnode):
        lllldict[index] = [llllnode.index(i) for i in iter.son()]

    if ScoreDictFile == '': 
        score_dict = Scoredict(root1.leaves([]),root2.leaves([]), mv)
    else:
        score_dict = QuantitativeScoreFile(ScoreDictFile)

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
    if Tqdm == 1:
        if notebook == 1:
            from tqdm.notebook import tqdm
        else:
            from tqdm import tqdm
        with tqdm(total=(root1.node_count()*root2.node_count()),desc='Matrix Node') as pbar:
            #执行循有规律就是(0,0)(0,1)(1,0)(1,1)(0,2)(2,0)(1,2)(2,1)(2,2)(0,3)(3,0)...(n,m)
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
                                                                        Algorithm=Alg,
                                                                        prune=pv,)
                        pbar.update(1)
    else:
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
                                                                        Algorithm=Alg,
                                                                        prune=pv,)
    
    if top == 0: #默认情况下
        T1root_T2root = []
        T1root_T2root.append({'Score':matrix_values[-1][-1],
                            'Root1_label':root1.label, 
                            'Root1_node':root1.nodeobj,
                            'Root1_seq':oroot1.nodeobj,
                            'Root2_label':root2.label, 
                            'Root2_node':root2.nodeobj, 
                            'Root2_seq':oroot2.nodeobj, 
                            'row':root1.node_count()-1, 
                            'col':root2.node_count()-1})

        return({'matrix':mmatrix, 'T1root_T2root':T1root_T2root})
    elif top > 0 and top < min(root1.node_count(), root2.node_count()):

        def changemat(rac, tracemat, mat):
            for i in tracemat[tuple(rac)]:
                #print(i[0],root1.leaf_count(), i[1],root2.leaf_count())
                if i == [] or (i[0]<root1.leaf_count() and i[1] <root2.leaf_count()):
                    mat[tuple(i)] = -99999.
                else:
                    mat[tuple(i)] = -99999.
                    #print(i)
                    changemat(i,tracemat,mat)
            return mat

        mat_tmp = deepcopy(matrix_values)
        scorelist=[]
        for _ in range(top):
            #print(mat_tmp)
            maxscore = np.max(mat_tmp),
            del_i_index = np.where(mat_tmp==np.max(mat_tmp))[0][0]
            del_j_index = np.where(mat_tmp==np.max(mat_tmp))[1][0]
            #scorelist.append([np.max(mat_tmp),mat.index[del_i_index],mat.columns[del_j_index]])
            #scorelist.append([np.max(mat_tmp), del_i_index, del_j_index])
            scorelist.append({'Score':maxscore[0], 
                            'Root1_label':lllnode[del_i_index].label, 
                            'Root1_node':lllnode[del_i_index].nodeobj,
                            'Root1_seq':olllnode[del_i_index].nodeobj,
                            'Root2_label':llllnode[del_j_index].label, 
                            'Root2_node':llllnode[del_j_index].nodeobj, 
                            'Root2_seq':ollllnode[del_j_index].nodeobj,
                            'row':del_i_index, 
                            'col':del_j_index})

            #trace_value[del_i_index, del_j_index]
            mat_tmp[del_i_index,del_j_index] = -99999.
            mat_tmp = changemat([del_i_index,del_j_index],trace_value,mat_tmp)


        return({'matrix':mmatrix, 'TopScoreList':scorelist})

    else:
        print("Parameter top cannot be negative, or it might be out of range.")
      

            
def FindNode(Seq: str, times: int) -> list:
    result = []
    if Seq.find('(') == -1:
        for i in range(times):
            result.append(Seq)
        return result
    Seq_list = []
    index_list = []
    index_dict = {}
    brackets_num = 0  # 括号个数
    node_num = -1  # 节点序号
    node_tmp = ''
    
    for i in list(Seq):
        if i == '(':
            brackets_num += 1
            Seq_list.append(i)
            node_num += 1
        elif i == ',':
            if brackets_num != 0 and node_tmp:
                Seq_list.append(node_tmp)
                node_num += 1
                index_list.append(node_num)
                index_dict[node_num] = node_tmp
                node_tmp = ''
            Seq_list.append(i)
            node_num += 1
        elif i == ')':
            if node_tmp:
                Seq_list.append(node_tmp)
                node_num += 1
                index_list.append(node_num)
                index_dict[node_num] = node_tmp
                node_tmp = ''
            brackets_num -= 1
            Seq_list.append(i)
            node_num += 1
        else:
            node_tmp += i
            if i == ';':
                Seq_list.append(i)
                node_num += 1
    # print(Seq_list)
    # print(index_dict)
    # print(index_list)
    Seq_list_tmp = deepcopy(Seq_list)
    index_list_tmp = deepcopy(index_list)
    #print('原来的序列: \n',"".join(Seq_list))
    #print('改变的序列: \n')
    for i in range(times):
        random.shuffle(index_list_tmp)
        # print(index_list_tmp)
        for i, j in zip(index_list_tmp, index_list):
            Seq_list_tmp[j] = index_dict[i]
        result.append("".join(Seq_list_tmp))
    return(result)


class OP:
    def __init__(self, seq1_list_result, seq2_list_result, ScoreDictFile, poolnum=1, mv: float = 2., pv: float = -1., notebook:int = 0, Tqdm:int = 1):
        # 直接调用 Manager 提供的 list() 和 dict()
        self.manager = mp.Manager
        self.mp_lst = self.manager().list()
        self.Seq1_list = seq1_list_result
        self.Seq2_list = seq2_list_result
        self.scoredictfile = ScoreDictFile
        self.mv = mv
        self.pv = pv
        self.notebook = notebook
        self.Tqdm = notebook
        self.poolnum = min(poolnum, max(psutil.cpu_count(False), 1))
        self.length = len(seq1_list_result)

    def Foo(self, i, j, scoredictfile):
        root1_tmp = MultiTree(i)
        root1_tmp.CreatTree()
        root1_tmp.Postorder_Level()
        lll_tmp = root1_tmp.nodes({})  # 二维表示
        lllnode_tmp = [j for i in lll_tmp for j in i]
        lllloop_tmp = []
        for i in lll_tmp:
            lllloop_tmp.append(len(i))
        llldict_tmp = {}
        for index, iter in enumerate(lllnode_tmp):
            llldict_tmp[index] = [lllnode_tmp.index(i) for i in iter.son()]

        root2_tmp = MultiTree(j)
        root2_tmp.CreatTree()
        root2_tmp.Postorder_Level()
        llll_tmp = root2_tmp.nodes({})  # 二维表示
        llllnode_tmp = [j for i in llll_tmp for j in i]
        llllloop_tmp = []
        for i in llll_tmp:
            llllloop_tmp.append(len(i))
        lllldict_tmp = {}
        for index, iter in enumerate(llllnode_tmp):
            lllldict_tmp[index] = [llllnode_tmp.index(i) for i in iter.son()]

        score_dict = {}
        if scoredictfile == '':
            score_dict = Scoredict(root1_tmp.leaves(
                []), root2_tmp.leaves([]), self.mv)
        else:
            score_dict = QuantitativeScoreFile(scoredictfile)

        mmatrix = pd.DataFrame([[0.0 for i in range(len(llllnode_tmp))] for j in range(len(lllnode_tmp))],
                               index=[i.nodeobj for i in lllnode_tmp],
                               columns=[j.nodeobj for j in llllnode_tmp])
        mmatrix.index.name = 'Root1'
        mmatrix.columns.name = 'Root2'
        matrix_values = mmatrix.values

        ttrace = pd.DataFrame([[[] for i in range(len(llllnode_tmp))] for j in range(len(lllnode_tmp))],
                              index=[i.label for i in lllnode_tmp],
                              columns=[j.label for j in llllnode_tmp])
        ttrace.index.name = 'Root1'
        ttrace.columns.name = 'Root2'
        trace_value = ttrace.values
        # 执行循有规律就是(0,0)(0,1)(1,0)(1,1)(0,2)(2,0)(1,2)(2,1)(2,2)(0,3)(3,0)...(n,m)
        for loop_index in loopindex(root1_tmp.level+1, root2_tmp.level+1):
            # print(loop_index)
            for i in range(lllloop_tmp[loop_index[0]]):
                for j in range(llllloop_tmp[loop_index[1]]):
                    i_index = 0
                    j_index = 0
                    for i_tmp in range(loop_index[0]):
                        i_index += lllloop_tmp[i_tmp]
                    i_index += i
                    for j_tmp in range(loop_index[1]):
                        j_index += llllloop_tmp[j_tmp]
                    j_index += j
                    matrix_tmp = matrix_values[llldict_tmp[i_index], :]
                    matrix_tmp = matrix_tmp[:, lllldict_tmp[j_index]]

                    matrix_values[i_index][j_index] = GetMaxScore(trace=trace_value,
                                                                  root1=lll_tmp[loop_index[0]][i],
                                                                  root2=llll_tmp[loop_index[1]][j],
                                                                  allmatrix=matrix_values,
                                                                  root1_index=i_index,
                                                                  root2_index=j_index,
                                                                  local_matrix=matrix_tmp,
                                                                  local_matrix_root1_index=llldict_tmp[i_index],
                                                                  local_matrix_root2_index=lllldict_tmp[j_index],
                                                                  dict_score=score_dict,
                                                                  prune=self.pv,
                                                                  Algorithm='')
        # print(mmatrix)
        # print(ttrace)
        # print(matrix_values[len(lllnode)-1][len(llllnode)-1])
        self.mp_lst.append(matrix_values[-1][-1])

    def flow(self):
        pool = mp.Pool(self.poolnum)
        if self.Tqdm == 1:
            if self.notebook == 1:
                from tqdm.notebook import tqdm
            else:
                from tqdm import tqdm
            pbar = tqdm(total=self.length)
            pbar.set_description(' Pvalue ')
            update = lambda *args: pbar.update()
        else:
            update = None
            
        for i, j in zip(self.Seq1_list, self.Seq2_list):
            pool.apply_async(func=self.Foo, args=(
                i, j, self.scoredictfile), callback=update)

        pool.close()
        pool.join()


def pvalue(times: int, 
           topscorelist, 
           ScoreDictFile: str = '', 
           CPUs: int = 50, 
           mv: float = 2., 
           pv: float = -1.,
           notebook: int = 0,
           Tqdm: int = 1,
           ):
    Seq1_list_result_max = []
    Seq2_list_result_max = []
    for i in topscorelist:
        Seq1_list_result_max.append(FindNode(i['Root1_node'], times))
        Seq2_list_result_max.append(FindNode(i['Root2_node'], times))

    score_list_max = []
    #print(len(topscorelist))
    for i in range(len(topscorelist)):
        op_max = OP(
            Seq1_list_result_max[i], Seq2_list_result_max[i], ScoreDictFile, CPUs, mv, pv, notebook, Tqdm)
        op_max.flow()
        score_list_max.append(op_max.mp_lst + [topscorelist[i]['Score']])

    # score_list_max.append(float(MaxScore))
    return(score_list_max)


if __name__ == '__main__':
    example = scoremat(TreeSeqFile = TreeSeqFile,
                         TreeSeqFile2 = TreeSeqFile2,
                         Name2TypeFile = Name2TypeFile,
                         Name2TypeFile2 = Name2TypeFile2,
                         ScoreDictFile = ScoreDictFile,
                         mv = mv,
                         top = top,
                         notebook = notebook,
                         pv = pv,
                         Tqdm = Tqdm) 
    print("\n********** Score Matrix **********\n", example['matrix'])
             
    if top == 0:
        print("\n********** T1root_T2root **********")
        for key,value in example['T1root_T2root'][0].items():
            print('{key}:{value}'.format(key = key, value = value))

    elif top > 0:
        for index,keyss in enumerate(example['TopScoreList']):
            print('\n********** Top ', index+1, '**********')
            for key,value in keyss.items():
                print('{key}:{value}'.format(key = key, value = value))
                

    if times > 0:
        ppp = pvalue(times = times, 
               topscorelist = example['T1root_T2root'] if top == 0 else example['TopScoreList'], 
               ScoreDictFile = ScoreDictFile,
               CPUs = CPUs, 
               mv = mv, 
               pv = pv,
               notebook = notebook,
               Tqdm = Tqdm)
        print("\n********** P Value **********")
        print(ppp)
        #print(psutil.cpu_count(False))
     
        