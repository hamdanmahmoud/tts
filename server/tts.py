#!/usr/bin/env python3

import time
import speech_recognition as sr
from deep_translator import GoogleTranslator

LANGUAGE = "ar-AR"
PAUSE_THRESHOLD = 0.1 # non-speaking duration that leads to phrase compelted
PHRASE_THRESHOLD = 0.05 # minimum duration for which spoken audio is considered a phrase (if this threshold is not reached, audio is considered noise)
NON_SPEAKING_DURATION = 0.05

def configurate_recognizer(recognizer, source):
    recognizer.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    recognizer.pause_threshold = PAUSE_THRESHOLD
    recognizer.phrase_threshold = PHRASE_THRESHOLD
    recognizer.non_speaking_duration = NON_SPEAKING_DURATION

# this callback gets called each time audio data is received from the background thread
def callback(recognizer, audio):
    try:
        recognized_text = recognizer.recognize_google(audio, language=LANGUAGE, )
        translated_text = GoogleTranslator(source="ar", target="en").translate(recognized_text)
        print(translated_text)
    except sr.UnknownValueError: # GSR could not understand audio
        pass
    except sr.RequestError as e:
        print("Error: Could not request results from Google Speech Recognition service; {0}".format(e))

mic = sr.Microphone()
r = sr.Recognizer()
with mic as source:
    configurate_recognizer(r, source)

# following line starts a new thread in the background
stop_listening = r.listen_in_background(mic, callback)
# stop_listening() # <<< uncomment this line to stop listening

while True:
    time.sleep(10)
