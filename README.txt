
This project is about updating the firmware for the pinball 2000 platform so
that it will run on a more modern machine.

                          Background

The Pinball 2000 architecture is comprised of an x86 computer that drives the
machines power board through a standard bi-directional parallel port.

The AT motherboard uses a Cyris MediaGX process (Pentium kind-of) running at 233
MHz. The MediaGX processor is somewhat unique in that it features a built in
video driver and sound blaster compatible audio. The firmware should not care
about the sound blaster as it uses it's own audio.

The program, or firmware, for the machine resides in ROM chips located on a PCI
card. The ROM chips are 16 bits wide and there are 8 of them. The audio is on 2
additional ROM chips. The ROM U100 through U107 are wired in parallel to create
32bit wide data for the CPU.

The 4 pairs of ROMs have their own selects. The controller card uses a PCI9050
PCI bridge which contains an eeprom that is programmed for the address space for
each of the 4 address selects.

The 2 sound ROMs appear to be independent from the the other ROMs, they have
their own address and data bus.


                        Goal of this project


Since all of this is based on x86 and a parallel port it should be possible to
run this program natively on a more modern computer. There are various
approaches that we can take but need to understand the code a little further.
Here are some ideas:

1. Put the code on a simple flash drive and run all the code as it was designed.
The code runs in it's own OS called XINA. We update the pieces that are broken,
perhaps change the audio to use the computers own audio card.

2. Extract the main program and run it under Linux.

Option 2 would be nice because the game could be modified to make use of the OS,
such as networking, graphics, sound and a file system.

The goal is not to run in an emulator under Linux, it shouldn't be necessary.

