# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 00:18:21 2022

author: raissa baldez

Description

This program plots the temporal series for the X, Y and Z components using the
original repeat station values, the calculated ones, and the values given
by IGRF

"""

# Import modules
import mestrado_module as mm
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Defitions for input and output
input_folder: Path = Path(mm.path_pipeline_04_igrf_calc)
input_file: Path = Path(mm.output_04e_code_complete_rs_igrf_database)

# Output
output_folder: Path = Path(mm.path_pipeline_04_igrf_calc_figures)
output_file: Path = Path(mm.output_04d_code_error_database)


# Load repeat station and IGRF data with Pandas
df = pd.read_csv(input_folder / input_file)

# Create a list with station codes
list_station_codes = df["Code"].unique()

# To acquire the RMSE values, a dataframe with only one row for each repeat
# station is necessary
df_rmse_values = df.drop_duplicates(
    subset="Code", keep="last", inplace=False)  # last occurence
df_rmse_values.reset_index(drop=True, inplace=True)
list_station_codes_rmse_values = df_rmse_values["Code"].unique()
df_rmse_values = df_rmse_values.round(3)


# Definitions for the figures
# Original
orig_symbol = "o"
orig_color = "blue"
orig_label = "Station original value"
orig_linestyle = '-'

# Calculated
calc_symbol = "+"
calc_color = "red"
calc_label = "Station calculated value"
calc_linestyle = "--"

# IGRF
igrf_symbol = "d"
igrf_color = "green"
igrf_label = "IGRF13"
igrf_linestyle = "-."

# General
axis_label_fsize = 14
title_fontsize = 16
tick_size = 14
legend_loc = "best"
dpi_quality = 300
value_bbox_inches = "tight"
fill_color = "purple"


# Plot X component: Original repeat station, Calculated value and IGRF
# Loop to reach each station code from the list, create and save the figure
# for each station component (IT TAKES TIME!!)
for i in list_station_codes:
    station_code = i

    # Define dataframe for each station
    df2 = df[df["Code"] == station_code]
    time = df2["Time"]

    # Define parameters to insert the RMSE of each component into the figure
    df3 = df_rmse_values[df_rmse_values["Code"] == station_code]

    unique_index_x = pd.Index(list_station_codes_rmse_values)
    index_rmse_x_orig = unique_index_x.get_loc(station_code)
    orig_x_rmse = df3.loc[index_rmse_x_orig].at["RMSE_X_Original_values_IGRF"]
    index_rmse_x_calc = unique_index_x.get_loc(station_code)
    calc_x_rmse = df3.loc[
        index_rmse_x_calc].at["RMSE_X_Calculated_values_IGRF"]

    # X field info for plot
    x_sts = df2["X"]
    x_calc = df2["Calculated_X"]
    x_igrf = df2["IGRF_X_nT"]
    fig_x = station_code + "_IGRF" + "_X_Field_comparison" + ".png"
    fig1, ax1 = plt.subplots()
    ax1.plot(time, x_sts, marker=orig_symbol, color=orig_color,
             label=orig_label, linestyle=orig_linestyle)
    ax1.plot(time, x_calc, marker=calc_symbol, color=calc_color,
             label=calc_label, linestyle=calc_linestyle)
    ax1.plot(time, x_igrf, marker=igrf_symbol, color=igrf_color,
             label=igrf_label, linestyle=igrf_linestyle)
    ax1.set_xlabel("Time (dy)", fontsize=axis_label_fsize)
    ax1.set_ylabel("X Field (nT)", fontsize=axis_label_fsize)
    ax1.set_title(
        f"{station_code}, RMSE Orig={orig_x_rmse}, RMSE Calc={calc_x_rmse}",
        fontsize=title_fontsize)
    ax1.tick_params(axis="both", labelsize=tick_size)
    ax1.legend(loc=legend_loc)
    plt.savefig(output_folder / fig_x, dpi=dpi_quality,
                bbox_inches=value_bbox_inches)
    plt.close(fig1)

# Y FIELD
# Loop to reach each station code from the list, create and save the figure
# for each station component (IT TAKES TIME!!)
for i in list_station_codes:
    station_code = i

    # Define dataframe for each station
    df2 = df[df["Code"] == station_code]
    time = df2["Time"]

    # Define parameters to insert the RMSE of each component into the figure
    df3 = df_rmse_values[df_rmse_values["Code"] == station_code]

    unique_index_y = pd.Index(list_station_codes)
    index_rmse_y_orig = unique_index_y.get_loc(station_code)
    orig_y_rmse = df3.loc[index_rmse_y_orig].at["RMSE_Y_Original_values_IGRF"]
    index_rmse_y_calc = unique_index_y.get_loc(station_code)
    calc_y_rmse = df3.loc[
        index_rmse_y_calc].at["RMSE_Y_Calculated_values_IGRF"]

    # Y field info for plot
    y_sts = df2["Y"]
    y_calc = df2["Calculated_Y"]
    y_igrf = df2["IGRF_Y_nT"]
    fig_y = station_code + "_IGRF" + "_Y_Field_comparison" + ".png"
    fig2, ax2 = plt.subplots()
    ax2.plot(time, y_sts, marker=orig_symbol, color=orig_color,
             label=orig_label, linestyle=orig_linestyle)
    ax2.plot(time, y_calc, marker=calc_symbol, color=calc_color,
             label=calc_label, linestyle=calc_linestyle)
    ax2.plot(time, y_igrf, marker=igrf_symbol, color=igrf_color,
             label=igrf_label, linestyle=igrf_linestyle)
    ax2.set_xlabel("Time (dy)", fontsize=axis_label_fsize)
    ax2.set_ylabel("Y Field (nT)", fontsize=axis_label_fsize)
    ax2.set_title(
        f"{station_code}, RMSE Orig={orig_y_rmse}, RMSE Calc={calc_y_rmse}",
        fontsize=title_fontsize)
    ax2.tick_params(axis="both", labelsize=tick_size)
    ax2.legend(loc=legend_loc)
    plt.savefig(output_folder / fig_y, dpi=dpi_quality,
                bbox_inches=value_bbox_inches)
    plt.close(fig2)


# Z FIELD
# Loop to reach each station code from the list, create and save the figure
# for each station component (IT TAKES TIME!!)
for i in list_station_codes:
    station_code = i

    # Define dataframe for each station
    df2 = df[df["Code"] == station_code]
    time = df2["Time"]

    # Define parameters to insert the RMSE of each component into the figure
    df3 = df_rmse_values[df_rmse_values["Code"] == station_code]

    unique_index_z = pd.Index(list_station_codes)
    index_rmse_z_orig = unique_index_z.get_loc(station_code)
    orig_z_rmse = df3.loc[index_rmse_z_orig].at["RMSE_Z_Original_values_IGRF"]
    index_rmse_z_calc = unique_index_z.get_loc(station_code)
    calc_z_rmse = df3.loc[
        index_rmse_z_calc].at["RMSE_Z_Calculated_values_IGRF"]

    # Z field info for plot
    z_sts = df2["Z"]
    z_calc = df2["Calculated_Z"]
    z_igrf = df2["IGRF_Z_nT"]
    fig_z = station_code + "_IGRF" + "_Z_Field_comparison" + ".png"
    fig3, ax3 = plt.subplots()
    ax3.plot(time, z_sts, marker=orig_symbol, color=orig_color,
             label=orig_label, linestyle=orig_linestyle)
    ax3.plot(time, z_calc, marker=calc_symbol, color=calc_color,
             label=calc_label, linestyle=calc_linestyle)
    ax3.plot(time, z_igrf, marker=igrf_symbol, color=igrf_color,
             label=igrf_label, linestyle=igrf_linestyle)
    ax3.set_xlabel("Time (dy)", fontsize=axis_label_fsize)
    ax3.set_ylabel("Z Field (nT)", fontsize=axis_label_fsize)
    ax3.set_title(
        f"{station_code}, RMSE Orig={orig_z_rmse}, RMSE Calc={calc_z_rmse}",
        fontsize=title_fontsize)
    ax3.tick_params(axis="both", labelsize=tick_size)
    ax3.legend(loc=legend_loc)
    plt.savefig(output_folder / fig_z, dpi=dpi_quality,
                bbox_inches=value_bbox_inches)
    plt.close(fig3)
