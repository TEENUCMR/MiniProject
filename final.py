import speech_recognition as sr
import smtplib
import email
import imaplib
from bs4 import BeautifulSoup
from gtts import gTTS
import os
from playsound import playsound 
from tkinter import *

root=Tk()


lbl1=Label(root, text='E-Mail ID:')
lbl1=Label(root, text='E-Mail ID:')
lbl2=Label(root, text='Password:') 
l3=Label(root, text='You Said:')
t1=Entry()
t2=Entry(show="*")
t3=Entry()

lbl1.place(x=100, y=50)
t1.place(x=200, y=50)
lbl2.place(x=100, y=100)
t2.place(x=200, y=100)
l3.place(x=100, y=200)
t3.place(x=200, y=200)

def clear():
        t1.delete(0,"end")
        t2.delete(0,"end")

def evaluate():
        eid=t1.get()
        pswd=t2.get()
        temp=t2.get()
        eid=eid.replace(" ","")
        eid=eid.replace("attherate","@")
        eid=eid.lower()
        pswd=pswd.replace(" ","")
        pswd=pswd.lower()
        temp=temp.replace(pswd, "*"*len(temp))
        
        l1=Label(root,text=eid)
        l1.place(x=150,y=230)
        l2=Label(root,text=temp)
        l2.place(x=150,y=270)

def action():
	tts = gTTS(text="Project: Voice based Email for Blind", lang='en',slow=False)
	ttsname=("a.mp3") 
	tts.save(ttsname)
	playsound("a.mp3")
	os.remove(ttsname)
	
	tts = gTTS(text="Email ID", lang='en',slow=False)
	ttsname=("a.mp3") 
	tts.save(ttsname)
	playsound("a.mp3")
	os.remove(ttsname)


btn1 = Button(root, text='Submit')
btn2=Button(root, text='Clear')
b1=Button(root, text='Submit', command=action)
b2=Button(root, text='Clear',command=clear)
b2.bind('<Button-1>',clear)
b1.place(x=100, y=150)
b2.place(x=200, y=150)




#b1=Button(root, text='Submit', command=action).pack()

""" self.lbl2=Label(root, text='Password:') 
        self.l3=Label(root, text='You Said:')
        self.t1=Entry()
        self.t2=Entry(show="*")
        self.t3=Entry()
        self.btn1 = Button(root, text='Submit')
        self.btn2=Button(root, text='Clear')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.l3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
        self.b1=Button(root, text='Submit', command=self.evaluate)
        self.b2=Button(root, text='Clear',command=self.clear)
        self.b2.bind('<Button-1>', self.clear)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        

    def clear(self):
        self.t1.delete(0,"end")
        self.t2.delete(0,"end")

    def evaluate(self):
        eid=self.t1.get()
        pswd=self.t2.get()
        temp=self.t2.get()
        eid=eid.replace(" ","")
        eid=eid.replace("attherate","@")
        eid=eid.lower()
        pswd=pswd.replace(" ","")
        pswd=pswd.lower()
        temp=temp.replace(pswd, "*"*len(temp))
        
        self.l1=Label(root,text=eid)
        self.l1.place(x=150,y=230)
        self.l2=Label(root,text=temp)
        self.l2.place(x=150,y=270)"""
        




root.config(bg='#49A')
root.title('Demo')
l=Label(root, text = "Voice Based E-Mail for Visually Impaired") 
l.config(font =("Courier", 9)) 
l.pack()
root.geometry("400x300+10+10")
root.mainloop()


