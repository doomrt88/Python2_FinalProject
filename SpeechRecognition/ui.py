import tkinter as tk
from tkinter import ttk,filedialog
from tkinter import messagebox
from tkinter import *
from BussinessCode.SpeechRecognition import SpeechBussiness

#from SpeechRecognition.BussinessCode.SpeechRecognition import SpeechBussiness

import speech_recognition as sr
#from pygame import mixer
from playsound import playsound
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

# install this is necessary pip install pyaudio SpeechRecognition requests
import pyaudio #used to use the mic
import wave #to use .WAV files
import speech_recognition as sr #para el trascript

#import site_packages.sounddevice as sound
#from sitepackages.scipy.io.wavfile import write
import time
#import wavio as wv
import threading
from DbCode.db import DB
from PIL import Image, ImageTk
from DbCode.db import DB, SpeechToAudio


class SpeechFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)
        self.parent=parent
        self.message = ""
        self.speechBussiness = SpeechBussiness()

        
        self.declareComponents()

    def declareComponents(self):
        #self.welcome_img = tk.PhotoImage(file= r"C:\Users\maria\GitHub\Python2_FinalProject\SpeechRecognition\BussinessCode\WelcomeTitle.gif")
        self.welcome_img = tk.PhotoImage(file= "./SpeechRecognition/UIImages/WelcomeTitle.png")
        self.home_page = tk.Frame(self,width=600, height=400)
        self.home_page.grid(row=0,column=0,sticky="ns")
        #tk.Label(self.home_page, text='Welcome to Speech Recognition in Python', font=("Arial", 25), bg='Blue').place(x=50)
        tk.Label(self.home_page,image=self.welcome_img, bg='Orange').grid(row=0,column=0,sticky=tk.W,padx=95,pady=60)
        #ttk.Label(self.home_page, text="Monthly Investment").grid(column=0, row=2, sticky=tk.W)
        nxt_btn = tk.Button(self.home_page,text="Next>>",font="arial 10 bold",fg="White",command=self.next_start,bg="#00A793")
        nxt_btn.grid(row=1,column=0,sticky="ew",padx=95)
        self.fr_buttons = tk.Frame(self) # a frame to hold all the buttons of our application
        self.fr_speech_to_text = tk.Frame(self,width=900, height=500,bg="#F7AC40")
        self.fr_text_to_speech = tk.Frame(self,width=900, height=500,bg="#F7AC40")
        self.fr_list_of_audios = tk.Frame(self,width=900, height=500,bg="#F7AC40")
        self.declareButtons()
    
    def declareButtons(self):
        btn_audioToTxt = tk.Button(self.fr_buttons,text="Speech To Text",command=self.speech_to_text)
        btn_txtToaudio = tk.Button(self.fr_buttons,text="Text To Speech",command=self.text_to_speech)
        btn_listAudios = tk.Button(self.fr_buttons,text="List of recorded audios",command=self.list_audios)
        btn_back = tk.Button(self.fr_buttons,text="<<Back",command=self.back,bg="#00A793")


        #btn placement on the window
        btn_audioToTxt.grid(row=0,column=0,sticky="ew",padx=5,pady=10)
        btn_txtToaudio.grid(row=1,column=0,sticky="ew",padx=5,pady=10)
        btn_listAudios.grid(row=2,column=0,sticky="ew",padx=5,pady=10)
        btn_back.grid(row=3,column=0,sticky="ew",padx=5)
        

    def next_start(self):

        # frame and text area placement on the app window
        self.home_page.grid_remove()
        self.fr_buttons.grid(row=0,column=0,sticky="ns")


    def back(self):
        self.fr_buttons.grid_remove()
        self.fr_speech_to_text.grid_remove()
        self.fr_text_to_speech.grid_remove()
        self.fr_list_of_audios.grid_remove()
        self.home_page.grid(row=0,column=1,sticky="ns")          

    def speech_to_text(self):
        self.fr_buttons.grid(row=0,column=0,sticky="nsew")
        self.fr_speech_to_text.grid(row=0,column=1,sticky="nsew")
        self.fr_speech_to_text_upper1 = tk.Frame(self.fr_speech_to_text,width=900, height=110,bg="#00A793")
        self.fr_speech_to_text_upper1.grid(row=0,column=0)
        #self.fr_speech_to_text_upper2 = tk.Frame(self.fr_speech_to_text,width=500, height=110,bg="#00A793")
        #self.fr_speech_to_text_upper2.grid(row=0,column=1)
        self.fr_speech_to_text2 = tk.Frame(self.fr_speech_to_text,width=900, height=110,bg="#F7AC40")
        self.fr_speech_to_text2.grid(row=1,column=0)

        self.fr_speech_to_text_2_1 = tk.Frame(self.fr_speech_to_text2,width=300, height=110,bg="#F7AC40")
        self.fr_speech_to_text_2_1.grid(row=0,column=0)


        self.fr_text_to_speech.grid_remove()
        self.fr_list_of_audios.grid_remove()
        
        # frame and text area placement on the app window
        tk.Label(self.fr_speech_to_text_upper1, text='Speech to Text', font=("Arial", 30, "bold"), fg='White',bg='#00A793',width=30,height=2).grid(row=0,column=0,sticky=tk.W)

        #self.record_img = tk.PhotoImage(file= "./SpeechRecognition/UIImages/Record.png")
        #self.record_img = self.record_img.subsample(3, 3) 
        #lb_record_img = tk.Label(self.fr_speech_to_text_upper2,image=self.record_img,width=80,height=110,bg='#00A793').grid(row=0,column=0,padx=30)
        #lb_title_record = tk.Label(self.fr_speech_to_text_upper2, text='Voice Recorder', font="arial 11 bold", fg='White',bg='#00A793',width=15)
        #lb_title_record.grid(row=0,column=1,sticky=tk.W,padx=30)

        #revisar desde aqui
        # lb_time = tk.Label(self.fr_speech_to_text, text='Enter time in seconds', font="arial 11 bold", fg='White',bg='#F7AC40')
        # lb_time.grid(row=4,column=0,sticky=tk.W,padx=90)
        # self.duration=tk.StringVar()
        # entryDuration=tk.Entry(self.fr_speech_to_text,textvariable=self.duration,font="arial 11",width=20)
        # entryDuration.grid(row=5, column=0, sticky=tk.W,padx=90)

        # lb_file = tk.Label(self.fr_speech_to_text, text='Enter the name of file', font="arial 11 bold", fg='White',bg='#F7AC40')
        # lb_file.grid(row=6,column=0,sticky=tk.W,padx=90)
        # self.filename=tk.StringVar()
        # entryFileName=tk.Entry(self.fr_speech_to_text,textvariable=self.filename,font="arial 11",width=20)
        # entryFileName.grid(row=7, column=0, sticky=tk.W,padx=90)
        
        # btn_record = tk.Button(self.fr_speech_to_text,font="arial 10 bold",text="Record",bg="#111111",fg="white",border=0,command=lambda:self.record_audio(self.filename.get(),self.duration.get()))
        # btn_record.grid(row=8,column=0,sticky=tk.W,padx=130,pady=10)

        lb_time = tk.Label(self.fr_speech_to_text_2_1, text='Enter time in seconds', font="arial 11 bold", fg='White',bg='#F7AC40')
        lb_time.grid(row=4,column=0,sticky=tk.W,padx=90)
        self.duration=tk.StringVar()
        entryDuration=tk.Entry(self.fr_speech_to_text_2_1,textvariable=self.duration,font="arial 11",width=20)
        entryDuration.grid(row=5, column=0, sticky=tk.W,padx=90)

        lb_file = tk.Label(self.fr_speech_to_text_2_1, text='Enter the name of file', font="arial 11 bold", fg='White',bg='#F7AC40')
        lb_file.grid(row=6,column=0,sticky=tk.W,padx=90)
        self.filename=tk.StringVar()
        entryFileName=tk.Entry(self.fr_speech_to_text_2_1,textvariable=self.filename,font="arial 11",width=20)
        entryFileName.grid(row=7, column=0, sticky=tk.W,padx=90)
        
        btn_record = tk.Button(self.fr_speech_to_text_2_1,font="arial 10 bold",text="Record",bg="#111111",fg="white",border=0,command=lambda:self.record_audio(self.filename.get(),self.duration.get()))
        btn_record.grid(row=8,column=0,sticky=tk.W,padx=130,pady=10)

        btn_clear_speech = tk.Button(self.fr_speech_to_text_2_1,font="arial 10 bold",text="Clear",bg="#111111",fg="white",border=0,command=lambda:self.clear_speech())
        btn_clear_speech.grid(row=9,column=0,sticky=tk.W,padx=130,pady=10)

        lb_add = tk.Label(self.fr_speech_to_text_2_1, text='', font="arial 11 bold", fg='White',bg='#F7AC40',height="5")
        lb_add.grid(row=10,column=0,sticky=tk.W,padx=90)
        

        self.fr_speech_to_text_2_2 = tk.Frame(self.fr_speech_to_text2,width=300, height=80,bg="#F7AC40")
        self.fr_speech_to_text_2_2.grid(row=0,column=1)
        

    def clear_speech(self):
        if(self.lb_waiting.winfo_exists()):
            self.lb_waiting.grid_remove()
        if(self.btn_playAudioToTxt.winfo_exists()):
            self.btn_playAudioToTxt.grid_remove()
        if(self.txt_area_recognize.winfo_exists()):
            self.txt_area_recognize.grid_remove()

        
    def record_audio(self,filename,duration): # Nombre que le queremos poner al audio y cuanto va a durar

        self.lb_waiting = tk.Label(self.fr_speech_to_text_2_2, text='Recording audio...', font="arial 11 bold", fg='White',bg='#F7AC40')
        self.lb_waiting.grid(row=0,column=0,sticky=tk.W)
        #messagebox.showinfo("Recording audio", "Recording audio...!")
        self.message=tk.StringVar()
        self.message=""
        self.message = self.speechBussiness.record_audio(filename,duration)
        if(self.message == ""):
            self.after(2000, self.display_playAudio(filename+".wav"))
        else:
            messagebox.showinfo("Error Recording Audio", "Error: " + self.message)
   
    def display_playAudio(self,filename):
        self.btn_playAudioToTxt = tk.Button(self.fr_speech_to_text_2_2,text="Play file: " + filename,bg="#111111",font="arial 10 bold",fg="White",border=0,command=lambda:self.audio_to_text(filename))
        self.btn_playAudioToTxt.grid(row=2,column=0,sticky=tk.W)

    def audio_to_text(self,filename):
        self.text_recognize=tk.StringVar()
        self.text_recognize="Could not recognize the audio"
        self.text_recognize=self.speechBussiness.audio_to_text(filename)

        self.txt_area_recognize=Text(self.fr_speech_to_text_2_2,font="arial 10",width=30,height=2,wrap=WORD)
        self.txt_area_recognize.insert(INSERT, self.text_recognize)
        self.txt_area_recognize.config(state=DISABLED)
        self.txt_area_recognize.grid(row=3,column=0,sticky=tk.W,pady=5)



    def text_to_speech(self):
        self.fr_buttons.grid(row=0,column=0,sticky="ns")
        self.fr_text_to_speech.grid(row=0,column=1,sticky="ns")
        self.fr_speech_to_text.grid_remove()
        self.fr_list_of_audios.grid_remove()

        self.fr_text_to_speech_upper1 = tk.Frame(self.fr_text_to_speech,width=1700, height=110,bg="#00A793")
        self.fr_text_to_speech_upper1.grid(row=0,column=0)

        tk.Label(self.fr_text_to_speech_upper1, text='Text to Speech', font=("Arial", 30, "bold"), fg='White',bg='#00A793',width=30,height=2).grid(row=0,column=0,sticky=tk.W)

        lb_time = tk.Label(self.fr_text_to_speech, text='Enter text to speech', font="arial 11 bold", fg='White',bg='#F7AC40')
        lb_time.grid(row=4,column=0,sticky=tk.W,padx=90)
        
        self.text=tk.StringVar()
        txt_area=Text(self.fr_text_to_speech,font="arial 10",width=40,height=5,wrap=WORD)
        txt_area.grid(row=5,column=0,sticky=tk.W,padx=90)
        
        tk.Label(self.fr_text_to_speech, text='Gender', font="arial 11 bold", fg='White',bg='#F7AC40').grid(row=6,column=0,sticky=tk.W,padx=90)

        self.gender=tk.StringVar()
        gender_combo = Combobox(self.fr_text_to_speech,textvariable=self.gender,values=['Male','Female'],font='arial 11',state='r')
        gender_combo.grid(row=7,column=0,sticky=tk.W,padx=90)
        gender_combo.set('Female')

        tk.Label(self.fr_text_to_speech, text='Speed', font="arial 11 bold", fg='White',bg='#F7AC40').grid(row=8,column=0,sticky=tk.W,padx=90)
        
        self.speed=tk.StringVar()
        speed_combo = Combobox(self.fr_text_to_speech,textvariable=self.speed,values=['Fast','Normal','Slow'],font='arial 11',state='r')
        speed_combo.grid(row=9,column=0,sticky=tk.W,padx=90)
        speed_combo.set('Normal')
        
        btn_play_text_to_speech = tk.Button(self.fr_text_to_speech,font="arial 10 bold",text="To Speech",bg="#111111",fg="white",border=0,command=lambda:self.speechBussiness.play_audio_text_speech(self.gender.get(),self.speed.get(),txt_area.get(1.0, END)))
        btn_play_text_to_speech.grid(row=10,column=0,sticky=tk.W,padx=130,pady=8)
        btn_download_text_to_speech = tk.Button(self.fr_text_to_speech,font="arial 10 bold",text="Download file",bg="#111111",fg="white",border=0,command=lambda:self.speechBussiness.download_file_text_speech(self.gender.get(),self.speed.get(),txt_area.get(1.0, END)))
        btn_download_text_to_speech.grid(row=12,column=0,sticky=tk.W,padx=130,pady=8)

   
    def list_audios(self):
        self.fr_speech_to_text.grid_remove()
        self.fr_text_to_speech.grid_remove()
        self.fr_buttons.grid(row=0,column=0,sticky="ns")
        self.fr_list_of_audios.grid(row=0,column=1,sticky="ns")


        self.fr_list_of_audios_upper1 = tk.Frame(self.fr_list_of_audios,width=1700, height=110,bg="#00A793")
        self.fr_list_of_audios_upper1.grid(row=0,column=0)

        tk.Label(self.fr_list_of_audios_upper1, text='List of recorded audios', font=("Arial", 30, "bold"), fg='White',bg='#00A793',width=30,height=2).grid(row=0,column=0,sticky=tk.W)

        db_file = './SpeechRecognition/DbCode/audios.db'
        dataBase = DB(db_file)
        self.handle_select(dataBase)
    
    def playAudio(self):
        curItem = self.listAudiosData.focus()
        itemValue = self.listAudiosData.item(curItem)
        dataList = itemValue.get("values")
        self.speechBussiness.playAudio(dataList[0])


    def handle_select(self,dataBase):
        audios = dataBase.get_audios()

        self.listAudiosData = ttk.Treeview(self.fr_list_of_audios, columns=('file_name', 'text_speech'), show="headings", height="8")

        self.listAudiosData.heading('file_name',text = 'File Name')
        self.listAudiosData.heading('text_speech',text = 'Text Speech')

        for dataFromAudio in audios:
            self.listAudiosData.insert('',tk.END,values=dataFromAudio)

        self.listAudiosData.grid(row=4,column=0,sticky=tk.W,padx=150)

        self.btn_playAudio = tk.Button(self.fr_list_of_audios,text="Play file ",bg="#111111",font="arial 10 bold",fg="White",border=0,command=lambda:self.playAudio())
        self.btn_playAudio.grid(row=5,column=0,sticky=tk.W, padx=90)

if __name__== '__main__':
    root = tk.Tk()
    root.title("Speech Recognition")
    root.geometry("900x400")
    root.resizable(False,False)

    SpeechFrame(root)

    print("Audios UI")

    root.mainloop()      

  
