import os

def quickhash(string):
	hash_=0
	for i,char in enumerate(string):
		hash_ += 31 ** i *ord(char)
		hash_ = hash_ % (2 ** 32)
	return hash_

i=0
list=os.listdir("path_to_your_folder")
for file in list:
    with open("C:/Users/youmb/Downloads/serverlog.4af8e4389eff/logs/" + file, "r") as f:
        cont=f.readlines()
        a=cont[0] #I will just extract their contents at positions 0 and 5 (I chose this positions randomly)
        a=a[:-1]
        b=cont[5]
        b=b[:-1]
        if quickhash(a)==quickhash(b): print(file)
