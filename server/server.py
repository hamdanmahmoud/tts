#!/usr/bin/env python

import flask
from flask_cors import CORS
import json
import time
import speech_recognition as sr
from deep_translator import GoogleTranslator
import random #remove this
import string #remove this

SOURCE_LANGUAGE = "en"
TARGET_LANGUAGE = "ro"
PAUSE_THRESHOLD = 0.1 # non-speaking duration that leads to phrase compelted
PHRASE_THRESHOLD = 0.05 # minimum duration for which spoken audio is considered a phrase (if this threshold is not reached, audio is considered noise)
NON_SPEAKING_DURATION = 0.05

NUMBER_OF_WORDS = 15

speech = []

app = flask.Flask(__name__)
CORS(app)

def save_speech(text):
    for word in text.split():
        speech.append(word)

@app.route('/', methods=['GET'])
def home():
    #letters = string.ascii_lowercase
    #random_words = []
    #for j in range(12):
    #    random_words.append(''.join(random.choice(letters) for i in range(8)))
    res = {
        "message": " ".join(speech[-NUMBER_OF_WORDS:]),
        #"message": " ".join(random_words),
        "source": SOURCE_LANGUAGE,
        "target": TARGET_LANGUAGE
    }
    return json.dumps(res)

def configurate_recognizer(recognizer, source):
    recognizer.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    recognizer.pause_threshold = PAUSE_THRESHOLD
    recognizer.phrase_threshold = PHRASE_THRESHOLD
    recognizer.non_speaking_duration = NON_SPEAKING_DURATION

# this callback gets called each time audio data is received from the background thread
def callback(recognizer, audio):
    try:
        recognized_text = recognizer.recognize_google(audio, language="en-EN")
        translated_text = GoogleTranslator(source=SOURCE_LANGUAGE, target=TARGET_LANGUAGE).translate(recognized_text)
        save_speech(translated_text)
    except sr.UnknownValueError: # GSR could not understand audio
        pass
    except sr.RequestError as e:
        print("Error: Could not request results from Google Speech Recognition service; {0}".format(e))

# If you are running it using python <filename> then below command will be used
if __name__ == '__main__':
    mic = sr.Microphone()
    r = sr.Recognizer()
    with mic as source:
        configurate_recognizer(r, source)

    stop_listening = r.listen_in_background(mic, callback)

    app.run()

    while True:
        time.sleep(10)