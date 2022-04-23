# -*- coding: utf-8 -*- 
from CreatTree import *
from ReadFile import *

if __name__ == '__main__':
    TreeSeqType = print(ReadTreeSeq_Name2Type('modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv'))
    root1 = MultiTree(TreeSeqType)
    print(root1.nodeobj)
    #root1.CreatTree()
    #root1.Postorder_Level()