# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:18:01 2022 (New analysis not finished)

author: raissa baldez

Description

This program reads the folium files (one record of each station, divided by
groups of occupations) in order to do the following:
- To plot each occupation group over a folium map
- The stations are then analyzed to choose which ones will be part of the 50
stations for the new network
- The underisable ones are removed from the analysis
- A folium file with the chosen 50 stations is created

The priority order for the chosen is
1. Especial (read <ATTENTION> below): Time of last occupation
2. Geographical coverage (using the coverage_radius parameter)
3. Number of occupations
4. Values of RMSE

ATTENTION:
New factor for the selection process: Time of last occupation of each station
(Not originally on master thesis). Since there is no status record for many
stations, the last time they were occupied became a relevant factor as the
chances the station is still in operational is greater than the ones occupied
a long time ago.

These changes presume that this work will be refined to be published in the
future.
"""


# Import modules
import mestrado_module as mm
from pathlib import Path
import pandas as pd
import geopandas as gpd
import folium
from folium import plugins
from shapely.geometry import Point, Polygon


# Original repeat station database
rs_database_folder: Path = Path(mm.path_pipeline_04_igrf_calc)
rs_database_file: Path = Path(mm.output_04d_code_rs_igrf_database)

# Input
input_folder: Path = Path(mm.path_pipeline_05b_selection_process_ocp_groups)
folium_file_g1: Path = Path(mm.output_05b_code_folium_file_g1)
folium_file_g2: Path = Path(mm.output_05b_code_folium_file_g2)
folium_file_g3: Path = Path(mm.output_05b_code_folium_file_g3)
folium_file_g4: Path = Path(mm.output_05b_code_folium_file_g4)
folium_file_g5: Path = Path(mm.output_05b_code_folium_file_g5)
folium_file_g6: Path = Path(mm.output_05b_code_folium_file_g6)
folium_file_g7: Path = Path(mm.output_05b_code_folium_file_g7)

# Save figures and files
output_folder: Path = Path(mm.path_pipeline_05e_selection)

# Output: list with the 50 selected repeat stations
selected_rs_database: Path = Path(mm.output_05e_code_selected_rs_database)

# Folium maps
mapa0 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/select_repeat_stations/"\
    "05e_repeat_stations_selection_process_map.html"

# read folium files
df_g1 = pd.read_csv(input_folder / folium_file_g1)
df_g2 = pd.read_csv(input_folder / folium_file_g2)
df_g3 = pd.read_csv(input_folder / folium_file_g3)
df_g4 = pd.read_csv(input_folder / folium_file_g4)
df_g5 = pd.read_csv(input_folder / folium_file_g5)
df_g6 = pd.read_csv(input_folder / folium_file_g6)
df_g7 = pd.read_csv(input_folder / folium_file_g7)


# START SELECTION PROCESS
# Criteria 1 (new): last time of occupation (YEAR 2000)
g1_filtered = mm.select_station_last_occupation_year_2000(df_g1)
g2_filtered = mm.select_station_last_occupation_year_2000(df_g2)
g3_filtered = mm.select_station_last_occupation_year_2000(df_g3)
g4_filtered = mm.select_station_last_occupation_year_2000(df_g4)
g5_filtered = mm.select_station_last_occupation_year_2000(df_g5)
g6_filtered = mm.select_station_last_occupation_year_2000(df_g6)
g7_filtered = mm.select_station_last_occupation_year_2000(df_g7)


# Criteria 2: geographical distribution using folium map for analysis

# Step 1: create geodataframes for the stations and magnetic observatories
# chosen_df_g1 = df_g1
chosen_df_g1 = g1_filtered  # df_g1 to ignore new criteria
gdf_g1 = gpd.GeoDataFrame(
    chosen_df_g1, geometry=gpd.points_from_xy(
        chosen_df_g1["Longitude"], chosen_df_g1["Latitude"]
    )
)

chosen_df_g2 = g2_filtered  # df_g2 to ignore new criteria
gdf_g2 = gpd.GeoDataFrame(
    chosen_df_g2, geometry=gpd.points_from_xy(
        chosen_df_g2["Longitude"], chosen_df_g2["Latitude"]
    )
)

# chosen_df_g3 = df_g3
chosen_df_g3 = g3_filtered  # df_g3 to ignore new criteria
gdf_g3 = gpd.GeoDataFrame(
    chosen_df_g3, geometry=gpd.points_from_xy(
        chosen_df_g3["Longitude"], chosen_df_g3["Latitude"]
    )
)

# chosen_df_g4 = df_g4
chosen_df_g4 = g4_filtered  # df_g4 to ignore new criteria
gdf_g4 = gpd.GeoDataFrame(
    chosen_df_g4, geometry=gpd.points_from_xy(
        chosen_df_g4["Longitude"], chosen_df_g4["Latitude"]
    )
)

# chosen_df_g5 = df_g5
chosen_df_g5 = g5_filtered  # df_g5 to ignore new criteria
gdf_g5 = gpd.GeoDataFrame(
    chosen_df_g5, geometry=gpd.points_from_xy(
        chosen_df_g5["Longitude"], chosen_df_g5["Latitude"]
    )
)

# chosen_df_g6 = df_g6
chosen_df_g6 = g6_filtered  # df_g6 to ignore new criteria
gdf_g6 = gpd.GeoDataFrame(
    chosen_df_g6, geometry=gpd.points_from_xy(
        chosen_df_g6["Longitude"], chosen_df_g6["Latitude"]
    )
)

# chosen_df_g7 = df_g7
chosen_df_g7 = g7_filtered  # df_g7 to ignore new criteria
gdf_g7 = gpd.GeoDataFrame(
    chosen_df_g7, geometry=gpd.points_from_xy(
        chosen_df_g7["Longitude"], chosen_df_g7["Latitude"]
    )
)


# Step 2: Create an Folium map to select the stations

# DEFINITIONS (distances in km)
# observatory_coverage_radius = 904000 # BASED ON ITALY CASTELLO TESINO
# embracer_coverage_radius = 150000 # germany
# embracer_coverage_radius = 230000 # italy GIB station

# Radius suggested by Katia and Cristiano (800 km, 500 km, 300 km, 500 km)
observatory_coverage_radius_m = 800000
repeat_station_coverage_radius_m = 300000


# =====================INTERACTIVE STATION REMOVAL BLOCK=======================
"""
# ITERATIVE PART OF SELECTION PROCESS!!!
The following block of code removes specific stations from the occupation
groups to create a better geographical distribution of the repeat stations
over the country each time the code is executed.
In terms of criteria importance, stations that have been recently occupied are
more important than the others since their status is known. The second most
important criteria is the geographical distribution.
Then comes temporal series size and RMSE values at last.

"""

# Group 1
new_gdf_g1 = gdf_g1.copy()
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "PNB"].index, inplace=True)
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "FRO"].index, inplace=True)
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "GOI"].index, inplace=True)
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "TLS"].index, inplace=True)
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "MRL"].index, inplace=True)
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "CTA"].index, inplace=True)

# ITU PRIORITY OVER CTO DUE TO LAST OCP AND GEO DISTRIB.
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "CTO"].index, inplace=True)
# ITU AND IPA PRIORITY OVER CTD DUE TO GEO DISTRIB.
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "CTD"].index, inplace=True)
# LAG PRIORITY OVER PAL DUE TO LAST OCP AND GEO DISTRIB.
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "PAL"].index, inplace=True)
# JPA PRIORITY OVER REC DUE TO LAST OCP
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "REC"].index, inplace=True)
# LAST TO GO DUE TO GEO DISTRIB
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "PAE"].index, inplace=True)


new_gdf_g1 = new_gdf_g1.reset_index()


# Group 2
new_gdf_g2 = gdf_g2.copy()
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "NAT"].index, inplace=True)
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "CRO"].index, inplace=True)
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "MCO"].index, inplace=True)
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "CAM"].index, inplace=True)
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "SJC"].index, inplace=True)
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "FLO"].index, inplace=True)
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "URU"].index, inplace=True)
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "PPO"].index, inplace=True)

# SAL, BJL, DIA AND CSV PRIORITY DUE TO GEO DISTRIB
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "VCQ"].index, inplace=True)
# PET, BJL, AND SAL PRIORITY DUE TO GEO DISTRIB.
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "MDN"].index, inplace=True)

new_gdf_g2 = new_gdf_g2.reset_index()


# Group 3
new_gdf_g3 = gdf_g3.copy()
new_gdf_g3.drop(new_gdf_g3[new_gdf_g3["Code"] == "SGL"].index, inplace=True)
new_gdf_g3.drop(new_gdf_g3[new_gdf_g3["Code"] == "PSF"].index, inplace=True)
new_gdf_g3.drop(new_gdf_g3[new_gdf_g3["Code"] == "BOT"].index, inplace=True)
new_gdf_g3.drop(new_gdf_g3[new_gdf_g3["Code"] == "VIT"].index, inplace=True)
new_gdf_g3.drop(new_gdf_g3[new_gdf_g3["Code"] == "APG_A"].index, inplace=True)
new_gdf_g3.drop(new_gdf_g3[new_gdf_g3["Code"] == "AMP_B"].index, inplace=True)

# CIT, PCS, AND DIA PRIORITY OVER UBA DUE TO GEO DISTRIB.
new_gdf_g3.drop(new_gdf_g3[new_gdf_g3["Code"] == "UBA"].index, inplace=True)


new_gdf_g3 = new_gdf_g3.reset_index()


# Group 4
new_gdf_g4 = gdf_g4.copy()
new_gdf_g4.drop(new_gdf_g4[new_gdf_g4["Code"] == "GJM"].index, inplace=True)
new_gdf_g4.drop(new_gdf_g4[new_gdf_g4["Code"] == "JIT"].index, inplace=True)
new_gdf_g4.drop(new_gdf_g4[new_gdf_g4["Code"] == "TAU"].index, inplace=True)
new_gdf_g4.drop(new_gdf_g4[new_gdf_g4["Code"] == "SMS"].index, inplace=True)
new_gdf_g4.drop(new_gdf_g4[new_gdf_g4["Code"] == "ILH"].index, inplace=True)
new_gdf_g4.drop(new_gdf_g4[new_gdf_g4["Code"] == "PAR"].index, inplace=True)

# RGE PRIORITY OVER SVP DUE TO GEO DISTRIB AND N OCP
new_gdf_g4.drop(new_gdf_g4[new_gdf_g4["Code"] == "SVP"].index, inplace=True)
# SBA PRIORITY OVER ALE DUE TO N OCP
new_gdf_g4.drop(new_gdf_g4[new_gdf_g4["Code"] == "ALE"].index, inplace=True)
# ARA__F EXCLUDED DUE TO GEO DISTRIB
new_gdf_g4.drop(new_gdf_g4[new_gdf_g4["Code"] == "ARA_F"].index, inplace=True)
new_gdf_g4 = new_gdf_g4.reset_index()


# Group 5
new_gdf_g5 = gdf_g5.copy()
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "MSS"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "BAR_A"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "BCH_B"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "PTA"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "PMO"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "GPO"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "UBR_F"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "MSS"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "BAM_D"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "PIR_E"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "BRS_C"].index, inplace=True)
new_gdf_g5.drop(new_gdf_g5[new_gdf_g5["Code"] == "VLT_A"].index, inplace=True)


new_gdf_g5 = new_gdf_g5.reset_index()

# Group 6
new_gdf_g6 = gdf_g6.copy()
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "CCA"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "IAM_C"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "PCS_B"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "CGS"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "DIV_C"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "EPI"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "PIM"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "PTR"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "ARR_C"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "ARU_C"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "FMA_B"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "JAN_E"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "MCS_D"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "SCC"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "CRS"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "ATI_A"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "CUR"].index, inplace=True)
new_gdf_g6.drop(new_gdf_g6[new_gdf_g6["Code"] == "GVS_D"].index, inplace=True)
new_gdf_g6 = new_gdf_g6.reset_index()


# Group 7
new_gdf_g7 = gdf_g7.copy()
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "CPS"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "MTS_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "TRA_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "BAG_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "IOA_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "CAP_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "PAC_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "EPI_B"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "CAC_B"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "ACI_C"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "TPS_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "SJB_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "CBA_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "PMS"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "COX_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "FSA"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "PAT"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "SCE_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "IGA_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "ITA_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "VAL_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "RLO_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "PPI"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "DVE_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "BJP_B"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "CHA"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "BAC_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "ACU"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "RPA"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "SLZ"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "CPO_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "BCO_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "CAR_D"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "VSU_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "COD_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "SIN"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "VRA_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "MAU_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "JUT_A"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "PAN"].index, inplace=True)
new_gdf_g7.drop(new_gdf_g7[new_gdf_g7["Code"] == "ARR"].index, inplace=True)

new_gdf_g7 = new_gdf_g7.reset_index()


# =====================END INTERACTIVE STATION REMOVAL BLOCK===================

# Folium map
tile_type0 = "OpenStreetMap"
map0 = folium.Map(location=[-15, -50], zoom_start=5, tiles=tile_type0)

# Main group
fg0 = folium.FeatureGroup()

# Group 1:
g01 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 10 or more',
                                          show=True)
for index, location_info in new_gdf_g1.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="red", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat:",
            location_info["Latitude"],
            "Lon",
            location_info["Longitude"],
            "Nearest Brazilian Observatory:",
            location_info["Nearest_Observatory"],
            "Number_of_occupations:",
            location_info["Number_occupations"],
            "Name:",
            location_info["Name"],
            "Last_occupation:",
            location_info["Time"],
        ],
    ).add_to(g01)
# Add the repeat stations coverage
for index, location_info in new_gdf_g1.iterrows():
    folium.Circle(
        [location_info["Latitude"], location_info["Longitude"]],
        radius=repeat_station_coverage_radius_m,
        color="red",
        # fill_color = "green"
    ).add_to(g01)


# Group 2:
g02 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 8 to 9',
                                          show=False)
for index, location_info in new_gdf_g2.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="blue", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat:",
            location_info["Latitude"],
            "Lon",
            location_info["Longitude"],
            "Nearest Brazilian Observatory:",
            location_info["Nearest_Observatory"],
            "Number_of_occupations:",
            location_info["Number_occupations"],
            "Name:",
            location_info["Name"],
            "Last_occupation:",
            location_info["Time"],
        ],
    ).add_to(g02)
# Add the repeat stations coverage
for index, location_info in new_gdf_g2.iterrows():
    folium.Circle(
        [location_info["Latitude"], location_info["Longitude"]],
        radius=repeat_station_coverage_radius_m,
        color="blue",
        # fill_color = "green"
    ).add_to(g02)


# Group 3:
g03 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 6 to 7',
                                          show=False)
for index, location_info in new_gdf_g3.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="green", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat:",
            location_info["Latitude"],
            "Lon",
            location_info["Longitude"],
            "Nearest Brazilian Observatory:",
            location_info["Nearest_Observatory"],
            "Number_of_occupations:",
            location_info["Number_occupations"],
            "Name:",
            location_info["Name"],
            "Last_occupation:",
            location_info["Time"],
        ],
    ).add_to(g03)
# Add the repeat stations coverage
for index, location_info in new_gdf_g3.iterrows():
    folium.Circle(
        [location_info["Latitude"], location_info["Longitude"]],
        radius=repeat_station_coverage_radius_m,
        color="green",
        # fill_color = "green"
    ).add_to(g03)


# Group 4:
g04 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 4 to 5',
                                          show=False)
for index, location_info in new_gdf_g4.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="purple", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat:",
            location_info["Latitude"],
            "Lon",
            location_info["Longitude"],
            "Nearest Brazilian Observatory:",
            location_info["Nearest_Observatory"],
            "Number_of_occupations:",
            location_info["Number_occupations"],
            "Name:",
            location_info["Name"],
            "Last_occupation:",
            location_info["Time"],
        ],
    ).add_to(g04)
# Add the repeat stations coverage
for index, location_info in new_gdf_g4.iterrows():
    folium.Circle(
        [location_info["Latitude"], location_info["Longitude"]],
        radius=repeat_station_coverage_radius_m,
        color="purple",
        # fill_color = "green"
    ).add_to(g04)


# Group 5:
g05 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 3',
                                          show=False)
for index, location_info in new_gdf_g5.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="orange", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat:",
            location_info["Latitude"],
            "Lon",
            location_info["Longitude"],
            "Nearest Brazilian Observatory:",
            location_info["Nearest_Observatory"],
            "Number_of_occupations:",
            location_info["Number_occupations"],
            "Name:",
            location_info["Name"],
            "Last_occupation:",
            location_info["Time"],
        ],
    ).add_to(g05)
# Add the repeat stations coverage
for index, location_info in new_gdf_g5.iterrows():
    folium.Circle(
        [location_info["Latitude"], location_info["Longitude"]],
        radius=repeat_station_coverage_radius_m,
        color="orange",
        # fill_color = "green"
    ).add_to(g05)


# Group 6:
g06 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 2',
                                          show=False)
for index, location_info in new_gdf_g6.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="black", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat:",
            location_info["Latitude"],
            "Lon",
            location_info["Longitude"],
            "Nearest Brazilian Observatory:",
            location_info["Nearest_Observatory"],
            "Number_of_occupations:",
            location_info["Number_occupations"],
            "Name:",
            location_info["Name"],
            "Last_occupation:",
            location_info["Time"],
        ],
    ).add_to(g06)
# Add the repeat stations coverage
for index, location_info in new_gdf_g6.iterrows():
    folium.Circle(
        [location_info["Latitude"], location_info["Longitude"]],
        radius=repeat_station_coverage_radius_m,
        color="black",
        # fill_color = "green"
    ).add_to(g06)


# Group 7:
g07 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 1',
                                          show=False)
for index, location_info in new_gdf_g7.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="gray", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat:",
            location_info["Latitude"],
            "Lon",
            location_info["Longitude"],
            "Nearest Brazilian Observatory:",
            location_info["Nearest_Observatory"],
            "Number_of_occupations:",
            location_info["Number_occupations"],
            "Name:",
            location_info["Name"],
            "Last_occupation:",
            location_info["Time"],
        ],
    ).add_to(g07)
# Add the repeat stations coverage
for index, location_info in new_gdf_g7.iterrows():
    folium.Circle(
        [location_info["Latitude"], location_info["Longitude"]],
        radius=repeat_station_coverage_radius_m,
        color="gray",
        # fill_color = "green"
    ).add_to(g07)

# Add the subgroups to the main map
map0.add_child(fg0)
map0.add_child(g01)
map0.add_child(g02)
map0.add_child(g03)
map0.add_child(g04)
map0.add_child(g05)
map0.add_child(g06)
map0.add_child(g07)

# Add the layer control
folium.LayerControl().add_to(map0)

# Add altitude and longitude tool map
lat_lon_vis0 = folium.LatLngPopup()
map0.add_child(lat_lon_vis0)

# Measurement control
measure_control0 = plugins.MeasureControl(position="topleft",
                                          active_color="red",
                                          completed_color="red",
                                          primary_length_unit="kilometers")
map0.add_child(measure_control0)

# Add the full screen button
fullscreen_button0 = plugins.Fullscreen(position='topright',
                                        title='Expand me',
                                        title_cancel='Exit me',
                                        force_separate_button=True)
map0.add_child(fullscreen_button0)

# Add a mini map
minimap0 = plugins.MiniMap()
map0.add_child(minimap0)

# Draw tools
# export=True exports the drawn shapes as a geojson file
draw0 = plugins.Draw(export=True)
map0.add_child(draw0)

# Save map
map0.save(mapa0)


# Create a df with the chosen repeat stations
merge_dfs = [new_gdf_g1, new_gdf_g2, new_gdf_g3,
             new_gdf_g4, new_gdf_g5, new_gdf_g7]
selected_df = pd.concat(merge_dfs)
selected_df = selected_df.drop(columns=["index"])

# Create a database for the selected repeat stations
# read original database
original_rs_db = pd.read_csv(rs_database_folder / rs_database_file)

list_chosen_rs = selected_df["Code"].to_list()
selected_df_db = original_rs_db.copy()
selected_df_db = selected_df_db.loc[
    selected_df_db["Code"].isin(list_chosen_rs)]
selected_df_db = selected_df_db.reset_index()
selected_df_db = selected_df_db.drop(columns=["index"])
selected_df_db.to_csv(output_folder / selected_rs_database, index=False,
                      na_rep="NaN")
