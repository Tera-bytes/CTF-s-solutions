# How'd I Get Hacked

Firstly, I realised most of the files were of length 21. So, to be sure, I wrote a script that outputs files of length different from 21. To my great surprise, there was one: **flag{qdolctmyâ€®{fdp.exeâ€¬**. But, when I tried looking for that in the .dat file, it didn't exist: instead, there was one flag similar to that, which was our flag:
## flag{qdolctmy‮{fdp.exe‬
(and that's it! question solved)

Now, the million-dollar question is: **where is "flag{qdolctmyâ€®{fdp.exeâ€¬" coming from? or in other words, why is "flag{qdolctmyexe.pdf}" our flag?**

So, to look closely at what was going on, I opened the .dat file in a hex editor and scroll to where that flag was. Surprisingly, what I saw in the hex editor was slightly different from what appeared in the .dat file. That's, in the .dat file I saw "flag{qdolctmy‮{fdp.exe‬", while in the hex editor (at that same position) I instead saw "flag{qdolctmyâ€®{fdp.exeâ€¬". 

NB:I was using HxD editor on Windows, whose default code page is ANSI.

Notice these weird characters: "â€®" and "â€¬". Their respective hex values are "E2 80 AE" (**U+202E**) and "E2 80 AC" (**U+202C**). In fact, "E2 80 AE"  causes a right-to-left override, meanwhile "E2 80 AC" cancels the effect of any previous override.

Example: if you open a hex editor and type:

**E2 80 AE** 62 61 6E 61 6E 61 **E2 80 AC** 20 72 69 63 65 (where "62 61 6E 61 6E 61" and "72 69 63 65" stand for banana and rice respectively), what you will see in a text editor will be: **ananab rice** . That's, the word banana would be flipped. 

Let's apply it to our problem. We see the following in a hex editor:

**E2 80 AE** 7B 66 64 70 2E 65 78 65 **E2 80 AC** ( â€®{fdp.exeâ€¬),

which means what will appear in a text editor won't be "{fdp.exe", but instead exe.pdf. This definitely lures you, as you will think you are dealing with a pdf file (flag{qdolctmyexe.pdf}), whereas it's in reality an executable (flag{qdolctmy{fdp.exe).

That was the principle used to build this task. 
