import pytube
import speech_recognition as sr
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pytube import YouTube
import pocketsphinx
from os import path
from moviepy.editor import *

text = input("Enter Youtube url:")
yt = YouTube(text)
yt.streams.filter(file_extension='mp4').first().download(filename="video.mp4")

video = VideoFileClip(os.path.join(path.dirname(path.realpath(__file__)), "video.mp4"))
video.audio.write_audiofile(os.path.join(path.dirname(path.realpath(__file__)), "video.wav"))

r = sr.Recognizer()
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "video.wav")
with sr.AudioFile(AUDIO_FILE) as source:
   audio = r.record(source)
   try:
        text = r.recognize_google(audio)
   except:
       print("trying sphinx")
       text = r.recognize_sphinx(audio)


word_cloud = WordCloud(collocations=False,

        background_color='white').generate(text)

plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()

os.remove(os.path.dirname(path.realpath(__file__)) + "\\video.mp4")
os.remove(os.path.dirname(path.realpath(__file__)) +"\\video.wav")



