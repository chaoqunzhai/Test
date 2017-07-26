#-*- coding:utf-8 -*-
import redis
conn =redis.Redis(host='192.168.12.48')
conn.publish('zcq','报警了！！！！！！！')