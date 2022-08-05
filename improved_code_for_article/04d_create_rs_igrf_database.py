# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 23:26:36 2022

author: raissa baldez

Description

This program creates the database from repeat station and IGRF data
"""

# Import modules
import mestrado_module as mm
import pandas as pd
from pathlib import Path

# Defitions for input and output

# Input repeat stations
input_rs_folder: Path = Path(mm.path_pipeline_03_rs_database_creation)
input_rs_file: Path = Path(mm.output_03_code_rs_database)

# Station list
input_list_stations_folder: Path = Path(
    mm.path_pipeline_03_rs_database_creation)
input_list_stations_file: Path = Path(mm.output_03_code_ocp_list)

# Input IGRF values
input_igrf_folder: Path = Path(mm.path_pipeline_04_igrf_calc)
input_igrf_file: Path = Path(mm.output_04c_code_igrf_database)

# Output
output_folder: Path = Path(mm.path_pipeline_04_igrf_calc)
output_file: Path = Path(mm.output_04d_code_rs_igrf_database)
err_db: Path = Path(mm.output_04d_code_error_database)


# Load station and IGRF data with Pandas
rs_df = pd.read_csv(input_rs_folder / input_rs_file)

# Load station and IGRF data with Pandas
igrf_df = pd.read_csv(input_igrf_folder / input_igrf_file)

# Create a dataframe with repeat station data and IGRF values
main_db = rs_df.copy()
main_db["IGRF_D_dd"] = igrf_df["IGRF_D_dd"]
main_db["IGRF_I_dd"] = igrf_df["IGRF_I_dd"]
main_db["IGRF_F_nT"] = igrf_df["IGRF_F_nT"]
main_db["IGRF_H_nT"] = igrf_df["IGRF_H_nT"]
main_db["IGRF_X_nT"] = igrf_df["IGRF_X_nT"]
main_db["IGRF_Y_nT"] = igrf_df["IGRF_Y_nT"]
main_db["IGRF_Z_nT"] = igrf_df["IGRF_Z_nT"]

# Organize main database
main_db = main_db[
    ["Name", "Code", "Latitude", "Longitude", "Altitude",
     "Time", "D", "IGRF_D_dd", "I", "IGRF_I_dd", "F",
     "IGRF_F_nT", "H", "IGRF_H_nT", "X", "IGRF_X_nT",
     "Calculated_X", "Y", "IGRF_Y_nT", "Calculated_Y", "Z",
     "IGRF_Z_nT", "Calculated_Z",
     "Number_occupations", "Nearest_Observatory", "TTB_distances_km",
     "VSS_distances_km", "State", "Region"]
]

# Save database
main_db.to_csv(output_folder / output_file, index=False, na_rep="NaN")
# float_format="%.3f"
