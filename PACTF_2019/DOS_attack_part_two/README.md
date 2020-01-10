# Denial of Searching attack, Part Two: Crash Collision!

So, the first thing is to identify what causes the DOS, and as the title implies, it's due to crash collion (precisely: hash collision). Let me try to give a brief explanation (in case you ain't familiar with hash tables):

#### Question: How is a hash table used to store data?

#### Answer: 
let's say we want to store string A in our hash table. String A is hashed (using the provided hash function), and the output is an integer(4 for example). That integer (known as the hash) is the index at which A is stored in the hash table. Now, let's assume we got another string B to be stored. Remember you already stored A in the hash table at position "4". Now, upon hashing B you still get "4", whereas that position is already occupied by A:hence the name hash collision (and that's where things start going south). If such a thing happens a bunch of times, your server/database will simply crash.


So, the task was to write a script that will find the file that leads to the greatest number of collisions. I over simplified the script by just comparing two elements in each file. Upon executing my code, I got these flags:

        flag{Bull_Herald_Her}
        flag{Celtic_Verbal_Qui}
        flag{Dos_Funded_Actor}
        flag{Drivers_Mouse_Nonprofit}
        flag{Helpful_Extent_Arkansas}
        flag{Just_Potatoes_Ball}
        flag{Shepherd_Acrylic_Luke}
        
Then I found the flag to be the third one:
# flag{Dos_Funded_Actor}

Yeah I know that was a pretty crazy assumption (as the flag could easily not have been part of those 8). Anyways, you could easily add a few more lines to get the total number of collisions of each file, and then extract the one with the highest collision (see https://github.com/Ptomerty/ctf-dump/tree/master/pactf-2019/denial-of-searching-2 for such an approach)
