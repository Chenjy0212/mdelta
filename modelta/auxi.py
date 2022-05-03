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