import pandas as pd
from pathlib import Path

# headers for the dataframe that holds the data which the model will train and test on
# Pressure sensors (PS1-6)
# Motor power sensor (EPS1)
# Volume flow sensors (FS1/2)
# Temperature sensors (TS1-4)
# Vibration sensor (VS1)
# Efficiency factor (SE)
# Virtual cooling efficiency sensor (CE)
# Virtual cooling power sensor (CP)

#headers for the processed dataframe
df_headers = ['ce_mean', 'ce_median', 'ce_std', 'cp_mean', 'cp_median', 'cp_std',
           'eps1_mean', 'eps1_median', 'eps1_std', 'fs1_mean', 'fs1_median', 'fs1_std',
           'fs2_mean', 'fs2_median', 'fs2_std', 'ps1_mean', 'ps1_median', 'ps1_std',
           'ps2_mean', 'ps2_median', 'ps2_std', 'ps3_mean', 'ps3_median', 'ps3_std',
           'ps4_mean', 'ps4_median', 'ps4_std', 'ps5_mean', 'ps5_median', 'ps5_std',
           'ps6_mean', 'ps6_median', 'ps6_std', 'se_mean', 'se_median', 'se_std',
           'ts1_mean', 'ts1_median', 'ts1_std', 'ts2_mean', 'ts2_median', 'ts2_std',
           'ts3_mean', 'ts3_median', 'ts3_std', 'ts4_mean', 'ts4_median', 'ts4_std',
           'vs1_mean', 'vs1_median', 'vs1_std',"Target Values"]

#list all the files in raw_model_data for calculating mean median and standard deviation
base_dir = Path(__file__).parent.parent /"raw_model_data"
data_file_list = sorted(base_dir.glob("*.txt"))

#instantiate the dataframes needed
processed_dataframe = pd.DataFrame()
target_values_df = pd.DataFrame()

#loop over the files in raw_model_data, read each file and concat to processed_dataframe
#profile.txt hold the targets values, the second column of profile.txt is stored in target_values_df
for f in data_file_list:
    if f.name != "profile.txt":
       temp_df = pd.read_csv(f, sep='\t',header=None)
       processed_dataframe= pd.concat([processed_dataframe,temp_df.mean(axis=1),temp_df.median(axis=1),temp_df.std(axis=1)],axis=1,ignore_index=True)
    elif f.name == "profile.txt":
        target_values = pd.read_csv(f, sep='\t',header=None)
        target_values_df = target_values[1]

#processed_dataframe and target_values_df are combined into one master dataframe for the model to use
#column headers are added for readability
processed_dataframe = pd.concat([processed_dataframe,target_values_df],axis=1)
processed_dataframe.columns = df_headers

#save the data for the model to use
processed_dataframe.to_csv(base_dir.parent/"process_train_data"/"processed_data.csv",index=False)

