#!/usr/bin/python

import sys
import array
import numpy as np

full = np.fromfile('pb2k.rom',dtype=np.uint8)

system_size = full.size - 0x5000

bios = np.empty((0x5000,),dtype=np.uint8)
system = np.empty((system_size,),dtype=np.uint8)

yy = 0
for x in range(0,0x5000):

  bios[yy] = full[x]

  yy = yy + 1

bios.tofile('bios.rom')

yy = 0
for x in range(0x5000,system_size):

  system[yy] = full[x]

  yy = yy + 1

system.tofile('system.rom')

print "Done"

