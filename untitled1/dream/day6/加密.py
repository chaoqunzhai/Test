import hashlib
import hmac
m=hashlib.md5()
m.update(b'admin')
print(m.hexdigest())
m.update(b'123')
print(m.hexdigest())         #打印的时2个update追加到一起的

m3=hashlib.md5()
m3.update(b'admin123')
print(m3.hexdigest())          #跟上面一样


hash = hashlib.sha256()
hash.update(b'admin')
print(hash.hexdigest())

hash = hashlib.sha512()
hash.update(b'admin')
print(hash.hexdigest())

h=hmac.new(b'zhaichaoqun')
h.update(b'rengchenghon')
print(h.hexdigest())