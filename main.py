# -*- coding: utf-8 -*-
from cProfile import run
from time import sleep
from pydoc import importfile
import random
import traceback
from turtle import exitonclick
from tkinter import *
import json
from datetime import datetime
import speedtest
import python_weather
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

    while nutzereingabe == "wetter":
        num = float(input("Postleitzahl: "))
        if num >= 36448:
            print("https://www.google.com/search?q=wetter+36448")
            url = 'https://www.google.com/search?q=wetter+36448'
            webbrowser.open(url)
            nutzereingabe = input("Frage / Antwort: ")
        if num >= 99867:
            print("https://www.google.com/search?q=wetter+99867")

        
            nutzereingabe = input("Frage / Antwort: ")
        
        else:
            print("Mhhm habe ich nicht im System")
            print("Du kannst aber selber nachschauen")
            print("https://google.de")
            print("Support@tizi-cloud.de")
   

        nutzereingabe = input("Frage / Antwort: ")

    while nutzereingabe == "Speedtest":
        st = speedtest.Speedtest()
  
        option = int(input('''Was willst du Testen?:  
  
        1) Download Geschindigkeit 
  
        2) Upload Geschindigkeit  
  
        3) Ping (Funktioniert derzeit nicht)
  
        Deine Antwort?: '''))
  
  
        if option == 1:  
            print("Warte der test ist an laufen...")
            print(st.download())  
  
        elif option == 2: 
            print("Warte der test ist an laufen...")
            print(st.upload())  
  
        elif option == 3:  
            
            servernames =[]  
            
            st.get_servers(servernames)  
            print("Warte der test ist an laufen...")
            print(st.results.ping)  
  
        else:
  
            print("Falsche eingabe wiederholen...") 


        nutzereingabe = input("Frage / Antwort: ")

    
    while nutzereingabe == "wie geht es dir":
        print("Darauf kann ich nicht antworten weil ich eine Künstliche inteligenz bin auf einem server bin, Ich wünschte ich wäre auch so ein toller mensch wie du")        
        nutzereingabe = input("Frage / Antwort: ")


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