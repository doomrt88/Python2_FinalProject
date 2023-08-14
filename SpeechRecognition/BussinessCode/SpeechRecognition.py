import speech_recognition as sr
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
import pyaudio #used to use the mic
import wave #to use .WAV files
from playsound import playsound
from DbCode.db import DB, SpeechToAudio
from tkinter import messagebox



class SpeechBussiness():
    def __init__(self):
        self.monthly_investment:float = 0.0
        self.apr:float = 0.0
        self.years:int = 0
    
    
    def record_audio(self,filename,duration): # Nombre que le queremos poner al audio y cuanto va a durar

        #messagebox.showinfo("Recording audio", "Recording audio...!")
        CHUNK = 1024 #tamano del audio en bytes
        FORMAT = pyaudio.paInt16 #formato del audio
        CHANNELS = 1 #porque solo tiene 1 canal de entrada que es el microfono
        RATE = 44100 #Numero de samples (single data point representing the amplitude of an audio signal at a specific point in time.)

        audio = pyaudio.PyAudio()  #crea una instancia de PyAudio para input y output de audio
        self.message=tk.StringVar()
        self.message=""

        stream = audio.open(format=FORMAT, #abre el archivo para grabar los valores anteriores
                        channels=CHANNELS,
                        rate=RATE,
                        input=True, #este indica que se va a hacer un input con microfono
                        frames_per_buffer=CHUNK)

        print("Recording...")

        frames = [] #collection of samples, inicialmente vacia y se llena leyendo el stream

        try:

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
        
        except Exception as e:
                self.message = str(e)
                print("Error in record_audio")

        return self.message

    def audio_to_text(self,filename):
        
        
        root_directory = "./audios_recorded"  # Change this to your desired root directory
        filen = f"{root_directory}/{filename}"
        print("directory: " + filename)

        self.text_play=tk.StringVar()
        self.text_play="Could not play the audio"

        try:
            playsound(filen)
            print('playing sound using  playsound')
        except Exception as e:
            self.message = str(e)
            print("Error in playing sound using playsound: " + str(e))

        self.text_recognize=tk.StringVar()
        self.text_recognize="Could not recognize the audio"

        r = sr.Recognizer()

        with sr.AudioFile(filen) as source:
            audio_data = r.record(source)
            try:
                textFile = r.recognize_google(audio_data)
                print("Text file: " + textFile)
                self.text_recognize = textFile

            except sr.UnknownValueError as e:
                print("Could not recognize the audio")
                print(e)
                self.text_recognize="Error: Could not recognize the audio"
            
            except sr.RequestError as e:
                print(e)
                self.text_recognize="Error: Could not recognize the audio"

        #Guardando el registro en la base de datos
        file_blob = self.convert_into_binary(filen)
        speechToAudio = SpeechToAudio(filename, file_blob, self.text_recognize)
        db_file = './SpeechRecognition/DbCode/audios.db'
        db = DB(db_file)
        db.insert(speechToAudio)

        return self.text_recognize
    
    def convert_into_binary(self,file_path):
        with open(file_path, 'rb') as file:
            binary = file.read()
        return binary
    
    def play_audio_text_speech(self,gender,speed,text): 
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




