softmech for OSX
=====
This is a little Python script originally created by rbino (http://github.com/rbino/softmech).
It was edited in order to work on OS X.

It plays a random sound whenever a key is pressed/released. Specifically, I sampled my CMStorm Quickfire TK with Blue Cherry switches.  
Use it to annoy people when you don't have a mechanical keyboard with you.

### Dependencies
This script uses SDL_Mixer, a component of DSL2 library.
 - Install [Homebrew](http://brew.sh/) and on Terminal write this:
```sh
$ brew install sdl2
$ brew install sdl2_mixer
```
It will install SDL2 and the SDL_Mixer component.
 - Go on the [PySDL2 repository](https://bitbucket.org/marcusva/py-sdl2/downloads) and download the latest version of PySDL2 (0.9.3 for now).
 - Extract the package and on Terminal go into the pysdl2 folder and launch the install script:
 ```sh
 $ cd PySDL2-0.9.3
 $ python setup.py install
 ```

### Launching
 - Open Terminal
 - Open System Preferences and go to the "Security & Privacy" section
 - On the "Privacy" tab, click on "Accessibility" and check "Terminal" on the list (remember, you must have Admin privileges)
 - Now, on the Terminal download the repository and launch the script:
```sh
$ git clone https://github.com/zeroerrequattro/softmech.git
$ cd softmech
$ python softmech-OSX.python
```

### Additional sounds
If you want to add your own sounds just put them in a folder and change the `sounddir` variable.  
Sounds to be played on KeyDown must end with "down.wav", sounds to be played on KeyUp must end with "up.wav"
