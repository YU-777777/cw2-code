'''
This code is used to generate a age and gender type correlation graph
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

colors = ['#0D4D4D', '#88CC88', '#004400']
n_bins = 100
custom_cmap = LinearSegmentedColormap.from_list('custom', colors, N=n_bins)

demographic_data = {
    'mean_ghgs': [-0.048, 0.048, -0.015, -0.020, -0.001, 0.002, 0.003, 0.031],
    'mean_land': [-0.028, 0.028, -0.028, -0.031, 0.001, 0.008, 0.012, 0.038],
    'mean_watscar': [-0.051, 0.051, -0.013, -0.009, -0.031, -0.021, 0.021, 0.053],
    'mean_eut': [-0.071, 0.071, 0.032, 0.000, -0.007, -0.016, -0.016, 0.007],
    'mean_ghgs_ch4': [-0.026, 0.026, -0.021, -0.030, -0.005, 0.002, 0.010, 0.043],
    'mean_ghgs_n2o': [-0.049, 0.049, -0.006, -0.019, -0.006, -0.004, 0.003, 0.032],
    'mean_bio': [-0.031, 0.031, -0.010, -0.009, 0.002, -0.006, 0.001, 0.022],
    'mean_watuse': [-0.032, 0.032, 0.010, 0.003, -0.031, -0.020, 0.007, 0.030],
    'mean_acid': [-0.049, 0.049, -0.004, -0.016, -0.008, -0.002, 0.007, 0.023],
}

demographic_index = ['female', 'male', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']

df_demographic = pd.DataFrame(demographic_data, index=demographic_index)

plt.figure(figsize=(12, 8))
sns.heatmap(df_demographic, annot=True, cmap=custom_cmap, center=0, fmt=".2f", linewidths=0.5)

plt.title("Correlation Matrix between Demographics and Environmental Indicators", fontsize=16)

plt.show()
