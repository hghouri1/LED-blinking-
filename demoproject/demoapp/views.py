from django.shortcuts import render
import  RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT,initial=GPIO.LOW)

# Create your views here.
def hi(req):
    return render(req,"demoapp\led.html")


def on(req):
    GPIO.output(3,GPIO.HIGH)
    sleep(4)
    return render(req,"demoapp\on.html")

def off(req):
    GPIO.output(3,GPIO.LOW)  
    sleep(5) 
    return render(req,"demoapp\off.html")
    