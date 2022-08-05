# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:06:28 2022

author: raissa baldez

Description

Something...

"""

# Import modules
import mestrado_module as mm
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

# Folder and file paths
rs_df_folder: Path = Path(mm.path_pipeline_05_rank_n_occupations)
rs_df_file_g1: Path = Path(mm.output_05a_code_database_g1)
rs_df_file_g2: Path = Path(mm.output_05a_code_database_g2)
rs_df_file_g3: Path = Path(mm.output_05a_code_database_g3)
rs_df_file_g4: Path = Path(mm.output_05a_code_database_g4)
rs_df_file_g5: Path = Path(mm.output_05a_code_database_g5)
rs_df_file_g6: Path = Path(mm.output_05a_code_database_g6)
# Save figure files
output_folder_g1: Path = Path(mm.path_pipeline_06a_plot_temporal_series_g1)
output_folder_g2: Path = Path(mm.path_pipeline_06b_plot_temporal_series_g2)
output_folder_g3: Path = Path(mm.path_pipeline_06c_plot_temporal_series_g3)
output_folder_g4: Path = Path(mm.path_pipeline_06d_plot_temporal_series_g4)
# Figure style
sns.set_style("darkgrid")


# read rs data
df_g1 = pd.read_csv(rs_df_folder / rs_df_file_g1)
df_g2 = pd.read_csv(rs_df_folder / rs_df_file_g2)
df_g3 = pd.read_csv(rs_df_folder / rs_df_file_g3)
df_g4 = pd.read_csv(rs_df_folder / rs_df_file_g4)

# create a variable to hold the station codes for looping to create figures
# using function from mestrado module
list_codes_g1 = mm.create_list_station_codes(df_g1)
list_codes_g2 = mm.create_list_station_codes(df_g2)
list_codes_g3 = mm.create_list_station_codes(df_g3)
list_codes_g4 = mm.create_list_station_codes(df_g4)


# Plots
# GROUP 1
mm.plot_total_field(list_codes_g1, df_g1, output_folder_g1)
mm.plot_h_field(list_codes_g1, df_g1, output_folder_g1)
mm.plot_x_field(list_codes_g1, df_g1, output_folder_g1)
mm.plot_y_field(list_codes_g1, df_g1, output_folder_g1)
mm.plot_z_field(list_codes_g1, df_g1, output_folder_g1)
mm.plot_dec_field(list_codes_g1, df_g1, output_folder_g1)
mm.plot_inc_field(list_codes_g1, df_g1, output_folder_g1)


# GROUP 2
mm.plot_total_field(list_codes_g2, df_g2, output_folder_g2)
mm.plot_h_field(list_codes_g2, df_g2, output_folder_g2)
mm.plot_x_field(list_codes_g2, df_g2, output_folder_g2)
mm.plot_y_field(list_codes_g2, df_g2, output_folder_g2)
mm.plot_z_field(list_codes_g2, df_g2, output_folder_g2)
mm.plot_dec_field(list_codes_g2, df_g2, output_folder_g2)
mm.plot_inc_field(list_codes_g2, df_g2, output_folder_g2)


# Group 3
mm.plot_total_field(list_codes_g3, df_g3, output_folder_g3)
mm.plot_h_field(list_codes_g3, df_g3, output_folder_g3)
mm.plot_x_field(list_codes_g3, df_g3, output_folder_g3)
mm.plot_y_field(list_codes_g3, df_g3, output_folder_g3)
mm.plot_z_field(list_codes_g3, df_g3, output_folder_g3)
mm.plot_dec_field(list_codes_g3, df_g3, output_folder_g3)
mm.plot_inc_field(list_codes_g3, df_g3, output_folder_g3)


# Group 4
mm.plot_total_field(list_codes_g4, df_g4, output_folder_g4)
mm.plot_h_field(list_codes_g4, df_g4, output_folder_g4)
mm.plot_x_field(list_codes_g4, df_g4, output_folder_g4)
mm.plot_y_field(list_codes_g4, df_g4, output_folder_g4)
mm.plot_z_field(list_codes_g4, df_g4, output_folder_g4)
mm.plot_dec_field(list_codes_g4, df_g4, output_folder_g4)
mm.plot_inc_field(list_codes_g4, df_g4, output_folder_g4)
