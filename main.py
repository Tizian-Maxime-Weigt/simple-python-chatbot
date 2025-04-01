# Made by Tizian Maxime Weigt
# Weather api Key musst be make at the openweathermap.org site

# -*- coding: utf-8 -*-
from cProfile import run
from time import sleep
from pydoc import importfile
import random
import traceback
from turtle import exitonclick
from tkinter import *
from datetime import datetime
import speedtest
import asyncio
import os
import webbrowser
import os
import re
import csv
import sys
import math
import errno
import signal
import socket
import timeit
import datetime
import platform
import threading
import xml.parsers.expat
import json
import requests
from pprint import pprint


zufallsantworten=["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ...", "mach dich aus meiner leitung du birne"]

reaktionsantworten = {"hallo": "aber Hallo",
					  "was geht": "ich rechne gerade aus wie weit du von mir entfernt bist...", 
					  "was ist du am liebsten": "Ich habe leider keinen Geschmackssinn :(",
                      "wie geht es dir": "Darauf kann ich nicht antworten weil ich auf einem server bin, Ich wünsche mir aber ich wäre so ein toller mensch wie du"
					  }
                      
print("Willkommen beim Tizi-Chatbot")
print("Worüber würden Sie gerne heute sprechen?")
print("Zum beenden einfach 'exit' eintippen")
print("Strg+c/ctrl+C zum Benden")
print("Tizi-Cloud.de - Tizi-Server.de")
print("")

nutzereingabe = ""
while nutzereingabe != "exit":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Frage / Antwort: ")

    while nutzereingabe == "Wetter":
            API_key = "Your API KEY"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"

            city_name = input("Name der Gesuchten Stadt : ")
            Final_url = base_url + "appid=" + API_key + "&q=" + city_name
            Final_url = Final_url + "&units=metric&lang=de"
            weather_data = requests.get(Final_url).json()
            
            temp = weather_data['main']['temp']
 
            wind_speed = weather_data['wind']['speed']
            
            description = weather_data['weather'][0]['description']

            latitude = weather_data['coord']['lat']

            longitude = weather_data['coord']['lon']
            
            print('\nTemperature : ',temp)
            print('\nWind Geschwindigkeit : ',wind_speed)
            print('\nBeschreibung : ',description)
 
            nutzereingabe = input("Frage / Antwort: ")

    while nutzereingabe == "speedtest":
        def test():
            s = speedtest.Speedtest()
            s.get_servers()
            s.get_best_server()
            s.download()
            s.upload()
            res = s.results.dict()
            return res["download"], res["upload"], res["ping"]
        def main():
            with open('file.csv', 'w') as f:
                f.write('download,upload,ping\n')
                for i in range(1):
                    print('Test im Gange... Bitte warten')
                    d, u, p = test()
            for i in range(1):
                d, u, p = test()
                print('Ergebnissse')
                print('Download: {:.2f} Mbit/s\n'.format(d / 1000000))
                print('Upload: {:.2f} Mbit/s\n'.format(u / 1000000))
                print('Ping: {}\n'.format(p))
        if __name__ == '__main__':
            main ()
        nutzereingabe = input("Frage / Antwort: ")
    while nutzereingabe == "Speedtest":
        def test():
            s = speedtest.Speedtest()
            s.get_servers()
            s.get_best_server()
            s.download()
            s.upload()
            res = s.results.dict()
            return res["download"], res["upload"], res["ping"]
        def main():
            with open('file.csv', 'w') as f:
                f.write('download,upload,ping\n')
                for i in range(1):
                    print('Test im Gange... Bitte warten')
                    d, u, p = test()
            for i in range(1):
                d, u, p = test()
                print('Ergebnissse')
                print('Download: {:.2f} Mbit/s\n'.format(d / 1000000))
                print('Upload: {:.2f} Mbit/s\n'.format(u / 1000000))
                print('Ping: {}\n'.format(p))
        if __name__ == '__main__':
            main ()
        nutzereingabe = input("Frage / Antwort: ")
    while nutzereingabe == "wie geht es dir":
        print("Darauf kann ich nicht antworten weil ich eine Künstliche inteligenz bin auf einem server bin, Ich wünschte ich wäre auch so ein toller mensch wie du")        
        nutzereingabe = input("Frage / Antwort: ")
    while nutzereingabe == "Google":
        google_input = input ("Was möchtest du Googlen? : ")



    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    
    intelligenteAntworten = True
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == True:
        print(random.choice(zufallsantworten))
        
    print("")

print("BYE kannst gerne mal bei Tizi-Server.de/Tizi-Cloud.de vorbeischauen! :D")
