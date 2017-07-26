from config import settings


##这样的话 就把这个plugins做成一个公共的完整的插件，与其他部分没有关系
#你如果想获取主机的各种信息 你只要导入这个plugins 就可以获得所有信息

def server_info(hostname=None):
    ret = {}
    for k,v in settings.PLUGINS_ITEMS.items():
        file_path,class_name = v.rsplit('.',1)
        # file_path = "src.plugins.disk"
        # class_name = "DiskPlugin"
        import importlib
        # 导入模块
        m = importlib.import_module(file_path)
        # 去模块中获取类
        cls = getattr(m,class_name)
        # 根据类创建对象
        obj = cls(hostname)
        # 执行对象的execute用于获取资产信息(对象)
        xx_info = obj.execute()
        ret[k] = xx_info.__dict__

    return ret
if __name__ == '__main__':
    server_info()