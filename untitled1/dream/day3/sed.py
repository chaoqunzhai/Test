#2016年10月24日19:52:36
##伪sed替换
import sys
mulu=sys.argv[1]
mulu2=sys.argv[2]
f=sys.argv[3]
f1=open(f,r)
f2=open(f.w)
for line in f1:
    if mulu in line:
        line = line.replace(mulu,mulu2)
    f2.write(line)
f1.close()
f2.close()