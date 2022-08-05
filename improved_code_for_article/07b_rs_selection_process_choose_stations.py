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
1. Geographical coverage (using the coverage_radius parameter)
1.1 Especial (read ATTENTION below): Time of last occupation
2. Number of occupations
3. Values of RMSE

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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import geopandas as gpd
from shapely.geometry import Point, Polygon
import folium
from folium import plugins
import seaborn as sns
import branca
from branca.element import Template, MacroElement


# Magnetic Observatories data
mags_obs_folder: Path = Path(mm.path_00_data_manual)
mags_obs_file: Path = Path(
    "models_intermagnet_observatories_south_america.csv")

# Input
input_folder: Path = Path(mm.path_pipeline_05_rank_n_occupations)
folium_file_g1: Path = Path(mm.output_05a_code_folium_file_g1)
folium_file_g2: Path = Path(mm.output_05a_code_folium_file_g2)
folium_file_g3: Path = Path(mm.output_05a_code_folium_file_g3)
folium_file_g4: Path = Path(mm.output_05a_code_folium_file_g4)

# Save figures and files
output_folder: Path = Path(mm.path_pipeline_07_selection_process)
chosen_rs: Path = Path(mm.output_7a_code_selected_rs_folium)

# Folium maps
mapa0 = "../02_pipeline/07_repeat_stations_selection_process/"\
    "07a_selection_process_repeat_stations_map.html"


# read folium files
df_g1 = pd.read_csv(input_folder / folium_file_g1)
df_g2 = pd.read_csv(input_folder / folium_file_g2)
df_g3 = pd.read_csv(input_folder / folium_file_g3)
df_g4 = pd.read_csv(input_folder / folium_file_g4)


# New selection criteria: last time of occupation
g1_filtered = mm.select_station_last_occupation_year_2000(df_g1)
g2_filtered = mm.select_station_last_occupation_year_2000(df_g2)
g3_filtered = mm.select_station_last_occupation_year_2000(df_g3)
g4_filtered = mm.select_station_last_occupation_year_2000(df_g4)


# Criteria: geographical distribution using folium map for analysis

# Step 1: create geodataframes for the stations and magnetic observatories
# chosen_df_g1 = df_g1
chosen_df_g1 = g1_filtered  # df_g1 to ignore new criteria
gdf_g1 = gpd.GeoDataFrame(
    chosen_df_g1, geometry=gpd.points_from_xy(
        chosen_df_g1["Longitude"], chosen_df_g1["Latitude"]
    )
)

# chosen_df_g2 = df_g2
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


# =====================INTERACTIVE STATION REMOVAL BLOCK=======================
"""
# ITERATIVE PART OF SELECTION PROCESS!!!
The following block of code removes specific stations from the occupation
groups to create a better geographical distribution of the repeat stations
over the country each time the code is executed.
"""

# Group 1
new_gdf_g1 = gdf_g1.copy()
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "GOI"].index, inplace=True)
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "MRL"].index, inplace=True)
new_gdf_g1.drop(new_gdf_g1[new_gdf_g1["Code"] == "CGE"].index, inplace=True)
new_gdf_g1 = new_gdf_g1.reset_index()

# Group 2
new_gdf_g2 = gdf_g2.copy()
new_gdf_g2.drop(new_gdf_g2[new_gdf_g2["Code"] == "PNB"].index, inplace=True)

# Group 3
new_gdf_g3 = gdf_g3.copy()


# Group 4
new_gdf_g4 = gdf_g4.copy()

# =====================END INTERACTIVE STATION REMOVAL BLOCK===================


# Step 2: Create an Folium map to select the stations
# DEFINITIONS (distances in km)
# observatory_coverage_radius = 904000 # BASED ON ITALY CASTELLO TESINO
# embracer_coverage_radius = 150000 # germany
# embracer_coverage_radius = 230000 # italy GIB station

# Radius suggested by Katia and Cristiano (800 km, 500 km, 300 km, 500 km)
observatory_coverage_radius_m = 800000
repeat_station_coverage_radius_m = 300000


# Folium map
tile_type0 = "OpenStreetMap"
map0 = folium.Map(location=[-15, -50], zoom_start=5, tiles=tile_type0)

# Main group
fg0 = folium.FeatureGroup()

# Group 1: Repeat Stations with 12 or more occupations
g01 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 12 or more')
for index, location_info in new_gdf_g1.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="red", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat_dd:",
            location_info["Latitude"],
            "Lon_dd",
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


# Group 2: Repeat Stations with 9 to 11 occupations
g02 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 9 to 11')
for index, location_info in new_gdf_g2.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="blue", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat_dd:",
            location_info["Latitude"],
            "Lon_dd",
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


# Group 3: Repeat Stations with 4 to 8 occupations
g03 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 4 to 8')
for index, location_info in new_gdf_g3.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="green", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat_dd:",
            location_info["Latitude"],
            "Lon_dd",
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


# Group 4: Repeat Stations with 1 to 3 occupations
g04 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 1 to 3')
for index, location_info in new_gdf_g4.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="purple", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station:",
            location_info["Code"],
            "Lat_dd:",
            location_info["Latitude"],
            "Lon_dd",
            location_info["Longitude"],
            "Nearest Brazilian Observatory:",
            location_info["Nearest_Observatory"],
            "Number_of_occupations:",
            location_info["Number_occupations"],
            "Name:",
            location_info["Name"]
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


# Add the subgroups to the main map
map0.add_child(fg0)
map0.add_child(g01)
map0.add_child(g02)
map0.add_child(g03)
map0.add_child(g04)

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
