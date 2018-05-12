import hashlib

st = 'wewqeqe'.encode('utf8')

hst = hashlib.sha1()
hst.update(st)
print(hst.hexdigest())