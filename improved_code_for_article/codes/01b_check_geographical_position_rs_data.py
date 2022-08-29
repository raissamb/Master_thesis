# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:14:38 2022

author: raissa baldez

Description

This program loads the 1a_filtered_repeat_stations_data.csv file to check the
stations locations:
- Plot the stations locations over States shapefiles to see if they are indeed
correct
- Remove stations with wrong locations from future analysis

"""


# Import modules
import mestrado_module as mm
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import folium
from folium import plugins


# Paths
input_folder: Path = Path(mm.path_pipeline_01_data_processing)
output_folder: Path = Path(mm.path_pipeline_01_data_processing)
# Files
input_file: Path = Path(mm.output_01a_code_clean_data)
output_file: Path = Path(mm.output_01b_code_processed_data)
# Shapefile info
shapefile_folder: Path = Path(mm.path_00_data_brazil_shapefile)
shapefile_file: Path = Path(mm.brazil_shapefile)
# Figure style
sns.set_style("darkgrid")
# Save figures
figs_folder: Path = Path("../02_pipeline/01_data_processing/figures_location")


# Create a geodataframe using info from the shapefile
brazil_gdf = gpd.read_file(shapefile_folder / shapefile_file)

# Check the used projection in the shapefile
# (EPSG:4326 is the WGS84 latitude-longitude projection)
print(brazil_gdf.crs)
# look here https://epsg.io/4674, projection used in latin america


# Load repeat station data with Pandas
rs_df = pd.read_csv(input_folder / input_file)

# Create a geometry column for the repeat stations dataframe
rs_gdf = gpd.GeoDataFrame(rs_df, geometry=gpd.points_from_xy(
    rs_df.Longitude, rs_df.Latitude))

# Set the same CRS for the repeat stations locations the same as the brazil_gdf
rs_gdf = rs_gdf.set_crs("EPSG:4674")


# Check the location of each station in relation to the Brazil shapefile
# Create a new gdf and a column to write State symbol
states_gdf = rs_gdf.copy()
states_gdf["State"] = 0
states_gdf["Region"] = 0


# function to check if points belong to a state polygon
def check_points_in_state_polygon(brazil_gdf_state_index):
    state_polygon = brazil_gdf["geometry"].iloc[brazil_gdf_state_index]
    state_points = rs_gdf.geometry.within(state_polygon)
    # state_points_counts = state_points.value_counts()
    state_true_index = state_points.index[state_points == True]
    # Write state symbol into the dataframe
    states_gdf.loc[state_true_index, "State"] = brazil_gdf["SIGLA_UF"].iloc[
        brazil_gdf_state_index]
    # Write region
    region = brazil_gdf["NM_REGIAO"].iloc[brazil_gdf_state_index]
    states_gdf.loc[state_true_index, "Region"] = region


# list of number to loop through the states of the brazil_gdf
number_list = list(range(0, 27))

# Loop to check points inside state polygon
for i in number_list:
    res = check_points_in_state_polygon(i)

# Check which stations were not marked as part of a polygon state (they have
# 0 instead of state symbols)
outside_polygons_gdf = states_gdf.loc[(states_gdf["State"] == 0)]

# Plot points outside polygon
fig, ax = plt.subplots()
ax.set_aspect("equal")
# plot
brazil_gdf.plot(ax=ax, color="gray", edgecolor="black")
outside_polygons_gdf.plot(ax=ax, marker="o", color="red",
                          markersize=20, alpha=1)
# Details
ax.set_title("Points outside State's borders", fontsize=16)
ax.set_xlabel("Longitude (degrees)", fontsize=14)
ax.set_ylabel("Latitude (degrees)", fontsize=14)
plt.savefig(figs_folder/"outside_points_locations.png",
            dpi=300, bbox_inches="tight")


# Create a Folium map with outside points
tile_type0 = "OpenStreetMap"
map0 = folium.Map(location=[-15, -50], zoom_start=5, tiles=tile_type0)
# Main group
fg0 = folium.FeatureGroup()

# Group 1: Repeat Stations with 12 or more occupations
g01 = folium.plugins.FeatureGroupSubGroup(fg0, name='Out', show=True)
for index, location_info in outside_polygons_gdf.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="red", icon="circle", prefix="fa"),
        tooltip=[
            "Repeat_Station_Code:",
            location_info["Code"],
            "Lat_dd:",
            location_info["Latitude"],
            "Lon_dd",
            location_info["Longitude"],
            "Local:",
            location_info["Name"],
            "Occupation time:",
            location_info["Time"],
        ],
    ).add_to(g01)
# Add the subgroups to the main map
map0.add_child(fg0)
map0.add_child(g01)
# Save map
map0.save(
    "../02_pipeline/01_data_processing/figures_location/points_outside_borders.html")

"""
NOTES ON THE RESULT OF THE OUTSIDE POINTS

1) BARRA DO CHUI (RS) A: BCH_A
- The BCH_A station point is at the water
- The RGE station point is at the water
- Decision: since the stations point to water, they will be removed from
 further analysis

2) CACERES MT: CAC
- The CAC station is at Bolivia
- Decision: since this station points to another country, it will be removed
from further analysis

3) CANANEIA (SP) A: CAN_A
- The CAN_A station point is at Paraguay
- Decision: since this station points far away from SP, it will be removed
from further analysis

4) FORTALEZA: FOR
- The FOR station point is at the water
- Decision: since this station points to water, it will be removed from
further analysis

5) ILHEUS: ILH
- The ILH station point is at the water
- Decision: since this station points to water, it will be removed from
further analysis

6) NATAL: NAT
- The NAT station points are at the water
- Decision: since this station points to water, it will be removed from
further analysis

7) PONTA PORA: PPO
- The PPO station is at Paraguay
- Decision: since this station points to another country, it will be removed
from further analysis

8) RECIFE: REC
- The REC station points are at the water
- Decision: since the PE_REC station points to water, it will be removed from
further analysis

9) RIO GRANDE
- The RGE station points are at the water
- Decision: since the PE_REC station points to water, it will be removed from
further analysis
"""

# Delete the points outside of states' borders
# Create new gdf
df_final = states_gdf.copy()
# get indexes of outside_states df
outside_df_indexes = outside_polygons_gdf.index
# Delete the necessary rows
df_final = df_final.drop(outside_df_indexes)
df_final = df_final.reset_index()
df_final = df_final.drop(columns=["index"])
df_final = df_final.drop(columns=["geometry"])
df_final.to_csv(output_folder / output_file, na_rep="NaN", index=False)
