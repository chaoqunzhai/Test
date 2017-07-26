import pickle
# data = {
#     'name':"alex",
#     "age":22,
#     "sex": "M",
# }
# with open('11','wb') as f:
#     pickle.dump(data,f)


with open('db_teacher',encoding='utf-8') as tfile:
    print(tfile.read())

# with open('day7_db','rb') as f1:
#     date=pickle.loads(f1.read())
#     print(date)

    # if os.path.isfile('db'):
    #     newname = 'db' + self.name
    #     os.rename('db', newname)
    # else:
    #     print('register the instance!')