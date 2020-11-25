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

eid=0




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
	tts = gTTS(text="Speak Now", lang='en',slow=False)
	ttsname=("sn.mp3") 
	tts.save(ttsname)
	tts = gTTS(text="Project: Voice based Email for Blind", lang='en',slow=False)
	ttsname=("output.mp3") 
	tts.save(ttsname)
	playsound("output.mp3")
	os.remove(ttsname)
	
	tts = gTTS(text="Email ID", lang='en',slow=False)
	ttsname=("output.mp3") 
	tts.save(ttsname)
	playsound("output.mp3")
	os.remove(ttsname)

	r = sr.Recognizer()
	with sr.Microphone() as source:
		playsound("sn.mp3")
		audio=r.listen(source)


	try:
		eid=r.recognize_google(audio)
		eid=eid.replace(" ","")
		eid=eid.replace("attherate","@")
		eid=eid.replace("at","@")
		eid=eid.lower()
		print ("You said : "+eid)
		l1=Label(root,text=eid)
		l1.place(x=150,y=230)

	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio.")

	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e)) 


	tts = gTTS(text="password ", lang='en',slow=False)
	ttsname=("a.mp3") 
	tts.save(ttsname)
	playsound("a.mp3")
	os.remove(ttsname)

	r = sr.Recognizer()
	with sr.Microphone() as source:
		playsound("sn.mp3")
		audio=r.listen(source)
		print ("ok done!!")

	try:
		pswd=r.recognize_google(audio)
		pswd=pswd.replace(" ","")
		pswd=pswd.lower()
		print ("You said : "+pswd)

	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio.")

	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

	temp=pswd
	temp=temp.replace(pswd, "*"*len(temp))

	l2=Label(root,text=temp)
	l2.place(x=150,y=270)


	tts = gTTS(text="Option 1. compose a mail.", lang='en')
	ttsname=("b.mp3") 
	tts.save(ttsname)
	playsound("b.mp3")
	os.remove(ttsname)


	tts = gTTS(text="option 2. Check your inbox", lang='en')
	ttsname=("second.mp3")
	tts.save(ttsname)
	playsound("second.mp3")
	os.remove(ttsname)

	tts = gTTS(text="Your choice ", lang='en')
	ttsname=("hello.mp3") 
	tts.save(ttsname)
	playsound("hello.mp3")
	os.remove(ttsname)


	r = sr.Recognizer()
	with sr.Microphone() as source:
		print ("Your choice:")
		audio=r.listen(source)
		print ("ok done!!")

	try:
		text=r.recognize_google(audio)
		print ("You said : "+text)

	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio.")

	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))


	if text == '1' or text == 'One' or text == 'one' or text=='option one':
		tts = gTTS(text="Reciever Email ID", lang='en')
		ttsname=("rid.mp3")
		tts.save(ttsname)
		playsound("rid.mp3")
		os.remove(ttsname)
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print ("Your message :")
			audio=r.listen(source)
			print ("ok done!!")

		try:
			text1=r.recognize_google(audio)
			print ("You said : "+text1)
			msg = rid
			rid=rid.lower()
			rid=rid.replace(" ","")
			rid=rid.replace("attherate","@")
			rid=rid.replace("at","@")



		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")

		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
		tts = gTTS(text="Your message", lang='en')
		ttsname=("msg1.mp3")
		tts.save(ttsname)
		playsound("msg1.mp3")
		os.remove(ttsname)
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print ("Your message :")
			audio=r.listen(source)
			print ("ok done!!")

		try:
			text1=r.recognize_google(audio)
			print ("You said : "+text1)
			msg = text1


		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio.")

		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))


		mail = smtplib.SMTP('smtp.gmail.com',587)    #host and port area
		mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
		mail.starttls() #security connection
		mail.login(eid,pswd) #login part
		mail.sendmail(eid,rid,msg) #send part
		print ("Congrates! Your mail has send. ")
		tts = gTTS(text="Congrates! Your mail has send. ", lang='en')
		ttsname=("send.mp3") 
		tts.save(ttsname)
		playsound("send.mp3")
		os.remove(ttsname)
		mail.close()


	if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' or text=='option two' :
		mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security
		mail.login(eid,pswd)  #login
		stat, total = mail.select('Inbox')  #total number of mails in inbox
		print ("Number of mails in your inbox :"+str(total))
		tts = gTTS(text="Total mails are :"+str(total), lang='en') #voice out
		ttsname=("total.mp3")
		tts.save(ttsname)
		playsound("total.mp3")
		os.remove(ttsname)

		unseen = mail.search(None, 'UnSeen')
		print ("Number of UnSeen mails :"+str(unseen))
		tts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
		ttsname=("unseen.mp3")
		tts.save(ttsname)
		playsound("unseen.mp3")
		os.remove(ttsname)


		#search mails
		result, data = mail.uid('search',None, "ALL")
		inbox_item_list = data[0].split()
		new = inbox_item_list[-1]
		old = inbox_item_list[0]
		result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
		raw_email = email_data[0][1].decode("utf-8") #decode
		email_message = email.message_from_string(raw_email)
		print ("From: "+email_message['From'])
		print ("Subject: "+str(email_message['Subject']))
		tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
		ttsname=("mail.mp3")
		tts.save(ttsname)
		playsound("mail.mp3")
		os.remove(ttsname)

		#Body part of mails
		stat, total1 = mail.select('Inbox')
		stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
		msg = data1[0][1]
		soup = BeautifulSoup(msg, "html.parser")
		txt = soup.get_text()
		print ("Body :"+txt)
		tts = gTTS(text="Body: "+txt, lang='en')
		ttsname=("body.mp3")
		tts.save(ttsname)
		playsound("body.mp3")
		os.remove(ttsname)
		mail.close()
		mail.logout()    





btn1 = Button(root, text='Submit')
btn2=Button(root, text='Clear')
b1=Button(root, text='Submit', command=action)
b2=Button(root, text='Clear',command=clear)
b2.bind('<Button-1>',clear)
b1.place(x=100, y=150)
b2.place(x=200, y=150)



root.config(bg='#49A')
root.title('Demo')
l=Label(root, text = "Voice Based E-Mail for Visually Impaired") 
l.config(font =("Courier", 9)) 
l.pack()
root.geometry("400x300+10+10")
root.mainloop()


