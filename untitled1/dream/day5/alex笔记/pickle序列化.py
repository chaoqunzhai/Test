import pickle

def sayhi():
    print("hey")
data = {
    'name':"alex",
    "age":22,
    "sex": "M",
    "func": sayhi
}

f = open("data.pkl","wb",)
f.write(pickle.dumps(data) )
f1=open("data.pkl","rb",)
data = pickle.loads(f.read())
print(data['name'])
