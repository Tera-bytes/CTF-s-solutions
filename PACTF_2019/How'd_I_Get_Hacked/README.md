# How'd I Get Hacked

Firstly, I realised most of the files were of length 21. So, to be sure, I wrote a script that outputs files of length different from 21. To my great surprise, there was one: **flag{qdolctmyâ€®{fdp.exeâ€¬**. But, when I tried looking for that in the .dat file, it didn't exist: instead, there was one flag similar to that and which was our flag:
## flag{qdolctmy‮{fdp.exe‬

Now, the million-dollar question is: where is **flag{qdolctmyâ€®{fdp.exeâ€¬** coming from?
So, to look closely at what was going on, I opened the .dat file in a hex editor and scroll to where that flag was found. Indeed, what I saw in the hex editor was slightly different from what appeared in the .dat file. That's, in the .dat file I saw "flag{qdolctmy‮{fdp.exe‬", while in the hex editor (at that same poosition) I instead saw "flag{qdolctmyâ€®{fdp.exeâ€¬". 

NB:I was using HxD editor on Windows, whose default code page is ANSI.

Notice these weird characters: "â€®" and "â€¬". Their respective hex values are "E2 80 AE" and "E2 80 AC". In fact, these are special characters used to reverse the order of a string.

Example: if you open a hex editor and type:

**E2 80 AE** 62 61 6E 61 6E 61 **E2 80 AC**  (where "62 61 6E 61 6E 61" stands for banana), what you will see in a text editor will be:
ananab. That's the word banana would be flipped. 

Let's apply it to our problem. We see the following in a hex editor:

**E2 80 AE** 7B 66 64 70 2E 65 78 65 **E2 80 AC** ( â€®{fdp.exeâ€¬),

which means what will appear in a text editor won't be "{fdp.exe", but instead exe.pdf, thereby luring you as you will think you are dealing with a pdf file.

That was the principle used to build this task. 
