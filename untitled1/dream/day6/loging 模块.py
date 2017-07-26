import logging

loger=logging.getLogger('nginx')
loger.setLevel(logging.DEBUG)


fh=logging.StreamHandler()
fh.setLevel(logging.DEBUG)

fh=logging.FileHandler('ceshi.log',encoding='utf-8')
fh.setLevel(logging.WARNING)

ch=logging.Formatter('%(asctime)s - %(name)s -  %(filename)s %(levelname)s - %(message)s')

fh.setFormatter(ch)

loger.addHandler(fh)

loger.debug('debug message')
loger.info('info message')
loger.warn('warn message')
loger.error('error message')
loger.critical('critical message')