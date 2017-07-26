import os
import sys

BaseDir = os.path.abspath( os.path.dirname(os.path.dirname(__file__))  )
BaseDir =  os.path.dirname(os.path.dirname(   os.path.abspath(__file__)   ))
sys.path.append(BaseDir)
print(sys.path)
# for i in sys.path:
#     print(i)
#


