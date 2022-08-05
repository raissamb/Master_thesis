# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# MODULES USED IN THIS MODULE
import numpy as np

# VARIABLES
## Observatories location according to Intermagnet in decimal degrees
TTB_lat = -1.205
TTB_lon = -48.513
VSS_lat = -22.400
VSS_lon = -43.650


# DATA FOLDER PATHS
path_00_data_manual = "../00_data/manual/"
path_brazil_shapefile = "../00_data/external/shapefiles_data/brazil/"
path_south_america_shapefile = "../00_data/external/shapefiles_data/south_america/"


# PIPELINE FOLDER PATHS
path_pipeline_01_data_processing = "../02_pipeline/01_data_processing/"
path_pipeline_02_icgem_file = "../02_pipeline/02_icgem_input_file_creation/"
path_pipeline_03_rs_database_creation = "../02_pipeline/03_repeat_stations_database_creation/"
path_pipeline_04_igrf_calc = "../02_pipeline/04_igrf_calculation/"
path_pipeline_04_igrf_calc_figures = "../02_pipeline/04_igrf_calculation/figures_comparison_x_y_z"
path_pipeline_05_rank_n_occupations = "../02_pipeline/05_rank_repeat_stations_n_occupations/"
path_pipeline_06a_temporal_series_n12 = "../02_pipeline/06_rank_repeat_stations_temporal_series/temp_series_n12"
path_pipeline_06b_temporal_series_n10 = "../02_pipeline/06_rank_repeat_stations_temporal_series/temp_series_n10"
path_pipeline_06c_temporal_series_n08 = "../02_pipeline/06_rank_repeat_stations_temporal_series/temp_series_n08"
path_pipeline_06d_temporal_series_n06 = "../02_pipeline/06_rank_repeat_stations_temporal_series/temp_series_n06"
path_pipeline_06e_temporal_series_n03 = "../02_pipeline/06_rank_repeat_stations_temporal_series/temp_series_n03"
path_pipeline_06f_temporal_series_n01 = "../02_pipeline/06_rank_repeat_stations_temporal_series/temp_series_n01"
path_pipeline_07_select_rs_geo_distribution = "../02_pipeline/07_select_repeat_stations_geo_distribution/"
path_pipeline_08_model_one = "../02_pipeline/08_rs_network_model_one/"
path_pipeline_09_model_two = "../02_pipeline/09_rs_network_model_two/"
path_pipeline_10_model_three = "../02_pipeline/10_rs_network_model_three/"
path_pipeline_11_quick_vis = "../02_pipeline/quick_visualization/"

path_pipeline_extra_01a_plot_stats = "../02_pipeline/extra_01_plots/rs_statistics/"
path_pipeline_extra_01b_plot_maps = "../02_pipeline/extra_01_plots/rs_maps/"


#path_pipeline_6a_plot_rs = "../02_pipeline/06_plot_info/6a_plot_repeat_stations/"
#path_pipeline_6b_plot_rs_igrf = "../02_pipeline/06_plot_info/6b_plot_repeat_stations_igrf/"
#path_pipeline_6c_plot_rs_stats = "../02_pipeline/06_plot_info/6c_plot_repeat_stations_stats/"
#path_pipeline_6d_plot_rs_interactive = "../02_pipeline/06_plot_info/6d_plot_repeat_stations_interactive/"
#path_pipeline_07_calculate_reference_distances = "../02_pipeline/07_calculate_reference_distances/"


# FILES
brazil_shapefile = "BR_UF_2020.shp"
south_america_shapefile = "South_America.shp"
unfiltered_data = "unfiltered_stations_data_manual.csv"
output_1a_code_filtered_data = "1a_filtered_repeat_stations_data.csv"
output_1b_code_processed_data = "1b_processed_repeat_stations_data.csv"
output_2_code_icgem_file = "2_lat_lon_input_icgem.csv"
output_3_code_ocp_list = "3_list_repeat_stations_occupations.csv"
output_3_code_rs_database = "3_repeat_stations_database.csv"

output_4a_code_igrf_input_file = "4a_igrf_input_alt_geoid.txt"
output_4b_geomag_file = "4b_igrf_output_alt_geoid.txt"
output_4c_code_igrf_database = "4c_igrf_database_alt_geoid.csv"
output_4d_code_rs_igrf_database = "4d_repeat_stations_igrf_database_alt_geoid.csv"
output_4d_code_error_database = "4d_repeat_stations_igrf_errors_alt_geoid.csv"
output_4e_code_complete_rs_igrf_database = "4e_repeat_stations_igrf_rmse_database_alt_geoid.csv"

output_5a_code_groups_ocp_df = "5a_number_ocp_by_groups.csv"
output_5a_code_database_n_12 = "5a_rs_ocp_high_n_12_database.csv"
output_5a_code_database_n_10 = "5a_rs_ocp_high_n_10_database.csv"
output_5a_code_database_n_08 = "5a_rs_ocp_high_n_08_database.csv"
output_5a_code_database_n_06 = "5a_rs_ocp_high_n_06_database.csv"
output_5a_code_database_n_03 = "5a_rs_ocp_high_n_03_database.csv"
output_5a_code_database_n_01 = "5a_rs_ocp_high_n_01_database.csv"
output_5a_code_folium_file_n_12 = "5a_n_12_folium_plot.csv"
output_5a_code_folium_file_n_10 = "5a_n_10_folium_plot.csv"
output_5a_code_folium_file_n_08 = "5a_n_08_folium_plot.csv"
output_5a_code_folium_file_n_06 = "5a_n_06_folium_plot.csv"
output_5a_code_folium_file_n_03 = "5a_n_03_folium_plot.csv"
output_5a_code_folium_file_n_01 = "5a_n_01_folium_plot.csv"

output_7a_code_selected_rs_folium = "7a_selected_repeat_stations_folium_file.csv"
output_7b_code_selected_rs_db = "7b_selected_repeat_stations_database.csv"
output_7b_code_distance_file =  "7b_selected_repeat_stations_distances.csv"
output_7b_code_selected_rs_table = "7b_selected_repeat_stations_database_table.csv"


# FUNCTIONS
def rmse(predictions, targets):
    """
    This function calculates the RMSE value of two array, one with
    the prediction and one with the observations values
    """
    return np.sqrt(((predictions - targets) ** 2).mean())




def dms2dd_neg(degrees, minutes, seconds):
    """
    This function converts degree, minute and second to decimal degrees. 
    It assumes that the degree is negative.
    """

    decimal_degrees = - (seconds/3600.0) - (minutes/60.0) + degrees
        
    return decimal_degrees


def dms2dd_pos(degrees, minutes, seconds):
    """
    This function converts degree, minute and second to decimal degrees. 
    It assumes that the degree is positive.
    """

    decimal_degrees = (seconds/3600.0) + (minutes/60.0) + degrees
        
    return decimal_degrees
   
    
def dms2dd(signal, degrees, minutes, seconds):
    if signal == "Positivo":
        decimal_degrees = (seconds/3600.0) + (minutes/60.0) + degrees
        
    else:
        
        decimal_degrees = - (seconds/3600.0) - (minutes/60.0) + degrees
    return decimal_degrees
        
        
def haversine_array(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the Earth (specified in decimal degrees) using arrays
    as inputs
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers
    return c * r

