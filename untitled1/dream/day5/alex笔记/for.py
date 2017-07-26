


data = [1,2,3,4,5,6,7]

for index,i in enumerate(data):
    data[index] +=1


print(data)
data = [ i+1 for i in data]
data = [ i*2 if i >5 else i for i in data]
print(data)