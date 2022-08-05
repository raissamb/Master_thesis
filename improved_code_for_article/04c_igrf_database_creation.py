# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:25:37 2022

author: raissa baldez

Description

This program organizes the IGRF13 output file (from the software Geomag70.exe
(Windows versions) available at
<https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html>) in order to create an IGRF13
dataframe. The changes are:
- The substitution of spaces for commas in order to create a truly csv file
- The letters "d" for degree and "m" for minute were deleted from the D_deg,
I_deg, D_min and I_min columns
- The letter "M" in the altitude column (for meters) was removed.

"""


# Import modules
import mestrado_module as mm
import numpy as np
import pandas as pd
from pathlib import Path


# Paths
input_folder: Path = Path(mm.path_pipeline_04_igrf_calc)
output_folder: Path = Path(mm.path_pipeline_04_igrf_calc)
# Files
input_file: Path = Path(mm.output_04b_geomag_file)  # result from geomag
output_file: Path = Path(mm.output_04c_code_igrf_database)  # igrf database
# Repeat station data
rs_file: Path = Path(mm.output_03_code_rs_database)
rs_folder: Path = Path(mm.path_pipeline_03_rs_database_creation)

# Load IGRF data with Pandas
igrf_df = pd.read_csv(input_folder / input_file, sep="\s+", engine="python")

# Read RS data
rs_df = pd.read_csv(rs_folder / rs_file)

# Add Code column from RS dataframe into the IGRF dataframe to act as index
# Create a new dataframe to work on
new_igrf_df = igrf_df.copy()

# Add the colum
new_igrf_df["Code"] = rs_df["Code"]

# Change column order and drop unnecessary columns
new_igrf_df = new_igrf_df[["Code", "Date", "Latitude", "Longitude", "Altitude",
                           "D_deg", "D_min", "I_deg", "I_min", "H_nT", "X_nT",
                           "Y_nT", "Z_nT", "F_nT", "dD_min", "dI_min", "dH_nT",
                           "dX_nT", "dY_nT", "dZ_nT", "dF_nT"]]


# Delete the "M", "d", and "min" words from the database
new_igrf_df["Altitude"] = new_igrf_df["Altitude"].str.replace("M", "")
new_igrf_df["D_deg"] = new_igrf_df["D_deg"].str.replace("d", "")
new_igrf_df["D_min"] = new_igrf_df["D_min"].str.replace("m", "")
new_igrf_df["I_deg"] = new_igrf_df["I_deg"].str.replace("d", "")
new_igrf_df["I_min"] = new_igrf_df["I_min"].str.replace("m", "")

# Convert object types to float64 type
new_igrf_df["Altitude"] = new_igrf_df["Altitude"].astype({"Altitude": float})
new_igrf_df["D_deg"] = new_igrf_df["D_deg"].astype({"D_deg": float})
new_igrf_df["D_min"] = new_igrf_df["D_min"].astype({"D_min": float})
new_igrf_df["I_deg"] = new_igrf_df["I_deg"].astype({"I_deg": float})
new_igrf_df["I_min"] = new_igrf_df["I_min"].astype({"I_min": float})

# Check the changes
# new_igrf_df.info()

# Mark the signal of each degree value for D and I as positive or negative
# to convert from dms to decimal degree correctly
new_igrf_df["D_signal"] = np.where(new_igrf_df["D_deg"] >= 0,
                                   "Positive", "Negative")
new_igrf_df["I_signal"] = np.where(new_igrf_df["I_deg"] >= 0,
                                   "Positive", "Negative")

# Add the colums with the markers for D and I
df_dec_dpositivo = new_igrf_df.loc[new_igrf_df["D_signal"] == "Positive"]
df_dec_dnegativo = new_igrf_df.loc[new_igrf_df["D_signal"] == "Negative"]
df_inc_dpositivo = new_igrf_df.loc[new_igrf_df["I_signal"] == "Positive"]
df_inc_dnegativo = new_igrf_df.loc[new_igrf_df["I_signal"] == "Negative"]

# Convert Declination to decimal degrees
new_igrf_df["IGRF_D_dd"] = np.where(new_igrf_df['D_signal'] == 'Positive',
                                    (new_igrf_df["D_deg"] +
                                     (new_igrf_df["D_min"] / 60)),
                                    (new_igrf_df["D_deg"] -
                                     (new_igrf_df["D_min"] / 60))
                                    )

# Convert Inclination to decimal degrees
new_igrf_df["IGRF_I_dd"] = np.where(new_igrf_df['I_signal'] == 'Positive',
                                    (new_igrf_df["I_deg"] +
                                     (new_igrf_df["I_min"] / 60)),
                                    (new_igrf_df["I_deg"] -
                                     (new_igrf_df["I_min"] / 60))
                                    )

"""
# EXPLANATION:
# For the case where degree is greater or equal to 0, the conversion is:
#    decimal = degrees + (minutes)/60
# When degree is a negative value, the formula becomes:
#    decimal = degrees - (minutes)/60

"""

# Create new main dataframe for IGRF13 values
# Change column names
new_igrf_df = new_igrf_df.rename(
    columns={
        "D_deg": "IGRF_D_deg",
        "D_min": "IGRF_D_min",
        "I_deg": "IGRF_I_deg",
        "I_min": "IGRF_I_min",
        "H_nT": "IGRF_H_nT",
        "X_nT": "IGRF_X_nT",
        "Y_nT": "IGRF_Y_nT",
        "Z_nT": "IGRF_Z_nT",
        "F_nT": "IGRF_F_nT",
        "dD_min": "IGRF_dD_min",
        "dI_min": "IGRF_dI_min",
        "dH_nT": "IGRF_dH_nT",
        "dX_nT": "IGRF_dX_nT",
        "dY_nT": "IGRF_dY_nT",
        "dZ_nT": "IGRF_dZ_nT",
        "dF_nT": "IGRF_dF_nT",
    }
)
new_igrf_df

# Save the IGRF database
new_igrf_df.to_csv(output_folder / output_file, index=False)

# float_format="%.3f"
