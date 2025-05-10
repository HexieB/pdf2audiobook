This is a project following a youtube tutorial guiding on how to use python libraries to use a pdf manipulation library and text-to-speech library
to create an "audio book" out of  a pdf file.

Log:
Created a new venv, 
installed pyttsx3 and PyPDF2, 
created main.py and readme.md, 
push to origin, 
Then we run into the pitfalls of following a two year old tutorial: missing dependencies and deprecated commands, 
this latest commit had me install espeak, ffmpeg, and libespeak, 
pdffilereader was deprecated, had to use pdfreader instead, 
so on until eventually I started seeing text print out in my terminal instead of errors, 
yet - segmentation fault, core dumped. WHY? possibly I chose too ambitious a pdf file which included graphics or is just too big, 
removing the print function which was meant as a visual indication that everything was working in the background.
Still running into the issue. I'm assuming the pdf is too big and feature rich, finding and choosing something simple with only text, 
We did get a 3 second audio file. So it definitely strikes me that the book is the issue here.
A smaller file with fewer frills was far more successful. program ran without issue, was able to add the print command back in, removed it anyway we don't need to read the pdf.
The output is only a second of audio. Commiting changes for now.
future tasks:
 - ensure full length audio file generation
 - change voice to something more pleasant
 - engineer better file handling, skipping images, page titles, page numbers, so on.
