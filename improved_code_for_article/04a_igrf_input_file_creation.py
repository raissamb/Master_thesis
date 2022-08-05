# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:08:40 2022

author: raissa baldez

Description

This program creates the input file to calculate the magnetic components values
for all the stations in the database using the IGRF13 model. This input file is
read by the software Geomag70.exe (Windows versions) available at
<https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html>

"""

# Import modules
import mestrado_module as mm
import pandas as pd
from pathlib import Path

# Paths
input_folder: Path = Path(mm.path_pipeline_03_rs_database_creation)
output_folder: Path = Path(mm.path_pipeline_04_igrf_calc)
# Files
input_file: Path = Path(mm.output_03_code_rs_database)
igrf_input_file: Path = Path(mm.output_04a_code_igrf_input_file)

# Load data with Pandas
df = pd.read_csv(input_folder / input_file)

# Create IGRF input dataframe (it only needs lat, lon, alt and time columns)
df2 = df[["Time", "Altitude", "Latitude", "Longitude"]].copy()
df2 = df2.round(3)


# Create "M" list for meters and "D" list for Geodetic coordinates
n = len(df2)
lst1 = ["M"] * n
lst2 = ["D"] * n

# Insert "D" column to mark Geodetic coordinates into the igrf input file
df2.insert(1, "D", lst2)

# Insert 'M" column to mark meter for the altitude values into the igrf columns
df2.insert(2, "M", lst1)

# Create a new df to modify the altitude column from float to string type
df3 = df2.copy()

# Create a new variable to hold the altitude in string type
alt_string = df3["Altitude"].apply(str)

# Insert alt_str into the dataframe
df3.insert(3, "Alt_string", alt_string)

# Concatenate the columns M and AlT_str to create the the format MX for the
# input file, where M is for meters and X is the altitude value
alt_m = df3["M"] + df3["Alt_string"]

# Insert alt_m column into the dataframe
df3.insert(2, "Alt_string_M", alt_m)

# Final database
df4 = df3.drop(columns=["M", "Altitude", "Alt_string"])

df4.to_csv(output_folder / igrf_input_file,
           index=False,
           header=False,
           sep="\t",
           float_format="%.3f",
           )
