# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 23:38:10 2022

author: raissa baldez

Description

This program does the calculates the RMSE for both datasets in relation to
IGRF13 model for all components

"""

# Import modules
import mestrado_module as mm
import pandas as pd
from pathlib import Path

# Defitions for input and output
input_folder: Path = Path(mm.path_pipeline_04_igrf_calc)
input_file: Path = Path(mm.output_04d_code_rs_igrf_database)

# Output
output_folder: Path = Path(mm.path_pipeline_04_igrf_calc)
rmse_file: Path = Path(mm.output_04d_code_error_database)
final_database: Path = Path(mm.output_04e_code_complete_rs_igrf_database)

# Load station and IGRF data with Pandas
df = pd.read_csv(input_folder / input_file)


# Create a list with station codes
list_station_codes = df["Code"].unique()


# RMSE calculation: Original repeat station values and IGRF

# Create the arrays for rmse component
rmse_original_igrf_d = []
rmse_original_igrf_i = []
rmse_original_igrf_f = []
rmse_original_igrf_h = []
rmse_original_igrf_x = []
rmse_original_igrf_y = []
rmse_original_igrf_z = []

for i in list_station_codes:
    station_name = i
    aux_df = df[df["Code"] == station_name]

    # Calculate RMSE
    rmse_val_orig_d = mm.rmse(aux_df["IGRF_D_dd"], aux_df["D"])
    # append the result of each loop to the array
    rmse_original_igrf_d.append(rmse_val_orig_d)

    # Calculate RMSE
    rmse_val_orig_i = mm.rmse(aux_df["IGRF_I_dd"], aux_df["I"])
    # append the result of each loop to the array
    rmse_original_igrf_i.append(rmse_val_orig_i)

    # Calculate RMSE
    rmse_val_orig_f = mm.rmse(aux_df["IGRF_F_nT"], aux_df["F"])
    # append the result of each loop to the array
    rmse_original_igrf_f.append(rmse_val_orig_f)

    # Calculate RMSE
    rmse_val_orig_h = mm.rmse(aux_df["IGRF_H_nT"], aux_df["H"])
    # append the result of each loop to the array
    rmse_original_igrf_h.append(rmse_val_orig_h)

    # Calculate RMSE
    rmse_val_orig_x = mm.rmse(aux_df["IGRF_X_nT"], aux_df["X"])
    # append the result of each loop to the array
    rmse_original_igrf_x.append(rmse_val_orig_x)

    # Calculate RMSE
    rmse_val_orig_y = mm.rmse(aux_df["IGRF_Y_nT"], aux_df["Y"])
    # append the result of each loop to the array
    rmse_original_igrf_y.append(rmse_val_orig_y)

    # Calculate RMSE
    rmse_val_orig_z = mm.rmse(aux_df["IGRF_Z_nT"], aux_df["Z"])
    # append the result of each loop to the array
    rmse_original_igrf_z.append(rmse_val_orig_z)


# RMSE calculation: calculated repeat station values and IGRF
# Create the arrays for rmse component
rmse_calculated_x_igrf_x = []
rmse_calculated_y_igrf_y = []
rmse_calculated_z_igrf_z = []

for i in list_station_codes:
    station_code = i
    aux_df = df[df["Code"] == station_code]

    # Calculate RMSE
    rmse_val_calc_x = mm.rmse(aux_df["IGRF_X_nT"], aux_df["Calculated_X"])
    # append the result of each loop to the array
    rmse_calculated_x_igrf_x.append(rmse_val_calc_x)

    # Calculate RMSE
    rmse_val_calc_y = mm.rmse(aux_df["IGRF_Y_nT"], aux_df["Calculated_Y"])
    # append the result of each loop to the array
    rmse_calculated_y_igrf_y.append(rmse_val_calc_y)

    # Calculate RMSE
    rmse_val_calc_z = mm.rmse(aux_df["IGRF_Z_nT"], aux_df["Calculated_Z"])
    # append the result of each loop to the array
    rmse_calculated_z_igrf_z.append(rmse_val_calc_z)

# Create dataframe for rmse values
rmse_data = {"Code": list_station_codes,
             "RMSE_D_Original_values_IGRF": rmse_original_igrf_d,
             "RMSE_I_Original_values_IGRF": rmse_original_igrf_i,
             "RMSE_F_Original_values_IGRF": rmse_original_igrf_f,
             "RMSE_H_Original_values_IGRF": rmse_original_igrf_h,
             "RMSE_X_Original_values_IGRF": rmse_original_igrf_x,
             "RMSE_X_Calculated_values_IGRF": rmse_calculated_x_igrf_x,
             "RMSE_Y_Original_values_IGRF": rmse_original_igrf_y,
             "RMSE_Y_Calculated_values_IGRF": rmse_calculated_y_igrf_y,
             "RMSE_Z_Original_values_IGRF": rmse_original_igrf_z,
             "RMSE_Z_Calculated_values_IGRF": rmse_calculated_z_igrf_z}

rmse_df = pd.DataFrame(data=rmse_data)

# Save df
rmse_df.to_csv(output_folder / rmse_file, index=False, na_rep="NaN")
# float_format="%.3f"

# Create the final database: Repeat station, IGRF and RMSE values
df_final = df.copy()
# Add the columns
df_final["RMSE_D_Original_values_IGRF"] = 0
df_final["RMSE_I_Original_values_IGRF"] = 0
df_final["RMSE_F_Original_values_IGRF"] = 0
df_final["RMSE_H_Original_values_IGRF"] = 0
df_final["RMSE_X_Original_values_IGRF"] = 0
df_final["RMSE_X_Calculated_values_IGRF"] = 0
df_final["RMSE_Y_Original_values_IGRF"] = 0
df_final["RMSE_Y_Calculated_values_IGRF"] = 0
df_final["RMSE_Z_Original_values_IGRF"] = 0
df_final["RMSE_Z_Calculated_values_IGRF"] = 0


# Create a loop to read the names rmse values to substitute the 0 value for
# the correct ones
for i in range(len(list_station_codes)):
    df_final.loc[df_final['Code'] == list_station_codes[i],
                 "RMSE_D_Original_values_IGRF"] = rmse_original_igrf_d[i]
    df_final.loc[df_final['Code'] == list_station_codes[i],
                 "RMSE_I_Original_values_IGRF"] = rmse_original_igrf_i[i]
    df_final.loc[df_final['Code'] == list_station_codes[i],
                 "RMSE_F_Original_values_IGRF"] = rmse_original_igrf_f[i]
    df_final.loc[df_final['Code'] == list_station_codes[i],
                 "RMSE_H_Original_values_IGRF"] = rmse_original_igrf_h[i]
    df_final.loc[df_final['Code'] == list_station_codes[i],
                 "RMSE_X_Original_values_IGRF"] = rmse_original_igrf_x[i]
    df_final.loc[df_final['Code'] == list_station_codes[i],
                 "RMSE_X_Calculated_values_IGRF"] = rmse_calculated_x_igrf_x[i]
    df_final.loc[df_final['Code'] == list_station_codes[i],
                 "RMSE_Y_Original_values_IGRF"] = rmse_original_igrf_y[i]
    df_final.loc[df_final['Code'] == list_station_codes[i],
                 "RMSE_Y_Calculated_values_IGRF"] = rmse_calculated_y_igrf_y[i]
    df_final.loc[df_final['Code'] == list_station_codes[i],
                 "RMSE_Z_Original_values_IGRF"] = rmse_original_igrf_z[i]
    df_final.loc[df_final['Code'] == list_station_codes[i],
                 "RMSE_Z_Calculated_values_IGRF"] = rmse_calculated_z_igrf_z[i]

df_final.to_csv(output_folder / final_database, index=False, na_rep="NaN")
# float_format="%.3f"
