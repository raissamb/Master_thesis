# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:35:02 2022

author: raissa baldez

Description

This program reads the Repeat station and IGRF database to do the following:
- It reads the data to separate the stations into groups of n occupations
- The groups are n12 (12 or more), n10 (10 to 11), n08 (8 yo 9), n06 (6 to 7),
n03 (3 to 5) and n01 (1 to 2)
- It creates a database file for each occupation group
- It creates a database file with only the last occupation of each station in
order to plot these stations using folium (one coordinate for each station)

ATTENTION: three stations were removed from analysis due to being magnetic
contaminated according to field reports from 2017 to 2020

"""

# Import modules
import mestrado_module as mm
import pandas as pd
from pathlib import Path


# Repeat station IGRF database info
rs_igrf_folder: Path = Path(mm.path_pipeline_04_igrf_calc)
rs_igrf_file: Path = Path(mm.output_04e_code_complete_rs_igrf_database)

# Save figure files
output_folder: Path = Path(mm.path_pipeline_05_rank_n_occupations)

groups_ocp_file: Path = Path(mm.output_05a_code_groups_ocp_df)

rs_df_file_g1: Path = Path(mm.output_05a_code_database_g1)
rs_df_file_g2: Path = Path(mm.output_05a_code_database_g2)
rs_df_file_g3: Path = Path(mm.output_05a_code_database_g3)
rs_df_file_g4: Path = Path(mm.output_05a_code_database_g4)
rs_df_file_g5: Path = Path(mm.output_05a_code_database_g5)
rs_df_file_g6: Path = Path(mm.output_05a_code_database_g6)

# Files for Folium plot
folium_file_g1: Path = Path(mm.output_05a_code_folium_file_g1)
folium_file_g2: Path = Path(mm.output_05a_code_folium_file_g2)
folium_file_g3: Path = Path(mm.output_05a_code_folium_file_g3)
folium_file_g4: Path = Path(mm.output_05a_code_folium_file_g4)
folium_file_g5: Path = Path(mm.output_05a_code_folium_file_g5)
folium_file_g6: Path = Path(mm.output_05a_code_folium_file_g6)


# read file
df = pd.read_csv(rs_igrf_folder / rs_igrf_file)

# Removal of contaminated stations acording to field reports from 2017 to 2020
"""
The following stations are going to be removed from further analysis due to
being marked as magnetic polluted
- Jatai: JAT
- Moraes de Almeida: MAL
- Santana do Livramento: SLI
"""

# Get index for the rows with stations to be deleted
index_jat = df[df.Code == "JAT"].index
index_mal = df[df.Code == "MAL"].index
index_sli = df[df.Code == "SLI"].index

# Deleting rows
df2 = df.copy()
df2.drop(index_jat, inplace=True)
df2.drop(index_mal, inplace=True)
df2.drop(index_sli, inplace=True)


# Separate the repeat stations that have n or more occupations into groups
# to create their geodataframe to save them in files for later use

# Group 01: 12 or more occupations
g1_start = 12
df_ocp_g1 = df2[df2["Number_occupations"] >= g1_start]
df_ocp_g1_folium = df_ocp_g1.drop_duplicates(subset="Code",
                                             keep="last",
                                             inplace=False)
# Save the file
df_ocp_g1.to_csv(output_folder / rs_df_file_g1, index=False)
df_ocp_g1_folium.to_csv(output_folder / folium_file_g1, index=False)


# Use a function from the mestrado module to create the groups
# Group 02: 9 to 11 occupations
g2_start = 9
g2_end = 11
mm.create_occupation_groups(df2, g2_start, g2_end, output_folder,
                            rs_df_file_g2, folium_file_g2)

# Group 03: 4 to 8 occupations
g3_start = 4
g3_end = 8
mm.create_occupation_groups(df2, g3_start, g3_end, output_folder,
                            rs_df_file_g3, folium_file_g3)

# Group 04: 1 to 3 occupations
g4_start = 1
g4_end = 3
mm.create_occupation_groups(df2, g4_start, g4_end, output_folder,
                            rs_df_file_g4, folium_file_g4)


# float_format="%.3f
