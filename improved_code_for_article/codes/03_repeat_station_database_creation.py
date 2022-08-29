# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:53:39 2022

author: raissa baldez

Description

This program creates the repeat station database. In order to create the
database, this program does the following:
- It inserts the values of altitude from the ICGGEM website
- It calculates the missing values for the Y and Z components using the
following equations:
 1. X =  F cos I cos D
 2. Y = F cos I sin D
 3. Z = F sin I

- It calculates the distance between a station and the VSS and TTB
observatories to see which is closer to the station. Then, it adds this info
to the database.
- It calculates how many times a station has been occupied over time and
associate the value with the station code into the dataframe

ATTENTION: IT IS UNCERTAIN IF THE REPEAT STATION DATA FROM 1980 TO 2019 WENT
THROUGH THE NECESSARY PROCESSING STEPS TO REMOVE THE EXTERNAL EFFECTS FROM THE
MAGNETIC FIELD IN ORDER TO USE IT TO STUDY SECULAR VARIATION.

"""


# Import modules
import pandas as pd
import numpy as np
import mestrado_module as mm
from pathlib import Path

# Path
input_folder: Path = Path(mm.path_pipeline_01_data_processing)
output_folder: Path = Path(mm.path_pipeline_03_rs_database_creation)
altitude_folder: Path = Path(mm.path_pipeline_02_icgem_file)
# File names
input_file: Path = Path(mm.output_01b_code_processed_data)
icgem_file: Path = Path("EIGEN-6C4_output_manual.csv")
ocp_list: Path = Path(mm.output_03_code_ocp_list)
output_file: Path = Path(mm.output_03_code_rs_database)

# Load data with Pandas
df = pd.read_csv(input_folder / input_file)

# Insert altitude values into the database
# Load ICGEM file with altitude
df_alt = pd.read_csv(altitude_folder / icgem_file)

# Choosing the altitude
# alt = df_alt["topo_ell"]
alt = df_alt["h_topo_over_geoid_meter"]

# Insert altitude values
df.insert(4, "Altitude", alt)


# Calculation of the X, Y and Z components
dec = df["D"]
inc = df["I"]
total_field = df["F"]
calc_x = mm.calculate_x_comp_mag_field(total_field, inc, dec)
calc_y = mm.calculate_y_comp_mag_field(total_field, inc, dec)
calc_z = mm.calculate_z_comp_mag_field(total_field, inc)

# Comparison between calculated values and observed for Y and Z components
# Add columns with the calculated values for each component
df["Calculated_X"] = calc_x
df["Calculated_Y"] = calc_y
df["Calculated_Z"] = calc_z

# RMSE calculation using the function in the mestrado module
obs_x = df["X"]
obs_y = df["Y"]
obs_z = df["Z"]
rmse_x = mm.rmse(calc_x, obs_x)
rmse_y = mm.rmse(calc_y, obs_y)
rmse_z = mm.rmse(calc_z, obs_z)


# Calculate distances between a station and an Observatory using the
# Haversine formula inside the mestrado module
# Create new dataframe to work on
df_dist_calc = df.copy()

# Observatories location according to Intermagnet in degrees
# (from mestrado module)
TTB_lat = mm.TTB_lat
TTB_lon = mm.TTB_lon
VSS_lat = mm.VSS_lat
VSS_lon = mm.VSS_lon

# Calculate
TTB_distances = mm.haversine_array(
    df_dist_calc["Longitude"], df_dist_calc["Latitude"], TTB_lon, TTB_lat)
VSS_distances = mm.haversine_array(
    df_dist_calc["Longitude"], df_dist_calc["Latitude"], VSS_lon, VSS_lat)

# Insert distances into the dataframe
df_dist_calc["TTB_distances_km"] = TTB_distances
df_dist_calc["VSS_distances_km"] = VSS_distances


# Determine which observatory is closer to each station
# Define conditions to see which is closer
conditions = [
    df_dist_calc["TTB_distances_km"] < df_dist_calc["VSS_distances_km"],
    df_dist_calc["TTB_distances_km"] > df_dist_calc["VSS_distances_km"]
]

# Define choices
choices = ["TTB", "VSS"]

# Create new column in DataFrame that displays results of comparisons
df_dist_calc["Nearest_Observatory"] = np.select(
    conditions, choices, default='Tie')


# Count the number of occupation for each station
# Dataframe to work
df_count = df_dist_calc.copy()

# Count the number of times each station was occupied
n_stations_occupations = df_count.groupby("Name").size()
# Another way to count the number of occupations: it creates a dataframe
# df2 = df_count.groupby("Code").count()

# Convert number of occupation from series to array of numbers
n_stations_occupations_array = n_stations_occupations.to_numpy()

# Create variable to hold stations name
rs_names_array = df_count.Name.unique()

# Create a dataframe from the arrays
rs_occupation_info = pd.DataFrame({"Name": rs_names_array})
rs_occupation_info["Number_occupations"] = pd.Series(
    n_stations_occupations_array)
# Save this to a file
rs_occupation_info.to_csv(output_folder / ocp_list, index=False)

# Add a column to the dataframe with the number of occupations for each
# stations based on the count done before
# Create a new dataframe to work on and the number of occupations column with
# an fixed value to be changed later
df_ocp = df_count.copy()
df_ocp["Number_occupations"] = 0

# Create a loop to read the names and number of occupations arrays to
# substitute the 0 value for the correct one
for i in range(len(rs_names_array)):
    df_ocp.loc[df_ocp['Name'] == rs_names_array[i],
               "Number_occupations"] = n_stations_occupations_array[i]


# Save the repeat station database
# Create main database
df_final = df_ocp.copy()

# Organize header order according to the IGRF software calculator
df_final = df_final.loc[:,
                        ["Name", "Code", "Latitude", "Longitude", "Altitude",
                         "Time", "D", "I", "H", "X", "Y", "Z", "F", "State",
                         "Region", "Calculated_X", "Calculated_Y",
                         "Calculated_Z", "TTB_distances_km",
                         "VSS_distances_km", "Nearest_Observatory",
                         "Number_occupations",
                         ]
                        ]


# Save main database file, three decimals places only
df_final.to_csv(output_folder / output_file, index=False,
                na_rep="NaN")


# float_format="%.3f
