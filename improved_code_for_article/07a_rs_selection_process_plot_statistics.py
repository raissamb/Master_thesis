# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 20:06:16 2022

author: raissa baldez

Description

This program plots the info about the stats of the network.

"""

# Import modules
import mestrado_module as mm
import pandas as pd
import seaborn as sns
from pathlib import Path

# Repeat station data
rs_folder: Path = Path(mm.path_pipeline_03_rs_database_creation)
rs_file: Path = Path(mm.output_03_code_rs_database)

# Output
output_folder: Path = Path(mm.path_pipeline_07_selection_process)

# Figure names
sts_distrib_region: Path = Path(mm.output_07a_code_fig_sts_distrib_region)
ocp_distrib_region: Path = Path(mm.output_07a_code_fig_ocp_distrib_region)

sts_distrib_states_n: Path = Path(
    mm.output_07a_code_fig_sts_distrib_states_n)
sts_distrib_states_ne: Path = Path(
    mm.output_07a_code_fig_sts_distrib_states_ne)
sts_distrib_states_co: Path = Path(
    mm.output_07a_code_fig_sts_distrib_states_co)
sts_distrib_states_se: Path = Path(
    mm.output_07a_code_fig_sts_distrib_states_se)
sts_distrib_states_s: Path = Path(
    mm.output_07a_code_fig_sts_distrib_states_s)

ocp_distrib_states_n: Path = Path(
    mm.output_07a_code_fig_ocp_distrib_states_n)
ocp_distrib_states_ne: Path = Path(
    mm.output_07a_code_fig_ocp_distrib_states_ne)
ocp_distrib_states_co: Path = Path(
    mm.output_07a_code_fig_ocp_distrib_states_co)
ocp_distrib_states_se: Path = Path(
    mm.output_07a_code_fig_ocp_distrib_states_se)
ocp_distrib_states_s: Path = Path(
    mm.output_07a_code_fig_ocp_distrib_states_s)


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


# Plot: DISTRIBUTION BY STATES IN A REGION

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


"""
# Creating Figures
# Bar plots
sns.set(rc={"figure.dpi": 300, 'savefig.dpi': 300})
fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.barplot(x="State", y="Stations", data=info_by_states,
            color="blue", ax=ax1)

# bar_label() function to annotate over the bars
ax1.bar_label(ax1.containers[-1])
ax1.set_title("Number of stations by State", fontsize=16)
# ax.set_xlabel(fontsize=14)
# ax.set_ylabel(fontsize=14)
# plt.legend(labels=["Legend_Day1","Legend_Day2"], fontsize = 20)

"""