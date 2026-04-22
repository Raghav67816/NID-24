import numpy as np
import pandas as pd
from os import getcwd
from random import randint
from neurokit2.emg import emg_simulate

"""
generate emg signals for specified duration
and sampling frequency and channels

* FOR 3 CHANNELS IN THIS SCRIPT *
"""
FREQ = 1000 #1KHZ
DURATION = 60 # 1 MIN
CHANNELS = 3

AMPL_MAX = 10 # mv
AMPL_MIN = 0 # mv

def generate():
    channels = []
    burst_number = randint(0, 5)
    for i in range(0, CHANNELS):
        signals = emg_simulate(
            duration=DURATION,
            sampling_rate=FREQ,
            burst_number=burst_number
        )
        
        channels.append(signals)
        
    df = pd.DataFrame({
        "channel_1": channels[0],
        "channel_2": channels[1],
        "channel_3": channels[2]
    })

    array = np.array(channels)
    
    nbin = open(f"{getcwd()}/data.npy", "wb+")
    csv_file = open(f"{getcwd()}/data.csv", "wb+")
    
    df.to_csv(csv_file, ",", float_format="%.6f", index=False)
    
    np.save(nbin, array)
    
    
generate()
