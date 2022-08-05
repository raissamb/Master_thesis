# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:23:08 2022

author: raissa baldez

Description

This program plots the stations locations over States shapefiles to see if
they are indeed in their correct geographical position

"""


# Import modules
import mestrado_module as mm
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Paths
input_folder: Path = Path(mm.path_pipeline_01_data_processing)
output_folder: Path = Path(mm.path_pipeline_01_data_processing)
# Files
input_file: Path = Path(mm.output_01b_code_processed_data)
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


# Function to plot each state shapefile and the locations of the
# repeat stations on it
def plot_states(state):
    state_rs_gdf = rs_gdf.loc[(rs_gdf["State"] == state)]
    state_brazil_gdf = brazil_gdf[brazil_gdf["SIGLA_UF"] == state]
    # Create the figure
    fig, ax = plt.subplots()
    # set aspect to equal. This is done automatically when using *geopandas*
    # plot on it's own, but not when working with pyplot directly.
    ax.set_aspect("equal")
    # Plot
    state_brazil_gdf.plot(ax=ax, color="gray", edgecolor="black")
    state_rs_gdf.plot(ax=ax, marker="o", color="red", markersize=20, alpha=1)
    # Details
    ax.set_title(f"{state}", fontsize=16)
    ax.set_xlabel("Longitude (degrees)", fontsize=14)
    ax.set_ylabel("Latitude (degrees)", fontsize=14)
    plt.savefig(figs_folder/f"{state}_locations.png",
                dpi=300, bbox_inches="tight")
    plt.close()


# Create a list with the symbol for each brazilian state
list_state_symbols = brazil_gdf["SIGLA_UF"]
# print(list_symbols)

# Plot the figures
for i in list_state_symbols:
    state = i
    plot_states(i)
