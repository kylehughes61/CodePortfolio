The code samples in this folder are from a Microcomputer Architecture / Embedded Systems course. Most of the code present was developed by the instructor, Christopher Coulston - with modifications written by myself and a partner in order to complete the lab objectives. The majority of the code found here belongs to Mr. Coulston, with the implementation of the buffering system and ADC being left to our team.



The purpose of these labs was to:

9. Record live microphone input onto an on-board SD card, using double-buffering to prevent read/write errors.

10. Play an audio recording stored on the SD card through an on-board speaker, again using a double buffer.



All of the code for this lab was written in C, and written onto a custom PCB using MPLAB and PuTTY software. The course focused heavily on timers, interrupts, BAUD rates, and the intricacies of writing code for a microcontroller. The specs for the custom board and the chip we were coding for can be found here:

https://inside.mines.edu/~coulston/courses/EENG383/dev21schematic.pdf
https://ww1.microchip.com/downloads/en/DeviceDoc/40001412G.pdf