# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:47:43 2022

author: raissa baldez

Description

This program loads the processed repeat station data file to extract the
latitude and longitude information from each station and write them in a file.
This file is the input to acquire the altitude data from the ICGEM website.

"""


# Import modules
import pandas as pd
import mestrado_module as mm
from pathlib import Path

# Paths
input_folder: Path = Path(mm.path_pipeline_01_data_processing)
output_folder: Path = Path(mm.path_pipeline_02_icgem_file)
# Files
input_file: Path = Path(mm.output_01b_code_processed_data)
output_file: Path = Path(mm.output_02_code_icgem_file)


# Load data with Pandas
df = pd.read_csv(input_folder / input_file)

# Check dataframe info
# df.info()

# Create file for LAT LON
icgem_df = df[["Latitude", "Longitude"]]

# Save lat lon file
icgem_df.to_csv(output_folder / output_file,
                index=False, header=False, sep="\t",)
