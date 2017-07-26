import random

def gen_fore(n):
    ids = list(range(1,n+1))
    yi = ['赵','钱','王','李','任','夏']
    er = ['刚','噶','二','三','四','五',]
    san = ['六','七','嗨','腌','海',]
    for i in range(n):
        id = ids[i]
        age = random.randint(18,100)
        name = random.choice(yi) + random.choice(er) + random.choice(san)
        print(name)

gen_fore(100)
def bin_search(data_set, val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return