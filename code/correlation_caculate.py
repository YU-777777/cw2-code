import pandas as pd
import numpy as np

# 读取数据文件
data = pd.read_csv('2.csv')

# 环境影响指标
columns = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid']

# 饮食组及其显示名称
diet_groups = ['fish','meat100', 'meat50', 'meat', 'vegan', 'veggie']
diet_display_names = {
    'fish': 'Fish',
    'meat50': 'Meat<50',
    'meat': '50<Meat<99',
    'meat100': 'Meat>100',
    'vegan': 'Vegan',
    'veggie': 'Veggie'
}

# 创建饮食类型的哑变量
diet_dummies = pd.get_dummies(data['diet_group'])

# 创建性别和年龄组的哑变量
sex_dummies = pd.get_dummies(data['sex'])
age_dummies = pd.get_dummies(data['age_group'])

# 计算饮食类型（哑变量）与环境指标之间的相关性
diet_env_corr = pd.DataFrame()
for col in columns:
    diet_env_corr[col] = [data[col].corr(diet_dummies[diet]) for diet in diet_groups]
diet_env_corr.index = [diet_display_names[diet] for diet in diet_groups]

# 分析性别和年龄组（哑变量）与环境指标的相关性
demographic_corr = pd.DataFrame()
for col in columns:
    # 获取性别的所有类别相关性
    sex_correlations = [data[col].corr(sex_dummies[sex_cat]) for sex_cat in sex_dummies.columns]
    # 获取年龄组的所有类别相关性
    age_correlations = [data[col].corr(age_dummies[age_cat]) for age_cat in age_dummies.columns]
    # 合并所有相关性
    demographic_corr[col] = sex_correlations + age_correlations

# 设置行索引为所有类别名称
demographic_corr.index = list(sex_dummies.columns) + list(age_dummies.columns)

# 打印相关性矩阵
print("\n饮食类型与环境指标的相关性矩阵:")
print(diet_env_corr.round(3))
print("\n人口统计特征（性别和年龄组）与环境指标的相关性矩阵:")
print(demographic_corr.round(3)) 