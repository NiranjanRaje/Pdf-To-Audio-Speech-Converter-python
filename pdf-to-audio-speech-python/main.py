from tkinter import *
import tkinter.messagebox as mb

from path import Path
from PyPDF4.pdf import PdfFileReader as PDFreader, PdfFileWriter as PDFwriter
import pyttsx3
from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment
import os

# Initializing the GUI window
class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("ProjectGurukul PDF to Audio and Audio to PDF converter")
        self.geometry('400x250')
        self.resizable(0, 0)
        self.config(bg='Burlywood')
    
        Label(self, text='ProjectGurukul PDF to Audio and Audio to PDF converter', wraplength=400,
              bg='Burlywood', font=("Comic Sans MS", 15)).place(x=0, y=0)
    
        Button(self, text="Convert PDF to Audio", font=("Comic Sans MS", 15), bg='Tomato',
               command=self.pdf_to_audio, width=25).place(x=40, y=80)
    
        

    def pdf_to_audio(self):
        pta = Toplevel(self)
        pta.title('Convert PDF to Audio')
        pta.geometry('500x300')
        pta.resizable(0, 0)
        pta.config(bg='Chocolate')

        Label(pta, text='Convert PDF to Audio', font=('Comic Sans MS', 15), bg='Chocolate').place(relx=0.3, y=0)

        Label(pta, text='Enter the PDF file location (with extension): ', bg='Chocolate', font=("Verdana", 11)).place(x=10, y=60)
        filename = Entry(pta, width=32, font=('Verdana', 11))
        filename.place(x=10, y=90)

        Label(pta, text='Enter the page to read from the PDF (only one can be read): ', bg='Chocolate',
              font=("Verdana", 11)).place(x=10, y=140)
        page = Entry(pta, width=15, font=('Verdana', 11))
        page.place(x=10, y=170)

        Button(pta, text='Speak the text', font=('Gill Sans MT', 12), bg='Snow', width=20,
               command=lambda: self.speak_text(filename.get(), page.get())).place(x=150, y=240)

    

    @staticmethod
    def speak_text(filename, page):
        if not filename or not page:
            mb.showerror('Missing field!', 'Please check your responses, because one of the fields is missing')
            return

        reader = PDFreader(filename)
        engine = pyttsx3.init()

        with Path(filename).open('rb'):
            page_to_read = reader.getPage(int(page)-1)
            text = page_to_read.extractText()

            engine.say(text)
            engine.runAndWait()

   

    


# Finalizing the GUI window
app = Window()

app.update()
app.mainloop()
