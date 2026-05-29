from os import listdir
from os.path import exists

import numpy as np
import pandas as pd

path = str(input("Enter directory path: "))

if not exists(path):
    print("Invalid directory path. Please recheck")
    exit()

files = []
cols = []
data_frame = pd.DataFrame()

print("Fetching files from directory.")

for file in listdir(path):
    files.append(f"{path}/{file}")

    print(f"Reading {file}")
    data = np.load(f"{path}/{file}", allow_pickle=True)

    for feature in data[1]:
        for idx, val in enumerate(data[1][feature]):
            cols.append(f"channel_{idx}_{feature}")

    
print(cols)
