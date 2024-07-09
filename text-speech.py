from gtts import gTTS
import os
import fileinput
for line in fileinput.input(files="output.txt"):
    mytext=line
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")