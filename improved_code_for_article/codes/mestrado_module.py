# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# MODULES USED IN THIS MODULE
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------- VARIABLES ---------------------------------------
# Observatories location according to Intermagnet in decimal degrees
TTB_lat = -1.205
TTB_lon = -48.513
VSS_lat = -22.400
VSS_lon = -43.650

# ---------------------------- SHAPEFILES -------------------------------------
brazil_shapefile = "BR_UF_2020.shp"
south_america_shapefile = "South_America.shp"

# --------------------------- DATA FOLDER PATHS -------------------------------
path_00_data_manual = "../00_data/manual/"
path_00_data_raw_data = "../00_data/raw_data/"
path_00_data_brazil_shapefile = "../00_data/shapefiles_data/brazil/"
path_00_data_south_america_shapefile = "../00_data/shapefiles_data/" \
    "south_america/"


# --------------------------- PIPELINE FOLDER PATHS ---------------------------
path_pipeline_01_data_processing = "../02_pipeline/01_data_processing/"

path_pipeline_02_icgem_file = "../02_pipeline/02_icgem_input_file_creation/"

path_pipeline_03_rs_database_creation = "../02_pipeline/" \
    "03_repeat_stations_database_creation/"

path_pipeline_04_igrf_calc = "../02_pipeline/04_igrf_calculation/"


path_pipeline_05_selection_process = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"
path_pipeline_05a_selection_process_plot_distrib = "../02_pipeline/"\
    "05_repeat_stations_selection_process/plot_distribution"
path_pipeline_05b_selection_process_ocp_groups = "../02_pipeline/"\
    "05_repeat_stations_selection_process/occupation_groups"

path_pipeline_05c_plot_temporal_series_g1 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_temporal_series_by_occupation_groups/temp_series_g1"
path_pipeline_05c_plot_temporal_series_g2 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_temporal_series_by_occupation_groups/temp_series_g2"
path_pipeline_05c_plot_temporal_series_g3 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_temporal_series_by_occupation_groups/temp_series_g3"
path_pipeline_05c_plot_temporal_series_g4 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_temporal_series_by_occupation_groups/temp_series_g4"
path_pipeline_05c_plot_temporal_series_g5 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_temporal_series_by_occupation_groups/temp_series_g5"
path_pipeline_05c_plot_temporal_series_g6 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_temporal_series_by_occupation_groups/temp_series_g6"
path_pipeline_05c_plot_temporal_series_g7 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_temporal_series_by_occupation_groups/temp_series_g7"

path_pipeline_05d_rmse_g1 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_rmse_by_occupation_groups/rmse_g1"
path_pipeline_05d_rmse_g2 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_rmse_by_occupation_groups/rmse_g2"
path_pipeline_05d_rmse_g3 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_rmse_by_occupation_groups/rmse_g3"
path_pipeline_05d_rmse_g4 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_rmse_by_occupation_groups/rmse_g4"
path_pipeline_05d_rmse_g5 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_rmse_by_occupation_groups/rmse_g5"
path_pipeline_05d_rmse_g6 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_rmse_by_occupation_groups/rmse_g6"
path_pipeline_05d_rmse_g7 = "../02_pipeline/"\
    "05_repeat_stations_selection_process/"\
    "plot_rmse_by_occupation_groups/rmse_g7"

path_pipeline_05e_selection = "../02_pipeline/"\
    "05_repeat_stations_selection_process/select_repeat_stations"


path_pipeline_08_model_one = "../02_pipeline/08_rs_network_model_one/"
path_pipeline_09_model_two = "../02_pipeline/09_rs_network_model_two/"
path_pipeline_10_model_three = "../02_pipeline/10_rs_network_model_three/"
path_pipeline_11_quick_vis = "../02_pipeline/quick_visualization/"


# --------------------------- OUTPUT FILES ------------------------------------
output_01a_code_clean_data = "01a_pre_processed_repeat_station_data.csv"
output_01b_code_processed_data = "01b_processed_repeat_stations_data.csv"

output_02_code_icgem_file = "02_lat_lon_input_icgem.csv"

output_03_code_ocp_list = "03_list_repeat_stations_occupations.csv"
output_03_code_rs_database = "03_repeat_stations_database.csv"

output_04a_code_igrf_input_file = "04a_igrf_input_alt_geoid.txt"
output_04b_geomag_file = "04b_igrf_output_alt_geoid.txt"
output_04c_code_igrf_database = "04c_igrf_database_alt_geoid.csv"
output_04d_code_rs_igrf_database = \
    "04d_repeat_stations_igrf_database_alt_geoid.csv"

# Distribution files
output_05a_code_fig_ocp_distrib_sts = \
    "05a_distribution_occupations_station.png"
output_05a_code_fig_sts_distrib_region = \
    "05a_distribution_region_station.png"
output_05a_code_fig_ocp_distrib_region = \
    "05a_distribution_region_occupation.png"

output_05a_code_fig_sts_distrib_states_n = \
    "05a_distribution_states_north_station.png"
output_05a_code_fig_sts_distrib_states_ne = \
    "05a_distribution_states_northeast_station.png"
output_05a_code_fig_sts_distrib_states_co = \
    "05a_distribution_states_centroeste_station.png"
output_05a_code_fig_sts_distrib_states_se = \
    "05a_distribution_states_southeast_station.png"
output_05a_code_fig_sts_distrib_states_s = \
    "05a_distribution_states_south_station.png"

output_05a_code_fig_ocp_distrib_states_n = \
    "05a_distribution_states_north_occupation.png"
output_05a_code_fig_ocp_distrib_states_ne = \
    "05a_distribution_states_northeast_occupation.png"
output_05a_code_fig_ocp_distrib_states_co = \
    "05a_distribution_states_centroeste_occupation.png"
output_05a_code_fig_ocp_distrib_states_se = \
    "05a_distribution_states_southeast_occupation.png"
output_05a_code_fig_ocp_distrib_states_s = \
    "05a_distribution_states_south_occupation.png"

output_05a_code_fig_geo_distrib = "05a_distribution_geographical_map.png"

# Occupation groups files
output_05b_code_database_g1 = "05b_rs_ocp_database_g1.csv"
output_05b_code_database_g2 = "05b_rs_ocp_database_g2.csv"
output_05b_code_database_g3 = "05b_rs_ocp_database_g3.csv"
output_05b_code_database_g4 = "05b_rs_ocp_database_g4.csv"
output_05b_code_database_g5 = "05b_rs_ocp_database_g5.csv"
output_05b_code_database_g6 = "05b_rs_ocp_database_g6.csv"
output_05b_code_database_g7 = "05b_rs_ocp_database_g7.csv"
output_05b_code_folium_file_g1 = "05b_folium_plot_g1.csv"
output_05b_code_folium_file_g2 = "05b_folium_plot_g2.csv"
output_05b_code_folium_file_g3 = "05b_folium_plot_g3.csv"
output_05b_code_folium_file_g4 = "05b_folium_plot_g4.csv"
output_05b_code_folium_file_g5 = "05b_folium_plot_g5.csv"
output_05b_code_folium_file_g6 = "05b_folium_plot_g6.csv"
output_05b_code_folium_file_g7 = "05b_folium_plot_g7.csv"

output_05e_code_selected_rs_database= "05e_selected_repeat_stations_database.csv"


#output_7b_code_selected_rs_db = "7b_selected_repeat_stations_database.csv"
#output_7b_code_distance_file = "7b_selected_repeat_stations_distances.csv"
#output_7b_code_selected_rs_table = "7b_selected_repeat_stations_database_table.csv"


# ---------------------------- FUNCTIONS --------------------------------------
def calculate_x_comp_mag_field(total_field_nT, inc_ddegreee, dec_ddegree):
    """
    This function calculates the X component of the magnetic field.

    Parameters
    ----------
    total_field_nT : array of values
        total field values in nanoTeslas
     inc_ddegreee : array of values
         inclination values in decimal degree.
    dec_ddegree : array of values
        declination values in decimal degree.

    Returns
    -------
    x_comp_nt : array of values
        x component in nanoTeslas

    """
    # First convert declination and inclination from degree to radian
    dec_radian = dec_ddegree.apply(np.radians)
    inc_radian = inc_ddegreee.apply(np.radians)
    # Calculate X
    x_comp_nT = total_field_nT * \
        inc_radian.apply(np.cos) * dec_radian.apply(np.cos)
    return x_comp_nT


def calculate_y_comp_mag_field(total_field_nT, inc_ddegreee, dec_ddegree):
    """
    This function calculates the Y component of the magnetic field.

    Parameters
    ----------
    total_field_nT : array of values
        total field values in nanoTeslas
     inc_ddegreee : array of values
         inclination values in decimal degree.
    dec_ddegree : array of values
        declination values in decimal degree.

    Returns
    -------
    y_comp_nt : array of values
        y component in nanoTeslas

    """
    # First convert declination and inclination from degree to radian
    dec_radian = dec_ddegree.apply(np.radians)
    inc_radian = inc_ddegreee.apply(np.radians)
    # Calculate X
    y_comp_nT = total_field_nT * \
        inc_radian.apply(np.cos) * dec_radian.apply(np.sin)
    return y_comp_nT


def calculate_z_comp_mag_field(total_field_nT, inc_ddegreee):
    """
    This function calculates the Z component of the magnetic field.

    Parameters
    ----------
    total_field_nT : array of values
        total field values in nanoTeslas
     inc_ddegreee : array of values
         inclination values in decimal degree.

    Returns
    -------
    z_comp_nt : array of values
        z component in nanoTeslas

    """
    # First convert declination and inclination from degree to radian
    inc_radian = inc_ddegreee.apply(np.radians)
    # Calculate X
    z_comp_nT = total_field_nT * inc_radian.apply(np.sin)
    return z_comp_nT


def rmse(predictions, targets):
    """
    This function calculates the RMSE value of two array, one with
    the prediction and one with the observations values.

    Parameters
    ----------
    predictions : array of values
        array with the predicted values
    targets : array of values
        array with the observation values

    Returns
    -------
    None.

    """

    return np.sqrt(((predictions - targets) ** 2).mean())


def haversine_array(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points on the Earth
    (specified in decimal degrees) using arrays as inputs.

    Parameters
    ----------
    lon1 : array of values
        longitude of the first location
    lat1 : array of values
        latitude of the first location
    lon2 : array of values
        longitude of the second location
    lat2 : array of values
        latitude of the second location

    Returns
    -------
    distances : array of values
        array of values containing the distances between each par of longitudes
        and latitudes of the locations 1 e 2

    """

    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # Radius of earth in kilometers
    distances = c * r
    return distances


def create_occupation_groups(df, g_start, g_end, output_folder, g_filename,
                             folium_filename):
    """
    This is a function to create the occupation groups

    Parameters
    ----------
    df : dataframe
        The dataframe with the information about the repeat stations.
    g_start : integer
        The minimum number of occupations for a group.
    g_end : integer
        The maximum number of occupations for a group.
    output_folder : pathlib variable
        The pathlib variable that contains the path to the output folder
    g_filename : pathlib variable
        The pathlib variable that contains the name of the output file of the
        dataframe for the created group
    folium_filename : pathlib variable
        The pathlib variable that contains the name of the output file to be
        plotted using folium

    Returns
    -------
    None.

    """
    df_aux = df.copy()
    df_group = df_aux[df_aux["Number_occupations"].between(g_start, g_end)]
    df_group.to_csv(output_folder / g_filename, index=False, na_rep="NaN")
    # folium
    df_folium = df_group.drop_duplicates(subset="Code",
                                         keep="last",
                                         )
    df_folium.to_csv(output_folder / folium_filename, index=False,
                     na_rep="NaN")
    return


def create_list_station_codes(df):
    """
    This function creates a list of unique values of repeat station codes
    given by a input dataframe.

    Parameters
    ----------
    df : dataframe
        Dataframe containing information about a occupation group

    Returns
    -------
    list_station_codes : TYPE
        DESCRIPTION.

    """
    df_aux = df.copy()
    df_unique = df_aux.drop_duplicates(subset="Code",
                                       keep="last"
                                       )
    list_station_codes = df_unique["Code"].unique()
    return list_station_codes


def plot_total_field(list_stations_group, df, output_folder):
    """
    This function plots the Total Field component of the repeat station
    and IGRF data.

    Parameters
    ----------
    list_stations_group : array of object
        It contains a list of the codes used for each station in the group
    df : dataframe
        It is the dataframe of the occupation group
    output_folder : windowspath
        Variable that contains the path to the output folder using pathlib
        package.

    Returns
    -------
    None.

    """
    for i in list_stations_group:
        station_code = i

        # Define dataframe for each station
        df_aux = df.copy()
        df2 = df_aux[df_aux["Code"] == station_code]
        time = df2["Time"]

        # Field info for plot
        f_orig = df2["F"]
        f_igrf = df2["IGRF_F_nT"]
        fig_f = station_code + "_IGRF" + "_Total_Field" + ".png"
        fig, ax = plt.subplots()
        # Plot station
        ax.plot(time, f_orig,
                marker="o",
                color="blue",
                label="Station original value",
                linestyle='-')
        # Plot IGRF
        ax.plot(time, f_igrf,
                marker="d",
                color="green",
                label="IGRF13",
                linestyle="-.")
        # ax1.fill_between(time, f_orig, f_igrf, color="purple", alpha=0.3)
        # Details
        ax.set_xlabel("Time (dy)", fontsize=14)
        ax.set_ylabel("Total Field (nT)", fontsize=14)
        ax.set_title(f"{station_code}", fontsize=16)
        ax.tick_params(axis="both", labelsize=14)
        ax.legend(loc="best")
        plt.savefig(output_folder / fig_f,
                    dpi=300,
                    bbox_inches="tight")
        plt.close(fig)


def plot_h_field(list_stations_group, df, output_folder):
    """
    This function plots the Horizontal Field component of the repeat station
    and IGRF data.

    Parameters
    ----------
    list_stations_group : array of object
        It contains a list of the codes used for each station in the group
    df : dataframe
        It is the dataframe of the occupation group
    output_folder : windowspath
        Variable that contains the path to the output folder using pathlib
        package.

    Returns
    -------
    None.

    """
    for i in list_stations_group:
        station_code = i

        # Define dataframe for each station
        df_aux = df.copy()
        df2 = df_aux[df_aux["Code"] == station_code]
        time = df2["Time"]

        # Field info for plot
        h_orig = df2["H"]
        h_igrf = df2["IGRF_H_nT"]
        fig_h = station_code + "_IGRF" + "_H_Field" + ".png"
        fig, ax = plt.subplots()
        # Plot station
        ax.plot(time, h_orig,
                marker="o",
                color="blue",
                label="Station original value",
                linestyle='-')
        # Plot IGRF
        ax.plot(time, h_igrf,
                marker="d",
                color="green",
                label="IGRF13",
                linestyle="-.")
        # ax1.fill_between(time, f_orig, f_igrf, color="purple", alpha=0.3)
        # Details
        ax.set_xlabel("Time (dy)", fontsize=14)
        ax.set_ylabel("H Field (nT)", fontsize=14)
        ax.set_title(f"{station_code}", fontsize=16)
        ax.tick_params(axis="both", labelsize=14)
        ax.legend(loc="best")
        plt.savefig(output_folder / fig_h,
                    dpi=300,
                    bbox_inches="tight")
        plt.close(fig)


def plot_x_field(list_stations_group, df, output_folder):
    """
    This function plots the X Field component of the repeat station original
    value, the calculated one and the IGRF data.

    Parameters
    ----------
    list_stations_group : array of object
        It contains a list of the codes used for each station in the group
    df : dataframe
        It is the dataframe of the occupation group
    output_folder : windowspath
        Variable that contains the path to the output folder using pathlib
        package.

    Returns
    -------
    None.

    """
    for i in list_stations_group:
        station_code = i

        # Define dataframe for each station
        df_aux = df.copy()
        df2 = df_aux[df_aux["Code"] == station_code]
        time = df2["Time"]

        # Field info for plot
        x_orig = df2["X"]
        x_calc = df2["Calculated_X"]
        x_igrf = df2["IGRF_X_nT"]
        fig_x = station_code + "_IGRF" + "_X_Field" + ".png"
        fig, ax = plt.subplots()
        # Plot station
        ax.plot(time, x_orig,
                marker="o",
                color="blue",
                label="Station original value",
                linestyle='-')
        # Plot Calculated
        ax.plot(time, x_calc,
                marker="+",
                color="red",
                label="Station calculated value",
                linestyle="--")
        # Plot IGRF
        ax.plot(time, x_igrf,
                marker="d",
                color="green",
                label="IGRF13",
                linestyle="-.")
        # ax1.fill_between(time, f_orig, f_igrf, color="purple", alpha=0.3)
        # Details
        ax.set_xlabel("Time (dy)", fontsize=14)
        ax.set_ylabel("X Field (nT)", fontsize=14)
        ax.set_title(f"{station_code}", fontsize=16)
        ax.tick_params(axis="both", labelsize=14)
        ax.legend(loc="best")
        plt.savefig(output_folder / fig_x,
                    dpi=300,
                    bbox_inches="tight")
        plt.close(fig)


def plot_y_field(list_stations_group, df, output_folder):
    """
    This function plots the Y Field component of the repeat station original
    value, the calculated one and the IGRF data.

    Parameters
    ----------
    list_stations_group : array of object
        It contains a list of the codes used for each station in the group
    df : dataframe
        It is the dataframe of the occupation group
    output_folder : windowspath
        Variable that contains the path to the output folder using pathlib
        package.

    Returns
    -------
    None.

    """
    for i in list_stations_group:
        station_code = i

        # Define dataframe for each station
        df_aux = df.copy()
        df2 = df_aux[df_aux["Code"] == station_code]
        time = df2["Time"]

        # F field info for plot
        y_orig = df2["Y"]
        y_calc = df2["Calculated_Y"]
        y_igrf = df2["IGRF_Y_nT"]
        fig_y = station_code + "_IGRF" + "_Y_Field" + ".png"
        fig, ax = plt.subplots()
        # Plot F station
        ax.plot(time, y_orig,
                marker="o",
                color="blue",
                label="Station original value",
                linestyle='-')
        # Plot Calculated
        ax.plot(time, y_calc,
                marker="+",
                color="red",
                label="Station calculated value",
                linestyle="--")
        # Plot F IGRF
        ax.plot(time, y_igrf,
                marker="d",
                color="green",
                label="IGRF13",
                linestyle="-.")
        # ax1.fill_between(time, f_orig, f_igrf, color="purple", alpha=0.3)
        # Details
        ax.set_xlabel("Time (dy)", fontsize=14)
        ax.set_ylabel("Total Field (nT)", fontsize=14)
        ax.set_title(f"{station_code}", fontsize=16)
        ax.tick_params(axis="both", labelsize=14)
        ax.legend(loc="best")
        plt.savefig(output_folder / fig_y,
                    dpi=300,
                    bbox_inches="tight")
        plt.close(fig)


def plot_z_field(list_stations_group, df, output_folder):
    """
    This function plots the Z Field component of the repeat station original
    value, the calculated one and the IGRF data.

    Parameters
    ----------
    list_stations_group : array of object
        It contains a list of the codes used for each station in the group
    df : dataframe
        It is the dataframe of the occupation group
    output_folder : windowspath
        Variable that contains the path to the output folder using pathlib
        package.

    Returns
    -------
    None.

    """
    for i in list_stations_group:
        station_code = i

        # Define dataframe for each station
        df_aux = df.copy()
        df2 = df_aux[df_aux["Code"] == station_code]
        time = df2["Time"]

        # F field info for plot
        z_orig = df2["Z"]
        z_calc = df2["Calculated_Z"]
        z_igrf = df2["IGRF_Z_nT"]
        fig_z = station_code + "_IGRF" + "_Z_Field" + ".png"
        fig, ax = plt.subplots()
        # Plot F station
        ax.plot(time, z_orig,
                marker="o",
                color="blue",
                label="Station original value",
                linestyle='-')
        # Plot Calculated
        ax.plot(time, z_calc,
                marker="+",
                color="red",
                label="Station calculated value",
                linestyle="--")
        # Plot F IGRF
        ax.plot(time, z_igrf,
                marker="d",
                color="green",
                label="IGRF13",
                linestyle="-.")
        # ax1.fill_between(time, f_orig, f_igrf, color="purple", alpha=0.3)
        # Details
        ax.set_xlabel("Time (dy)", fontsize=14)
        ax.set_ylabel("Z Field (nT)", fontsize=14)
        ax.set_title(f"{station_code}", fontsize=16)
        ax.tick_params(axis="both", labelsize=14)
        ax.legend(loc="best")
        plt.savefig(output_folder / fig_z,
                    dpi=300,
                    bbox_inches="tight")
        plt.close(fig)


def plot_dec_field(list_stations_group, df, output_folder):
    """
    This function plots the Declination Field component of the repeat station
    and IGRF data.

    Parameters
    ----------
    list_stations_group : array of object
        It contains a list of the codes used for each station in the group
    df : dataframe
        It is the dataframe of the occupation group
    output_folder : windowspath
        Variable that contains the path to the output folder using pathlib
        package.

    Returns
    -------
    None.

    """
    for i in list_stations_group:
        station_code = i

        # Define dataframe for each station
        df_aux = df.copy()
        df2 = df_aux[df_aux["Code"] == station_code]
        time = df2["Time"]

        # F field info for plot
        d_orig = df2["D"]
        d_igrf = df2["IGRF_D_dd"]
        fig_d = station_code + "_IGRF" + "_Declination_Field" + ".png"
        fig, ax = plt.subplots()
        # Plot F station
        ax.plot(time, d_orig,
                marker="o",
                color="blue",
                label="Station original value",
                linestyle='-')
        # Plot F IGRF
        ax.plot(time, d_igrf,
                marker="d",
                color="green",
                label="IGRF13",
                linestyle="-.")
        # ax1.fill_between(time, f_orig, f_igrf, color="purple", alpha=0.3)
        # Details
        ax.set_xlabel("Time (dy)", fontsize=14)
        ax.set_ylabel("Declination Field (nT)", fontsize=14)
        ax.set_title(f"{station_code}", fontsize=16)
        ax.tick_params(axis="both", labelsize=14)
        ax.legend(loc="best")
        plt.savefig(output_folder / fig_d,
                    dpi=300,
                    bbox_inches="tight")
        plt.close(fig)


def plot_inc_field(list_stations_group, df, output_folder):
    """
    This function plots the Inclination Field component of the repeat station
    and IGRF data.

    Parameters
    ----------
    list_stations_group : array of object
        It contains a list of the codes used for each station in the group
    df : dataframe
        It is the dataframe of the occupation group
    output_folder : windowspath
        Variable that contains the path to the output folder using pathlib
        package.

    Returns
    -------
    None.

    """
    for i in list_stations_group:
        station_code = i

        # Define dataframe for each station
        df_aux = df.copy()
        df2 = df_aux[df_aux["Code"] == station_code]
        time = df2["Time"]

        # F field info for plot
        i_orig = df2["I"]
        i_igrf = df2["IGRF_I_dd"]
        fig_i = station_code + "_IGRF" + "_Inclination_Field" + ".png"
        fig, ax = plt.subplots()
        # Plot F station
        ax.plot(time, i_orig,
                marker="o",
                color="blue",
                label="Station original value",
                linestyle='-')
        # Plot F IGRF
        ax.plot(time, i_igrf,
                marker="d",
                color="green",
                label="IGRF13",
                linestyle="-.")
        # ax1.fill_between(time, f_orig, f_igrf, color="purple", alpha=0.3)
        # Details
        ax.set_xlabel("Time (dy)", fontsize=14)
        ax.set_ylabel("Inclination Field (nT)", fontsize=14)
        ax.set_title(f"{station_code}", fontsize=16)
        ax.tick_params(axis="both", labelsize=14)
        ax.legend(loc="best")
        plt.savefig(output_folder / fig_i,
                    dpi=300,
                    bbox_inches="tight")
        plt.close(fig)


def select_station_last_occupation_year_2000(df):
    """
    This function selects the stations inside an occupation group that had
    their last occupation in the year 2000 at minimum.

    Parameters
    ----------
    df : dataframe
        dataframe of an occupation group.

    Returns
    -------
    filtered_df_aux : dataframe
        dataframe containing the repeat stations with their last occupation
        in the year 2000 at minimum.

    """
    df_aux = df.copy()
    out_limit_df_aux = df_aux[df_aux["Time"] < 2000.0]
    out_limit_df_aux_index = out_limit_df_aux.index
    filtered_df_aux = df_aux.drop(out_limit_df_aux_index)
    return filtered_df_aux


def pie_chart_values(pct, allvalues):
    """
    This function shows the percentual and actual value of the pie chart data
    inside the wedges. In summary, it creates the autocpt arguments for the
    pie chart plots.
    autopct = '%1.1f%%', this example "%1.1f%%" gives the percentage to 1
    decimal place (eg segment A occupies 13.3% of the total).

    Parameters
    ----------
    pct : TYPE
        DESCRIPTION.
    allvalues : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    absolute = np.round((pct / 100.) * np.sum(allvalues))
    return "{:.1f}%  ({:n})".format(pct, absolute)
# \n


def station_distribution_region(data, labels, colors, output_folder,
                                figure_name):
    """
    This function plots the station distribution by region

    Parameters
    ----------
    data : series
        The data corresponding to the stations distribution
    labels : series
        The states names.
    colors : TYPE
        The color pallete defined by seaborn
    output_folder : path
        The variable containing the path to the folder
    figure_name : TYPE
        The variable with the name of the figure

    Returns
    -------
    None.

    """
    # Create pie chart
    fig = plt.figure()
    patches, labels, pct_texts = plt.pie(data,
                                         labels=labels,
                                         colors=colors,
                                         radius=1,
                                         startangle=140,
                                         autopct=lambda pct: pie_chart_values(
                                             pct, data),
                                         pctdistance=0.5,
                                         rotatelabels=True,
                                         )
    for label, pct_text in zip(labels, pct_texts):
        pct_text.set_rotation(label.get_rotation())

    plt.title("Station distribution by region", pad=20)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(output_folder / figure_name, dpi=300)
    plt.close(fig)


def occupation_distribution_region(data, labels, colors, output_folder,
                                   figure_name):
    """
    This function plots the occupation distribution by region

    Parameters
    ----------
    data : series
        The data corresponding to the occupation distribution
    labels : series
        The states names.
    colors : TYPE
        The color pallete defined by seaborn
    output_folder : path
        The variable containing the path to the folder
    figure_name : TYPE
        The variable with the name of the figure

    Returns
    -------
    None.

    """
    # Create pie chart
    fig = plt.figure()
    patches, labels, pct_texts = plt.pie(data,
                                         labels=labels,
                                         colors=colors,
                                         radius=1,
                                         startangle=140,
                                         autopct=lambda pct: pie_chart_values(
                                             pct, data),
                                         pctdistance=0.5,
                                         rotatelabels=True,
                                         )
    for label, pct_text in zip(labels, pct_texts):
        pct_text.set_rotation(label.get_rotation())

    plt.title("Occupation distribution by region", pad=20)
    plt.tight_layout()
    plt.savefig(output_folder / figure_name, dpi=300)
    plt.close(fig)


def station_distribution_states_region(data, labels, colors, output_folder,
                                       figure_name, region):
    """
    This function plots the station distribution by states in a region

    Parameters
    ----------
    data : series
        The data corresponding to the stations distribution
    labels : series
        The states names.
    colors : TYPE
        The color pallete defined by seaborn
    output_folder : path
        The variable containing the path to the folder
    figure_name : TYPE
        The variable with the name of the figure
    region : TYPE
        The variable with the region name

    Returns
    -------
    None.

    """
    # Create pie chart
    fig = plt.figure()
    patches, labels, pct_texts = plt.pie(data,
                                         labels=labels,
                                         colors=colors,
                                         radius=1,
                                         startangle=140,
                                         autopct=lambda pct: pie_chart_values(
                                             pct, data),
                                         pctdistance=0.5,
                                         rotatelabels=True,
                                         )
    for label, pct_text in zip(labels, pct_texts):
        pct_text.set_rotation(label.get_rotation())
    # plt.tight_layout()
    plt.title(f"Station distribution by states ({region})", pad=20)
    plt.savefig(output_folder / figure_name, dpi=300)
    plt.close(fig)


def occupation_distribution_states_region(data, labels, colors, output_folder,
                                          figure_name, region):
    """
    This function plots the occupation distribution by states in a region

    Parameters
    ----------
    data : series
        The data corresponding to the stations distribution
    labels : series
        The states names.
    colors : TYPE
        The color pallete defined by seaborn
    output_folder : path
        The variable containing the path to the folder
    figure_name : TYPE
        The variable with the name of the figure
    region : TYPE
        The variable with the region name

    Returns
    -------
    None.

    """
    # Create pie chart
    fig = plt.figure()
    patches, labels, pct_texts = plt.pie(data,
                                         labels=labels,
                                         colors=colors,
                                         radius=1,
                                         startangle=140,
                                         autopct=lambda pct: pie_chart_values(
                                             pct, data),
                                         pctdistance=0.5,
                                         rotatelabels=True,
                                         )
    for label, pct_text in zip(labels, pct_texts):
        pct_text.set_rotation(label.get_rotation())
    # plt.tight_layout()
    plt.title(f"Occupation distribution by states ({region})", pad=20)
    plt.savefig(output_folder / figure_name, dpi=300)
    plt.close(fig)


def calculate_rmse_by_group(station_list, df_group, comp_igrf, comp_rs):
    rmse_comp = []
    df_copy = df_group.copy()

    for i in station_list:
        station_name = i
        aux_df = df_copy[df_copy["Code"] == station_name]

        # Calculate RMSE
        rmse_calc = rmse(aux_df[comp_igrf], aux_df[comp_rs])
        # append the result of each loop to the array
        rmse_comp.append(rmse_calc)

    return rmse_comp


def plot_rmse_by_group_fhdi(rmse_df, column, component, unit, group,
                            output_folder, figure_name):
    # Figure style
    sns.set_style("darkgrid")

    df_aux = rmse_df.copy()
    rmse = df_aux[column]
    station_name = df_aux["Code"]
    # Figure
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.scatter(station_name, rmse, marker="o")
    ax.set_xlabel("Station name", fontsize=14)
    ax.set_ylabel(f"{unit}", fontsize=14)
    ax.set_title(f"RMSE Value for {component}: Group {group}", fontsize=16)
    plt.legend(["Original value"])
    plt.xticks(rotation=90)
    plt.savefig(output_folder / figure_name,
                dpi=300,
                bbox_inches="tight")
    plt.grid(True)
    plt.close()


def plot_rmse_by_group_xyz(rmse_df, column_orig, column_calc, component,
                           unit, group,
                           output_folder, figure_name):
    # Figure style
    sns.set_style("darkgrid")

    df_aux = rmse_df.copy()
    rmse_orig = df_aux[column_orig]
    rmse_calc = df_aux[column_calc]
    station_name = df_aux["Code"]
    # Figure
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.scatter(station_name, rmse_orig, marker="o")
    ax.scatter(station_name, rmse_calc, marker="+")
    ax.set_xlabel("Station name", fontsize=14)
    ax.set_ylabel(f"{unit}", fontsize=14)
    ax.set_title(f"RMSE Value for {component}: Group {group}", fontsize=16)
    plt.legend(["Original value", "Calculated value"])
    plt.xticks(rotation=90)
    plt.savefig(output_folder / figure_name,
                dpi=300,
                bbox_inches="tight")
    plt.grid(True)
    plt.close()
