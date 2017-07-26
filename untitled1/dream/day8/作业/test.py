import os
# afile = 'Download'
# print(os.getcwd())
# os.chdir(afile)
# print(os.getcwd())
# with open('11','w') as f:
#     f.write('111')
ainput=input('>>')
print(type(ainput))
if os.path.isfile(ainput):
    print('11111')
    fileSize = os.path.getsize(ainput)
    print(fileSize)
else:
    print('--')