duochelist=['duoche118','duoche119','duoche130','duoche131','duoche132','duoche133','duoche137','duoche138']
minion_id = 'duoche130'
test={}
for i in duochelist:
    if minion_id == i:
        test[i] = duochelist.index(i)
        print(test)
        # print(i,duochelist.index(i))