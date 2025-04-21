"""
This code is used to generate a diet type correlation graph
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

colors = ['#0D4D4D', '#88CC88', '#004400']
n_bins = 100
custom_cmap = LinearSegmentedColormap.from_list('custom', colors, N=n_bins)

data = {
    'mean_ghgs': [-0.151, 0.760, -0.054, 0.200, -0.515, -0.240],
    'mean_land': [-0.192, 0.683, -0.099, 0.126, -0.311, -0.207],
    'mean_watscar': [0.019, 0.324, -0.039, 0.075, -0.234, -0.144],
    'mean_eut': [-0.124, 0.756, -0.023, 0.244, -0.564, -0.289],
    'mean_ghgs_ch4': [-0.161, 0.752, -0.027, 0.213, -0.570, -0.208],
    'mean_ghgs_n2o': [-0.200, 0.789, -0.083, 0.194, -0.435, -0.266],
    'mean_bio': [-0.049, 0.415, -0.006, 0.125, -0.423, -0.061],
    'mean_watuse': [0.083, 0.330, 0.060, 0.174, -0.407, -0.239],
    'mean_acid': [-0.133, 0.739, -0.015, 0.248, -0.613, -0.226],
}

index = ['Fish', 'Meat>100', 'Meat<50', '50<Meat<99', 'Vegan', 'Veggie']

df = pd.DataFrame(data, index=index)

plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap=custom_cmap, center=0, fmt=".2f", linewidths=0.5)

plt.title("Correlation Matrix between Diet Types and Environmental Indicators", fontsize=16)

plt.show()
