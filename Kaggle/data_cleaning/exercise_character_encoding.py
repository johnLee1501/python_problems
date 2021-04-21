# modules we'll use
import pandas as pd
import numpy as np

# helpful character encoding module
import chardet

# set seed for reproducibility
np.random.seed(0)
# You're working with a dataset composed of bytes. Run the code cell below to print a sample entry.
sample_entry = b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))
# Use the next code cell to create a variable new_entry that changes the encoding from "big5-tw" to "utf-8".
# new_entry should have the bytes datatype.
before = sample_entry.decode("big5-tw")
new_entry = before.encode()
# Use the code cell below to read in this file at path "../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv".
# Figure out what the correct encoding should be and read in the file to a DataFrame police_killings.
# police_killings = ____
with open("../data/PoliceKillingsUS.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read())
police_killings = pd.read_csv("../data/PoliceKillingsUS.csv", encoding='Windows-1252')
# Save a version of the police killings dataset to CSV with UTF-8 encoding.
# Your answer will be marked correct after saving this file.
# Note: When using the to_csv() method, supply only the name of the file (e.g., "my_file.csv").
# This saves the file at the filepath "/kaggle/working/my_file.csv"
police_killings.to_csv("police_killings-utf8.csv")
pass
