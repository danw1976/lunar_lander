import pygame, sys, pyaudio, array
from random import *
from pygame import *
from math import *

speed = 30
gravity = 1.622
fuel = 1500
altitude = 1000
burn = 0

for i in range(mn + 1):
    mx.append(z*i)
    my.append(int(randint(-mh, 0) + am * (4-sin((i + ph) / 5.))) -fs)
