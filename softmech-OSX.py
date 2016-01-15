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

sounddir = 'CMStormTKBlue'
sounds = os.listdir(sounddir)

# call subprocess to play the sound (too slow)
def playrandom(sounds):
    Mix_PlayChannel(-1, choice(sounds), 0)
    
# Keyboard Events
class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        downMask = NSKeyDownMask
        upMask = NSKeyUpMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(downMask, downHandler)
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(upMask, upHandler)

# Where the magic begins
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
        raise

# Where the magic begins
def upHandler(event):
    try:
        if(event.keyCode() == 49): # space button
            playrandom(spaceups)
        elif(event.keyCode() == 36): # return button
            playrandom(returnups)
        else:
            playrandom(ups)
    except KeyboardInterrupt:
        raise
        
SDL_Init(SDL_INIT_AUDIO)
Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 1, 256)
sounds = os.listdir(sounddir)

downs =         [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'down.wav' in f]
ups =           [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'up.wav' in f]
spacedowns =    [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'down_space.wav' in f]
spaceups =      [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'up_space.wav' in f]
returndowns =   [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'down_return.wav' in f]
returnups =     [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8')) for f in sounds if 'up_return.wav' in f]
       
#main function
def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    
if __name__ == '__main__':
    print 'let\'s start!'
    try:
        main()
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
        