# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 20:21:19 2022

author: raissa baldez

Description

Something...

"""

# Import modules
from pathlib import Path
import pandas as pd
from plotly.subplots import make_subplots
from plotly import graph_objects as go
import folium
from folium import plugins
import branca


# Selected repeat stations (folium file)
selected_rs_folder: Path = Path(
    "../../05_repeat_stations_selection_process/select_repeat_stations/")
selected_rs_file: Path = Path("05e_selected_repeat_stations_database.csv")

# read selected rs info
df = pd.read_csv(selected_rs_folder / selected_rs_file)
df_unique = df.copy().drop_duplicates(subset="Code", keep="last")


# ------------ # START STEP 1: CREATE THE REPEAT STATION INFO PLOTS

# Fuction to create popup with repeat station information
def popup_html(row):
    i = row
    code = df_unique["Code"].iloc[i]
    rs_name = df_unique["Name"].iloc[i]
    lat = df_unique["Latitude"].iloc[i]
    lon = df_unique["Longitude"].iloc[i]
    n_ocp = df_unique["Number_occupations"].iloc[i]
    last_ocp = df_unique["Time"].iloc[i]

    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"

    html_info = """<!DOCTYPE html>
<html>

<head>
<h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(code) + """

</head>
    <table style="height: 126px; width: 350px;">
<tbody>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Name</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(rs_name) + """
</tr>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Latitude (dd)</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(lat) + """
</tr>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Longitude (dd)</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(lon) + """
</tr>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Total occupations</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(n_ocp) + """
</tr>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Last occupation</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(last_ocp) + """
</tr>
</tbody>
</table>
</html>
"""
    return html_info


# ------------ # START STEP 2: CREATE THE REPEAT STATION TIME SERIES PLOTS

# Create the time series plots and save them in html format
figs = {}  # Create an empty figure to add all the plotly figures
rsnew_list = []  # Create an empty list to add all the stations
html_list = []  # Create an empty list to add all the exported html files
rsnew = df['Code'].unique()  # Get the list of station names

for i, rs in enumerate(rsnew, start=0):
    rsnew_list.append(rs)
    html_list.append('fig'+str(i)+'.html')
    df_rs = df[df['Code'] == rs]

    # Create figure using subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Observed F", "Calculated X",
                        "Calculated Y", "Calculated Z")
    )

    # Add traces
    fig.add_trace(go.Scatter(x=df_rs["Time"], y=df_rs["F"]),
                  row=1, col=1)

    fig.add_trace(go.Scatter(x=df_rs["Time"], y=df_rs["Calculated_X"]),
                  row=1, col=2)

    fig.add_trace(go.Scatter(x=df_rs["Time"], y=df_rs["Calculated_Y"]),
                  row=2, col=1)

    fig.add_trace(go.Scatter(x=df_rs["Time"], y=df_rs["Calculated_Z"]),
                  row=2, col=2)

    # Update xaxis properties
    fig.update_xaxes(title_text="Time (dy)", row=1, col=1)
    fig.update_xaxes(title_text="Time (dy)", row=1, col=2)
    fig.update_xaxes(title_text="Time (dy)", row=2, col=1)
    fig.update_xaxes(title_text="Time (dy)", row=2, col=2)

    # Update yaxis properties
    fig.update_yaxes(title_text="Intensity (nT)", row=1, col=1)
    fig.update_yaxes(title_text="Intensity (nT)", row=1, col=2)
    fig.update_yaxes(title_text="Intensity (nT)", row=2, col=1)
    fig.update_yaxes(title_text="Intensity (nT)", row=2, col=2)

    # Layout
    fig.update_layout(height=500, width=850,
                      title_text="Magnetic field components at the repeat station",
                      title_font_size=20,
                      showlegend=False)

    figs['fig'+str(i)] = fig
    fig.write_html('fig'+str(i)+".html")

# Create a dataframe to hold results from the figure
df1 = pd.DataFrame(rsnew_list, columns=['Code'])
df2 = pd.DataFrame(html_list, columns=['html_file'])
df3 = pd.concat([df1, df2], axis=1)

# Create a final df to hold all results
lat_list = df_unique["Latitude"].tolist()
lon_list = df_unique["Longitude"].tolist()
name_list = df_unique["Name"].tolist()
n_ocp_list = df_unique["Number_occupations"].tolist()
last_ocp_list = df_unique["Time"].tolist()

df_aux = df3.copy()
df_aux.insert(2, "Latitude", lat_list)
df_aux.insert(3, "Longitude", lon_list)
df_aux.insert(4, "Name", name_list)
df_aux.insert(5, "Occupations", n_ocp_list)
df_aux.insert(6, "Last Occupation", last_ocp_list)
df_aux
df_final = df_aux.copy()


# ------------ # START STEP 3: CREATE A DF WITH OBSERVATORIES IN S. AMERICA

# Create a dataframe with magnetic observatories in South America (Intermagnet)
sa_data = {"Observatory": ["Huancayo", "Kourou",
                           "Pilar", "Tatuoca", "Vassouras"],
           "Latitude": [-12.0500, 5.2100, -31.4000, -1.2050, -22.4000],
           "Longitude": [-75.3300, -53.7300, -63.8800, -48.5130, -43.6500],
           "Country": ["Peru", "French Guiana", "Argentina",
                       "Brazil", "Brazil"],
           "Code": ["HUA", "KOU", "PIL", "TTB", "VSS"],
           }
sa_df = pd.DataFrame(data=sa_data)


# ------------ # START STEP 4: CREATE THE FOLIUM MAP

# Create folium map
tile_type0 = "OpenStreetMap"
map0 = folium.Map(location=[-15, -50], zoom_start=5, tiles=tile_type0)

# Create subgroups in the folium map to host all the necessary information
# Main group
fg0 = folium.FeatureGroup()

# Group 1: General information
g01 = folium.plugins.FeatureGroupSubGroup(
    fg0, name='Selected Repeat Stations: information', show=True)
for i in range(0, len(df_final)):
    html_info = popup_html(i)
    iframe = branca.element.IFrame(html=html_info, width=510, height=280)
    popup = folium.Popup(folium.Html(html_info, script=True), max_width=500)
    folium.Marker([df_final["Latitude"].iloc[i],
                   df_final["Longitude"].iloc[i]],
                  popup=popup,
                  icon=folium.Icon(icon='magnet', prefix='fa'),
                  tooltip="Magnetic Repeat Station, click me for general information").add_to(g01)


# Group 2: Selected Repeat Stations with coverage radius active
g02 = folium.plugins.FeatureGroupSubGroup(
    fg0, name="Selected Repeat Stations, show coverage radius (300 km)",
    show=False)
for i in range(0, len(df_final)):
    html = popup_html(i)
    iframe = branca.element.IFrame(html=html_info, width=510, height=280)
    popup = folium.Popup(folium.Html(html_info, script=True), max_width=500)
    folium.Marker([df_final["Latitude"].iloc[i],
                   df_final["Longitude"].iloc[i]],
                  popup=popup,
                  icon=folium.Icon(icon='magnet', prefix='fa'),
                  tooltip="Magnetic Repeat Station, click me for more information").add_to(g02)
# Add the repeat stations coverage
for index, location_info in df_final.iterrows():
    folium.Circle(
        [location_info["Latitude"], location_info["Longitude"]],
        radius=300000,
        color="black"  # ,
        #fill_color = "green"
    ).add_to(g02)


# Group 3: Time series
g03 = folium.plugins.FeatureGroupSubGroup(
    fg0, name="Selected Repeat Stations: time series (uncheck information layer)",
    show=False)
for i in range(0, len(df_final)):
    html = """
    <iframe src=\"""" + df_final['html_file'][i] + """\" width="850" height="400"  frameborder="0">
    """

    popup = folium.Popup(folium.Html(html, script=True))
    folium.Marker([df_final["Latitude"].iloc[i],
                   df_final["Longitude"].iloc[i]],
                  popup=popup,
                  tooltip=df_final["Code"].iloc[i],
                  icon=folium.Icon(icon='magnet', prefix='fa')
                  ).add_to(map0)


# Group 4: Magnetic Observatories in South America
g04 = folium.plugins.FeatureGroupSubGroup(
    fg0, name="Magnetic Observatories in South America", show=True)
for index, location_info in sa_df.iterrows():
    folium.Marker(
        [location_info["Latitude"], location_info["Longitude"]],
        icon=folium.Icon(color="black", icon="home", prefix="fa"),
        tooltip=[
            "Observatory:",
            location_info["Observatory"],
            "Latitude:",
            location_info["Latitude"],
            "Longitude",
            location_info["Longitude"],
            "Country:",
            location_info["Country"]
        ],
    ).add_to(g04)


# Add the subgroups to the main map
map0.add_child(fg0)
map0.add_child(g01)
map0.add_child(g02)
map0.add_child(g03)
map0.add_child(g04)

# Add the layer control
folium.LayerControl().add_to(map0)


# Add title to the map
loc = "Proposed magnetic repeat stations for the new Brazilian Network: use the control layer button (top right corner) to display more information"
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)
map0.get_root().html.add_child(folium.Element(title_html))


map0.save("selected_repeat_stations_folium_map.html")
