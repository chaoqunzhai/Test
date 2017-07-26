data = [3,5,6,7,25,56,60,70,90,100]
def binarg(datasets,number):
    if int(len(datasets)/2) >0:
        middle_pos = int(len(datasets)/2)
        if datasets[middle_pos] == number:
            print('num',datasets[middle_pos])
        elif datasets[middle_pos] > number:
            print('查询数值不在右边',datasets[0:middle_pos],datasets[middle_pos])
            binarg(datasets[0:middle_pos],number)
        else:
            print('查询数值在左边',datasets[middle_pos+1:],datasets[middle_pos])
            binarg(datasets[middle_pos + 1:], number)
    else:
        print('查询数值不在')

binarg(data,100)