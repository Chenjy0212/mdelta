# modelta

Chen and Yang Lab Multi fork Development cell lineage tree alignment.

<!-- TOC -->

- [modelta](#modelta)
  - [01 Brief introduction](#01-brief-introduction)
  - [02 Result](#02-result)

<!-- /TOC -->

## 01 Brief introduction

>pip install modelta

Then you can use this function in your Python code. As shown below(**/modelta/test2.py**):

```python
import modelta
modelta.demola()
print(modelta.scoremat('modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv','modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv'))
```

## 02 Result

>something output!
Matrix Node: 100%|¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€| 121/121 [00:00<00:00, 30337.19it/s]
Root2                    a    b    c    d    e    f    a  (a,b,c)  (e,f)  ((a,b,c),d,(e,f))  (((a,b,c),d,(e,f)),a)
Root1
a                      4.0 -1.0  0.0 -1.0  2.0  2.0  4.0      2.0    1.0               -1.0                   -1.0
b                     -2.0  4.0  1.0  0.0 -2.0  0.0 -2.0      2.0   -1.0               -1.0                   -1.0
c                     -2.0  1.0  4.0 -1.0  0.0 -1.0 -2.0      2.0   -1.0               -1.0                   -1.0
d                     -2.0  0.0 -2.0  4.0  2.0  0.0 -2.0     -1.0    1.0               -1.0                   -1.0
e                     -2.0 -2.0 -2.0 -1.0  4.0 -1.0 -2.0     -1.0    3.0               -1.0                   -1.0
f                      0.0  2.0  2.0  1.0 -2.0  4.0  0.0      0.0    3.0               -1.0                   -1.0
a                      4.0 -1.0  0.0 -1.0  2.0  2.0  4.0      2.0    1.0               -1.0                   -1.0
(a,b,c)                2.0  2.0  2.0 -1.0  0.0  0.0  2.0     12.0    1.0                9.0                    8.0
(e,f)                 -1.0  1.0  1.0  0.0  3.0  3.0 -1.0     -1.0    8.0                4.0                    3.0
((a,b,c),d,(e,f))     -1.0 -1.0 -1.0 -1.0 -1.0 -1.0 -1.0      9.0    4.0               24.0                   23.0
(((a,b,c),d,(e,f)),a) -1.0 -1.0 -1.0 -1.0 -1.0 -1.0 -1.0      8.0    3.0               23.0                   28.0
