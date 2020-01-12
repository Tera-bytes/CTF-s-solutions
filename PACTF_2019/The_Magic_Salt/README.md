# The Magic Salt
Given hash: **832c8f6be1b48ce9abcd6deb4ebcdc31**

Our task is to write a script that will take each word in the dictionary, append the salt to it, then hash it; and if it happens to be equal to our given hash, that would be our flag. But, first things first, we need to get the salt. How? We were told it was hidden in the word document provided. 

I waisted time navigating through the document provided in search of hidden contents, but after googling, I realised there was a trick to perform.

Question: what's is a .docx file?
Answer: A .docx file is simply a bunch of XML files (Extensible Markup Language). To view these XML files, you have to change the word's file extension to ".zip", and then open it using any compression program like Winrar or 7z. 

Navigating through the zip content, we find an XML document in the folder **word**, titled **document.xml**. When we open it, we see an interesting comment on line 2: **The salt is the name of the card at "s:A25 cn:50"**. But, what's "s:A25 cn:50"? 
Googling a few words contained in the dictionary, we realise that they  refer to names of cards in a certain game card known as **Scryfall**. So, I just searched for the card at position "s:A25 cn:50", which was **Counterspell**.

We finally got our salt and can now move on to write our script. At the end, I got the flag to be:
## siege-rhino
