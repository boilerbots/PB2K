#!/usr/bin/python

import sys
import array
import math
import numpy as np

list = [ ['swe1_u100.rom','swe1_u101.rom'],
        ['swe1_u102.rom','swe1_u103.rom'],
        ['swe1_u104.rom','swe1_u105.rom'],
        ['swe1_u106.rom','swe1_u107.rom']]

#total_size = (8*(math.pow(2,22))*2) / 4  # 8 chips * 8meg bytes in words
total_size = (len(list)*(math.pow(2,22))*2) / 4  # n chips * 8meg bytes in words
print("Total Size: ", total_size)
wd = np.empty((int(total_size),),dtype=np.uint32)
xx = 0

for (ln,hn) in list:

  print("Opening: ", ln, " and ", hn)
  low = np.fromfile( ln,dtype=np.uint16)
  high = np.fromfile( hn,dtype=np.uint16)

  yy = 0
  for lw in low:

    wd[xx] = (lw + (high[yy] << 16))

    xx = xx + 1
    yy = yy + 1

wd.tofile('pb2k.rom')

print("Done")

