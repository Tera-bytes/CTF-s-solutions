# Lost Password
This was pretty straight forward, as you just had to write a few lines of code to fetch the password:
 "help", "copyright", "credits" or "license" for more information.
>>> f=open(r"C:\Users\youmb\OneDrive\Desktop\data.txt","r")
>>> a=f.readlines()
>>> for elmt in a:
...     elmt=elmt[:-1]
...     if len(elmt)==20 and elmt.startswith("fe") and elmt.endswith("g"): print(elmt)


