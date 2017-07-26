a = 5
b = 4
n = 10
d = a if a>10 else b
print(b)


print('------------------------')

def say(n):
    return -n
data=map(lambda  n:n*n if n>5 else n,range(10))
date2=map(lambda n:n*n if n>5 else say(n),range(10))
for i in data:
    print(i)

print('------------------------')

for q in date2:
    print(q)