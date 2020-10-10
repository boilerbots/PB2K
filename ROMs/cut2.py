#!/usr/bin/python

import sys
import array
import numpy as np

full = np.fromfile('pb2k.rom',dtype=np.uint8)

expansion_size = 0x40 * 512
system_size = full.size - expansion_size

bios = np.empty((expansion_size,),dtype=np.uint8)
system = np.empty((system_size,),dtype=np.uint8)

yy = 0
for x in range(0,expansion_size):

  bios[yy] = full[x]

  yy = yy + 1

bios.tofile('bios.rom')

yy = 0
for x in range(expansion_size,system_size):

  system[yy] = full[x]

  yy = yy + 1

system.tofile('system.rom')

print "Done"

