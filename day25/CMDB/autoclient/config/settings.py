
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

MODE = "SSH" # Agent,Salt,SSH


ERROR_LOG_PATH = "log/error.log"
RUN_LOG_PATH = "log/run.log"

PLUGINS_ITEMS = {
    'disk': "src.plugins.disk.DiskPlugin",
    'nic': "src.plugins.nic.NicPlugin",
    'mem': "src.plugins.mem.MemPlugin",
}

API = "http://127.0.0.1:8000/post-info.html"