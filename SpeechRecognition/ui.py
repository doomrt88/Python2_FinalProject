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
from PIL import Image, ImageTk
from DbCode.db import DB, SpeechToAudio

class SpeechFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)
        self.parent=parent
        self.message = ""
        self.monthly_investment = tk.StringVar()
        self.yearly_interest_rate = tk.StringVar()
        self.years = tk.StringVar()
        self.future_value = tk.StringVar()
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
        nxt_btn = tk.Button(self.home_page,text="Next>>",font="arial 10 bold",fg="White",command=self.notepad,bg="#00A793")
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
        

    def notepad(self):

        self.speechBussiness.monthly_investment = 1
        self.speechBussiness.apr = 2
        self.speechBussiness.years = 2
        fv = self.speechBussiness.calculateFutureValue()
        self.future_value.set("${:.2f}".format(fv, 2))


        # frame and text area placement on the app window
        self.home_page.grid_remove()
        self.fr_buttons.grid(row=0,column=0,sticky="ns")
        #self.fr_speech_to_text.grid(row=0,column=1,sticky="ns")
    
        #tk.Label(self.fr_principal, text='Welcome to Speech Recognition in Python', font=("Arial", 25), bg='Blue').place(x=50)
        #self.txt_labelprincipal.grid(row=0,column=0,sticky="ew",padx=5,pady=60)
        #self.txt_entry.grid(row=1,column=0,sticky="ns",padx=5,pady=1)




    def back(self):
        self.fr_buttons.grid_remove()
        #self.txt_edit.grid_remove()
        #self.fr_pg.grid_remove()
        self.fr_speech_to_text.grid_remove()
        self.fr_text_to_speech.grid_remove()
        self.fr_list_of_audios.grid_remove()
        self.home_page.grid(row=0,column=1,sticky="ns")          

    def speech_to_text(self):

        self.fr_buttons.grid(row=0,column=0,sticky="nsew")
        self.fr_speech_to_text.grid(row=0,column=1,sticky="nsew")
        self.fr_speech_to_text_upper1 = tk.Frame(self.fr_speech_to_text,width=200, height=110,bg="#00A793")
        self.fr_speech_to_text_upper1.grid(row=0,column=0)

        self.fr_speech_to_text_upper2 = tk.Frame(self.fr_speech_to_text,width=500, height=110,bg="#00A793")
        self.fr_speech_to_text_upper2.grid(row=0,column=1)


        self.fr_text_to_speech.grid_remove()
        self.fr_list_of_audios.grid_remove()
        

        # frame and text area placement on the app window
        #tk.Label(self.fr_principal, text='Speech to Text', font=("Arial", 15), fg='White',bg='Orange').place(x=50)
        #tk.Label(self.fr_speech_to_text, text='Speech to Text', font=("Arial", 15), fg='White',bg='#00ffff').grid(row=0,column=0,sticky=tk.W,padx=95,pady=30)
        tk.Label(self.fr_speech_to_text_upper1, text='Speech to Text', font=("Arial", 30, "bold"), fg='White',bg='#00A793').grid(row=0,column=0,sticky=tk.W,padx=40,pady=31)
        #self.welcome_img = tk.PhotoImage(file= r"C:\Users\maria\GitHub\Python2_FinalProject\SpeechRecognition\BussinessCode\Record.png")
        #self.record_img = tk.PhotoImage(file= r"C:\Users\maria\GitHub\Python2_FinalProject\SpeechRecognition\BussinessCode\Record.png")
        #image=Image.open('./SpeechRecognition/UIImages/Record.png')
        #img=image.resize((50, 50))

        self.record_img = tk.PhotoImage(file= "./SpeechRecognition/UIImages/Record.png")
        self.record_img = self.record_img.subsample(3, 3) 
        #self.record_img = tk.PhotoImage(img)
        #self.record_img = self.record_img.zoom(40)
        #tk.Label(self.fr_principal,image=self.record_img).grid(row=1,column=0,sticky=tk.W,padx=20,pady=50)
        #tk.Label(self.fr_speech_to_text,image=self.record_img,width=80,height=80).grid(row=1,column=0,sticky=tk.W,padx=210)
        lb_record_img = tk.Label(self.fr_speech_to_text_upper2,image=self.record_img,width=80,height=110,bg='#00A793').grid(row=0,column=0,padx=30)
        #lb_record_img.place(x=480,y=20)
        #self.iconphoto(False,self.record_img)
        #tk.Label(self.fr_speech_to_text, text='Voice Recorder', font="arial 10 bold", fg='Black',bg='#00ffff').grid(row=2,column=0,sticky=tk.W,padx=190)
        lb_title_record = tk.Label(self.fr_speech_to_text_upper2, text='Voice Recorder', font="arial 11 bold", fg='White',bg='#00A793',width=15)
        #lb_title_record.place(x=570,y=70)
        lb_title_record.grid(row=0,column=1,sticky=tk.W,padx=30)

        lb_time = tk.Label(self.fr_speech_to_text, text='Enter time in seconds', font="arial 11 bold", fg='White',bg='#F7AC40')
        lb_time.grid(row=4,column=0,sticky=tk.W,padx=90)
        #lb_time.place(x=200,y=240)
        self.duration=tk.StringVar()
        entryDuration=tk.Entry(self.fr_speech_to_text,textvariable=self.duration,font="arial 11",width=20)
        entryDuration.grid(row=5, column=0, sticky=tk.W,padx=90)
        

        lb_file = tk.Label(self.fr_speech_to_text, text='Enter the name of file', font="arial 11 bold", fg='White',bg='#F7AC40')
        lb_file.grid(row=6,column=0,sticky=tk.W,padx=90)
        self.filename=tk.StringVar()
        entryFileName=tk.Entry(self.fr_speech_to_text,textvariable=self.filename,font="arial 11",width=20)
        entryFileName.grid(row=7, column=0, sticky=tk.W,padx=90)
        

        btn_record = tk.Button(self.fr_speech_to_text,font="arial 10 bold",text="Record",bg="#111111",fg="white",border=0,command=lambda:self.record_audio(self.filename.get(),self.duration.get()))
        btn_record.grid(row=8,column=0,sticky=tk.W,padx=130,pady=10)
        
        #self.audio_to_text(self.filename.get())

       

    def text_to_speech(self):
        
        
        self.fr_buttons.grid(row=0,column=0,sticky="ns")
        self.fr_text_to_speech.grid(row=0,column=1,sticky="ns")
        #self.fr_text_to_speech.place(width=600,height=300)
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
        
        #btn_play_text_to_speech = tk.Button(self.fr_text_to_speech,font="arial 10",text="To Speech",bg="#111111",fg="white",border=0,command=lambda:self.play_audio_text_speech(self.gender.get(),self.speed.get(),"Hello, My name is Sandra")).grid(row=11,column=0,sticky=tk.W,padx=130)
        
        btn_play_text_to_speech = tk.Button(self.fr_text_to_speech,font="arial 10 bold",text="To Speech",bg="#111111",fg="white",border=0,command=lambda:self.play_audio_text_speech(self.gender.get(),self.speed.get(),txt_area.get(1.0, END)))
        btn_play_text_to_speech.grid(row=10,column=0,sticky=tk.W,padx=130,pady=8)
        btn_download_text_to_speech = tk.Button(self.fr_text_to_speech,font="arial 10 bold",text="Download file",bg="#111111",fg="white",border=0,command=lambda:self.download_file_text_speech(self.gender.get(),self.speed.get(),txt_area.get(1.0, END)))
        btn_download_text_to_speech.grid(row=12,column=0,sticky=tk.W,padx=130,pady=8)
        #scrol_bar.config(command=txt_area.yview)



    # def record_audio(self,filename,duration): # Nombre que le queremos poner al audio y cuanto va a durar
    #     #messagebox.showinfo("Recording audio", "Recording audio...!")
    #     lb_waiting = tk.Label(self.fr_principal, text='Recording audio...', font="arial 10 bold", fg='Black',bg='#00ffff')
    #     lb_waiting.grid(row=7,column=1,sticky=tk.W,padx=95)
    #     self.record_audio2(filename,duration)

    def record_audio(self,filename,duration): # Nombre que le queremos poner al audio y cuanto va a durar

        lb_waiting = tk.Label(self.fr_speech_to_text, text='Recording audio...', font="arial 11 bold", fg='White',bg='#F7AC40')
        lb_waiting.grid(row=4,column=1,sticky=tk.W)
        #messagebox.showinfo("Recording audio", "Recording audio...!")
        CHUNK = 1024 #tamano del audio en bytes
        FORMAT = pyaudio.paInt16 #formato del audio
        CHANNELS = 1 #porque solo tiene 1 canal de entrada que es el microfono
        RATE = 44100 #Numero de samples (single data point representing the amplitude of an audio signal at a specific point in time.)

        audio = pyaudio.PyAudio()  #crea una instancia de PyAudio para input y output de audio

        stream = audio.open(format=FORMAT, #abre el archivo para grabar los valores anteriores
                        channels=CHANNELS,
                        rate=RATE,
                        input=True, #este indica que se va a hacer un input con microfono
                        frames_per_buffer=CHUNK)

        print("Recording...")

        frames = [] #collection of samples, inicialmente vacia y se llena leyendo el stream

        for i in range(0, int(RATE / CHUNK * int(duration))): #RATE / CHUNK = numero de chunks per second and * duration para tener el total de 
        #chunks per record
            data = stream.read(CHUNK)  #en cada loop se toma el valor y despues se agrega al frame
            frames.append(data)

        print("Finished recording.")  #finaliza la grabacion

        stream.stop_stream() #se detiene el stream
        stream.close()# se cierra el stream
        audio.terminate() # finaliza el pyAudio 

        root_directory = "./audios_recorded"  # Change this to your desired root directory
        filename_full = f"{root_directory}/{filename}.wav"
        print(filename_full)

        #No se si esto ponerlo en una funcion por si se quiere guardar el audio o si no

        wf = wave.open(filename_full, 'wb') #utilizamos la libreria WAVE para abrir el audio y en este caso write binary
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        #los 3 anteriores establecen los valores del audio usando funciones del WAVE, todos los set
        wf.writeframes(b''.join(frames)) #usamos los frames que se incluyeron en la parte de grabar y queda en el audio file
        #la b es para convertir en bytes antes de escribirlo en el audio
        wf.close()#se cierra el nuevo wav file

        #time.sleep(5)
        self.after(2000, self.display_playAudio(filename+".wav"))

    def display_playAudio(self,filename):
        btn_playAudioToTxt = tk.Button(self.fr_speech_to_text,text="Play file: " + filename,bg="#111111",font="arial 10 bold",fg="White",border=0,command=lambda:self.audio_to_text(filename))
        btn_playAudioToTxt.grid(row=6,column=1,sticky=tk.W)

    def audio_to_text(self,filename):
        r = sr.Recognizer()
        root_directory = "./audios_recorded"  # Change this to your desired root directory
        filen = f"{root_directory}/{filename}"
        print("directory: " + filename)


        #mixer.music.load(filen)
        #mixer.music.play()
        #playsound('/path/note.wav')
        playsound(filen)
        print('playing sound using  playsound')

        self.text_recognize=tk.StringVar()
        self.text_recognize="Could not recognize the audio"

        with sr.AudioFile(filen) as source:
            audio_data = r.record(source)
            try:
                textFile = r.recognize_google(audio_data)
                print("Text file: " + textFile)
                self.text_recognize = textFile
                #lb_recog_title = tk.Label(self.fr_speech_to_text, text='Recognize Text:', font="arial 11 bold", fg='White',bg='#F7AC40')
                #lb_recog_title.grid(row=8,column=1,sticky=tk.W,pady=10)
                #lb_recognize_text = ttk.Label(self.fr_speech_to_text, text=textFile,width=60)
                #lb_recognize_text.grid(row=7,column=1, sticky=tk.W)

                txt_area_recognize=Text(self.fr_speech_to_text,font="arial 10",width=30,height=2,wrap=WORD)
                txt_area_recognize.insert(INSERT, textFile)
                txt_area_recognize.config(state=DISABLED)
                txt_area_recognize.grid(row=8,column=1,sticky=tk.W)

            except sr.UnknownValueError:
                print("Could not recognize the audio")
            
            except sr.RequestError as e:
                print(e)

        #Guardando el registro en la base de datos
        file_blob = convert_into_binary(filen)
        speechToAudio = SpeechToAudio(filename, file_blob, self.text_recognize)
        db.insert(speechToAudio)


    def play_audio_text_speech(self,gender,speed,text): # Nombre que le queremos poner al audio y cuanto va a durar

        
        #language = 'en'
        #speech = gTTS(text = text1, lang = language, slow = False)
        #speech.save("text.mp3")
        #os.system("start text.mp3")

        print(gender)
        print(speed)
        print(text)
        e=pyttsx3.init()
        v = e.getProperty('voices')

        if (speed == 'Fast'):
            e.setProperty('rate', 300)
            #check_voice()
        elif (speed == 'Normal'):
            e.setProperty('rate', 150)
            #check_voice()
        else:
            e.setProperty('rate', 50)
            #check_voice()

        if (gender == 'Male'):
            e.setProperty('voice', v[0].id)
        else:
            e.setProperty('voice', v[1].id)
        e.setProperty('volume', (100) / 100)
        e.say(text)
        e.runAndWait()
         
    def download_file_text_speech(self,gender,speed,text):
        
        e=pyttsx3.init()
        v = e.getProperty('voices')

        if (speed == 'Fast'):
            e.setProperty('rate', 300)
            #check_voice()
        elif (speed == 'Normal'):
            e.setProperty('rate', 150)
            #check_voice()
        else:
            e.setProperty('rate', 50)
            #check_voice()

        if (gender == 'Male'):
            e.setProperty('voice', v[0].id)
        else:
            e.setProperty('voice', v[1].id)
        e.setProperty('volume', (100) / 100)
        path=filedialog.askdirectory()
        os.chdir(path)
        e.save_to_file(text,'Audio_File.mp3')
        e.runAndWait()
        messagebox.showinfo("Download Audio", "File has been created!")
    
    def list_audios(self):
        self.fr_buttons.grid(row=0,column=0,sticky="ns")
        self.fr_list_of_audios.grid(row=0,column=1,sticky="ns")
        self.fr_speech_to_text.grid_remove()
        self.fr_text_to_speech.grid_remove()

        self.fr_list_of_audios_upper1 = tk.Frame(self.fr_list_of_audios,width=1700, height=110,bg="#00A793")
        self.fr_list_of_audios_upper1.grid(row=0,column=0)

        tk.Label(self.fr_list_of_audios_upper1, text='List of recorded audios', font=("Arial", 30, "bold"), fg='White',bg='#00A793',width=30,height=2).grid(row=0,column=0,sticky=tk.W)

        lb_time = tk.Label(self.fr_list_of_audios, text='Audios', font="arial 11 bold", fg='White',bg='#F7AC40')
        lb_time.grid(row=4,column=0,sticky=tk.W,padx=90)
    

def handle_select(db):
    audios = db.get_audios()
    for m in audios:
        print(type(m))
        print(m)

def convert_into_binary(file_path):
    with open(file_path, 'rb') as file:
        binary = file.read()
    return binary

        
    

if __name__== '__main__':
    root = tk.Tk()
    root.title("Speech Recognition")
    root.geometry("900x400")
    root.resizable(False,False)

    SpeechFrame(root)

    print("Audios UI")
    #db_file = 'audios.db'
    db_file = './SpeechRecognition/DbCode/audios.db'
    
    db = DB(db_file)
    db.ping()
    #handle_select(db)

    root.mainloop()      

  
