import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import os
import numpy as np

if not os.path.exists('correlation_results'):
    os.makedirs('correlation_results')

pio.renderers.default = "browser"

data = pd.read_csv('./data/Results_21Mar2022.csv')

custom_colorscale = [
    [0.0, '#003333'],
    [0.2, '#0D4D4D'],
    [0.4, '#226666'],
    [0.5, '#88CC88'],
    [0.6, '#2D882D'],
    [0.8, '#116611'],
    [1.0, '#004400']
]

columns = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid']

correlation_matrix = data[columns].corr()

diet_groups = ['fish','meat100', 'meat50', 'meat', 'vegan', 'veggie']
diet_display_names = {
    'fish': 'Fish',
    'meat50': 'Meat<50',
    'meat': '50<Meat<99',
    'meat100': 'Meat>100',
    'vegan': 'Vegan',
    'veggie': 'Veggie'
}
age_group = ['20-29','30-39','40-49','50-59','60-69','70-79']
sex = ['female','male']

frames = []

diet_overall_corr = data[columns].corr().values
frames.append(go.Frame(
    data=[go.Heatmap(
        z=diet_overall_corr,
        x=columns,
        y=columns,
        colorscale=custom_colorscale,
        colorbar=dict(
            title=dict(
                text="Correlation",
                font=dict(size=14)
            ),
            tickfont=dict(size=12)
        ),
        zmin=-1,
        zmax=1
    )],
    name="diet_overall"
))

for diet in diet_groups:
    diet_corr = data[data['diet_group'] == diet][columns].corr().values
    frames.append(go.Frame(
        data=[go.Heatmap(
            z=diet_corr,
            x=columns,
            y=columns,
            colorscale=custom_colorscale,
            colorbar=dict(
                title=dict(
                    text="Correlation",
                    font=dict(size=14)
                ),
                tickfont=dict(size=12)
            ),
            zmin=-1,
            zmax=1
        )],
        name=f"diet_{diet}"
    ))

age_overall_corr = data[columns].corr().values
frames.append(go.Frame(
    data=[go.Heatmap(
        z=age_overall_corr,
        x=columns,
        y=columns,
        colorscale=custom_colorscale,
        colorbar=dict(
            title=dict(
                text="Correlation",
                font=dict(size=14)
            ),
            tickfont=dict(size=12)
        ),
        zmin=-1,
        zmax=1
    )],
    name="age_overall"
))

for age in age_group:
    age_corr = data[data['age_group'] == age][columns].corr().values
    frames.append(go.Frame(
        data=[go.Heatmap(
            z=age_corr,
            x=columns,
            y=columns,
            colorscale=custom_colorscale,
            colorbar=dict(
                title=dict(
                    text="Correlation",
                    font=dict(size=14)
                ),
                tickfont=dict(size=12)
            ),
            zmin=-1,
            zmax=1
        )],
        name=f"age_{age}"
    ))

sex_overall_corr = data[columns].corr().values
frames.append(go.Frame(
    data=[go.Heatmap(
        z=sex_overall_corr,
        x=columns,
        y=columns,
        colorscale=custom_colorscale,
        colorbar=dict(
            title=dict(
                text="Correlation",
                font=dict(size=14)
            ),
            tickfont=dict(size=12)
        ),
        zmin=-1,
        zmax=1
    )],
    name="sex_overall"
))

for gender in sex:
    sex_corr = data[data['sex'] == gender][columns].corr().values
    frames.append(go.Frame(
        data=[go.Heatmap(
            z=sex_corr,
            x=columns,
            y=columns,
            colorscale=custom_colorscale,
            colorbar=dict(
                title=dict(
                    text="Correlation",
                    font=dict(size=14)
                ),
                tickfont=dict(size=12)
            ),
            zmin=-1,
            zmax=1
        )],
        name=f"sex_{gender}"
    ))

fig = go.Figure(
    data=[go.Heatmap(
        z=correlation_matrix.values,
        x=columns,
        y=columns,
        colorscale=custom_colorscale,
        colorbar=dict(
            title=dict(
                text="Correlation",
                font=dict(size=14)
            ),
            tickfont=dict(size=12)
        ),
        zmin=-1,
        zmax=1
    )],
    layout=go.Layout(
        title=dict(
            text="Environmental Impact Indicators Correlation Heatmap",
            font=dict(size=16)
        ),
        width=1000,
        height=800,
        updatemenus=[
            {
                'buttons': [
                    {
                        'label': 'Play',
                        'method': 'animate',
                        'args': [None, {'frame': {'duration': 1000, 'redraw': True}, 'fromcurrent': True}]
                    },
                    {
                        'label': 'Pause',
                        'method': 'animate',
                        'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate'}]
                    }
                ],
                'direction': 'left',
                'pad': {'r': 10, 't': 87},
                'showactive': False,
                'type': 'buttons',
                'x': 0.1,
                'xanchor': 'left',
                'y': 1,
                'yanchor': 'top'
            },
            {
                'buttons': [
                    {
                        'label': 'Diet Groups',
                        'method': 'animate',
                        'args': [['diet_overall']]
                    },
                    {
                        'label': 'Age Groups',
                        'method': 'animate',
                        'args': [['age_overall']]
                    },
                    {
                        'label': 'Gender',
                        'method': 'animate',
                        'args': [['sex_overall']]
                    }
                ],
                'direction': 'down',
                'pad': {'r': 10, 't': 10},
                'showactive': True,
                'x': 0.1,
                'xanchor': 'left',
                'y': 0.9,
                'yanchor': 'top'
            }
        ],
        sliders=[{
            'currentvalue': {
                'font': {'size': 20},
                'prefix': 'Current Group: ',
                'visible': True,
                'xanchor': 'center'
            },
            'pad': {'b': 10},
            'steps': [
                {
                    'args': [
                        ['diet_overall'],
                        {'frame': {'duration': 1000, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 300, 'easing': 'cubic-in-out'}}
                    ],
                    'label': 'Diet Overall',
                    'method': 'animate'
                }
            ] + [
                {
                    'args': [
                        [f"diet_{diet}"],
                        {'frame': {'duration': 1000, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 300, 'easing': 'cubic-in-out'}}
                    ],
                    'label': f"Diet-{diet_display_names[diet]}",
                    'method': 'animate'
                }
                for diet in diet_groups
            ] + [
                {
                    'args': [
                        ['age_overall'],
                        {'frame': {'duration': 1000, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 300, 'easing': 'cubic-in-out'}}
                    ],
                    'label': 'Age Overall',
                    'method': 'animate'
                }
            ] + [
                {
                    'args': [
                        [f"age_{age}"],
                        {'frame': {'duration': 1000, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 300, 'easing': 'cubic-in-out'}}
                    ],
                    'label': f"Age-{age}",
                    'method': 'animate'
                }
                for age in age_group
            ] + [
                {
                    'args': [
                        ['sex_overall'],
                        {'frame': {'duration': 1000, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 300, 'easing': 'cubic-in-out'}}
                    ],
                    'label': 'Gender Overall',
                    'method': 'animate'
                }
            ] + [
                {
                    'args': [
                        [f"sex_{gender}"],
                        {'frame': {'duration': 1000, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 300, 'easing': 'cubic-in-out'}}
                    ],
                    'label': f"Gender-{gender}",
                    'method': 'animate'
                }
                for gender in sex
            ]
        }]
    ),
    frames=frames
)

fig.write_html("heatmap.html")
pio.show(fig)

def save_correlation_matrix(corr_matrix, group_name, file_path):
    df = pd.DataFrame(corr_matrix, columns=columns, index=columns)
    df = df.round(3)
    df.to_excel(file_path)

save_correlation_matrix(diet_overall_corr, 'Diet Overall', 'correlation_results/diet_overall_correlation.xlsx')
for diet in diet_groups:
    diet_corr = data[data['diet_group'] == diet][columns].corr().values
    save_correlation_matrix(diet_corr, f'Diet-{diet_display_names[diet]}', f'correlation_results/diet_{diet}_correlation.xlsx')

save_correlation_matrix(age_overall_corr, 'Age Overall', 'correlation_results/age_overall_correlation.xlsx')
for age in age_group:
    age_corr = data[data['age_group'] == age][columns].corr().values
    save_correlation_matrix(age_corr, f'Age-{age}', f'correlation_results/age_{age}_correlation.xlsx')

save_correlation_matrix(sex_overall_corr, 'Gender Overall', 'correlation_results/gender_overall_correlation.xlsx')
for gender in sex:
    sex_corr = data[data['sex'] == gender][columns].corr().values
    save_correlation_matrix(sex_corr, f'Gender-{gender}', f'correlation_results/gender_{gender}_correlation.xlsx')

with pd.ExcelWriter('correlation_results/all_correlations.xlsx') as writer:
    pd.DataFrame(correlation_matrix, columns=columns, index=columns).round(3).to_excel(writer, sheet_name='Overall')
    
    pd.DataFrame(diet_overall_corr, columns=columns, index=columns).round(3).to_excel(writer, sheet_name='Diet_Overall')
    for diet in diet_groups:
        diet_corr = data[data['diet_group'] == diet][columns].corr()
        diet_corr.round(3).to_excel(writer, sheet_name=f'Diet_{diet[:7]}')
    
    pd.DataFrame(age_overall_corr, columns=columns, index=columns).round(3).to_excel(writer, sheet_name='Age_Overall')
    for age in age_group:
        age_corr = data[data['age_group'] == age][columns].corr()
        age_corr.round(3).to_excel(writer, sheet_name=f'Age_{age}')
    
    pd.DataFrame(sex_overall_corr, columns=columns, index=columns).round(3).to_excel(writer, sheet_name='Gender_Overall')
    for gender in sex:
        sex_corr = data[data['sex'] == gender][columns].corr()
        sex_corr.round(3).to_excel(writer, sheet_name=f'Gender_{gender}')

diet_dummies = pd.get_dummies(data['diet_group'])

diet_env_corr = pd.DataFrame()
for col in columns:
    diet_env_corr[col] = [data[col].corr(diet_dummies[diet]) for diet in diet_groups]
diet_env_corr.index = [diet_display_names[diet] for diet in diet_groups]

diet_env_fig = go.Figure(data=go.Heatmap(
    z=diet_env_corr.values,
    x=columns,
    y=diet_env_corr.index,
    colorscale=custom_colorscale,
    colorbar=dict(
        title=dict(
            text="Correlation",
            font=dict(size=14)
        ),
        tickfont=dict(size=12)
    ),
    zmin=-1,
    zmax=1
))

diet_env_fig.update_layout(
    title=dict(
        text="Correlation between Diet Types and Environmental Indicators",
        font=dict(size=16)
    ),
    width=1200,
    height=600,
    xaxis=dict(
        title="Environmental Indicators",
        tickangle=45,
        tickfont=dict(size=12)
    ),
    yaxis=dict(
        title="Diet Types",
        tickfont=dict(size=12)
    )
)

diet_env_corr.round(3).to_excel('correlation_results/diet_environmental_correlation.xlsx')

diet_env_fig.write_html("diet_environmental_heatmap.html")
diet_env_fig.show()

for col in columns:
    bar_fig = go.Figure()
    bar_fig.add_trace(go.Bar(
        x=diet_env_corr.index,
        y=diet_env_corr[col],
        marker_color=diet_env_corr[col].map(lambda x: 
            '#226666' if x < 0 else '#2D882D'),
    ))
    
    bar_fig.update_layout(
        title=dict(
            text=f"Correlation between Diet Types and {col}",
            font=dict(size=16)
        ),
        width=1000,
        height=600,
        xaxis=dict(
            title="Diet Types",
            tickangle=45,
            tickfont=dict(size=12)
        ),
        yaxis=dict(
            title="Correlation Coefficient",
            tickfont=dict(size=12),
            range=[-1, 1]
        ),
        showlegend=False
    )
    
    bar_fig.add_hline(y=0, line_dash="dash", line_color="gray")
    
    bar_fig.write_html(f"correlation_results/diet_{col}_correlation_bar.html")
    bar_fig.show()

