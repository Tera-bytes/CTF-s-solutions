from hashlib import md5

Hash="832c8f6be1b48ce9abcd6deb4ebcdc31"
salt="counterspell"
f=open("path_to_dictionary","r")
lst=f.readlines()
for elmt in lst:
    elmt=elmt[:-1]
    password=elmt + salt
    get_hash=md5(password.encode())
    if get_hash.hexdigest()==Hash:
       print(elmt)
       break
