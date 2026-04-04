# NID-24

NID-24 stands for **Neural Intent Decoder** and 24 stands for **24-bit ADC**.

This project aims at developing an EMG based human device interface system.
For example: Using a cursor without a traditional mouse just with your hand.

The project is divided into following parts:
 - PCB
 - Software
 - Firmware

All the topics stated above are explored in depth further in this documentation.

!!! note "NOTE"

	Project files including PCB and software are subject to frequent changes


## Quick Overview

We are developing a custom ADS1293 (24-bit Analog Front End) to acquire and 
filter signals. These signals are then sent to MCU (Teensy 4.0, initially), which is then processed
to extract features to identify muscle intent.

We target for lowest possible latency for intent classification for smoother user experience.

The process above is PHASE-1 which focuses on building the foundation of the system.

PHASE-2 involves solidifying the foundational architecture by making the system compatible with 
muscle fatigue.

