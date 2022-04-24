import numpy as np
from munkres import Munkres, print_matrix

class Greedy_Algorithm:
    def __init__(self, Local_matrix, 
                 local_matrix_root1_index=[], 
                 local_matrix_root2_index=[],
                 prune=-1):
        self.Local_matrix = Local_matrix
        self.local_matrix_root1_index = local_matrix_root1_index
        self.local_matrix_root2_index = local_matrix_root2_index
        self.prune = prune
    def calculate(self):
        mat_tmp = self.Local_matrix
        sum = 0
        for i in range(min(self.Local_matrix.shape)):
            #print(mat_tmp)
            sum += np.max(mat_tmp)
            del_i_index = np.where(mat_tmp==np.max(mat_tmp))[0][0]
            del_j_index = np.where(mat_tmp==np.max(mat_tmp))[1][0]
            mat_tmp = np.delete(mat_tmp, del_i_index, 0) 
            mat_tmp = np.delete(mat_tmp, del_j_index, 1)
        return sum
    def trace_back(self):
        mat_tmp = self.Local_matrix
        trace = []
        for i in range(min(self.Local_matrix.shape)):
            if np.max(mat_tmp) <= self.prune:
                break
            del_i_index = np.where(mat_tmp==np.max(mat_tmp))[0][0]
            del_j_index = np.where(mat_tmp==np.max(mat_tmp))[1][0]
            trace.append([self.local_matrix_root1_index[del_i_index],self.local_matrix_root2_index[del_j_index]])
            mat_tmp[del_i_index,:] = -99999 
            mat_tmp[:,del_j_index] = -99999
        return trace

def GetMaxScore(trace,
                root1,
                root2, 
                allmatrix,
                root1_index:int,
                root2_index:int,
                local_matrix,
                local_matrix_root1_index,
                local_matrix_root2_index,
                prune=-1,
                dict_score={},
                Algorithm:str = 'KM'):
    # ������������ǣ����Ǹ��ڵ�Ҳ��Ҷ�ڵ㣨��һԪ�أ���ֱ�Ӳ��ֵ䣬�鲻���ͻ���Ϊ����ֵprune
    root1node = root1
    root2node = root2
    score = prune
    key = root1node.nodeobj+'_'+root2node.nodeobj
    key2 = root2node.nodeobj+'_'+root1node.nodeobj
    if root1node.left == None and root2node.left == None:
        #·��ֻ���ǽڵ�ֱ��ƥ��
        if key in dict_score:
            if dict_score[key] > prune:
                trace[root1_index][root2_index].append([root1.nodeobj,root2.nodeobj])
            return dict_score[key]
        else:
            dict_score[key] = score
            dict_score[key2]= score
            return score
    # ���ֻ��һ������ʾΪ���ڵ�
    elif root1node.left == None and root2node.left is not None:
        #if key in dict_score:
        #    return dict_score[key]
        if (dict_score[root1node.nodeobj+'_'+root1node.nodeobj]+prune*(root2node.leaf_count()-1) < prune):
            #dict_score[key] = score
            #dict_score[key2] = score
            return score
        else:
            dearr = local_matrix.flatten()
            maxnum = np.max(dearr)
            score = max(score, maxnum+(root2.leaf_count()-1)*prune)
            if score > prune:
                trace[root1_index][root2_index].append([root1_index, local_matrix_root2_index[dearr.tolist().index(maxnum)]])
            #root2node = root2node.left #����������
            #key_tmp = root1node.nodeobj+'_'+root2node.nodeobj
            #score = max(score, dict_score[key_tmp])
            #while root2node.right: #�������нڵ�
            #    root2node = root2node.right
            #    key_tmp = root1node.nodeobj+'_'+root2node.nodeobj
            #    score = max(score, dict_score[key_tmp])
            #score = max(score+((root2.leaf_count()-1)*prune),prune)    
            #dict_score[key] = score
            #dict_score[key2] = score
            #return root2.leaf_count()
            return score
        
    elif root1node.left is not None and root2node.left == None:
        #if key in dict_score:
        #    return dict_score[key]
        #print(max(local_matrix))
        if (dict_score[root2node.nodeobj+'_'+root2node.nodeobj]+prune*(root1node.leaf_count()-1) < prune):
            #dict_score[key] = score
            #dict_score[key2] = score
            return score
        else:
            dearr = local_matrix.flatten()
            maxnum = np.max(dearr)
            score = max(score, maxnum+(root1.leaf_count()-1)*prune)
            if score > prune:
                trace[root1_index][root2_index].append([local_matrix_root1_index[dearr.tolist().index(maxnum)],root2_index] )
            #root1node = root1node.left #����������
            #key_tmp = root1node.nodeobj+'_'+root2node.nodeobj
            #score = max(score, dict_score[key_tmp])
            #while root1node.right: #�������нڵ�
            #    root1node = root1node.right
            #    key_tmp = root1node.nodeobj+'_'+root2node.nodeobj
            #    score = max(score, dict_score[key_tmp])
            #score = max(score+((root1.leaf_count()-1)*prune),prune)    
            #dict_score[key] = score
            #dict_score[key2] = score
            #return root2.leaf_count()
            return score
    #���������Ƿ�Ҷ�ӽ��
    else:
        summ = 0
        r1leaf = root1node.leaf_count()
        r2leaf = root2node.leaf_count()
        if r1leaf >= r2leaf:
            for i in root2node.leaves([]):
                summ += dict_score[i.nodeobj+'_'+i.nodeobj]
            if (summ + prune*(r1leaf-r2leaf) < r2leaf*prune):
                return r2leaf*prune
        else:
            for i in root1node.leaves([]):
                summ += dict_score[i.nodeobj+'_'+i.nodeobj]
            if (summ + prune*(r2leaf-r1leaf) < r1leaf*prune):
                return r1leaf*prune
        
        
        if(Algorithm == 'GA'):
            ga= Greedy_Algorithm(local_matrix,local_matrix_root1_index, local_matrix_root2_index,prune)
            score = ga.calculate()+abs(r1leaf-r2leaf)*prune
            if score > min(r1leaf,r2leaf)*prune :
                trace[root1_index][root2_index]=ga.trace_back()
            else:
                score = min(r1leaf,r2leaf)*prune
        elif(Algorithm == 'GAR'):
            pass
        
        else:#Ĭ��ΪKM����
            #github���汾
            trace_tmp = []
            cost_matrix = []
            for row in local_matrix:
                #print(row)
                cost_row = []
                for col in row:
                    cost_row += [99999 - col]
                cost_matrix += [cost_row]
            m = Munkres()
            indexes = m.compute(cost_matrix)
            #print_matrix(local_matrix, msg='Highest profit through this local_matrix:')
            total = 0
            for row, column in indexes:
                value = local_matrix[row][column]
                total += value
                if value > prune:
                    trace_tmp.append([local_matrix_root1_index[row],local_matrix_root2_index[column]])
                #print(f'({row}, {column}) -> {value}')
            #print('total profit= ',total)
            score = total+abs(r1leaf-r2leaf)*prune
            if score > min(r1leaf,r2leaf)*prune:
                trace[root1_index][root2_index]=trace_tmp
            else:
                score = min(r1leaf,r2leaf)*prune
        
        
        #����
        for i in zip(root1node.son(),local_matrix_root1_index):
            if i[0].left is not None:
                score_tmp = allmatrix[i[1],root2_index] + prune*(r1leaf - i[0].leaf_count())
                if score < score_tmp:
                    score = score_tmp
                    trace[root1_index][root2_index].clear()
                    trace[root1_index][root2_index].append([i[1],root2_index])
                #score = max(allmatrix[i[1],root2_index] + prune*(r1leaf - i[0].leaf_count()), score)
        for j in zip(root2node.son(),local_matrix_root2_index):
            if j[0].left is not None:
                score_tmp = allmatrix[root1_index,j[1]] + prune*(r2leaf - j[0].leaf_count())
                if score < score_tmp:
                    score = score_tmp
                    trace[root1_index][root2_index].clear()
                    trace[root1_index][root2_index].append([root1_index,j[1]])
                #score = max(allmatrix[root1_index,j[1]] + prune*(r2leaf - j[0].leaf_count()), score)      
        return score