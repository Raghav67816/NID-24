# NID-24

NID-24 is a EMG based Humand Device Interface system that allows users to experience unique ways to interact with computers.

![alt text](<images/Zine.png>)

Demo Link - [NID-24 Demo](https://youtu.be/rfTXhZ9J3WQ)

This project allows users to use their hand as mouse. Based on ADS1293 and state-of-the-art software architecture, it continously classifies intent and executes it via bluetooth.

## Why I am building NID-24 ?
Biotech is super awesome, it sits at the intersection of biology and technology. Most of my projects that I made are inspired by sci-fi movies. So, this one is special one from Iron Man 3.

Also, I have some experience in working with EEG, however, I don't have access to a specialised lab, I am building this surface EMG (sEMG) system.


**The second phase of this project will involve finding relevant techniques for making robust EMG system which will can tolerate muscle fatigue and deliver similar performance.**

## Features

 - Analysis Software - Watch and Record Signals In Real Time.

  - ADS1293 Simulator Android App - Don't have the hardware ? Don't worry we have an android app to simulate the hardware readings.

  - Controller Board - Consists of the main MCU Teensy 4.0 for on-board processing, 3 push buttons for menu control, a bluetooth module for data transfer and an OLED 0.96 Inch display

  - ADS1293 based Board - ADS1293 the heart of this project sits at the center of this PCB allowing easy interfacing of chip with the system.

## Directory Structure
- nsys - Analysis Software
- controller_board - The Controller Board
- ads1293_board - The ADS1293 based board
- SignalsSimulator - The Android App (It has it's own readme. Follow instructions to use and install)


## Analysis Software 

![alt text](<images/image copy.png>)
 <!-- Replace this image -->

The Analysis Software allows developers to study the signals to gather information about the signal.

This software visualises all the information from ADS1293.


The features are as follows:
 - 3 Channel EMG (50 ms visual update rate)
 - Latency Meter
 - Data Recorder


## ADS1293 Simulator
Don't worry if you don't have your hardware yet. Just download this app and it will act like our ADS1293 based board.

![alt text](images/image.png)
Currently, it is orientated in Landscape mode, works with potrait too.

This will act like ADS1293 and send data to our computer/analysis software for analysis.

**After using/disconnecting this app. Please make sure to clear it from the background also to avoid residual**


## ADS1293 Based Board (THE HEART)


| Render | PCB |
|--------|--------|
| ![alt text](images/ads-reimagined.png) | ![alt text](<images/Screenshot from 2026-03-30 13-17-23-2.png>) |

### Features:
 - 24-bit resolution
 - Reduced EMI
 - Saperated analog and digital traces
 - Meets SIMEAN safety standards


This board acquires raw signals from the muscle fibers, the in-built amplifier amplifies the signals and converts AC values to DC values that an be understood by our machines.

We read this data and draw our conclusions

## Controller Board

| Render | PCB |
|--------|--------|
| ![alt text](images/cb-reimagined.png) | ![alt text](images/cb-case.png)|

Using simulator is easy you can connect to your PC via system ui bluetooth but we don't have any way to connect out Teensy 4.0 to our PC. So, this PCB has 3 push buttons, 
Teensy 4.0, OLED 0.96 Display and a bluetooth module for data transfer.

Controller Board case Onshape [link here.](https://cad.onshape.com/documents/cf77a823cf461f5b911517e3/w/527c1a40b344ced2cb5cf64d/e/4507412c1ac5528a6c833cb1?renderMode=0&uiState=69ee44c7155ef2a92238ec7a)

Features of Case:

1. Smooth curves / No sharp edges
2. No screws required
3. Proper spacing for NRF24L01 module and USB for debugging


## BOM
Please refer to [BOM.csv](https://github.com/Raghav67816/NID-24/blob/9190ff4f1dc71be3fecc9d7e1874cc27b3e914db/BOM%20Final.csv)

## Software Installation 

 - Clone the repository
   ```bash
   git clone https://github.com/Raghav67816/NID-24.git
   ```

- Install requirements
  ```bash
  pip3 install -r requirements.txt
  ```
  
- Either Setup Real Hardware or Use The Simulator
**WARNING FOR HARDWARE USERS: I am currently unable to disable RLD because of some unknown reasons, their are strong chances that ADS1293 was damaged during assembly. Please measure RLD output before putting electrodes on your body**.

  For hardware, assemble both the boards as defined in the PCB files. And flash the firmware on Controller Board

  Or, safest option is to use the ADS1293 Simulator app

  1. Install the app
  2. Make sure that you enable bluetooth and connect to your PC before starting the app.
  3. Open the app
  4. Select your PC as target device
  5. Click start in NID-24 Analysis Software on your PC
  6. Click Start in your simulator app on mobile
