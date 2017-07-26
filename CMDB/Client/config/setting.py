


MODE = 'SSH'  #Agent,Salt,SSH

ERROR_LOG_PATH = "log/error.log"

RUN_LOG_PATH= "log/run.log"

PLUGINS_ITEMS = {
    'disk':'src.plugin.disk.DiskPlugin',
    'nic':'src.plugin.nic.NicPlugin',
}