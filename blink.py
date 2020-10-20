#!/usr/bin/env python

"""blink.py: Turn off and on the onboard RaspberryPi LEDS."""

__author__      = "Christopher Woodall"
__copyright__   = "None"

import sys, os, time

statusGPIO = '/sys/class/leds/led0'

os.system( 'echo gpio | sudo tee {}/trigger > /dev/null 2>&1'.format( statusGPIO ) )

for j in range(10):
  #os.system( 'echo 1 | sudo tee {}/brightness > /dev/null 2>&1'.format( statusGPIO ) ) # led on
  os.system( 'echo 1 | sudo dd status=none of={}/brightness'.format( statusGPIO ) ) # led on
  time.sleep(1)
  #os.system( 'echo 0 | sudo tee {}/brightness > /dev/null 2>&1'.format( statusGPIO ) ) # led off
  os.system( 'echo 0 | sudo dd status=none of={}/brightness'.format( statusGPIO ) ) # led off
  time.sleep(1)

'''
print( sys.argv )

import getopt

#try:
opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
print( opts, args )

'''
