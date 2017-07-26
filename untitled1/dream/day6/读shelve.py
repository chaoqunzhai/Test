import shelve
def sayhai(name,gae):
    print('you name %s is age%s' %(name,age))

f=shelve.open('shelve_obj')

print(f['name'])
print(f['test'])