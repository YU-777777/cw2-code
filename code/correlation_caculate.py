import pandas as pd
import numpy as np

# Read data file
data = pd.read_csv('r.\data\Results_21Mar2022.csv')

# Environmental impact indicators
columns = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid']

# Diet groups and their display names
diet_groups = ['fish','meat100', 'meat50', 'meat', 'vegan', 'veggie']
diet_display_names = {
    'fish': 'Fish',
    'meat50': 'Meat<50',
    'meat': '50<Meat<99',
    'meat100': 'Meat>100',
    'vegan': 'Vegan',
    'veggie': 'Veggie'
}

# Create dummy variables for diet types
diet_dummies = pd.get_dummies(data['diet_group'])

# Create dummy variables for gender and age groups
sex_dummies = pd.get_dummies(data['sex'])
age_dummies = pd.get_dummies(data['age_group'])

# Calculate correlations between diet types (dummy variables) and environmental indicators
diet_env_corr = pd.DataFrame()
for col in columns:
    diet_env_corr[col] = [data[col].corr(diet_dummies[diet]) for diet in diet_groups]
diet_env_corr.index = [diet_display_names[diet] for diet in diet_groups]

# Analyze correlations between gender/age groups (dummy variables) and environmental indicators
demographic_corr = pd.DataFrame()
for col in columns:
    # Get correlations for all gender categories
    sex_correlations = [data[col].corr(sex_dummies[sex_cat]) for sex_cat in sex_dummies.columns]
    # Get correlations for all age group categories
    age_correlations = [data[col].corr(age_dummies[age_cat]) for age_cat in age_dummies.columns]
    # Combine all correlations
    demographic_corr[col] = sex_correlations + age_correlations

# Set row indices to all category names
demographic_corr.index = list(sex_dummies.columns) + list(age_dummies.columns)

# Print correlation matrices
print("\nCorrelation matrix between diet types and environmental indicators:")
print(diet_env_corr.round(3))
print("\nCorrelation matrix between demographic features (gender and age groups) and environmental indicators:")
print(demographic_corr.round(3)) 