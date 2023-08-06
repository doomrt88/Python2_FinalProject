# install this is necessary pip install pyaudio SpeechRecognition requests
import pyaudio #used to use the mic
import wave #to use .WAV files
import speech_recognition as sr #para el trascript


def record_audio(filename, duration): # Nombre que le queremos poner al audio y cuanto va a durar
    CHUNK = 1024 #tamano del audio en bytes
    FORMAT = pyaudio.paInt16 #formato del udio
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

    for i in range(0, int(RATE / CHUNK * duration)): #RATE / CHUNK = numero de chunks per second and * duration para tener el total de 
        #chunks per record
        data = stream.read(CHUNK)  #en cada loop se toma el valor y despues se agrega al frame
        frames.append(data)

    print("Finished recording.")  #finaliza la grabacion

    stream.stop_stream() #se detiene el stream
    stream.close()# se cierra el stream
    audio.terminate() # finaliza el pyAudio 

    root_directory = "./Python2_FinalProject/audios_recorded"  # Change this to your desired root directory
    filename = f"{root_directory}/{filename}"

    #No se si esto ponerlo en una funcion por si se quiere guardar el audio o si no

    wf = wave.open(filename, 'wb') #utilizamos la libreria WAVE para abrir el audio y en este caso write binary
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    #los 3 anteriores establecen los valores del audio usando funciones del WAVE, todos los set
    wf.writeframes(b''.join(frames)) #usamos los frames que se incluyeron en la parte de grabar y queda en el audio file
    #la b es para convertir en bytes antes de escribirlo en el audio
    wf.close()#se cierra el nuevo wav file


def transcribe_audio(filename):
    recognizer = sr.Recognizer() #se crea una instancia Recognizer de la libreria que va a reconocer el audio y pasar a texto

    with sr.AudioFile("./Python2_FinalProject/audios_recorded/"+filename) as source: #AudioFile es propio de la libreria y en el se pasa el nombre del audio, aca se abre el file
        audio = recognizer.record(source)#record es un metodo del recognizer class y lee el audio desde el source

    try:
        text = recognizer.recognize_google(audio) #recognize_google es otro metodo de Recognizer class y audio 
        # a el Google's Web Speech API for transcription.
        print("The audio says: ", text) #se va a mostrar el contenido del audio
    except sr.UnknownValueError:
        print("Could not understand audio.") #si se devuelve UnknownValueError puede ser que no se entendio o esta mal el audio
        #me paso aveces diciendo en espanol y creo que lee mejor el ingles
    except sr.RequestError as e:
        print("Error with the transcription service; {0}".format(e)) #si hay un error en el API o en el servidor aca se va a mostrar


if __name__ == "__main__":
    # Graba y lee
    record_audio("output.wav", 5) # llamando a la funcion la idea es que el usuario de el nombre y se pase el valor, igual que el tiempo
    transcribe_audio("output.wav") # para hacer el transcript
    # Lee para los que se carguen, se guarden en la carpeta y se lean
    # transcribe_audio("output2.wav") # para hacer el transcript
 