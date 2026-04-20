import numpy as np
import pandas as pd
from os import getcwd
from random import randint
from neurokit2.emg import emg_simulate

"""
generate emg signals for specified duration
and sampling frequency and channels

* FOR 3 CHANNELS IN THIS SCRIPT *`
"""
freq = float(input("Enter sampling frequency (hz): "))
channels = int(input("Enter number of channels: "))
duration = int(input("Enter duration (secs): "))
filename = str(input("Enter filename: "))

def generate():
    channels = []
    burst_number = randint(0, 5)
    for i in range(0, len(channels)):
        signals = emg_simulate(
            duration=duration,
            sampling_rate=freq,
            burst_number=burst_number
        )
        
        channels.append([signals])
        
    df = pd.DataFrame({
        "channel_1": channels[0][0],
        "channel_2": channels[1][0],
        "channel_3": channels[2][0]
    })
        
    array = np.array(channels)
    
    nbin = open(f"{getcwd()}/synthetic_data/{filename}.npy", "wb+")
    csv_file = open(f"{getcwd()}/synthetic_data/{filename}.csv", "wb+")
    
    df.to_csv(csv_file, ",", "%.6f")
    
    np.save(nbin, array)
    
generate()
