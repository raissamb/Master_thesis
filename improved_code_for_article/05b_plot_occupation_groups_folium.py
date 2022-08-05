# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:14:25 2022

author: raissa baldez

Description

This program plots does the following using the Repeat station and IGRF
database:
- It creates a geodataframe usind Geopandas for each occupation group
- It plots the location of these stations (each occupation group has a color)
over the Brazil shapefile
- It uses the folium package to create an interactive map of the occupation
groups

"""

# Import modules
import mestrado_module as mm
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import geopandas as gpd
from shapely.geometry import Point, Polygon
import folium
from folium import plugins
import seaborn as sns
from branca.element import Template, MacroElement


# Shapefile info
shapefile_folder: Path = Path(mm.path_00_data_brazil_shapefile)
shapefile_file: Path = Path(mm.brazil_shapefile)

# Input folder
input_folder: Path = Path(mm.path_pipeline_05_rank_n_occupations)

# Files for Folium plot
folium_file_g1: Path = Path(mm.output_05a_code_folium_file_g1)
folium_file_g2: Path = Path(mm.output_05a_code_folium_file_g2)
folium_file_g3: Path = Path(mm.output_05a_code_folium_file_g3)
folium_file_g4: Path = Path(mm.output_05a_code_folium_file_g4)
folium_file_g5: Path = Path(mm.output_05a_code_folium_file_g5)
folium_file_g6: Path = Path(mm.output_05a_code_folium_file_g6)

# Save figures and files
output_folder: Path = Path(mm.path_pipeline_05_rank_n_occupations)

static_map: Path = Path("05b_rs_network_map_by_occupations.png")
mapa0 = "../02_pipeline/05_rank_repeat_stations_n_occupations/"\
    "05b_rs_network_interactive_map_by_occupations.html"

# Figure style
sns.set_style("darkgrid")


# Brazil shapefile data
# Create a geodataframe to plot the stations using Brazil shapefile
gdf_brazil = gpd.read_file(shapefile_folder / shapefile_file)

# Check geodaframe info
# gdf_brazil.info()

# Check the used projection in the shapefile
# (EPSG:4326 is the WGS84 latitude-longitude projection)
print(gdf_brazil.crs)
# look here https://epsg.io/4674, projection used in latin america

# read repeat station data
df_g1 = pd.read_csv(input_folder / folium_file_g1)
df_g2 = pd.read_csv(input_folder / folium_file_g2)
df_g3 = pd.read_csv(input_folder / folium_file_g3)
df_g4 = pd.read_csv(input_folder / folium_file_g4)

# create geodataframes for repeat station data
gdf_g1 = gpd.GeoDataFrame(
    df_g1, geometry=gpd.points_from_xy(df_g1["Longitude"], df_g1["Latitude"])
)

gdf_g2 = gpd.GeoDataFrame(
    df_g2, geometry=gpd.points_from_xy(df_g2["Longitude"], df_g2["Latitude"])
)

gdf_g3 = gpd.GeoDataFrame(
    df_g3, geometry=gpd.points_from_xy(df_g3["Longitude"], df_g3["Latitude"])
)

gdf_g4 = gpd.GeoDataFrame(
    df_g4, geometry=gpd.points_from_xy(df_g4["Longitude"], df_g4["Latitude"])
)

# Plot the data using Brazil shapefile
# STATIC MAP PNG
# Define plot variables
# Figure size (figsize=(f1, f2))
f1 = 7
f2 = 7

brazil_color = "silver"
brazil_edge_color = "black"
rs_station_symbol = "o"
rs_station_symbol_g1_color = "red"
rs_station_symbol_g2_color = "blue"
rs_station_symbol_g3_color = "green"
rs_station_symbol_g4_color = "purple"
rs_station_symbol_size = 10
leg_loc = "lower right"


# Legend
g1_leg = mlines.Line2D([], [], marker=rs_station_symbol,
                       color=rs_station_symbol_g1_color,
                       linestyle='None',
                       markersize=rs_station_symbol_size,
                       label="Occupations: 12 or more")
g2_leg = mlines.Line2D([], [], marker=rs_station_symbol,
                       color=rs_station_symbol_g2_color,
                       linestyle='None',
                       markersize=rs_station_symbol_size,
                       label="Occupations: 9 to 11")
g3_leg = mlines.Line2D([], [], marker=rs_station_symbol,
                       color=rs_station_symbol_g3_color,
                       linestyle='None',
                       markersize=rs_station_symbol_size,
                       label="Occupations: 4 to 8")
g4_leg = mlines.Line2D([], [], marker=rs_station_symbol,
                       color=rs_station_symbol_g4_color,
                       linestyle='None',
                       markersize=rs_station_symbol_size,
                       label="Occupations: 1 to 3")


# Create the figure
fig, ax = plt.subplots(figsize=(f1, f2))
# set aspect to equal. This is done automatically when using *geopandas* plot
# on it's own, but not when working with pyplot directly.
ax.set_aspect("equal")

# Plot
gdf_brazil.plot(ax=ax, color=brazil_color, edgecolor=brazil_edge_color)

gdf_g1.plot(ax=ax,
            marker=rs_station_symbol,
            color=rs_station_symbol_g1_color,
            markersize=rs_station_symbol_size,
            alpha=1)
gdf_g2.plot(ax=ax,
            marker=rs_station_symbol,
            color=rs_station_symbol_g2_color,
            markersize=rs_station_symbol_size,
            alpha=1)
gdf_g3.plot(ax=ax,
            marker=rs_station_symbol,
            color=rs_station_symbol_g3_color,
            markersize=rs_station_symbol_size,
            alpha=1)
gdf_g4.plot(ax=ax,
            marker=rs_station_symbol,
            color=rs_station_symbol_g4_color,
            markersize=rs_station_symbol_size,
            alpha=1)
ax.legend(handles=[g1_leg, g2_leg, g3_leg, g4_leg], loc=leg_loc)

# Details
ax.set_title(
    "Representation of stations by their number of occupations", fontsize=16)
ax.set_xlabel("Longitude (decimal degrees)", fontsize=14)
ax.set_ylabel("Latitude (decimal degrees)", fontsize=14)
ax.legend(handles=[g1_leg, g2_leg, g3_leg, g4_leg], loc=leg_loc)

# Savefig
plt.savefig(output_folder / static_map, dpi=300, bbox_inches="tight")
plt.show()
# plt.close()


# Plot the stations group using folium
# INTERACTIVE MAP

# Create the Interactive map using folium
tile_type0 = "OpenStreetMap"
map0 = folium.Map(location=[-15, -50], zoom_start=5, tiles=tile_type0)

# Main group
fg0 = folium.FeatureGroup()

# Group 1: Repeat Stations with 12 or more occupations
g01 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 12 or more')
for index, location_info in gdf_g1.iterrows():
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
            location_info["Name"]
        ],
    ).add_to(g01)

# Group 2: Repeat Stations with 9 to 11 occupations
g02 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 9 to 11')
for index, location_info in gdf_g2.iterrows():
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
            location_info["Name"]
        ],
    ).add_to(g02)

# Group 3: Repeat Stations with 4 to 8 occupations
g03 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 4 to 8')
for index, location_info in gdf_g3.iterrows():
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
            location_info["Name"]
        ],
    ).add_to(g03)

# Group 4: Repeat Stations with 1 to 3 occupations
g04 = folium.plugins.FeatureGroupSubGroup(fg0, 'Occupations: 1 to 3')
for index, location_info in gdf_g4.iterrows():
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


# Add the subgroups to the main map
map0.add_child(fg0)
map0.add_child(g01)
map0.add_child(g02)
map0.add_child(g03)
map0.add_child(g04)

# Add other layers to the map
folium.TileLayer('Stamen Terrain').add_to(map0)
folium.TileLayer('Stamen Toner').add_to(map0)
folium.TileLayer('Stamen Water Color').add_to(map0)
folium.TileLayer('cartodbpositron').add_to(map0)
folium.TileLayer('cartodbdark_matter').add_to(map0)

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


# ADD LEGEND TO THE MAP
template = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Brazilian Repeat Station Network: Repeat Stations by occupations</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
     
<div class='legend-title'>Legend (draggable!)</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:red;opacity:0.7;'></span>Occupations: 12 or more</li>
    <li><span style='background:blue;opacity:0.7;'></span>Occupations: 9 to 11</li>
    <li><span style='background:green;opacity:0.7;'></span>Occupations: 4 to 8</li>
    <li><span style='background:purple;opacity:0.7;'></span>Occupations: 1 to 3</li>
  </ul>
</div>
</div>
 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro = MacroElement()
macro._template = Template(template)
map0.get_root().add_child(macro)


# Save map
map0.save(mapa0)
