#!/usr/bin/python

from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask, NSKeyUpMask
from PyObjCTools import AppHelper
from random import choice
from sdl2 import *
from sdl2.ext.compat import byteify
from sdl2.sdlmixer import *
import os

# select the audio folder
sounddir    = 'CMStormTKBlue'
sounds      = os.listdir(sounddir)

# initialization of the SDL audio component
SDL_Init(SDL_INIT_AUDIO)
Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 1, 256)

downs =         [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'down.wav' in f]
ups =           [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'up.wav' in f]
spacedowns =    [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'down_space.wav' in f]
spaceups =      [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'up_space.wav' in f]
returndowns =   [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'down_return.wav' in f]
returnups =     [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'up_return.wav' in f]

# Keyboard Events, keyDown and keyUp events are catched here
class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        downMask = NSKeyDownMask
        upMask = NSKeyUpMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(downMask, downHandler)
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(upMask, upHandler)
        
# play a random audiofile from a list
def playrandom(sounds):
    Mix_PlayChannel(-1, choice(sounds), 0)

# keyboard Down event handler
def downHandler(event):
    try:
        if (not event.isARepeat()):
            if(event.keyCode() == 49): # space button
                playrandom(spacedowns)
            elif(event.keyCode() == 36): # return button
                playrandom(returndowns)
            else:
                playrandom(downs)
        if(event.keyCode() == 53 and event.isARepeat()): #ESC key
            playrandom(ups)
            AppHelper.stopEventLoop()
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
        raise

# keyboard Up event handler
def upHandler(event):
    try:
        if(event.keyCode() == 49): # space button
            playrandom(spaceups)
        elif(event.keyCode() == 36): # return button
            playrandom(returnups)
        else:
            playrandom(ups)
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
        raise
       
#main function
def main():
    try:
        app = NSApplication.sharedApplication()
        delegate = AppDelegate.alloc().init()
        NSApp().setDelegate_(delegate)
        AppHelper.runEventLoop()
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
    
if __name__ == '__main__':
    main()