# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:51:11 2022

author: raissa baldez

Description

This program reads the file with the dataframe from the n occupation stations
group to calculate the RMSE for each component and then plot the results

"""


# Import modules
import mestrado_module as mm
import pandas as pd
from pathlib import Path


# Input
input_folder: Path = Path(mm.path_pipeline_05b_selection_process_ocp_groups)

dd_unit = "decimal degrees"
nt_unit = "nT"

# ----------------------G1-----------------
g1_input: Path = Path(mm.output_05b_code_database_g1)
g1_output_folder: Path = Path(mm.path_pipeline_05d_rmse_g1)


# Create dataframe and station list
g1_df = pd.read_csv(input_folder / g1_input)
g1_station_list = g1_df["Code"].unique()
group = "1"

# RMSE calculation: Original repeat station values and IGRF
g1_rmse_original_igrf_d = mm.calculate_rmse_by_group(
    g1_station_list, g1_df, "IGRF_D_dd", "D")
g1_rmse_original_igrf_i = mm.calculate_rmse_by_group(
    g1_station_list, g1_df, "IGRF_I_dd", "I")
g1_rmse_original_igrf_f = mm.calculate_rmse_by_group(
    g1_station_list, g1_df, "IGRF_F_nT", "F")
g1_rmse_original_igrf_h = mm.calculate_rmse_by_group(
    g1_station_list, g1_df, "IGRF_H_nT", "H")

# RMSE calculation: Original repeat station values, calculated values
# and IGRF
g1_rmse_original_igrf_x = mm.calculate_rmse_by_group(
    g1_station_list, g1_df, "IGRF_X_nT", "X")
g1_rmse_calculated_igrf_x = mm.calculate_rmse_by_group(
    g1_station_list, g1_df, "IGRF_X_nT", "Calculated_X")

g1_rmse_original_igrf_y = mm.calculate_rmse_by_group(
    g1_station_list, g1_df, "IGRF_Y_nT", "Y")
g1_rmse_calculated_igrf_y = mm.calculate_rmse_by_group(
    g1_station_list, g1_df, "IGRF_Y_nT", "Calculated_Y")

g1_rmse_original_igrf_z = mm.calculate_rmse_by_group(
    g1_station_list, g1_df, "IGRF_Z_nT", "Z")
g1_rmse_calculated_igrf_z = mm.calculate_rmse_by_group(
    g1_station_list, g1_df, "IGRF_Z_nT", "Calculated_Z")

# Create dataframe for group
g1_rmse_data = {"Code": g1_station_list,
                "RMSE_ORIGINAL_IGRF_D": g1_rmse_original_igrf_d,
                "RMSE_ORIGINAL_IGRF_I": g1_rmse_original_igrf_i,
                "RMSE_ORIGINAL_IGRF_F": g1_rmse_original_igrf_f,
                "RMSE_ORIGINAL_IGRF_H": g1_rmse_original_igrf_h,
                "RMSE_ORIGINAL_IGRF_X": g1_rmse_original_igrf_x,
                "RMSE_CALCULATED_IGRF_X": g1_rmse_calculated_igrf_x,
                "RMSE_ORIGINAL_IGRF_Y": g1_rmse_original_igrf_y,
                "RMSE_CALCULATED_IGRF_Y": g1_rmse_calculated_igrf_y,
                "RMSE_ORIGINAL_IGRF_Z": g1_rmse_original_igrf_z,
                "RMSE_CALCULATED_IGRF_Z": g1_rmse_calculated_igrf_z,
                }
g1_rmse_df = pd.DataFrame(data=g1_rmse_data)
g1_rmse_df.to_csv(g1_output_folder / "g1_rmse_database.csv",
                  index=False,
                  na_rep="NaN")

# Plot figures for G1
mm.plot_rmse_by_group_fhdi(g1_rmse_df, "RMSE_ORIGINAL_IGRF_F",
                           "F", nt_unit, group,
                           g1_output_folder, "g1_rmse_f.png")

mm.plot_rmse_by_group_fhdi(g1_rmse_df, "RMSE_ORIGINAL_IGRF_H",
                           "H", nt_unit, group,
                           g1_output_folder, "g1_rmse_h.png")

mm.plot_rmse_by_group_fhdi(g1_rmse_df, "RMSE_ORIGINAL_IGRF_D",
                           "D", dd_unit, group,
                           g1_output_folder, "g1_rmse_d.png")

mm.plot_rmse_by_group_fhdi(g1_rmse_df, "RMSE_ORIGINAL_IGRF_I",
                           "I", dd_unit, group,
                           g1_output_folder, "g1_rmse_i.png")


mm.plot_rmse_by_group_xyz(g1_rmse_df, "RMSE_ORIGINAL_IGRF_X",
                          "RMSE_CALCULATED_IGRF_X", "X",
                          nt_unit, group,
                          g1_output_folder, "g1_rmse_x.png")

mm.plot_rmse_by_group_xyz(g1_rmse_df, "RMSE_ORIGINAL_IGRF_Y",
                          "RMSE_CALCULATED_IGRF_Y", "Y",
                          nt_unit, group,
                          g1_output_folder, "g1_rmse_y.png")

mm.plot_rmse_by_group_xyz(g1_rmse_df, "RMSE_ORIGINAL_IGRF_Z",
                          "RMSE_CALCULATED_IGRF_Z", "Z",
                          nt_unit, group,
                          g1_output_folder, "g1_rmse_z.png")


# ----------------------G2-----------------
g2_input: Path = Path(mm.output_05b_code_database_g2)
g2_output_folder: Path = Path(mm.path_pipeline_05d_rmse_g2)


# Create dataframe and station list
g2_df = pd.read_csv(input_folder / g2_input)
g2_station_list = g2_df["Code"].unique()
group = "2"

# RMSE calculation: Original repeat station values and IGRF
g2_rmse_original_igrf_d = mm.calculate_rmse_by_group(
    g2_station_list, g2_df, "IGRF_D_dd", "D")
g2_rmse_original_igrf_i = mm.calculate_rmse_by_group(
    g2_station_list, g2_df, "IGRF_I_dd", "I")
g2_rmse_original_igrf_f = mm.calculate_rmse_by_group(
    g2_station_list, g2_df, "IGRF_F_nT", "F")
g2_rmse_original_igrf_h = mm.calculate_rmse_by_group(
    g2_station_list, g2_df, "IGRF_H_nT", "H")

# RMSE calculation: Original repeat station values, calculated values
# and IGRF
g2_rmse_original_igrf_x = mm.calculate_rmse_by_group(
    g2_station_list, g2_df, "IGRF_X_nT", "X")
g2_rmse_calculated_igrf_x = mm.calculate_rmse_by_group(
    g2_station_list, g2_df, "IGRF_X_nT", "Calculated_X")

g2_rmse_original_igrf_y = mm.calculate_rmse_by_group(
    g2_station_list, g2_df, "IGRF_Y_nT", "Y")
g2_rmse_calculated_igrf_y = mm.calculate_rmse_by_group(
    g2_station_list, g2_df, "IGRF_Y_nT", "Calculated_Y")

g2_rmse_original_igrf_z = mm.calculate_rmse_by_group(
    g2_station_list, g2_df, "IGRF_Z_nT", "Z")
g2_rmse_calculated_igrf_z = mm.calculate_rmse_by_group(
    g2_station_list, g2_df, "IGRF_Z_nT", "Calculated_Z")

# Create dataframe for group
g2_rmse_data = {"Code": g2_station_list,
                "RMSE_ORIGINAL_IGRF_D": g2_rmse_original_igrf_d,
                "RMSE_ORIGINAL_IGRF_I": g2_rmse_original_igrf_i,
                "RMSE_ORIGINAL_IGRF_F": g2_rmse_original_igrf_f,
                "RMSE_ORIGINAL_IGRF_H": g2_rmse_original_igrf_h,
                "RMSE_ORIGINAL_IGRF_X": g2_rmse_original_igrf_x,
                "RMSE_CALCULATED_IGRF_X": g2_rmse_calculated_igrf_x,
                "RMSE_ORIGINAL_IGRF_Y": g2_rmse_original_igrf_y,
                "RMSE_CALCULATED_IGRF_Y": g2_rmse_calculated_igrf_y,
                "RMSE_ORIGINAL_IGRF_Z": g2_rmse_original_igrf_z,
                "RMSE_CALCULATED_IGRF_Z": g2_rmse_calculated_igrf_z,
                }
g2_rmse_df = pd.DataFrame(data=g2_rmse_data)
g2_rmse_df.to_csv(g2_output_folder / "g2_rmse_database.csv",
                  index=False,
                  na_rep="NaN")

# Plot figures for g2
mm.plot_rmse_by_group_fhdi(g2_rmse_df, "RMSE_ORIGINAL_IGRF_F",
                           "F", nt_unit, group,
                           g2_output_folder, "g2_rmse_f.png")

mm.plot_rmse_by_group_fhdi(g2_rmse_df, "RMSE_ORIGINAL_IGRF_H",
                           "H", nt_unit, group,
                           g2_output_folder, "g2_rmse_h.png")

mm.plot_rmse_by_group_fhdi(g2_rmse_df, "RMSE_ORIGINAL_IGRF_D",
                           "D", dd_unit, group,
                           g2_output_folder, "g2_rmse_d.png")

mm.plot_rmse_by_group_fhdi(g2_rmse_df, "RMSE_ORIGINAL_IGRF_I",
                           "I", dd_unit, group,
                           g2_output_folder, "g2_rmse_i.png")


mm.plot_rmse_by_group_xyz(g2_rmse_df, "RMSE_ORIGINAL_IGRF_X",
                          "RMSE_CALCULATED_IGRF_X", "X",
                          nt_unit, group,
                          g2_output_folder, "g2_rmse_x.png")

mm.plot_rmse_by_group_xyz(g2_rmse_df, "RMSE_ORIGINAL_IGRF_Y",
                          "RMSE_CALCULATED_IGRF_Y", "Y",
                          nt_unit, group,
                          g2_output_folder, "g2_rmse_y.png")

mm.plot_rmse_by_group_xyz(g2_rmse_df, "RMSE_ORIGINAL_IGRF_Z",
                          "RMSE_CALCULATED_IGRF_Z", "Z",
                          nt_unit, group,
                          g2_output_folder, "g2_rmse_z.png")


# ----------------------g3-----------------
g3_input: Path = Path(mm.output_05b_code_database_g3)
g3_output_folder: Path = Path(mm.path_pipeline_05d_rmse_g3)


# Create dataframe and station list
g3_df = pd.read_csv(input_folder / g3_input)
g3_station_list = g3_df["Code"].unique()
group = "3"

# RMSE calculation: Original repeat station values and IGRF
g3_rmse_original_igrf_d = mm.calculate_rmse_by_group(
    g3_station_list, g3_df, "IGRF_D_dd", "D")
g3_rmse_original_igrf_i = mm.calculate_rmse_by_group(
    g3_station_list, g3_df, "IGRF_I_dd", "I")
g3_rmse_original_igrf_f = mm.calculate_rmse_by_group(
    g3_station_list, g3_df, "IGRF_F_nT", "F")
g3_rmse_original_igrf_h = mm.calculate_rmse_by_group(
    g3_station_list, g3_df, "IGRF_H_nT", "H")

# RMSE calculation: Original repeat station values, calculated values
# and IGRF
g3_rmse_original_igrf_x = mm.calculate_rmse_by_group(
    g3_station_list, g3_df, "IGRF_X_nT", "X")
g3_rmse_calculated_igrf_x = mm.calculate_rmse_by_group(
    g3_station_list, g3_df, "IGRF_X_nT", "Calculated_X")

g3_rmse_original_igrf_y = mm.calculate_rmse_by_group(
    g3_station_list, g3_df, "IGRF_Y_nT", "Y")
g3_rmse_calculated_igrf_y = mm.calculate_rmse_by_group(
    g3_station_list, g3_df, "IGRF_Y_nT", "Calculated_Y")

g3_rmse_original_igrf_z = mm.calculate_rmse_by_group(
    g3_station_list, g3_df, "IGRF_Z_nT", "Z")
g3_rmse_calculated_igrf_z = mm.calculate_rmse_by_group(
    g3_station_list, g3_df, "IGRF_Z_nT", "Calculated_Z")

# Create dataframe for group
g3_rmse_data = {"Code": g3_station_list,
                "RMSE_ORIGINAL_IGRF_D": g3_rmse_original_igrf_d,
                "RMSE_ORIGINAL_IGRF_I": g3_rmse_original_igrf_i,
                "RMSE_ORIGINAL_IGRF_F": g3_rmse_original_igrf_f,
                "RMSE_ORIGINAL_IGRF_H": g3_rmse_original_igrf_h,
                "RMSE_ORIGINAL_IGRF_X": g3_rmse_original_igrf_x,
                "RMSE_CALCULATED_IGRF_X": g3_rmse_calculated_igrf_x,
                "RMSE_ORIGINAL_IGRF_Y": g3_rmse_original_igrf_y,
                "RMSE_CALCULATED_IGRF_Y": g3_rmse_calculated_igrf_y,
                "RMSE_ORIGINAL_IGRF_Z": g3_rmse_original_igrf_z,
                "RMSE_CALCULATED_IGRF_Z": g3_rmse_calculated_igrf_z,
                }
g3_rmse_df = pd.DataFrame(data=g3_rmse_data)
g3_rmse_df.to_csv(g3_output_folder / "g3_rmse_database.csv",
                  index=False,
                  na_rep="NaN")

# Plot figures for g3
mm.plot_rmse_by_group_fhdi(g3_rmse_df, "RMSE_ORIGINAL_IGRF_F",
                           "F", nt_unit, group,
                           g3_output_folder, "g3_rmse_f.png")

mm.plot_rmse_by_group_fhdi(g3_rmse_df, "RMSE_ORIGINAL_IGRF_H",
                           "H", nt_unit, group,
                           g3_output_folder, "g3_rmse_h.png")

mm.plot_rmse_by_group_fhdi(g3_rmse_df, "RMSE_ORIGINAL_IGRF_D",
                           "D", dd_unit, group,
                           g3_output_folder, "g3_rmse_d.png")

mm.plot_rmse_by_group_fhdi(g3_rmse_df, "RMSE_ORIGINAL_IGRF_I",
                           "I", dd_unit, group,
                           g3_output_folder, "g3_rmse_i.png")


mm.plot_rmse_by_group_xyz(g3_rmse_df, "RMSE_ORIGINAL_IGRF_X",
                          "RMSE_CALCULATED_IGRF_X", "X",
                          nt_unit, group,
                          g3_output_folder, "g3_rmse_x.png")

mm.plot_rmse_by_group_xyz(g3_rmse_df, "RMSE_ORIGINAL_IGRF_Y",
                          "RMSE_CALCULATED_IGRF_Y", "Y",
                          nt_unit, group,
                          g3_output_folder, "g3_rmse_y.png")

mm.plot_rmse_by_group_xyz(g3_rmse_df, "RMSE_ORIGINAL_IGRF_Z",
                          "RMSE_CALCULATED_IGRF_Z", "Z",
                          nt_unit, group,
                          g3_output_folder, "g3_rmse_z.png")


# ----------------------g4-----------------
g4_input: Path = Path(mm.output_05b_code_database_g4)
g4_output_folder: Path = Path(mm.path_pipeline_05d_rmse_g4)


# Create dataframe and station list
g4_df = pd.read_csv(input_folder / g4_input)
g4_station_list = g4_df["Code"].unique()
group = "4"

# RMSE calculation: Original repeat station values and IGRF
g4_rmse_original_igrf_d = mm.calculate_rmse_by_group(
    g4_station_list, g4_df, "IGRF_D_dd", "D")
g4_rmse_original_igrf_i = mm.calculate_rmse_by_group(
    g4_station_list, g4_df, "IGRF_I_dd", "I")
g4_rmse_original_igrf_f = mm.calculate_rmse_by_group(
    g4_station_list, g4_df, "IGRF_F_nT", "F")
g4_rmse_original_igrf_h = mm.calculate_rmse_by_group(
    g4_station_list, g4_df, "IGRF_H_nT", "H")

# RMSE calculation: Original repeat station values, calculated values
# and IGRF
g4_rmse_original_igrf_x = mm.calculate_rmse_by_group(
    g4_station_list, g4_df, "IGRF_X_nT", "X")
g4_rmse_calculated_igrf_x = mm.calculate_rmse_by_group(
    g4_station_list, g4_df, "IGRF_X_nT", "Calculated_X")

g4_rmse_original_igrf_y = mm.calculate_rmse_by_group(
    g4_station_list, g4_df, "IGRF_Y_nT", "Y")
g4_rmse_calculated_igrf_y = mm.calculate_rmse_by_group(
    g4_station_list, g4_df, "IGRF_Y_nT", "Calculated_Y")

g4_rmse_original_igrf_z = mm.calculate_rmse_by_group(
    g4_station_list, g4_df, "IGRF_Z_nT", "Z")
g4_rmse_calculated_igrf_z = mm.calculate_rmse_by_group(
    g4_station_list, g4_df, "IGRF_Z_nT", "Calculated_Z")

# Create dataframe for group
g4_rmse_data = {"Code": g4_station_list,
                "RMSE_ORIGINAL_IGRF_D": g4_rmse_original_igrf_d,
                "RMSE_ORIGINAL_IGRF_I": g4_rmse_original_igrf_i,
                "RMSE_ORIGINAL_IGRF_F": g4_rmse_original_igrf_f,
                "RMSE_ORIGINAL_IGRF_H": g4_rmse_original_igrf_h,
                "RMSE_ORIGINAL_IGRF_X": g4_rmse_original_igrf_x,
                "RMSE_CALCULATED_IGRF_X": g4_rmse_calculated_igrf_x,
                "RMSE_ORIGINAL_IGRF_Y": g4_rmse_original_igrf_y,
                "RMSE_CALCULATED_IGRF_Y": g4_rmse_calculated_igrf_y,
                "RMSE_ORIGINAL_IGRF_Z": g4_rmse_original_igrf_z,
                "RMSE_CALCULATED_IGRF_Z": g4_rmse_calculated_igrf_z,
                }
g4_rmse_df = pd.DataFrame(data=g4_rmse_data)
g4_rmse_df.to_csv(g4_output_folder / "g4_rmse_database.csv",
                  index=False,
                  na_rep="NaN")

# Plot figures for g4
mm.plot_rmse_by_group_fhdi(g4_rmse_df, "RMSE_ORIGINAL_IGRF_F",
                           "F", nt_unit, group,
                           g4_output_folder, "g4_rmse_f.png")

mm.plot_rmse_by_group_fhdi(g4_rmse_df, "RMSE_ORIGINAL_IGRF_H",
                           "H", nt_unit, group,
                           g4_output_folder, "g4_rmse_h.png")

mm.plot_rmse_by_group_fhdi(g4_rmse_df, "RMSE_ORIGINAL_IGRF_D",
                           "D", dd_unit, group,
                           g4_output_folder, "g4_rmse_d.png")

mm.plot_rmse_by_group_fhdi(g4_rmse_df, "RMSE_ORIGINAL_IGRF_I",
                           "I", dd_unit, group,
                           g4_output_folder, "g4_rmse_i.png")


mm.plot_rmse_by_group_xyz(g4_rmse_df, "RMSE_ORIGINAL_IGRF_X",
                          "RMSE_CALCULATED_IGRF_X", "X",
                          nt_unit, group,
                          g4_output_folder, "g4_rmse_x.png")

mm.plot_rmse_by_group_xyz(g4_rmse_df, "RMSE_ORIGINAL_IGRF_Y",
                          "RMSE_CALCULATED_IGRF_Y", "Y",
                          nt_unit, group,
                          g4_output_folder, "g4_rmse_y.png")

mm.plot_rmse_by_group_xyz(g4_rmse_df, "RMSE_ORIGINAL_IGRF_Z",
                          "RMSE_CALCULATED_IGRF_Z", "Z",
                          nt_unit, group,
                          g4_output_folder, "g4_rmse_z.png")


# ----------------------g5-----------------
g5_input: Path = Path(mm.output_05b_code_database_g5)
g5_output_folder: Path = Path(mm.path_pipeline_05d_rmse_g5)


# Create dataframe and station list
g5_df = pd.read_csv(input_folder / g5_input)
g5_station_list = g5_df["Code"].unique()
group = "5"

# RMSE calculation: Original repeat station values and IGRF
g5_rmse_original_igrf_d = mm.calculate_rmse_by_group(
    g5_station_list, g5_df, "IGRF_D_dd", "D")
g5_rmse_original_igrf_i = mm.calculate_rmse_by_group(
    g5_station_list, g5_df, "IGRF_I_dd", "I")
g5_rmse_original_igrf_f = mm.calculate_rmse_by_group(
    g5_station_list, g5_df, "IGRF_F_nT", "F")
g5_rmse_original_igrf_h = mm.calculate_rmse_by_group(
    g5_station_list, g5_df, "IGRF_H_nT", "H")

# RMSE calculation: Original repeat station values, calculated values
# and IGRF
g5_rmse_original_igrf_x = mm.calculate_rmse_by_group(
    g5_station_list, g5_df, "IGRF_X_nT", "X")
g5_rmse_calculated_igrf_x = mm.calculate_rmse_by_group(
    g5_station_list, g5_df, "IGRF_X_nT", "Calculated_X")

g5_rmse_original_igrf_y = mm.calculate_rmse_by_group(
    g5_station_list, g5_df, "IGRF_Y_nT", "Y")
g5_rmse_calculated_igrf_y = mm.calculate_rmse_by_group(
    g5_station_list, g5_df, "IGRF_Y_nT", "Calculated_Y")

g5_rmse_original_igrf_z = mm.calculate_rmse_by_group(
    g5_station_list, g5_df, "IGRF_Z_nT", "Z")
g5_rmse_calculated_igrf_z = mm.calculate_rmse_by_group(
    g5_station_list, g5_df, "IGRF_Z_nT", "Calculated_Z")

# Create dataframe for group
g5_rmse_data = {"Code": g5_station_list,
                "RMSE_ORIGINAL_IGRF_D": g5_rmse_original_igrf_d,
                "RMSE_ORIGINAL_IGRF_I": g5_rmse_original_igrf_i,
                "RMSE_ORIGINAL_IGRF_F": g5_rmse_original_igrf_f,
                "RMSE_ORIGINAL_IGRF_H": g5_rmse_original_igrf_h,
                "RMSE_ORIGINAL_IGRF_X": g5_rmse_original_igrf_x,
                "RMSE_CALCULATED_IGRF_X": g5_rmse_calculated_igrf_x,
                "RMSE_ORIGINAL_IGRF_Y": g5_rmse_original_igrf_y,
                "RMSE_CALCULATED_IGRF_Y": g5_rmse_calculated_igrf_y,
                "RMSE_ORIGINAL_IGRF_Z": g5_rmse_original_igrf_z,
                "RMSE_CALCULATED_IGRF_Z": g5_rmse_calculated_igrf_z,
                }
g5_rmse_df = pd.DataFrame(data=g5_rmse_data)
g5_rmse_df.to_csv(g5_output_folder / "g5_rmse_database.csv",
                  index=False,
                  na_rep="NaN")

# Plot figures for g5
mm.plot_rmse_by_group_fhdi(g5_rmse_df, "RMSE_ORIGINAL_IGRF_F",
                           "F", nt_unit, group,
                           g5_output_folder, "g5_rmse_f.png")

mm.plot_rmse_by_group_fhdi(g5_rmse_df, "RMSE_ORIGINAL_IGRF_H",
                           "H", nt_unit, group,
                           g5_output_folder, "g5_rmse_h.png")

mm.plot_rmse_by_group_fhdi(g5_rmse_df, "RMSE_ORIGINAL_IGRF_D",
                           "D", dd_unit, group,
                           g5_output_folder, "g5_rmse_d.png")

mm.plot_rmse_by_group_fhdi(g5_rmse_df, "RMSE_ORIGINAL_IGRF_I",
                           "I", dd_unit, group,
                           g5_output_folder, "g5_rmse_i.png")


mm.plot_rmse_by_group_xyz(g5_rmse_df, "RMSE_ORIGINAL_IGRF_X",
                          "RMSE_CALCULATED_IGRF_X", "X",
                          nt_unit, group,
                          g5_output_folder, "g5_rmse_x.png")

mm.plot_rmse_by_group_xyz(g5_rmse_df, "RMSE_ORIGINAL_IGRF_Y",
                          "RMSE_CALCULATED_IGRF_Y", "Y",
                          nt_unit, group,
                          g5_output_folder, "g5_rmse_y.png")

mm.plot_rmse_by_group_xyz(g5_rmse_df, "RMSE_ORIGINAL_IGRF_Z",
                          "RMSE_CALCULATED_IGRF_Z", "Z",
                          nt_unit, group,
                          g5_output_folder, "g5_rmse_z.png")


# ----------------------g6-----------------
g6_input: Path = Path(mm.output_05b_code_database_g6)
g6_output_folder: Path = Path(mm.path_pipeline_05d_rmse_g6)


# Create dataframe and station list
g6_df = pd.read_csv(input_folder / g6_input)
g6_station_list = g6_df["Code"].unique()
group = "6"

# RMSE calculation: Original repeat station values and IGRF
g6_rmse_original_igrf_d = mm.calculate_rmse_by_group(
    g6_station_list, g6_df, "IGRF_D_dd", "D")
g6_rmse_original_igrf_i = mm.calculate_rmse_by_group(
    g6_station_list, g6_df, "IGRF_I_dd", "I")
g6_rmse_original_igrf_f = mm.calculate_rmse_by_group(
    g6_station_list, g6_df, "IGRF_F_nT", "F")
g6_rmse_original_igrf_h = mm.calculate_rmse_by_group(
    g6_station_list, g6_df, "IGRF_H_nT", "H")

# RMSE calculation: Original repeat station values, calculated values
# and IGRF
g6_rmse_original_igrf_x = mm.calculate_rmse_by_group(
    g6_station_list, g6_df, "IGRF_X_nT", "X")
g6_rmse_calculated_igrf_x = mm.calculate_rmse_by_group(
    g6_station_list, g6_df, "IGRF_X_nT", "Calculated_X")

g6_rmse_original_igrf_y = mm.calculate_rmse_by_group(
    g6_station_list, g6_df, "IGRF_Y_nT", "Y")
g6_rmse_calculated_igrf_y = mm.calculate_rmse_by_group(
    g6_station_list, g6_df, "IGRF_Y_nT", "Calculated_Y")

g6_rmse_original_igrf_z = mm.calculate_rmse_by_group(
    g6_station_list, g6_df, "IGRF_Z_nT", "Z")
g6_rmse_calculated_igrf_z = mm.calculate_rmse_by_group(
    g6_station_list, g6_df, "IGRF_Z_nT", "Calculated_Z")

# Create dataframe for group
g6_rmse_data = {"Code": g6_station_list,
                "RMSE_ORIGINAL_IGRF_D": g6_rmse_original_igrf_d,
                "RMSE_ORIGINAL_IGRF_I": g6_rmse_original_igrf_i,
                "RMSE_ORIGINAL_IGRF_F": g6_rmse_original_igrf_f,
                "RMSE_ORIGINAL_IGRF_H": g6_rmse_original_igrf_h,
                "RMSE_ORIGINAL_IGRF_X": g6_rmse_original_igrf_x,
                "RMSE_CALCULATED_IGRF_X": g6_rmse_calculated_igrf_x,
                "RMSE_ORIGINAL_IGRF_Y": g6_rmse_original_igrf_y,
                "RMSE_CALCULATED_IGRF_Y": g6_rmse_calculated_igrf_y,
                "RMSE_ORIGINAL_IGRF_Z": g6_rmse_original_igrf_z,
                "RMSE_CALCULATED_IGRF_Z": g6_rmse_calculated_igrf_z,
                }
g6_rmse_df = pd.DataFrame(data=g6_rmse_data)
g6_rmse_df.to_csv(g6_output_folder / "g6_rmse_database.csv",
                  index=False,
                  na_rep="NaN")

# Plot figures for g6
mm.plot_rmse_by_group_fhdi(g6_rmse_df, "RMSE_ORIGINAL_IGRF_F",
                           "F", nt_unit, group,
                           g6_output_folder, "g6_rmse_f.png")

mm.plot_rmse_by_group_fhdi(g6_rmse_df, "RMSE_ORIGINAL_IGRF_H",
                           "H", nt_unit, group,
                           g6_output_folder, "g6_rmse_h.png")

mm.plot_rmse_by_group_fhdi(g6_rmse_df, "RMSE_ORIGINAL_IGRF_D",
                           "D", dd_unit, group,
                           g6_output_folder, "g6_rmse_d.png")

mm.plot_rmse_by_group_fhdi(g6_rmse_df, "RMSE_ORIGINAL_IGRF_I",
                           "I", dd_unit, group,
                           g6_output_folder, "g6_rmse_i.png")


mm.plot_rmse_by_group_xyz(g6_rmse_df, "RMSE_ORIGINAL_IGRF_X",
                          "RMSE_CALCULATED_IGRF_X", "X",
                          nt_unit, group,
                          g6_output_folder, "g6_rmse_x.png")

mm.plot_rmse_by_group_xyz(g6_rmse_df, "RMSE_ORIGINAL_IGRF_Y",
                          "RMSE_CALCULATED_IGRF_Y", "Y",
                          nt_unit, group,
                          g6_output_folder, "g6_rmse_y.png")

mm.plot_rmse_by_group_xyz(g6_rmse_df, "RMSE_ORIGINAL_IGRF_Z",
                          "RMSE_CALCULATED_IGRF_Z", "Z",
                          nt_unit, group,
                          g6_output_folder, "g6_rmse_z.png")


# ----------------------g7-----------------
g7_input: Path = Path(mm.output_05b_code_database_g7)
g7_output_folder: Path = Path(mm.path_pipeline_05d_rmse_g7)


# Create dataframe and station list
g7_df = pd.read_csv(input_folder / g7_input)
g7_station_list = g7_df["Code"].unique()
group = "7"

# RMSE calculation: Original repeat station values and IGRF
g7_rmse_original_igrf_d = mm.calculate_rmse_by_group(
    g7_station_list, g7_df, "IGRF_D_dd", "D")
g7_rmse_original_igrf_i = mm.calculate_rmse_by_group(
    g7_station_list, g7_df, "IGRF_I_dd", "I")
g7_rmse_original_igrf_f = mm.calculate_rmse_by_group(
    g7_station_list, g7_df, "IGRF_F_nT", "F")
g7_rmse_original_igrf_h = mm.calculate_rmse_by_group(
    g7_station_list, g7_df, "IGRF_H_nT", "H")

# RMSE calculation: Original repeat station values, calculated values
# and IGRF
g7_rmse_original_igrf_x = mm.calculate_rmse_by_group(
    g7_station_list, g7_df, "IGRF_X_nT", "X")
g7_rmse_calculated_igrf_x = mm.calculate_rmse_by_group(
    g7_station_list, g7_df, "IGRF_X_nT", "Calculated_X")

g7_rmse_original_igrf_y = mm.calculate_rmse_by_group(
    g7_station_list, g7_df, "IGRF_Y_nT", "Y")
g7_rmse_calculated_igrf_y = mm.calculate_rmse_by_group(
    g7_station_list, g7_df, "IGRF_Y_nT", "Calculated_Y")

g7_rmse_original_igrf_z = mm.calculate_rmse_by_group(
    g7_station_list, g7_df, "IGRF_Z_nT", "Z")
g7_rmse_calculated_igrf_z = mm.calculate_rmse_by_group(
    g7_station_list, g7_df, "IGRF_Z_nT", "Calculated_Z")

# Create dataframe for group
g7_rmse_data = {"Code": g7_station_list,
                "RMSE_ORIGINAL_IGRF_D": g7_rmse_original_igrf_d,
                "RMSE_ORIGINAL_IGRF_I": g7_rmse_original_igrf_i,
                "RMSE_ORIGINAL_IGRF_F": g7_rmse_original_igrf_f,
                "RMSE_ORIGINAL_IGRF_H": g7_rmse_original_igrf_h,
                "RMSE_ORIGINAL_IGRF_X": g7_rmse_original_igrf_x,
                "RMSE_CALCULATED_IGRF_X": g7_rmse_calculated_igrf_x,
                "RMSE_ORIGINAL_IGRF_Y": g7_rmse_original_igrf_y,
                "RMSE_CALCULATED_IGRF_Y": g7_rmse_calculated_igrf_y,
                "RMSE_ORIGINAL_IGRF_Z": g7_rmse_original_igrf_z,
                "RMSE_CALCULATED_IGRF_Z": g7_rmse_calculated_igrf_z,
                }
g7_rmse_df = pd.DataFrame(data=g7_rmse_data)
g7_rmse_df.to_csv(g7_output_folder / "g7_rmse_database.csv",
                  index=False,
                  na_rep="NaN")

# Plot figures for g7
mm.plot_rmse_by_group_fhdi(g7_rmse_df, "RMSE_ORIGINAL_IGRF_F",
                           "F", nt_unit, group,
                           g7_output_folder, "g7_rmse_f.png")

mm.plot_rmse_by_group_fhdi(g7_rmse_df, "RMSE_ORIGINAL_IGRF_H",
                           "H", nt_unit, group,
                           g7_output_folder, "g7_rmse_h.png")

mm.plot_rmse_by_group_fhdi(g7_rmse_df, "RMSE_ORIGINAL_IGRF_D",
                           "D", dd_unit, group,
                           g7_output_folder, "g7_rmse_d.png")

mm.plot_rmse_by_group_fhdi(g7_rmse_df, "RMSE_ORIGINAL_IGRF_I",
                           "I", dd_unit, group,
                           g7_output_folder, "g7_rmse_i.png")


mm.plot_rmse_by_group_xyz(g7_rmse_df, "RMSE_ORIGINAL_IGRF_X",
                          "RMSE_CALCULATED_IGRF_X", "X",
                          nt_unit, group,
                          g7_output_folder, "g7_rmse_x.png")

mm.plot_rmse_by_group_xyz(g7_rmse_df, "RMSE_ORIGINAL_IGRF_Y",
                          "RMSE_CALCULATED_IGRF_Y", "Y",
                          nt_unit, group,
                          g7_output_folder, "g7_rmse_y.png")

mm.plot_rmse_by_group_xyz(g7_rmse_df, "RMSE_ORIGINAL_IGRF_Z",
                          "RMSE_CALCULATED_IGRF_Z", "Z",
                          nt_unit, group,
                          g7_output_folder, "g7_rmse_z.png")