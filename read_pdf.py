################## reads aloud pdf files (Russian and English) ########################

import pyttsx3
import PyPDF2

file, lang = input("What is a file to read?\n"), input("What is the language: ru, en?\n")
lang_index = 0 if lang == "ru" else 1
book = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current tempo
print (rate)                        #printing current voice rate
engine.setProperty('rate', 300)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[lang_index].id)   #changing index, changes voices. 1 for English speaker
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

pages = pdfReader.numPages
for num in range(int(input("From what page should I start reading?\n")), pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()

engine.stop()
book.close()