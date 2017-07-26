import importlib
from config import settings

def server_info(hostname=None):
    ret = {}
    for k,v in settings.PLUGINS_ITEMS.items():
        file_path,class_name = v.rsplit('.',1)
        # file_path = "src.plugins.disk"
        # class_name = "DiskPlugin"
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