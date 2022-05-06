# -*- coding: utf-8 -*- 

from numpy import NaN
from .ReadFile import *
from .mytest import *
from .mymath import *
from .auxi import *
from .Pvalue import *
#import itertools
#import random
import pandas as pd


class MultiTree:
    def __init__(self, nodeobj:str, level:'int'=0, label:str="root"):
        self.nodeobj = nodeobj if nodeobj[-1] != ';' else nodeobj[:-1]
        self.left = None
        self.right = None
        self.level = level
        self.label = label
    # 鍓嶅簭閬嶅巻,鑾峰彇鎸夌収灞傜骇鎺掑簭鐨勫叏鑺傜偣搴忓垪瀵? [node:level]
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
    # 鍚庡簭閬嶅巻_寰楀埌nodeobj:level瀵?
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.nodeobj is not None:
            print(self.nodeobj,' Level:',self.level,' Label:',self.label)
    # 鍓嶅簭閬嶅巻_寰楀埌nodeobj:level瀵?
    def preorder(self):
        if self.nodeobj is not None:
            print(self.nodeobj,' Level:',self.level,' Label:',self.label)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
    # 灞傚簭閬嶅巻
    def levelorder(self):
        # 杩斿洖鏌愪釜鑺傜偣鐨勫乏瀛╁瓙
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None
        # 杩斿洖鏌愪釜鑺傜偣鐨勫彸瀛╁瓙
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None
        # 灞傚簭閬嶅巻鍒楄〃
        level_order = []
        # 鏄惁娣诲姞鏍硅妭鐐逛腑鐨勬暟鎹?
        if self.nodeobj is not None:
            level_order.append([self])
        # 浜屽弶鏍戠殑楂樺害
        height = self.height()
        if height >= 1:
            # 瀵圭浜屽眰鍙婂叾浠ュ悗鐨勫眰鏁拌繘琛屾搷浣?, 鍦╨evel_order涓坊鍔犺妭鐐硅€屼笉鏄暟鎹?
            for _ in range(2, height + 1):
                level = []  # 璇ュ眰鐨勮妭鐐?
                for node in level_order[-1]:
                    # 濡傛灉宸﹀瀛愰潪绌猴紝鍒欐坊鍔犲乏瀛╁瓙
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 濡傛灉鍙冲瀛愰潪绌猴紝鍒欐坊鍔犲彸瀛╁瓙
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 濡傛灉璇ュ眰闈炵┖锛屽垯娣诲姞璇ュ眰
                if level:
                    level_order.append(level)

            # 鍙栧嚭姣忓眰涓殑鏁版嵁
            for i in range(0, height):  # 灞傛暟
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].nodeobj
        return level_order
    # 浜屽弶鏍戠殑楂樺害
    def height(self):
        # 绌虹殑鏍戦珮搴︿负0, 鍙湁root鑺傜偣鐨勬爲楂樺害涓?1
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
    # 鍘熸潵鐨勫鍙夋爲鐨勫彾瀛愯妭鐐?
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
    #鐢熸垚鏍?
    def CreatTree(self):
        if(self.nodeobj[0] == '('): #瀛樺湪鎷彿鎰忓懗鐫€杩樻病杈惧埌鍙跺瓙缁撶偣
            node_list = []
            brackets_num = 0 #鎷彿涓暟
            node_num = 0 #鑺傜偣搴忓彿
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
            #print(node_list)    #鏌ョ湅鎷嗗垎鍚庣殑鑺傜偣搴忓垪
            self_tmp = self
            for index,item in enumerate(node_list):
                if index == 0:
                #绗竴涓瓙鑺傜偣閮芥槸鐖惰妭鐐圭殑宸﹁妭鐐?
                #鍚庣画瀛愯妭鐐瑰氨鏄笂涓€涓瓙鑺傜偣鐨勫彸鑺傜偣 
                #璧嬩簣label
                    label = str(index) if self.label == 'root' else self_tmp.label+','+str(index)    
                    self.left = MultiTree(item,label=label)
                    self = self.left
                    self.CreatTree()
                else:
                    label = str(index) if not ',' in self.label else self_tmp.label+','+str(index)    
                    self.right = MultiTree(item,label=label)
                    self = self.right
                    self.CreatTree()
    #璧嬪眰宸﹀瓙鏍戝悗搴忛亶鍘嗘壘鍑烘渶澶у眰绾
    def Posorder_Max_Level(self):
        level = self.level;
        while self.right:
            #鏈夊彸瀛愭爲灏辨槸鏈夊厔寮熺粨鐐?
            level = max(level, self.right.level)
            self = self.right
        return level
    #璧嬩簣灞傜骇level
    def Level(self):
        if self.left == None: #鍙跺瓙鑺傜偣
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
    #鍙跺瓙鑺傜偣涓暟,闇€瑕佺殑鏄妭鐐逛笅鐨勫乏鑺傜偣鎵嶆纭?
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
        
    #鎬昏妭鐐逛釜鏁?
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
    #鑾峰彇褰撳墠鑺傜偣涓€绾у瓙鑺傜偣涓暟
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
    #鑾峰彇褰撳墠鑺傜偣涓€绾у瓙鑺傜偣self
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
    # 涓簭閬嶅巻锛屽緱鍒扮敓鎴愭爲鏁版嵁
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
            Tqdm:bool = True,
            notebook:bool = False):
    if Name2TypeFile != '':
        TreeSeqType = ReadTreeSeq_Name2Type(TreeSeqFile,Name2TypeFile)
    if Name2TypeFile2 != '':
        TreeSeqType2 = ReadTreeSeq_Name2Type(TreeSeqFile2,Name2TypeFile2)
    root1 = MultiTree(TreeSeqType)
    root2 = MultiTree(TreeSeqType2)
    root1.CreatTree()
    root1.Postorder_Level()
    lll = root1.nodes({}) #二维表示
    lllnode = [j for i in lll for j in i]
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
    if Tqdm:
        if notebook == True:
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
                            'Root2_label':root2.label, 
                            'Root2_node':root2.nodeobj, 
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

        mat_tmp = copy.deepcopy(matrix_values)
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
                            'Root2_label':llllnode[del_j_index].label, 
                            'Root2_node':llllnode[del_j_index].nodeobj, 
                            'row':del_i_index, 
                            'col':del_j_index})

            #trace_value[del_i_index, del_j_index]
            mat_tmp[del_i_index,del_j_index] = -99999.
            mat_tmp = changemat([del_i_index,del_j_index],trace_value,mat_tmp)


        return({'matrix':mmatrix, 'TopScoreList':scorelist})

    else:
        print("Parameter top cannot be negative and zero, or it might be out of range.")
    #return({'matrix':mmatrix, 'mrow_addr':lllnode,'mcol_addr':llllnode})
    #return({'matrix':mmatrix, 'mrow_addr':lllnode,'mcol_addr':llllnode})
    #print(ttrace)
    #print(matrix_values[len(lllnode)-1][len(llllnode)-1])

#print(scoremat('modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv','modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv','modelta/ExampleFile/Qscorefile.csv'))
#print(scoremat('modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv','modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv'))
