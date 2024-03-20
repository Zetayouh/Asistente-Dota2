from pyttsx3 import init

engine = init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 175)     # setting up new voice rate
#print (rate)                        #printing current voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')   #changing index, changes voices. 1 for female

#engine.say("Comienza la partida!")
#engine.say('Mi velocidad actual de lectura es de ' + str(rate))
#engine.runAndWait()
#engine.stop()

"""Saving Voice to a file"""
#engine.save_to_file('Hello World', 'test.mp3')
#engine.runAndWait()
