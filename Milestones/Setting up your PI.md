#Setting up your PI 

Grab the items from the store that marty linked above, and have a look at the learn raspberry pi learn guide
Make sure all peripherals are plugged in before you turn on your pi (microSD card, wifi addapter, keyboard, screen)
Depending on what screen you use, you may have to change some settings in the config.txt file on the Pi's SD card

Once you get the pi to boot, login with username pi and password raspberry

To enable wifi we will need to use a few linux commands
   sudo - this allows us to run a command as 'super user', who has all privileges to do whatever they want on the system
   nano - this is a simple linux text editor program

type into the command line sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

At the bottom of this file, add the lines:
    network={
       ssid="your wifi network name here"
       psk="your wifi password here"
     }
using your network info

hit ctrl + x to exit nano.

then type sudo reboot to apply these changes

you can test that your pi is connected to the network by typing ping google.com and then once you see that you are in fact getting pings, ctrl + c to stop pinging and return to the command line

##Updating your pi
once you are connected to the internet, you can use apt-get, a linux command line package manager, to update the software on your pi.
First however, you may want to remove some unnecessary software from your pi. Otherwise you will likely run out of space when trying to update or install new software

run sudo apt-get purge wolfram-engine to remove the wolfram engine (google it if you'd like) from your pi and get like 450 MB of disk space back for other things

then you can run sudo apt-get update and once that's done sudo apt-get upgrade to update and upgrade software on your pi. This may take some time to complete

once that's done (or if you get any errors that say you've run out of disk space) you can run sudo apt-get clean to clean up unnecessary stuff

##Installing a python library
We will use the linux package manager again to get a python library we need to work on our project. We will get pycurl to request data from the server

use sudo apt-get install python-pycurl to find the pycurl package on the internet and install it onto your pi

##running python on the pi
to run python commands on the pi, we can use the python interpreter. type python to bring up the interpreter, and you can write python code directly into the terminal. once you are finished type exit() to exit the interpreter.

we can also run python files with the python interpreter that comes with the pi. type nano test.py to create a file called test.py. Write a few lines of python, and then pres ctrl + x to exit.

you can then type python test.py to run the program you just wrote!

##MILESTONE 2

From here, we want to get the same data (the contents of https://www.adafruit.com/python_rocks.txt) we got in milestone 1 to the pi. Use the pycurl documentation and nano to write a python program that, when run using python myPythonFile.py, will output the contents of https://www.adafruit.com/python_rocks.txt to your screen.

Good luck and let me know if you have any questions!