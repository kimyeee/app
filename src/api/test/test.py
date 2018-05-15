import hashlib

st = '3946cab88d6af5b20744472a8980fddb1234sad567891526267968'.encode('utf8')

hst = hashlib.sha1()
hst.update(st)
print(hst.hexdigest())