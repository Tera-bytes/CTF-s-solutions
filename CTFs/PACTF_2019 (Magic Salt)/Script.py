from hashlib import md5

salt="counterspell" #which I discovered earlier
Hash="832c8f6be1b48ce9abcd6deb4ebcdc31" #which was given in the question
f=open("library.txt","r")
lines=f.readlines() #lines is a list in which each element ends with "\n" character

for i in lines:
    string=i[:-1]+salt # i[:-1] is to make sure the last character "\n" isn't considered
    if md5(string.encode()).hexdigest() == Hash:
        print(string)
        break

f.close()