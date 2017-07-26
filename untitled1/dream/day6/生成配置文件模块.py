import configparser
config=configparser.ConfigParser()

config["DEBUG"] ={'Servename':'192.168.23.50',
                  'Compression':'yes',
                  'Compressionlevel':'9'}
config['www.cnblogs.com'] = {}
config['www.cnblogs.com']['user']='zhaichaoqun'
config['www.cnblogs.com']['id'] ='2457'
config['home']={}
top=config['home']
top['Host id'] ='844612'
top['Forwareall']='True'
config['DEBUG']['Forwareall'] = 'yes'
#with open('ceshi3.ini','w') as f:
#    config.write(f)
print(config.sections())
#print(config.options('home'))
