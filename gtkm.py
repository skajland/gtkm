import pygame
import time
# GTKM GAME JAM SNOOPY AND SKAJLAND
timePerFrame = 1000000000. / 60
lastFrame = time.time_ns()
now = 16666667
accumulator = 0
while 1:

    currentTime = time.time_ns()

    accumulator += currentTime-lastFrame
    lastFrame = currentTime

    if (accumulator >= now)

        accumulator -= now
