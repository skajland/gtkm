# GTKM GAME JAM SNOOPY AND SKAJLAND
import pygame
import time
lastFrame = time.time_ns()
timePerFrame = 16666667
accumulator = 0

while 1:
    currentTime = time.time_ns()

    accumulator += currentTime-lastFrame
    lastFrame = currentTime

    if accumulator >= timePerFrame:
        accumulator -= timePerFrame
