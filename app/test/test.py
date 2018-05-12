import hashlib

st = 'wewqeqe'

hst = hashlib.sha1()
hst.update(st)
print(hst.hexdigest())