# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 20:06:16 2022

author: raissa baldez

Description

This program plots the info about the stats of the network in 2019.

"""

# Import modules
import mestrado_module as mm
import pandas as pd
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import geopandas as gpd


# Repeat station data
rs_folder: Path = Path(mm.path_pipeline_03_rs_database_creation)
rs_file: Path = Path(mm.output_03_code_rs_database)

# Shapefile info
shapefile_folder: Path = Path(mm.path_00_data_brazil_shapefile)
shapefile_file: Path = Path(mm.brazil_shapefile)

# Output
output_folder: Path = Path(mm.path_pipeline_05a_selection_process_plot_distrib)

# Figure names
ocp_distrib_by_sts: Path = Path(mm.output_05a_code_fig_ocp_distrib_sts)
sts_distrib_region: Path = Path(mm.output_05a_code_fig_sts_distrib_region)
ocp_distrib_region: Path = Path(mm.output_05a_code_fig_ocp_distrib_region)

sts_distrib_states_n: Path = Path(
    mm.output_05a_code_fig_sts_distrib_states_n)
sts_distrib_states_ne: Path = Path(
    mm.output_05a_code_fig_sts_distrib_states_ne)
sts_distrib_states_co: Path = Path(
    mm.output_05a_code_fig_sts_distrib_states_co)
sts_distrib_states_se: Path = Path(
    mm.output_05a_code_fig_sts_distrib_states_se)
sts_distrib_states_s: Path = Path(
    mm.output_05a_code_fig_sts_distrib_states_s)

ocp_distrib_states_n: Path = Path(
    mm.output_05a_code_fig_ocp_distrib_states_n)
ocp_distrib_states_ne: Path = Path(
    mm.output_05a_code_fig_ocp_distrib_states_ne)
ocp_distrib_states_co: Path = Path(
    mm.output_05a_code_fig_ocp_distrib_states_co)
ocp_distrib_states_se: Path = Path(
    mm.output_05a_code_fig_ocp_distrib_states_se)
ocp_distrib_states_s: Path = Path(
    mm.output_05a_code_fig_ocp_distrib_states_s)

geo_distrib: Path = Path(mm.output_05a_code_fig_geo_distrib)


# Figure style
sns.set_style('darkgrid')


# Load data with Pandas
df = pd.read_csv(rs_folder / rs_file)
df_unique = df.drop_duplicates(subset="Name", keep="last")


# Create a df with information organized by state: region, number of stations
# and number of occupations in a state
info_by_states = df_unique.groupby(['State', 'Region']).agg(
    Station=pd.NamedAgg(column="Name", aggfunc="count"),
    Occupation=pd.NamedAgg(column="Number_occupations",
                           aggfunc="sum")
)
# reset index to create a df with numbers as index instead of state and region
info_by_states = info_by_states.reset_index()
info_by_states["Region"] = info_by_states["Region"].replace(
    "Centro-oeste", "MW")
info_by_states["Region"] = info_by_states["Region"].replace(
    "Nordeste", "NE")
info_by_states["Region"] = info_by_states["Region"].replace(
    "Norte", "N")
info_by_states["Region"] = info_by_states["Region"].replace(
    "Sudeste", "SE")
info_by_states["Region"] = info_by_states["Region"].replace(
    "Sul", "S")


# Create a df with information organized by region: state, number of stations
# and number of occupations in a region
info_by_region = info_by_states.groupby(['Region']).agg(
    State=pd.NamedAgg(column="State", aggfunc="count"),
    Station=pd.NamedAgg(column="Station", aggfunc="sum"),
    Occupation=pd.NamedAgg(column="Occupation",
                           aggfunc="sum")
)
# reset index to create a df with numbers as index instead of state and region
info_by_region = info_by_region.reset_index()
info_by_region["Region"] = info_by_region["Region"].replace(
    "Centro-oeste", "MW")
info_by_region["Region"] = info_by_region["Region"].replace(
    "Nordeste", "NE")
info_by_region["Region"] = info_by_region["Region"].replace(
    "Norte", "N")
info_by_region["Region"] = info_by_region["Region"].replace(
    "Sudeste", "SE")
info_by_region["Region"] = info_by_region["Region"].replace(
    "Sul", "S")


# Plot: distribution of number of occupations by station
fig_ocp, ax_fig_ocp = plt.subplots()
ax_fig_ocp = sns.countplot(x="Number_occupations", data=df_unique)
ax_fig_ocp.set_xlabel("Number of occupations")
ax_fig_ocp.set_ylabel("Number of stations")
ax_fig_ocp.set_title("Occupation distribution by station")
fig_ocp.savefig(output_folder / ocp_distrib_by_sts, dpi=300)


# Plot: Station distribution by region
data1 = info_by_region["Station"]
labels1 = info_by_region["Region"]
colors = sns.color_palette('pastel')  # define Seaborn color palette to use

mm.station_distribution_region(info_by_region["Station"],
                               info_by_region["Region"],
                               colors,
                               output_folder,
                               sts_distrib_region)


# Plot: Occupation distribution by region
data2 = info_by_region["Occupation"]
labels2 = info_by_region["Region"]
mm.occupation_distribution_region(data2,
                                  labels2,
                                  colors,
                                  output_folder,
                                  ocp_distrib_region)


# Plot: distribution by states in a region
# North
df_north = info_by_states[info_by_states["Region"] == "N"]
mm.station_distribution_states_region(df_north["Station"],
                                      df_north["State"],
                                      colors,
                                      output_folder,
                                      sts_distrib_states_n,
                                      "North")

mm.occupation_distribution_states_region(df_north["Occupation"],
                                         df_north["State"],
                                         colors,
                                         output_folder,
                                         ocp_distrib_states_n,
                                         "North")

# Northeast
df_northeast = info_by_states[info_by_states["Region"] == "NE"]
mm.station_distribution_states_region(df_northeast["Station"],
                                      df_northeast["State"],
                                      colors,
                                      output_folder,
                                      sts_distrib_states_ne,
                                      "Northeast")

mm.occupation_distribution_states_region(df_northeast["Occupation"],
                                         df_northeast["State"],
                                         colors,
                                         output_folder,
                                         ocp_distrib_states_ne,
                                         "Northeast")

# Centro oeste
df_co = info_by_states[info_by_states["Region"] == "MW"]
mm.station_distribution_states_region(df_co["Station"],
                                      df_co["State"],
                                      colors,
                                      output_folder,
                                      sts_distrib_states_co,
                                      "Midwest")

mm.occupation_distribution_states_region(df_co["Occupation"],
                                         df_co["State"],
                                         colors,
                                         output_folder,
                                         ocp_distrib_states_co,
                                         "Midwest")

# Southeast
df_se = info_by_states[info_by_states["Region"] == "SE"]
mm.station_distribution_states_region(df_se["Station"],
                                      df_se["State"],
                                      colors,
                                      output_folder,
                                      sts_distrib_states_se,
                                      "Southeast")

mm.occupation_distribution_states_region(df_se["Occupation"],
                                         df_se["State"],
                                         colors,
                                         output_folder,
                                         ocp_distrib_states_se,
                                         "Southeast")

# South
df_s = info_by_states[info_by_states["Region"] == "S"]
mm.station_distribution_states_region(df_s["Station"],
                                      df_s["State"],
                                      colors,
                                      output_folder,
                                      sts_distrib_states_s,
                                      "South")

mm.occupation_distribution_states_region(df_s["Occupation"],
                                         df_s["State"],
                                         colors,
                                         output_folder,
                                         ocp_distrib_states_s,
                                         "South")


# Plot geographical distribution
# Create a geodataframe with info from the shapefile
brazil_gdf = gpd.read_file(shapefile_folder / shapefile_file)

# Check the used projection in the shapefile
# (EPSG:4326 is the WGS84 latitude-longitude projection)
# look here https://epsg.io/4674, projection used in latin america
print(brazil_gdf.crs)

# Create the geodataframe for the lat lon points of the stations
repeat_stations_gdf = gpd.GeoDataFrame(df_unique,
                                       geometry=gpd.points_from_xy(
                                           df_unique.Longitude,
                                           df_unique.Latitude)
                                       )

# Create a geodataframe for Observatories location according to Intermagnet
TTB_lat = mm.TTB_lat
TTB_lon = mm.TTB_lon
VSS_lat = mm.VSS_lat
VSS_lon = mm.VSS_lon
obs_data = {"Latitude": [TTB_lat, VSS_lat], "Longitude": [TTB_lon, VSS_lon]}
obs_data_df = pd.DataFrame(data=obs_data)
obs_data_gdf = gpd.GeoDataFrame(obs_data_df,
                                geometry=gpd.points_from_xy(
                                    obs_data_df.Longitude,
                                    obs_data_df.Latitude)
                                )

# Define plot variables
# Figure size (figsize=(f1, f2))
f1 = 6
f2 = 6

# Plot
brazil_color = "lightgray"
brazil_edge_color = "black"
station_symbol_plot = "o"
station_symbol_plot_color = "darkred"
station_size = 10
obs_symbol_plot = "*"
obs_symbol_plot_color = "darkblue"
obs_size = 50

# Legend
blue_star = mlines.Line2D([], [], marker=obs_symbol_plot,
                          color=obs_symbol_plot_color,
                          linestyle='None',
                          markersize=6,
                          label='Observatory')
red_circle = mlines.Line2D([], [], marker=station_symbol_plot,
                           color=station_symbol_plot_color,
                           linestyle='None',
                           markersize=6, label='Repeat Station')

# Create the figure
fig, ax = plt.subplots(figsize=(f1, f2))
# set aspect to equal. This is done automatically when using *geopandas* plot
# on it's own, but not when working with pyplot directly.
ax.set_aspect("equal")

# Plot
brazil_gdf.plot(ax=ax, color=brazil_color, edgecolor=brazil_edge_color)
repeat_stations_gdf.plot(ax=ax, marker=station_symbol_plot,
                         color=station_symbol_plot_color,
                         markersize=station_size,
                         alpha=1)
obs_data_gdf.plot(ax=ax, marker=obs_symbol_plot,
                  color=obs_symbol_plot_color,
                  markersize=obs_size,
                  alpha=1)
ax.legend(handles=[blue_star, red_circle], loc="lower right")

# Details
ax.set_title("Brazilian Repeat Station Network in 2019", fontsize=16)
ax.set_xlabel("Longitude (decimal degrees)", fontsize=14)
ax.set_ylabel("Latitude (decimal degrees)", fontsize=14)
plt.savefig(output_folder / geo_distrib, dpi=300, bbox_inches="tight")
plt.show()
