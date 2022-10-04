import imp
import cryptocompare
from time import sleep
import pyttsx3
from pygame import mixer
mixer.init()
spek=pyttsx3.init()


dwon=19914
up=19920
hold=50


while True:
    btc_price=cryptocompare.get_price('BTC', currency='USD')["BTC"]["USD"]
    if btc_price < dwon:
        print("btc went low: " , btc_price)
        dwon-=hold
        up-=hold
        mixer.music.load('not_low.mp3')
        mixer.music.play()
        spek.say("price is {}".format(btc_price))
        spek.runAndWait()
    elif btc_price>up :
        print("btc went high : ", btc_price)
        dwon+=hold
        up+=hold
        mixer.music.load('not_hi.mp3')
        mixer.music.play()
        spek.say("price is {}".format(btc_price))
        spek.runAndWait()
    else:
        print(dwon,'<',"btc price: " ,btc_price , '>',up)  
    sleep(5)


