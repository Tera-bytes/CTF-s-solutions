import re
import time
#Before writing this script, I initially extracted all the regex from the logs file to a file named regex.txt (but that's pretty useless; 
#so you might not go for it)

f=open("regex.txt","r")  #regex.txt contains all the regular expressions
g=open("dictionary.txt","r")
timing=open("time.txt","w") #time.txt records the time taken by each regex to go through the given dictionary
regex=f.readlines()
dictionary=g.readlines()

for elmt in regex:
    start=time.time()
    for dict in dictionary:
        lst=re.findall(elmt[:-1],dict[:-1]) #findall outputs a list containing all the occurrences of the string (elmt).
                                            #[:-1] to exclude the new line character that may spoil some stuffs here!
        
    a="%.3f"%(time.time()-start) #NB: a is now a string and not a float
    timing.write(a + "\n")
    
    #REMARK:
    #To reduce your execution time (which is way too large), you can use do the following combined (I noticed it lately):
    #    *use a single for loop,
    #    *replace the "findall" instruction by "search()", and
    #    *instead of taking the content of the dictionary in the form of a list, you could take it in the form of a string using
    #    read() instead of readlines()
