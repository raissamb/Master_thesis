# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:51:01 2022

author: raissa baldez

Description

Pre processing data
- Convert comma to dot to separate decimal places
- Create a code for each repeat station name
- Sort the data in alphabetical order for station name and ascending order for
time
- Mark data gaps as NaN values
- Save the result as output file

"""


# Import modules

# Paths
import mestrado_module as mm
import pandas as pd
from pathlib import Path
input_folder: Path = Path(mm.path_00_data_raw_data)
output_folder: Path = Path(mm.path_pipeline_01_data_processing)

# Files
input_file: Path = Path("Estacoes_2019.csv")
output_file: Path = Path(mm.output_01a_code_clean_data)


# Load data with Pandas
df = pd.read_csv(input_folder / input_file)

# Conversions: comma to dot and types
df["LAT"] = df["LAT"].str.replace(",", ".").astype(float)
df["LON"] = df["LON"].str.replace(",", ".").astype(float)
df["F"] = df["F"].astype(float)
df["X"] = df["X"].astype(float)

# Convert string to number then to float type
df["H"] = df["H"].str.replace(",", ".").astype(float)

# Fix station names
df["ESTACAO"] = df["ESTACAO"].replace(
    "ARAíUAI C", "ARACUAI (MG) C")
df["ESTACAO"] = df["ESTACAO"].replace(
    "VALENíA A", "VALENÇA (BA) A")
df["ESTACAO"] = df["ESTACAO"].replace(
    "CAMBUQUIRA A", "CAMBUQUIRA (MG) A")
df["ESTACAO"] = df["ESTACAO"].replace(
    "Catanduva 20189134", "CATANDUVA")

# Convert to maiuscules all station names
df["ESTACAO"] = df["ESTACAO"].str.upper()

# Sort by alphabetical order: station names
df= df.sort_values(by=["ESTACAO", "EPOCA"])

# Create a code for each station
rs_names = df["ESTACAO"].unique()

# Create a list with the code for each station
rs_codes = ["ACU", "ALE", "AFT", "ALT",
            "ALT_B", "ALT_C", "APG_A", "AMP_A",
            "AMP_B", "ARA_B", "ARA_C",
            "ARA_E", "ARA_F", "ACI_A",
            "ACI_B", "ACI_C", "ARR", "ARR_A",
            "ARR_B", "ARR_C", "ARU_A",
            "ARU_B", "ARU_C", "ATI_A",
            "BAC_A", "BAG_A", "BAL_A", "BAM_A",
            "BAM_B", "BAM_C", "BAM_D", "BAR_A",
            "BCS", "BCH_A", "BCH_B",
            "BCO_A", "BRG_B",
            "BRG_C", "BRG_D",
            "BRS_A", "BRS_B", "BRS_C",
            "BHE_A", "BHE_B",
            "BHE_C", "BHE_D",
            "BHE_E", "BHE_F",
            "BHE_G", "BCT", "BVA",
            "BJL", "BJP_A",
            "BJP_B", "BOT", "BRA_A",
            "CAC", "CAC_B", "CCO_A",
            "CIT", "CAM", "CQA_A",
            "CPS", "CGE", "CGS",
            "CAN_A", "CAP_A", "CPO_A",
            "CRI", "CVS", "CAR", "CAR_D", "CTO",
            "CTD", "CHA",
            "COD_A", "CAA", "CBA_A", "COR", "CMS", "COX_A", "CRS", "CRO",
            "CCA", "CZS", "CUI", "CTA",
            "CUR", "DIA", "DIA_D", "DVE_A", "DIV", "DIV_C", "EIR", "EPI",
            "EPI_B", "FSA", "FNA", "FRO",
            "FLO", "FMA", "FMA_B", "FOR", "FPB", "FIU", "GDN_A", "GPO", "GCO",
            "GOI", "GVS", "GVS_D",
            "GJM", "GUI", "IGA_A", "ILH", "ITA_A", "IBA", "IAM", "IAM_C",
            "IPA", "IOA_A", "ITU",
            "JAC", "JAN", "JAN_E", "JAT", "JIT", "JPA", "JUT_A", "LAG", "LDN",
            "MAC", "MCO", "MAN",
            "MNE_A", "MRA", "MRL", "MAU_A", "MDR", "MCS", "MCS_D", "MAL",
            "MSS", "MTS_A", "MDN",
            "NAT", "NSJ_A", "OIA", "PAC_A", "PAL", "PAN", "PAR", "PNB", "PSF",
            "PAT", "PMS",
            "PPI", "PET", "PIM", "PIR_A", "PIR_B", "PIR_C", "PIR_D", "PIR_E",
            "PTA", "PCS",
            "PCS_B", "PPO", "PAE", "PMO", "PNL", "PTR", "PVO", "RPA", "REC",
            "RAB", "RBO",
            "RJO", "RGE", "RLO_A", "RON", "ROR_A", "SAL", "SCC", "SCE_A",
            "SMA", "SVP", "SLI",
            "SAN", "SGL", "SBA", "SFA", "SFX_A", "SGC", "SJB_A", "SJC", "SLZ",
            "SMS", "SPO",
            "SPA", "SIN", "TAB", "TAU", "TFE", "TER", "TIR", "TRA_A", "TLS",
            "TPS_A", "UBA",
            "UBR", "UBR_F", "URU", "VAL_A", "VLT_A", "VRA_A", "VIL", "VSU",
            "VSU_A", "VIT", "VCQ",
            ]

# Compare the size of rs_names and codes
size_rs_names = len(rs_names)
size_rs_codes = len(rs_codes)

# Create a column for code
df["Code"] = 0

# Loop to fill the column
for i in range(len(rs_names)):
    df.loc[df['ESTACAO'] == rs_names[i], "Code"] = rs_codes[i]

# Create new df to check for errors in lat and long
df_check_lat = df.copy()

# Check if the LAT values are in the -90 to 90 degrees range.
# Values out of this range will be excluded
lat_values = df_check_lat["LAT"].between(-90.0, 90.0, inclusive="both")

# Add a column to the current dataframe with True or False to mark which
# values belong to the specified range
df_check_lat["lat_in_range"] = lat_values

# Count the number of outside values for latitude
lat_values_count = df_check_lat["lat_in_range"].value_counts()
# true_lat_values_count = df_check_lat["lat_in_range"].value_counts()[True]
# false_lat_values_count = df_check_lat["lat_in_range"].value_counts()[False]
# print(lat_values_count)
# print(true_lat_values_count)
# print(false_lat_values_count)
# RESULT: NO LATITUDE VALUES OUTSIDE OF RANGE

# Check LON values
df_check_lon = df_check_lat.copy()
# df_check_lon = df_check_lon.sort_values(["Lon_dd"], ascending=True)

# Check if the values are in the -180 to 180 degrees range. Values out of this
# range will be excluded
lon_values = df_check_lon["LON"].between(-180.0, 180.0, inclusive="both")

# Add a column to the current dataframe with True or False to mark which values
# belong to the specified range
df_check_lon["lon_in_range"] = lon_values

# Count the number of outside values for latitude
lon_values_count = df_check_lon["lon_in_range"].value_counts()
# true_lon_values_count = df_check_lon["lon_in_range"].value_counts()[True]
# false_lon_values_count = df_check_lon["lon_in_range"].value_counts()[False]
# print(true_lon_values_count)
# print(false_lon_values_count)

# Get the index for the rows where the longitude values are out of range
lon_out_range_index = df_check_lon[df_check_lon["lon_in_range"] == False].index

# RESULT: four longitude values were out of range. They were elimated from
# further analysis.

# Create new df without the wrong longitude values
df_check_lon_result = df_check_lon.copy()

# Delete these row indexes from dataFrame
df_check_lon_result = df_check_lon.drop(lon_out_range_index, inplace=False)


# Create final df
df_final = df_check_lon_result.copy()
df_final = df_final.reset_index().drop(columns=["index"])
df_final = df_final.drop(columns=["Indice"])

# Check if there is any duplicate rows
bool_series = df_final.duplicated()
print(bool_series.value_counts())

# Keep the first occurence of the duplicated row
df_final = df_final.drop_duplicates()

# Organize
df_final = df_final.loc[:, ["ESTACAO", "Code", "LAT",
                            "LON", "EPOCA", "D", "I", "H", "F", "X", "Y", "Z"]]
df_final = df_final.rename(
    columns={'ESTACAO': "Name", "LAT": "Latitude", "LON": "Longitude",
             "EPOCA": "Time"})

# Save it
df_final.to_csv(output_folder / output_file, na_rep="NaN", index=False)
