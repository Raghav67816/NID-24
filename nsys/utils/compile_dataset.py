from os.path import exists
from os import listdir, getcwd

import numpy as np
import pandas as pd

path = str(input("Enter directory path: "))

if not exists(path):
    print("Invalid directory path. Please recheck")
    exit()

frame = {}
rows = []

print("Fetching files from directory.")

for file in listdir(path):

    print(f"Reading {file}")
    data = np.load(f"{path}/{file}", allow_pickle=True)

    row = {}

    for feature in data[1]:
        for idx, val in enumerate(data[1][feature]):
            row[f'channel_{idx + 1}_{feature}'] = val
            row['label'] = data[0]

    rows.append(row)

dataframe = pd.DataFrame(rows, index=[x for x in range(len(rows))])
save_path = f"{getcwd()}/dataset.csv"
dataframe.to_csv(save_path, ",")
print(f"Dataset saved at: {save_path}")
