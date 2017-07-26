import tarfile
tar_obj=tarfile.open(r'C:\zcq.zip','w')
tar_obj.add(r"C:\Users\Administrator\PycharmProjects\untitled1")
tar_obj.add(r"C:\Users\Administrator\PycharmProjects\untitled1\ATM",arcname='zhaichaoqun')
tar_obj.close()