from os import listdir
from pandas import DataFrame, read_csv


files = listdir("./data/")

for index, file in enumerate(files):
    temp_df = DataFrame(read_csv(f"./data/{file}"))
    temp_df = temp_df.drop(columns=temp_df.columns[3:8], axis=0)
    print(f"Trimming {file}....")
    temp_df.to_csv(f"./cropped_data/{index}.csv")
    print(f"Done: Saved as {index}.csv")
