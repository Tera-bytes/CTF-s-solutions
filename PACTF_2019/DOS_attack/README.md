# DENIAL OF SEARCHING ATTACK!
The key to this is knowing what **regexes** are. The threat here is what is known as **ReDOS (Regular expressions Denial Of Service)**: This is a situation where a regex takes an exponential time to process a given string/data. Such regexes are call **malicious/evil** regexes.

I wrote a script that writes the time taken by each regex to go through the entire list of words, and at the end I just had to extract the one which took the longest. I eventually got the flag:

### flag{Housewives_Headlines_Cosmetic}
which took 0.909s to go through the dictionary (NB: that time is surely system dependent). This is around 45 times the time taken by the average regex.
#### Question: Guess what's the **huge** drawback of this method!

#### Answer: 
This code took around 5hrs to reach to completion. However, this ain't **totally** the fault of the script. Look at it this way: each regex took at least 0.02 to go through the dictionary, but we had a million of them! That does explains while it took so long!

After solving it, I reached one of the administrators of PACTF and I was told that wasn't the right approach (though correct). See below link to the writeup made by the problem maker himself:

https://nicholas-miklaucic.github.io/posts/pactf-2019-writeup-denial-of-service-attack/
