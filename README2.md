# mDELTA

<div align=center><img alt="logo" src="./image/mDELTAt.png" width=70% style="float:right; padding:40px"/></div>

- mDELTA is an algorithm for *m*ultifuricating *D*evelopmental c*E*ll *L*ineage *T*ree *A*lignment. In essence, it compares two rooted, unordered, tip-labeled trees, and finds the best global / local correspondence between the nodes. The mDELTA program is designed for analyzing developmental cell lineage trees reconstructed through single-cell DNA barcoding (such as done by scGESTALT or SMALT, while greater cellular coverage is expected to yield more meaningful mDELTA alignments).
- Except for dealing with cell lineage trees instead of biological sequences, mDELTA is conceptually similar to sequence alignment. It helps quantify similarity among different lineage trees, disentangle the consensus and variation, find recurrent motifs, and facilitate comparative/evolutionary analyses.
- Also included in this repository are Python/R scripts for statistical analyses and visualization of mDELTA results, which facilitates their biological interpretation.
- mDELTA was developed by Jingyu Chen under the supervision of Professor Jian-Rong Yang at the Zhongshan School of Medicine of Sun Yat-Sen University in China.


# Quick start
#### Installation
```sh
pip install mdelta
```

This will install mDELTA and its prerequisites

#### Running the program
```sh
mDELTA.py -h
```

#### Aligning a tree with itself, output top three local alignments
```sh
mDELTA.py ExampleFile/tree.nwk ExampleFile/tree.nwk -t 3
```


#### Required package

- [pandas](https://pypi.org/project/pandas/): Score matrix architecture based on dataframe.
- [numpy](https://pypi.org/project/numpy/): Many computing essential packages.
- [munkres](https://pypi.org/project/munkres/): An algorithm for finding the maximum value of score matrix dynamic programming

#### Optional package

- [tqdm](https://pypi.org/project/tqdm/): Displays the progress during the calculation phase.
- [multiprocess](https://pypi.org/project/multiprocess/): When calculating the p value, because it needs to disrupt the original sequence many times and perform multiple calculations, using multiple processes can effectively reduce the waiting time.

#### Source code install

```sh
(1) Offline
Step1: $git clone https://github.com/Chenjy0212/mdelta.git
Step2: $cd mdelta -> run "python setup.py install"
(2) Online
$pip install git+https://github.com/Chenjy0212/mdelta.git@main
```

# For python coder user ↓

You can use this package in your Python code. For example, run under Jupiter notebook:

```python
import mdelta
from pprint import pprint
#前两项为必选项，后者皆为可选
example = mdelta.scoremat(TreeSeqFile = 'ExampleFile/tree.nwk',  
                       TreeSeqFile2 = 'ExampleFile/tree.nwk',      
                       Name2TypeFile = 'ExampleFile/Name2Type.csv',
                       Name2TypeFile2 ='ExampleFile/Name2Type.csv',
                       ScoreDictFile = 'ExampleFile/TypeTypeScore.csv',
                       top = 3,
                       notebook = 1,
                       overlap = 5,
                          )
```

#### Result

```
Matrix Node: |██████████| 121/121 100%
121/121 [00:00<00:00, 2573.11it/s]
{'TopScoreList': [{'Root1_label': 'root',
                   'Root1_match': ['0',
                                   '1',
                                   '0,0',
                                   '0,1',
                                   '0,2',
                                   '0,0,0',
                                   '0,0,1',
                                   '0,0,2',
                                   '0,2,0',
                                   '0,2,1'],
                   'Root1_match_tree': '(((a,b,c),d,(e,f)),a);',
                   'Root1_node': '(((a,b,c),d,(e,f)),a)',
                   'Root1_prune': [],
                   'Root1_seq': '(((a1,a2,a3),a4,(a5,a6)),a1)',
                   'Root2_label': 'root',
                   'Root2_match': ['0',
                                   '1',
                                   '0,0',
                                   '0,1',
                                   '0,2',
                                   '0,0,0',
                                   '0,0,1',
                                   '0,0,2',
                                   '0,2,0',
                                   '0,2,1'],
                   'Root2_match_tree': '(((a,b,c),d,(e,f)),a);',
                   'Root2_node': '(((a,b,c),d,(e,f)),a)',
                   'Root2_prune': [],
                   'Root2_seq': '(((a1,a2,a3),a4,(a5,a6)),a1)',
                   'Score': 21.0,
                   'col': 10,
                   'row': 10},
                  {'Root1_label': '0',
                   'Root1_match': ['0',
                                   '0,0',
                                   '0,1',
                                   '0,2',
                                   '0,0,0',
                                   '0,0,1',
                                   '0,0,2',
                                   '0,2,0',
                                   '0,2,1'],
                   'Root1_match_tree': '(((a,b,c),d,(e,f)));',
                   'Root1_node': '((a,b,c),d,(e,f))',
                   'Root1_prune': [],
                   'Root1_seq': '((a1,a2,a3),a4,(a5,a6))',
                   'Root2_label': 'root',
                   'Root2_match': ['0',
                                   '0,0',
                                   '0,1',
                                   '0,2',
                                   '0,0,0',
                                   '0,0,1',
                                   '0,0,2',
                                   '0,2,0',
                                   '0,2,1'],
                   'Root2_match_tree': '(((a,b,c),d,(e,f)));',
                   'Root2_node': '(((a,b,c),d,(e,f)),a)',
                   'Root2_prune': ['1'],
                   'Root2_seq': '(((a1,a2,a3),a4,(a5,a6)),a1)',
                   'Score': 17.0,
                   'col': 10,
                   'row': 9},
                  {'Root1_label': '0,0',
                   'Root1_match': ['0,0', '0,0,0', '0,0,1', '0,0,2'],
                   'Root1_match_tree': '(((a,b,c),d,(e,f)),(a,b,c));',
                   'Root1_node': '(a,b,c)',
                   'Root1_prune': [],
                   'Root1_seq': '(a1,a2,a3)',
                   'Root2_label': '0',
                   'Root2_match': ['0,0', '0,0,0', '0,0,1', '0,0,2'],
                   'Root2_match_tree': '(((a,b,c),d,(e,f)),(a,b,c));',
                   'Root2_node': '((a,b,c),d,(e,f))',
                   'Root2_prune': ['0,1', '0,2,0', '0,2,1'],
                   'Root2_seq': '((a1,a2,a3),a4,(a5,a6))',
                   'Score': 6.0,
                   'col': 9,
                   'row': 7}],
 'matrix': Root2  0,0,0  0,0,1  0,0,2  0,1  0,2,0  0,2,1    1  0,0  0,2     0  root
Root1                                                                   
0,0,0    3.0    2.0    2.0  1.0    1.0    0.0  3.0  1.0  0.0  -1.0  -1.0
0,0,1    2.0    3.0    1.0 -1.0   -1.0   -1.0  2.0  1.0 -1.0  -1.0  -1.0
0,0,2    2.0    1.0    3.0 -1.0   -1.0   -1.0  2.0  1.0 -1.0  -1.0  -1.0
0,1      1.0   -1.0   -1.0  3.0    0.0   -1.0  1.0 -1.0 -1.0  -1.0  -1.0
0,2,0    1.0   -1.0   -1.0  0.0    3.0   -1.0  1.0 -1.0  2.0  -1.0  -1.0
0,2,1    0.0   -1.0   -1.0 -1.0   -1.0    3.0  0.0 -1.0  2.0  -1.0  -1.0
1        3.0    2.0    2.0  1.0    1.0    0.0  3.0  1.0  0.0  -1.0  -1.0
0,0      1.0    1.0    1.0 -1.0   -1.0   -1.0  1.0  9.0 -1.0   6.0   5.0
0,2      0.0   -1.0   -1.0 -1.0    2.0    2.0  0.0 -1.0  6.0   2.0   1.0
0       -1.0   -1.0   -1.0 -1.0   -1.0   -1.0 -1.0  6.0  2.0  18.0  17.0
root    -1.0   -1.0   -1.0 -1.0   -1.0   -1.0 -1.0  5.0  1.0  17.0  21.0,
 'score_dict': {'a_a': 3.0,
                'a_b': 2.0,
                'a_c': 2.0,
                'a_d': 1.0,
                'a_e': 1.0,
                'a_f': 0.0,
                'b_a': 2.0,
                'b_b': 3.0,
                'b_c': 1.0,
                'b_d': -1.0,
                'b_e': -1.0,
                'b_f': -1.0,
                'c_a': 2.0,
                'c_b': 1.0,
                'c_c': 3.0,
                'c_d': -1.0,
                'c_e': -1.0,
                'c_f': -1.0,
                'd_a': 1.0,
                'd_b': -1.0,
                'd_c': -1.0,
                'd_d': 3.0,
                'd_e': 0.0,
                'd_f': -1.0,
                'e_a': 1.0,
                'e_b': -1.0,
                'e_c': -1.0,
                'e_d': 0.0,
                'e_e': 3.0,
                'e_f': -1.0,
                'f_a': 0.0,
                'f_b': -1.0,
                'f_c': -1.0,
                'f_d': -1.0,
                'f_e': -1.0,
                'f_f': 3.0},
 'tree1_leaves_celltype': 'a;b;c;d;e;f;a',
 'tree1_leaves_label': '0,0,0;0,0,1;0,0,2;0,1;0,2,0;0,2,1;1',
 'tree1_leaves_nodename': 'a1;a2;a3;a4;a5;a6;a1',
 'tree2_leaves_celltype': 'a;b;c;d;e;f;a',
 'tree2_leaves_label': '0,0,0;0,0,1;0,0,2;0,1;0,2,0;0,2,1;1',
 'tree2_leaves_nodename': 'a1;a2;a3;a4;a5;a6;a1'}
```

#### Parameter analysis

**If the parameter has an `*`, it is required; otherwise, it is optional**

- `TreeSeqFile` & `TreeSeqFile2`: [*path/filename* `*`] Cell lineage tree file with branch length information removed. The format of reference documents is as follows: [ExampleFile/tree.nwk](https://github.com/Chenjy0212/mdelta/blob/main/mdelta/ExampleFile/tree.nwk)
- `mv`: [*float* and `default` = *2.*] The matching score between the same nodes, which is often used when the parameter `ScoreDictFile` is the default.
- `pv`: [*float* and `default` = *-1.*] The prune score between the different nodes.
- `top`: [*int > 0* and `default` = *0*] Select the top few meaningful scores in the score matrix. if it is default:

```
{'T1root_T2root': [{'Root1_label': 'root',
                    'Root1_match': ['0',
                                    '1',
                                    '0,0',
                                    '0,1',
                                    '0,2',
                                    '0,0,0',
                                    '0,0,1',
                                    '0,0,2',
                                    '0,2,0',
                                    '0,2,1'],
                    'Root1_match_tree': '(((a,b,c),d,(e,f)),a);',
                    'Root1_node': '(((a,b,c),d,(e,f)),a)',
                    'Root1_prune': [],
                    'Root1_seq': '(((a1,a2,a3),a4,(a5,a6)),a1)',
                    'Root2_label': 'root',
                    'Root2_match': ['0',
                                    '1',
                                    '0,0',
                                    '0,1',
                                    '0,2',
                                    '0,0,0',
                                    '0,0,1',
                                    '0,0,2',
                                    '0,2,0',
                                    '0,2,1'],
                    'Root2_match_tree': '(((a,b,c),d,(e,f)),a);',
                    'Root2_node': '(((a,b,c),d,(e,f)),a)',
                    'Root2_prune': [],
                    'Root2_seq': '(((a1,a2,a3),a4,(a5,a6)),a1)',
                    'Score': 21.0,
                    'col': 10,
                    'row': 10}],            
```

- `notebook`: [*bool* and `default`=*False*] Is it written and run in the jupyter notebook environment.
- `Tqdm`: [*bool* and `default`=*True*] Whether to display the operation progress bar.
- `overlap`: [*int > 0* and `default` = *0*] In the local results, the later comparison results cannot have X% or more node pairs that duplicate the previous results.
- `merge`:  [*int > 0* and `default` = *0*] Merge internal node to prune.

**if Qualitative calculation:**

- `Name2TypeFile` & `Name2TypeFile2`: [*path/filename* `*`] Convert tree node name to type. The format of reference documents is as follows: [ExampleFile/Name2Type.csv](https://github.com/Chenjy0212/mdelta/blob/main/mdelta/ExampleFile/Name2Type.csv)
- `ScoreDictFile`: [*path/filename* and `default`=''] Defines the score of matches between nodes. The format of reference documents is as follows: [ExampleFile/socrefile.csv](https://github.com/Chenjy0212/mdelta/blob/main/mdelta/ExampleFile/scorefile.csv)

```
The matching score between nodes is determined according to the "ScoreDictFile" file.
If the file is empty, only the same nodes are taken for pairing, and the default matching score is 2 (float)

node: a <-> a = 2.(custom)
      b <-> b = 3.(custom)
      a <-> b = ?(custom)
The higher the score, the stronger the similarity
```

**If Quantitative calculation**

- `ScoreDictFile`: [*path/filename* `*`] Defines the score of matches between nodes. The format of reference documents is as follows: [ExampleFile/Qscorefile.csv](https://github.com/Chenjy0212/mdelta/blob/main/mdelta/ExampleFile/Qscorefile.csv)
- `Name2TypeFile` & `Name2TypeFile2`: [*path/filename* or *No input*] Convert tree node name to type. The format of reference documents is as follows: [ExampleFile/Name2Type.csv](https://github.com/Chenjy0212/mdelta/blob/main/mdelta/ExampleFile/Name2Type.csv)

```
The matching score between nodes is determined according to the "ScoreDictFile" file.
The file is required. You can modify the score of the same node by modifying parameter "mv"

   Gene0  Gene1  Gene2  
a    1      2      3  
b    2      3      4

node: (1-2)**2 + (2-3)**2 + (3-4)**2 #Euclidean distance
Then get the final score according to the smoothing function. 
The lower the score, the stronger the similarity
```

## P-value calculation

```
mdelta.pvalue(times = 3, 
               topscorelist = example['TopScoreList'], 
               ScoreDictFile='',
               CPUs = 50, 
               mv = 2, 
               pv = -1)
```
#### Result

```
 Pvalue : 100%|██████████| 3/3 [00:00<00:00,  4.05it/s]
 Pvalue : 100%|██████████| 3/3 [00:00<00:00,  4.38it/s]
 Pvalue : 100%|██████████| 3/3 [00:00<00:00,  4.45it/s]
[[3.0, 4.0, 0.0, 14.0], [4.0, 5.0, 3.0, 11.0], [5.0, 0.0, 1.0, 11.0]]
```

The returned results represent `times` matching scores corresponding to the `top` maximum values

#### Parameter analysis

**If the parameter has an `*`, it is required; otherwise, it is optional**

- `times`: [*int > 0* `*`] The number of times the original sequence needs to be disrupted, such as:

```python
times = 3 #Randomly disrupt the nodes, but the structure remains unchanged
(((a,b,c),d,(e,f)),a) -> (((a,b,c),d,(e,f)),a)
                      -> (((a,c,d),b,(a,f)),e)
                      -> (((e,f,a),d,(b,c)),a)
```

- `topscorelist`: [*example['TopScoreList']* `*`] The input parameter is the maximum value sequence obtained earlier.
- `CPUs`: [*int > 0* and `default` = *50*] Multi process computing can greatly reduce the waiting time. The default process pool is 50, but limited by local computer resources, it can reach the maximum number of local CPU cores - 1.
- `mv` & `pv` & `notebook` & `Tqdm` & `overlap` parameters have been described in detail before

# For Ordinary user ↓

## Quick Start
#### Running the program
```sh
mDELTA.py -h
```

#### Windows

```sh
mDELTA.py ./ExampleFile/tree.nwk ./ExampleFile/tree.nwk -t 3
```

#### Linux

```sh
./mDELTA.py ../ExampleFile/tree.nwk ../ExampleFile/tree.nwk -t 3
```

#### Help

```sh
Windows: $mDELTA.py -h
 Linux:  $./mDELTA.py -h
```

```
usage: mDELTA [-h] [-nt NAME2TYPEFILE] [-nt2 NAME2TYPEFILE2] [-sd SCOREDICTFILE] [-t TOP] [-ma MAV] [-mi MIV] [-p PV] [-T TQDM]
              [-n NOTEBOOK] [-P PERM] [-a ALG] [-c CPUS] [-o OUTPUT] [-x DIFF] [-mg MERGE]
              TreeSeqFile TreeSeqFile2

Multifuricating Developmental cEll Lineage Tree Alignment(mDELTA)

positional arguments:
  TreeSeqFile           [path/filename] A text file storing cell lineage tree #1 in newick format. Tips can be labeled by name or
                        cell type. Branch lengths should be removed.
  TreeSeqFile2          [path/filename] A text file storing cell lineage tree #2 in newick format. Tips can be labeled by name or
                        cell type. Branch lengths should be removed.

optional arguments:
  -h, --help            show this help message and exit
  -nt NAME2TYPEFILE, --Name2TypeFile NAME2TYPEFILE
                        [path/filename] List of correspondance between tip name and cell type for cell lineage tree #1.
  -nt2 NAME2TYPEFILE2, --Name2TypeFile2 NAME2TYPEFILE2
                        [path/filename] List of correspondance between tip name and cell type for cell lineage tree #2.
  -sd SCOREDICTFILE, --ScoreDictFile SCOREDICTFILE
                        [path/filename] A comma-delimited text file used to determine similarity scores between cells. If there
                        are exactly three columns, they will be interpreted as (1) the cell (name or type) in Tree #1, (2) the
                        cell in Tree #2, and (3) the similarity score. If otherwise, the first column will be interpreted as the
                        cell (name or type) and the remaining columns as features of the cell (e.g. expression of a gene). The
                        similarity scores will be estimated between all pairs of cells based on the Euclidean distance calculated
                        using all the features. Overrides `-ma` and `-mi`.
  -t TOP, --top TOP     [int > 0] Performs local (instead of global) alignment, and output the top NUM local alignments with the
                        highest score (e.g. `-t 10`). In the case of global alignment, this parameter should be omitted.
  -ma MAV, --mav MAV    [float]
  -mi MIV, --miv MIV    [float] Shorthand for a simple matching score scheme, where the matching score between a pair of the same
                        cell types is MAV and all other pairs are MIV. (e.g. `-ma 2 -mi -2`). Overridden by `-sd`.
  -p PV, --pv PV        [float] The score for pruning a tip of the tree (e.g. `-p -2`). Default to -1.
  -T TQDM, --Tqdm TQDM  [0(off) or 1(on)] Toggle for the jupyter notebook environment.
  -n NOTEBOOK, --notebook NOTEBOOK
                        [0(off) or 1(on)] Toggle for the jupyter notebook environment.
  -P PERM, --PERM PERM  [int > 0] Toggle for the statistical significance. For each observed alignment, the aligned trees will be
                        permuted PERM times to generate a null distribution of alignment scores, with which a P value can be
                        calculated for the observed alignment score.
  -a ALG, --Alg ALG     [KM / GA] Use Kuhn-Munkres or Greedy Algorithm to find the optimal alignment score.
  -c CPUS, --CPUs CPUS  [int > 0] Number of threads for multi-processing. Default to 50., it can reach the maximum number of local
                        CPU cores - 1.
  -o OUTPUT, --output OUTPUT
                        [path/filename] Output filename
  -x DIFF, --diff DIFF  [int > 0] Alignment must consist of a minimal 
                        of DIFF% aligned cell pairs that are different from previous(better) local
                        alignments in order to be considered as another new alignment (e.g. `-x 20` means 20%).
  -mg MERGE, --merge MERGE
                        [float] This is the scaling factor for calculating the score of merging an internal node (e.g. -mg -1),
                        which is multiplied by the number of tips of the internal node to be merged. Default to 0.

More details on https://github.com/Chenjy0212/mdelta
```

# Citation

If you use this project in your research, please cite this project.

```
@misc{mdelta2022,
    author = {Jingyu Chen},
    title = {mDELTA: Multifuricating Developmental cEll Lineage Tree Alignment},
    year = {2022},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/Chenjy0212/mdelta}},
}
```

# Introduction

<div align=center>

Student of [@SYSU](https://github.com/sysu). :school:

Undergraduate majoring in computer science, 
master majoring in bioinformatics. :man_technologist:

I hope my program can be helpful to your research. :heart:

How to contact the author has been written at the top. :eyes:

<img alt="sysulogo" src="./image/sysulogo.png" width=200 />
</div>
<div align=center>

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/DecryptLogin?logo=python&labelColor=white)](https://pypi.org/project/mdelta/) [![PyPI](https://img.shields.io/pypi/v/DecryptLogin)](https://pypi.org/project/mdelta) [![license](https://img.shields.io/github/license/Chenjy0212/mdelta.svg)](https://github.com/Chenjy0212/mdelta/blob/main/LICENSE)<br>
[![Github Stars](https://img.shields.io/github/stars/Chenjy0212?color=faf408&label=github%20stars&logo=github)](https://github.com/Chenjy0212) [![Bilibili](https://img.shields.io/badge/dynamic/json?labelColor=FE7398&logo=bilibili&logoColor=white&label=Bilibili&color=00aeec&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dbilibili%26queryKey%3D423592635)](https://space.bilibili.com/423592635) [![Zhihu](https://img.shields.io/badge/dynamic/json?color=142026&labelColor=0066ff&logo=zhihu&logoColor=white&label=知乎&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dzhihu%26queryKey%3Dxing-ru-yu-yxl)](https://www.zhihu.com/people/xing-ru-yu-yxl) [![Weibo](https://img.shields.io/badge/%E5%BE%AE%E5%8D%9A-445-faf408?logo=sina-weibo&labelColor=e72d2c)](https://weibo.com/u/6326895746) [![neteasy-mysic](https://img.shields.io/badge/dynamic/json?label=网易云&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3DneteaseMusic%26queryKey%3D596006674&color=282c34&labelColor=e72d2c&logo=data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iOTYiIGhlaWdodD0iOTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik02MjcuMDg2IDUuMTE1YzI4LjEzMi03LjY3MiA1OC44MjItNy42NzIgODYuOTUzIDAgMzMuMjQ3IDcuNjcyIDYzLjkzNyAyMy4wMTcgODkuNTEyIDQzLjQ3NyAxMC4yMyA3LjY3MyAxNy45MDIgMTUuMzQ0IDIzLjAxNyAyOC4xMzEgNy42NzIgMTcuOTAzIDUuMTE0IDM4LjM2My01LjExNSA1My43MDgtNy42NzIgMTIuNzg3LTIzLjAxNyAyMy4wMTctNDAuOTIgMjUuNTc0LTEyLjc4NyAyLjU1OC0yNS41NzQgMC0zOC4zNjItNy42NzItNS4xMTUtMi41NTgtMTAuMjMtMTAuMjMtMTcuOTAyLTEyLjc4Ny0xNy45MDItMTAuMjMtMzUuODA0LTIwLjQ2LTU2LjI2NC0xNy45MDMtMTUuMzQ1IDAtMjguMTMyIDcuNjczLTM1LjgwNCAxNy45MDMtMTAuMjMgMTAuMjMtMTIuNzg4IDIzLjAxNy0xMC4yMyAzNS44MDQgNy42NzIgMjUuNTc0IDEyLjc4NyA1My43MDYgMjAuNDYgNzkuMjgxIDUxLjE1IDIuNTU4IDk5Ljc0IDE1LjM0NSAxNDMuMjE4IDQwLjkyIDQwLjkyIDI1LjU3NSA3OS4yOCA1OC44MjEgMTA5Ljk3IDk3LjE4MyAyNS41NzUgMzMuMjQ3IDQ2LjAzNSA3MS42MSA1Ni4yNjUgMTEyLjUzIDEyLjc4NiA0My40NzYgMTcuOTAxIDg5LjUxIDEyLjc4NiAxMzIuOTg2LTIuNTU3IDM4LjM2My0xMC4yMyA3NC4xNjYtMjMuMDE2IDEwOS45NzEtMzMuMjQ3IDg0LjM5Ni05Mi4wNyAxNjEuMTItMTcxLjM1IDIwOS43MTMtNTYuMjY1IDM1LjgwMy0xMjIuNzYgNTguODIxLTE4OS4yNTMgNjYuNDkzLTQ2LjAzNCA1LjExNS05Mi4wNjkgNS4xMTUtMTM4LjEwMi0yLjU1Ny05NC42MjctMTUuMzQ1LTE4MS41OC02MS4zOC0yNTAuNjMxLTEzMC40MzEtNjYuNDk1LTY2LjQ5My0xMTIuNTMtMTUzLjQ0OC0xMzIuOTktMjQ1LjUxNi03LjY3MS02OS4wNTItNy42NzEtMTM4LjEwMyA3LjY3My0yMDcuMTU0IDE3LjkwMy04MS44NCA2MS4zOC0xNjEuMTIgMTE3LjY0NC0yMjIuNSA0OC41OTItNTEuMTUgMTA3LjQxNC04OS41MTEgMTcxLjM1LTExNy42NDMgNy42NzItMi41NTggMTIuNzg3LTUuMTE1IDIwLjQ2LTcuNjczIDE1LjM0NC0yLjU1NyAzMC42OSAwIDQzLjQ3NyAxMC4yMyAxNy45MDIgMTIuNzg4IDI1LjU3NCAzMy4yNDggMjMuMDE3IDUzLjcwNy0yLjU1NyAyMC40Ni0xNy45MDIgMzguMzYzLTM1LjgwNSA0Ni4wMzQtNjMuOTM3IDI1LjU3NS0xMjIuNzU4IDY5LjA1Mi0xNjMuNjc4IDEyMi43Ni0zOC4zNjIgNTMuNzA1LTYzLjkzNiAxMTIuNTI3LTcxLjYwOCAxNzMuOTA2LTcuNjcyIDYxLjM4IDAgMTIyLjc1OCAyMC40NiAxODEuNTggMzAuNjkgODQuMzk2IDk0LjYyNiAxNTYuMDA0IDE3My45MDcgMTk2LjkyNCA0OC41OTIgMjUuNTc1IDEwMi4yOTggMzguMzYyIDE1Ni4wMDUgMzguMzYyIDQzLjQ3NyAwIDg5LjUxMS03LjY3MiAxMzAuNDMtMjMuMDE3IDM1LjgwNS0xMi43ODcgNzEuNjEtMzMuMjQ3IDk5Ljc0MS01OC44MjIgMjguMTMzLTIzLjAxNiA1MS4xNS01My43MDYgNjYuNDk1LTg0LjM5NiA3LjY3Mi0xNS4zNDUgMTcuOTAxLTMzLjI0NyAyMC40Ni01MS4xNSAxNS4zNDQtNTEuMTQ5IDE3LjkwMS0xMDcuNDEzIDIuNTU2LTE1OC41NjEtMTIuNzg2LTQzLjQ3OC0zOC4zNjEtODEuODQtNzEuNjA5LTEwOS45NzEtMTUuMzQ0LTEyLjc4Ny0zMC42OS0yNS41NzUtNDguNTkyLTM1LjgwNS0xNS4zNDQtNy42NzItMzAuNjktMTUuMzQ1LTQ4LjU5MS0xNy45MDIgMTIuNzg4IDQ2LjAzNCAyMy4wMTggOTIuMDcgMzUuODA0IDEzNS41NDUgMi41NTggMTAuMjMgNS4xMTUgMjMuMDE4IDUuMTE1IDMzLjI0OCAyLjU1OCA0Ni4wMzMtMTUuMzQ0IDk0LjYyNS00Ni4wMzQgMTMwLjQzLTI4LjEzMiAzMy4yNDYtNjkuMDUyIDU4LjgyMS0xMTIuNTI4IDY2LjQ5NC00Ni4wMzQgMTAuMjMtOTcuMTg0IDAtMTM4LjEwMy0yNS41NzUtMzguMzYyLTI1LjU3NC02Ni40OTQtNjMuOTM2LTgxLjg0LTEwNC44NTYtNy42NzItMjMuMDE3LTEyLjc4Ny00OC41OTEtMTIuNzg3LTc0LjE2Ni0yLjU1Ni01Ni4yNjQgMTIuNzg4LTEwOS45NzEgNDMuNDc4LTE1Ni4wMDUgMzUuODA0LTUzLjcwNyA5NC42MjUtOTIuMDcgMTU4LjU2Mi0xMDkuOTcxLTUuMTE1LTE3LjkwMi0xMC4yMy0zNS44MDUtMTIuNzg3LTUzLjcwNy0xMi43ODctMzguMzYxLTEwLjIzLTgxLjgzOSA3LjY3Mi0xMTUuMDg2IDEwLjIzLTIwLjQ2IDIzLjAxOC0zOC4zNjEgNDAuOTItNTEuMTUgMjMuMDE2LTIwLjQ2IDQzLjQ3Ni0zMy4yNDYgNjYuNDk0LTQwLjkxOE00NzguNzUzIDQxOS40MjRjLTE3LjkwMyAxNy45MDItMjguMTMzIDQwLjkyLTMzLjI0NyA2My45MzYtNS4xMTQgMjAuNDYtNS4xMTQgNDMuNDc3IDAgNjYuNDk1IDUuMTE0IDIzLjAxNiAxNy45MDIgNDYuMDMzIDM4LjM2MiA2MS4zOCAxNS4zNDUgMTAuMjI4IDM1LjgwNCAxNS4zNDMgNTYuMjY0IDEwLjIyOCAzNS44MDQtNS4xMTUgNjMuOTM2LTM4LjM2MiA2My45MzYtNzQuMTY2LTIuNTU3LTcuNjcyLTIuNTU3LTE3LjkwMi01LjExNS0yNS41NzUtMTIuNzg3LTQ4LjU5Mi0yNS41NzMtOTkuNzQxLTM4LjM2MS0xNDguMzMzLTMwLjY5IDcuNjczLTU4LjgyMiAyMy4wMTgtODEuODQgNDYuMDM1eiIgZmlsbD0iI2ZmZiIvPjwvc3ZnPg==&longCache=true)](https://music.163.com/?from=infinity#/user/home?id=596006674) [![douyin](https://img.shields.io/badge/%E6%8A%96%E9%9F%B3-52-pink?logo=tiktok)](https://www.douyin.com/user/MS4wLjABAAAA_CY_CeCScPPCisOkDiwYyy75KvacuYh_jexNwgxj7P8) [![instagram](https://img.shields.io/badge/dynamic/json?label=Instagram&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dinstagram%26queryKey%3Deewhile0212&logo=instagram&labelColor=d8415f&logoColor=white&color=white)](https://www.instagram.com/eewhile0212/)<br>
![QQ](https://img.shields.io/badge/-1026224216-informational?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iODAwIiB3aWR0aD0iMTIwMCIgdmlld0JveD0iLTE4LjE1IC0zNS45NzI1IDE1Ny4zIDIxNS44MzUiPjxwYXRoIGZpbGw9IiNmYWFiMDciIGQ9Ik02MC41MDMgMTQyLjIzN2MtMTIuNTMzIDAtMjQuMDM4LTQuMTk1LTMxLjQ0NS0xMC40Ni0zLjc2MiAxLjEyNC04LjU3NCAyLjkzMi0xMS42MSA1LjE3NS0yLjYgMS45MTgtMi4yNzUgMy44NzQtMS44MDcgNC42NjMgMi4wNTYgMy40NyAzNS4yNzMgMi4yMTYgNDQuODYyIDEuMTM2em0wIDBjMTIuNTM1IDAgMjQuMDM5LTQuMTk1IDMxLjQ0Ny0xMC40NiAzLjc2IDEuMTI0IDguNTczIDIuOTMyIDExLjYxIDUuMTc1IDIuNTk4IDEuOTE4IDIuMjc0IDMuODc0IDEuODA1IDQuNjYzLTIuMDU2IDMuNDctMzUuMjcyIDIuMjE2LTQ0Ljg2MiAxLjEzNnptMCAwIi8+PHBhdGggZD0iTTYwLjU3NiA2Ny4xMTljMjAuNjk4LS4xNCAzNy4yODYtNC4xNDcgNDIuOTA3LTUuNjgzIDEuMzQtLjM2NyAyLjA1Ni0xLjAyNCAyLjA1Ni0xLjAyNC4wMDUtLjE4OS4wODUtMy4zNy4wODUtNS4wMUMxMDUuNjI0IDI3Ljc2OCA5Mi41OC4wMDEgNjAuNSAwIDI4LjQyLjAwMSAxNS4zNzUgMjcuNzY5IDE1LjM3NSA1NS40MDFjMCAxLjY0Mi4wOCA0LjgyMi4wODYgNS4wMSAwIDAgLjU4My42MTUgMS42NS45MTMgNS4xOSAxLjQ0NCAyMi4wOSA1LjY1IDQzLjMxMiA1Ljc5NXptNTYuMjQ1IDIzLjAyYy0xLjI4My00LjEyOS0zLjAzNC04Ljk0NC00LjgwOC0xMy41NjggMCAwLTEuMDItLjEyNi0xLjUzNy4wMjMtMTUuOTEzIDQuNjIzLTM1LjIwMiA3LjU3LTQ5LjkgNy4zOTJoLS4xNTNjLTE0LjYxNi4xNzUtMzMuNzc0LTIuNzM3LTQ5LjYzNC03LjMxNS0uNjA2LS4xNzUtMS44MDItLjEtMS44MDItLjEtMS43NzQgNC42MjQtMy41MjUgOS40NC00LjgwOCAxMy41NjgtNi4xMTkgMTkuNjktNC4xMzYgMjcuODM4LTIuNjI3IDI4LjAyIDMuMjM5LjM5MiAxMi42MDYtMTQuODIxIDEyLjYwNi0xNC44MjEgMCAxNS40NTkgMTMuOTU3IDM5LjE5NSA0NS45MTggMzkuNDEzaC44NDhjMzEuOTYtLjIxOCA0NS45MTctMjMuOTU0IDQ1LjkxNy0zOS40MTMgMCAwIDkuMzY4IDE1LjIxMyAxMi42MDcgMTQuODIyIDEuNTA4LS4xODMgMy40OTEtOC4zMzItMi42MjctMjguMDIxIi8+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTQ5LjA4NSA0MC44MjRjLTQuMzUyLjE5Ny04LjA3LTQuNzYtOC4zMDQtMTEuMDYzLS4yMzYtNi4zMDUgMy4wOTgtMTEuNTc2IDcuNDUtMTEuNzczIDQuMzQ3LS4xOTUgOC4wNjQgNC43NiA4LjMgMTEuMDY1LjIzOCA2LjMwNi0zLjA5NyAxMS41NzctNy40NDYgMTEuNzcxbTMxLjEzMy0xMS4wNjNjLS4yMzMgNi4zMDItMy45NTEgMTEuMjYtOC4zMDMgMTEuMDYzLTQuMzUtLjE5NS03LjY4NC01LjQ2NS03LjQ0Ni0xMS43Ny4yMzYtNi4zMDUgMy45NTItMTEuMjYgOC4zLTExLjA2NiA0LjM1Mi4xOTcgNy42ODYgNS40NjggNy40NDkgMTEuNzczIi8+PHBhdGggZmlsbD0iI2ZhYWIwNyIgZD0iTTg3Ljk1MiA0OS43MjVDODYuNzkgNDcuMTUgNzUuMDc3IDQ0LjI4IDYwLjU3OCA0NC4yOGgtLjE1NmMtMTQuNSAwLTI2LjIxMiAyLjg3LTI3LjM3NSA1LjQ0NmEuODYzLjg2MyAwIDAwLS4wODUuMzY3Ljg4Ljg4IDAgMDAuMTYuNDk2Yy45OCAxLjQyNyAxMy45ODUgOC40ODcgMjcuMyA4LjQ4N2guMTU2YzEzLjMxNCAwIDI2LjMxOS03LjA1OCAyNy4yOTktOC40ODdhLjg3My44NzMgMCAwMC4xNi0uNDk4Ljg1Ni44NTYgMCAwMC0uMDg1LS4zNjUiLz48cGF0aCBkPSJNNTQuNDM0IDI5Ljg1NGMuMTk5IDIuNDktMS4xNjcgNC43MDItMy4wNDYgNC45NDMtMS44ODMuMjQyLTMuNTY4LTEuNTgtMy43NjgtNC4wNy0uMTk3LTIuNDkyIDEuMTY3LTQuNzA0IDMuMDQzLTQuOTQ0IDEuODg2LS4yNDQgMy41NzQgMS41OCAzLjc3MSA0LjA3bTExLjk1Ni44MzNjLjM4NS0uNjg5IDMuMDA0LTQuMzEyIDguNDI3LTIuOTkzIDEuNDI1LjM0NyAyLjA4NC44NTcgMi4yMjMgMS4wNTcuMjA1LjI5Ni4yNjIuNzE4LjA1MyAxLjI4Ni0uNDEyIDEuMTI2LTEuMjYzIDEuMDk1LTEuNzM0Ljg3NS0uMzA1LS4xNDItNC4wODItMi42Ni03LjU2MiAxLjA5Ny0uMjQuMjU3LS42NjguMzQ2LTEuMDczLjA0LS40MDctLjMwOC0uNTc0LS45My0uMzM0LTEuMzYyIi8+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTYwLjU3NiA4My4wOGgtLjE1M2MtOS45OTYuMTItMjIuMTE2LTEuMjA0LTMzLjg1NC0zLjUxOC0xLjAwNCA1LjgxOC0xLjYxIDEzLjEzMi0xLjA5IDIxLjg1MyAxLjMxNiAyMi4wNDMgMTQuNDA3IDM1LjkgMzQuNjE0IDM2LjFoLjgyYzIwLjIwOC0uMiAzMy4yOTgtMTQuMDU3IDM0LjYxNi0zNi4xLjUyLTguNzIzLS4wODctMTYuMDM1LTEuMDkyLTIxLjg1NC0xMS43MzkgMi4zMTUtMjMuODYyIDMuNjQtMzMuODYgMy41MTgiLz48cGF0aCBmaWxsPSIjZWIxOTIzIiBkPSJNMzIuMTAyIDgxLjIzNXYyMS42OTNzOS45MzcgMi4wMDQgMTkuODkzLjYxNlY4My41MzVjLTYuMzA3LS4zNTctMTMuMTA5LTEuMTUyLTE5Ljg5My0yLjMiLz48cGF0aCBmaWxsPSIjZWIxOTIzIiBkPSJNMTA1LjUzOSA2MC40MTJzLTE5LjMzIDYuMTAyLTQ0Ljk2MyA2LjI3NWgtLjE1M2MtMjUuNTkxLS4xNzItNDQuODk2LTYuMjU1LTQ0Ljk2Mi02LjI3NUw4Ljk4NyA3Ni41N2MxNi4xOTMgNC44ODIgMzYuMjYxIDguMDI4IDUxLjQzNiA3Ljg0NWguMTUzYzE1LjE3NS4xODMgMzUuMjQyLTIuOTYzIDUxLjQzNy03Ljg0NXptMCAwIi8+PC9zdmc+) ![wechat](https://img.shields.io/badge/-rain6842169-07c160?logo=wechat&logoColor=white) [![mail](https://img.shields.io/badge/QQmail-1026224216@qq.com-blue?logo=data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjIuODggOTAuNTQiPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojMmIzMzQ0O30uY2xzLTJ7ZmlsbDojZmUwMDAwO2ZpbGwtcnVsZTpldmVub2RkO30uY2xzLTN7ZmlsbDojZmZmO308L3N0eWxlPjwvZGVmcz48dGl0bGU+bmV3LW1haWw8L3RpdGxlPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTAsODcuMjQsMzQuNTEsNTIuMTgsMCwyMy42N1Y4Ny4yNFptMy42NC02Ni45TDUxLjgxLDU5bDE3LjkyLTE1YTMyLjc0LDMyLjc0LDAsMCwxLTUtMjMuNlpNMzguODMsNTUuNzksMy43LDkwLjU0SDk3Ljg3TDY0LjM0LDU1LjgsNTMuNDUsNjUuNDdoMGEyLjQ2LDIuNDYsMCwwLDEtMy4xNywwTDM4LjgzLDU1Ljc5Wm0yOS43NS0zLjY4LDMzLjI5LDM1LjQxVjU4LjI4QTMyLjgyLDMyLjgyLDAsMCwxLDczLjEsNDguMjFsLTQuNTIsMy45WiIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTk3LjA5LDBhMjUuOCwyNS44LDAsMSwxLTI1LjgsMjUuNzlBMjUuNzksMjUuNzksMCwwLDEsOTcuMDksMFoiLz48cGF0aCBjbGFzcz0iY2xzLTMiIGQ9Ik05My44MywzMS4zNlYyMC4yN2E3LjI5LDcuMjksMCwwLDEtNC42LDIuMzFWMTYuMjljMi4xLS4yLDQuODYtMS40OCw2LTMuMzVoNi4wOFYzMS4zNkgxMDV2NS43SDkwdi01LjdaIi8+PC9zdmc+&labelColor=white)](https://mail.qq.com) [![gmail](https://img.shields.io/badge/Gmail-cjy1026224216@gmail.com-orange?logo=Gmail&labelColor=white)](https://mail.google.com/mail)<br>
[![sysu](https://img.shields.io/badge/%20SYSU-系统与进化基因组学实验室-black?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMTAyLjM0IDEyMi44OCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTAyLjM0IDEyMi44OCIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+PHN0eWxlIHR5cGU9InRleHQvY3NzIj48IVtDREFUQVsNCgkuc3Qwe2ZpbGwtcnVsZTpldmVub2RkO2NsaXAtcnVsZTpldmVub2RkO30NCl1dPjwvc3R5bGU+PGc+PHBhdGggY2xhc3M9InN0MCIgZD0iTTUzLjM2LDMuMzFjOC43LTYuMDEsOS4zNSw1Ljg5LDE3Ljg5LTEuNTVWMTMuOWMtOC4xNCw3LjMzLTkuOS00LjUxLTE3Ljg5LDEuNVYzLjMxTDUzLjM2LDMuMzFMNTMuMzYsMy4zMXogTTQ5LjQ1LDM3LjAxaDEuNTJjMC4yOCwwLDAuNSwwLjIzLDAuNSwwLjV2NS44NGg1LjMzYzAuMjgsMCwwLjUsMC4yMywwLjUsMC41djEuNTJjMCwwLjI4LTAuMjMsMC41LTAuNSwwLjVoLTcuODZ2LTguMzcgQzQ4Ljk0LDM3LjI0LDQ5LjE3LDM3LjAxLDQ5LjQ1LDM3LjAxTDQ5LjQ1LDM3LjAxTDQ5LjQ1LDM3LjAxeiBNNTEuMTcsMzAuMTdjNi44NSwwLDEyLjQsNS41NSwxMi40LDEyLjQgYzAsNi44NS01LjU1LDEyLjQtMTIuNCwxMi40Yy02Ljg1LDAtMTIuNC01LjU1LTEyLjQtMTIuNEMzOC43NywzNS43Myw0NC4zMiwzMC4xNyw1MS4xNywzMC4xN0w1MS4xNywzMC4xN0w1MS4xNywzMC4xN3ogTTUyLjg3LDcxLjc0djQwLjI3aDEyLjI1VjcxLjc0SDUyLjg3TDUyLjg3LDcxLjc0eiBNNDkuNDcsMTEyLjAxVjcxLjc0SDM3LjIybDAsMHY0MC4yN0g0OS40N0w0OS40NywxMTIuMDF6IE0xMDIuMzQsMTIyLjg1IFY1MS44Nkg3NS4zOFYzNC42N0w1Mi4xMywxOS42OVYzLjA5aC0wLjA4YzAuNDktMC4yOCwwLjgxLTAuODIsMC44MS0xLjQzYzAtMC45Mi0wLjc0LTEuNjYtMS42Ni0xLjY2cy0xLjY2LDAuNzQtMS42NiwxLjY2IGMwLDAuNjEsMC4zMywxLjE0LDAuODEsMS40M2gtMC4wOHYxNi41N2wtMjMuMywxNS4wMXYxNy4xOUg3LjIzSDB2NzEuMDJDMzQuMTIsMTIyLjg4LDY4LjIyLDEyMi44NSwxMDIuMzQsMTIyLjg1TDEwMi4zNCwxMjIuODUgTDEwMi4zNCwxMjIuODV6IE0xMC45OSw3MS43NGgxMy40OXY1LjI1SDEwLjk5VjcxLjc0TDEwLjk5LDcxLjc0TDEwLjk5LDcxLjc0eiBNNzcuODUsNzEuNzRoMTMuNDl2NS4yNUg3Ny44NVY3MS43NEw3Ny44NSw3MS43NCBMNzcuODUsNzEuNzR6IE0xMC45OSw4My4zM2gxMy40OXY1LjI1SDEwLjk5VjgzLjMzTDEwLjk5LDgzLjMzTDEwLjk5LDgzLjMzeiBNNzcuODUsODMuMzNoMTMuNDl2NS4yNUg3Ny44NVY4My4zM0w3Ny44NSw4My4zMyBMNzcuODUsODMuMzN6IE0xMC45OSw5NC45MmgxMy40OXY1LjI1SDEwLjk5Vjk0LjkyTDEwLjk5LDk0LjkyTDEwLjk5LDk0LjkyeiBNNzcuODUsOTQuOTJoMTMuNDl2NS4yNUg3Ny44NVY5NC45Mkw3Ny44NSw5NC45MiBMNzcuODUsOTQuOTJ6IE0xMC45OSwxMDYuNTFoMTMuNDl2NS4yNUgxMC45OVYxMDYuNTFMMTAuOTksMTA2LjUxTDEwLjk5LDEwNi41MXogTTc3Ljg1LDEwNi41MWgxMy40OXY1LjI1SDc3Ljg1VjEwNi41MSBMNzcuODUsMTA2LjUxTDc3Ljg1LDEwNi41MXoiLz48L2c+PC9zdmc+&labelColor=darkgreen)](https://www.labxing.com/lab/719/members)
</div>

# Update

**2022-07-27**

