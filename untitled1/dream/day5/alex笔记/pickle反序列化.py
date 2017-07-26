

import pickle

def sayhi():
    print("hahahhah")

f = open("data.pkl","rb")
data = pickle.loads(f.read())

print(data["age"]())