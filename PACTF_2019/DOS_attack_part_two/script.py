import os

def quickhash(string):
	hash_=0
	for i,char in enumerate(string):
		hash_ += 31 ** i *ord(char)
		hash_ = hash_ % (2 ** 32)
	return hash_

i=0
list=os.listdir(r"C:\Users\youmb\Downloads\serverlog.4af8e4389eff\logs")
print(list)
for file in list:
    with open("C:/Users/youmb/Downloads/serverlog.4af8e4389eff/logs/" + file, "r") as f:
        cont=f.readlines()
        a=cont[0]
        a=a[:-1]
        b=cont[5]
        b=b[:-1]
        if quickhash(a)==quickhash(b): print(file)
