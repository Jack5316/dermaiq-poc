#!/usr/bin/env python3
"""
DermaIQ Business Plan Dashboard
-------------------------------
An interactive dashboard visualizing key business metrics and projections
for the DermaIQ startup using Dash.
"""

import pandas as pd
import numpy as np
import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Initialize the Dash app
app = dash.Dash(__name__, title="DermaIQ Business Analytics Dashboard")

# Define color scheme
colors = {
    'primary': '#2E86C1',
    'secondary': '#85C1E9',
    'accent': '#D4AC0D',
    'background': '#F5F5F5',
    'text': '#212F3D'
}

# Create sample data based on our business plan projections
# User Growth Data
years = [1, 2, 3, 4, 5]
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
all_quarters = []
for year in years:
    for quarter in quarters:
        all_quarters.append(f'Y{year} {quarter}')

# User growth data
user_data = pd.DataFrame({
    'Quarter': all_quarters,
    'Total Users': [
        8000, 18000, 33000, 50000,  # Year 1
        68000, 85000, 105000, 125000,  # Year 2
        150000, 180000, 215000, 250000,  # Year 3
        290000, 340000, 400000, 450000,  # Year 4
        500000, 570000, 650000, 750000,  # Year 5
    ],
    'Paying Users': [
        1200, 2880, 5445, 8500,  # Year 1
        12240, 15725, 20475, 25000,  # Year 2
        33750, 43200, 53750, 62500,  # Year 3
        87000, 102000, 120000, 135000,  # Year 4
        175000, 199500, 227500, 262500,  # Year 5
    ],
    'Conversion Rate': [
        15, 16, 16.5, 17,  # Year 1
        18, 18.5, 19.5, 20,  # Year 2
        22.5, 24, 25, 25,  # Year 3
        30, 30, 30, 30,  # Year 4
        35, 35, 35, 35,  # Year 5
    ]
})

# Financial data
financial_data = pd.DataFrame({
    'Year': years,
    'Revenue': [320000, 1250000, 5500000, 12800000, 24500000],
    'Expenses': [500000, 1125000, 3850000, 7680000, 13475000],
    'EBITDA': [-180000, 125000, 1650000, 5120000, 11025000],
    'EBITDA Margin': [-56, 10, 30, 40, 45],
    'CAC': [2.50, 3.20, 3.80, 4.20, 4.50],
    'LTV': [35.90, 48.00, 72.00, 84.00, 92.40],
    'LTV:CAC Ratio': [14.4, 15, 18.9, 20, 20.5]
})

# Revenue breakdown data
revenue_streams_y1 = pd.DataFrame({
    'Stream': ['Premium Subscriptions', 'B2B API Licensing', 'Affiliate Marketing'],
    'Amount': [243000, 32000, 45000],
    'Year': ['Year 1', 'Year 1', 'Year 1']
})

revenue_streams_y3 = pd.DataFrame({
    'Stream': ['Premium Subscriptions', 'B2B API Licensing', 'Affiliate Marketing', 'Market Research Data'],
    'Amount': [3750000, 1100000, 375000, 275000],
    'Year': ['Year 3', 'Year 3', 'Year 3', 'Year 3']
})

revenue_streams = pd.concat([revenue_streams_y1, revenue_streams_y3])

# Market research data
market_research = pd.DataFrame({
    'Finding': [
        'Struggle with ingredient labels',
        'Concerned about harmful ingredients',
        'Would use an ingredient decoding app',
        'Willing to pay for personalized recommendations',
        'Experienced negative reactions',
        'Research ingredients before purchasing',
        'Find current research time-consuming'
    ],
    'Percentage': [87, 92, 76, 68, 64, 72, 89]
})

# Competitor analysis data
competitor_data = pd.DataFrame({
    'Competitor': ['DermaIQ', 'SkinSafe', 'IngrediChecker', 'CleanBeautyAI', 'Other Apps', 'Retailer Apps'],
    'Current Market Share': [0, 28, 22, 12, 18, 20],
    'Projected Market Share (2028)': [30, 22, 18, 15, 8, 7],
    'Current User Base': [0, 320000, 250000, 140000, 210000, 230000],
    'Projected User Base': [480000, 350000, 290000, 240000, 130000, 110000]
})

# App layout
app.layout = html.Div(style={'backgroundColor': colors['background'], 'padding': '20px'}, children=[
    html.H1("DermaIQ Business Analytics Dashboard", 
            style={'textAlign': 'center', 'color': colors['primary'], 'marginBottom': '30px'}),
    
    # Tabs for different sections
    dcc.Tabs([
        # User Growth Tab
        dcc.Tab(label='User Growth', children=[
            html.Div(style={'padding': '20px'}, children=[
                html.H2("User Growth Projections", style={'color': colors['primary']}),
                html.P("Track our user acquisition, conversion rates, and growth over time."),
                
                # User growth chart
                dcc.Graph(
                    figure=make_subplots(specs=[[{"secondary_y": True}]]).add_trace(
                        go.Bar(
                            x=user_data['Quarter'],
                            y=user_data['Total Users'],
                            name='Total Users',
                            marker_color=colors['primary']
                        )
                    ).add_trace(
                        go.Bar(
                            x=user_data['Quarter'],
                            y=user_data['Paying Users'],
                            name='Paying Users',
                            marker_color=colors['accent']
                        )
                    ).add_trace(
                        go.Scatter(
                            x=user_data['Quarter'],
                            y=user_data['Conversion Rate'],
                            name='Conversion Rate (%)',
                            mode='lines+markers',
                            marker=dict(color='red'),
                            line=dict(width=2, dash='dot'),
                            yaxis='y2'
                        ),
                        secondary_y=True
                    ).update_layout(
                        title='User Growth by Quarter',
                        xaxis_title='Quarter',
                        yaxis_title='Number of Users',
                        yaxis2_title='Conversion Rate (%)',
                        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
                        barmode='group',
                        hovermode='x unified'
                    )
                ),
                
                # Year selector for detailed view
                html.Div(style={'marginTop': '30px'}, children=[
                    html.H3("Detailed Quarterly View", style={'color': colors['primary']}),
                    dcc.Dropdown(
                        id='year-selector',
                        options=[{'label': f'Year {year}', 'value': year} for year in years],
                        value=1,
                        style={'width': '200px', 'marginBottom': '20px'}
                    ),
                    dcc.Graph(id='quarterly-detail-chart')
                ])
            ])
        ]),
        
        # Financial Projections Tab
        dcc.Tab(label='Financial Projections', children=[
            html.Div(style={'padding': '20px'}, children=[
                html.H2("Financial Projections", style={'color': colors['primary']}),
                html.P("Analyze our revenue, expenses, and profitability metrics."),
                
                # Revenue and EBITDA chart
                dcc.Graph(
                    figure=make_subplots(specs=[[{"secondary_y": True}]]).add_trace(
                        go.Bar(
                            x=financial_data['Year'],
                            y=financial_data['Revenue'],
                            name='Revenue',
                            marker_color=colors['primary']
                        )
                    ).add_trace(
                        go.Bar(
                            x=financial_data['Year'],
                            y=financial_data['Expenses'],
                            name='Expenses',
                            marker_color=colors['secondary']
                        )
                    ).add_trace(
                        go.Scatter(
                            x=financial_data['Year'],
                            y=financial_data['EBITDA Margin'],
                            name='EBITDA Margin (%)',
                            mode='lines+markers',
                            marker=dict(color='green'),
                            line=dict(width=2),
                            yaxis='y2'
                        ),
                        secondary_y=True
                    ).update_layout(
                        title='Revenue, Expenses and EBITDA Margin by Year',
                        xaxis_title='Year',
                        yaxis_title='Amount (£)',
                        yaxis2_title='EBITDA Margin (%)',
                        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
                        barmode='group',
                        hovermode='x unified'
                    )
                ),
                
                # Revenue breakdown
                html.Div(style={'marginTop': '30px'}, children=[
                    html.H3("Revenue Breakdown", style={'color': colors['primary']}),
                    dcc.Dropdown(
                        id='revenue-year-selector',
                        options=[
                            {'label': 'Year 1', 'value': 'Year 1'},
                            {'label': 'Year 3', 'value': 'Year 3'}
                        ],
                        value='Year 1',
                        style={'width': '200px', 'marginBottom': '20px'}
                    ),
                    dcc.Graph(id='revenue-breakdown-chart')
                ]),
                
                # Unit economics
                html.Div(style={'marginTop': '30px'}, children=[
                    html.H3("Unit Economics", style={'color': colors['primary']}),
                    dcc.Graph(
                        figure=make_subplots(specs=[[{"secondary_y": True}]]).add_trace(
                            go.Bar(
                                x=financial_data['Year'],
                                y=financial_data['CAC'],
                                name='Customer Acquisition Cost (£)',
                                marker_color=colors['secondary']
                            )
                        ).add_trace(
                            go.Bar(
                                x=financial_data['Year'],
                                y=financial_data['LTV'],
                                name='Lifetime Value (£)',
                                marker_color=colors['primary']
                            )
                        ).add_trace(
                            go.Scatter(
                                x=financial_data['Year'],
                                y=financial_data['LTV:CAC Ratio'],
                                name='LTV:CAC Ratio',
                                mode='lines+markers',
                                marker=dict(color='red'),
                                line=dict(width=2),
                                yaxis='y2'
                            ),
                            secondary_y=True
                        ).update_layout(
                            title='Unit Economics by Year',
                            xaxis_title='Year',
                            yaxis_title='Amount (£)',
                            yaxis2_title='LTV:CAC Ratio',
                            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
                            barmode='group',
                            hovermode='x unified'
                        )
                    )
                ])
            ])
        ]),
        
        # Market Research Tab
        dcc.Tab(label='Market Research', children=[
            html.Div(style={'padding': '20px'}, children=[
                html.H2("Market Research Insights", style={'color': colors['primary']}),
                html.P("Key findings from our consumer surveys and market analysis."),
                
                # Consumer survey results
                dcc.Graph(
                    figure=px.bar(
                        market_research,
                        x='Finding',
                        y='Percentage',
                        title='Consumer Survey Results',
                        labels={'Percentage': 'Percentage of Respondents (%)'},
                        color='Percentage',
                        color_continuous_scale=px.colors.sequential.Blues,
                        text='Percentage'
                    ).update_traces(
                        texttemplate='%{text}%',
                        textposition='outside'
                    ).update_layout(
                        xaxis={'categoryorder': 'total descending'},
                        yaxis_range=[0, 100]
                    )
                ),
                
                # Demographic breakdown
                html.Div(style={'marginTop': '30px', 'display': 'flex', 'justifyContent': 'space-between'}, children=[
                    html.Div(style={'width': '32%'}, children=[
                        dcc.Graph(
                            figure=px.pie(
                                values=[22, 31, 26, 14, 7],
                                names=['18-24', '25-34', '35-44', '45-54', '55-65'],
                                title='Age Distribution',
                                color_discrete_sequence=px.colors.sequential.Blues
                            ).update_traces(
                                textinfo='percent+label'
                            )
                        )
                    ]),
                    html.Div(style={'width': '32%'}, children=[
                        dcc.Graph(
                            figure=px.pie(
                                values=[68, 30, 2],
                                names=['Female', 'Male', 'Non-binary/Other'],
                                title='Gender Distribution',
                                color_discrete_sequence=px.colors.sequential.Blues
                            ).update_traces(
                                textinfo='percent+label'
                            )
                        )
                    ]),
                    html.Div(style={'width': '32%'}, children=[
                        dcc.Graph(
                            figure=px.pie(
                                values=[35, 18, 12, 9, 8, 18],
                                names=['London', 'South East', 'North West', 'Scotland', 'West Midlands', 'Other UK'],
                                title='Geographic Distribution',
                                color_discrete_sequence=px.colors.sequential.Blues
                            ).update_traces(
                                textinfo='percent+label'
                            )
                        )
                    ])
                ])
            ])
        ]),
        
        # Competitor Analysis Tab
        dcc.Tab(label='Competitor Analysis', children=[
            html.Div(style={'padding': '20px'}, children=[
                html.H2("Competitive Landscape", style={'color': colors['primary']}),
                html.P("Analysis of our position relative to competitors in the market."),
                
                # Market share comparison
                dcc.Graph(
                    figure=make_subplots(rows=1, cols=2, subplot_titles=('Current Market Share (%)', 'Projected Market Share 2028 (%)'),
                                        specs=[[{'type': 'domain'}, {'type': 'domain'}]])
                    .add_trace(go.Pie(
                        labels=competitor_data['Competitor'],
                        values=competitor_data['Current Market Share'],
                        name='Current Market Share',
                        marker_colors=px.colors.qualitative.Set2
                    ), row=1, col=1)
                    .add_trace(go.Pie(
                        labels=competitor_data['Competitor'],
                        values=competitor_data['Projected Market Share (2028)'],
                        name='Projected Market Share',
                        marker_colors=px.colors.qualitative.Set2
                    ), row=1, col=2)
                    .update_traces(textinfo='percent+label')
                    .update_layout(title='Market Share Comparison')
                ),
                
                # User base comparison
                dcc.Graph(
                    figure=px.bar(
                        competitor_data,
                        x='Competitor',
                        y=['Current User Base', 'Projected User Base'],
                        title='User Base Comparison (Current vs. 2028)',
                        barmode='group',
                        labels={'value': 'Number of Users', 'variable': 'Time Period'},
                        color_discrete_sequence=[colors['secondary'], colors['primary']]
                    )
                ),
                
                # Competitive positioning map
                html.Div(style={'marginTop': '30px'}, children=[
                    html.H3("Competitive Positioning Map", style={'color': colors['primary']}),
                    dcc.Graph(
                        figure=go.Figure(data=go.Scatter(
                            x=[0.2, 0.8, 0.7, 0.5, 0.3, 0.1],
                            y=[0.8, 0.2, 0.9, 0.6, 0.4, 0.3],
                            mode='markers+text',
                            marker=dict(
                                size=[40, 30, 25, 20, 15, 15],
                                color=[colors['primary'], '#FFA15A', '#00CC96', '#AB63FA', '#B6E880', '#FF97FF']
                            ),
                            text=['DermaIQ', 'SkinSafe', 'Dermatologist<br>Resources', 'CleanBeautyAI', 'IngrediChecker', 'Retailer Apps'],
                            textposition='top center'
                        )).update_layout(
                            title='Competitive Positioning Map',
                            xaxis=dict(
                                title='Scientific Credibility',
                                showgrid=False,
                                zeroline=False,
                                range=[-0.1, 1.1],
                                showticklabels=False
                            ),
                            yaxis=dict(
                                title='Personalization',
                                showgrid=False,
                                zeroline=False,
                                range=[-0.1, 1.1],
                                showticklabels=False
                            ),
                            annotations=[
                                dict(x=0, y=0, text='LOW', showarrow=False),
                                dict(x=1, y=0, text='HIGH', showarrow=False),
                                dict(x=0, y=1, text='HIGH', showarrow=False),
                                dict(x=0.5, y=-0.1, text='SCIENTIFIC CREDIBILITY', showarrow=False),
                                dict(x=-0.1, y=0.5, text='PERSONALIZATION', textangle=-90, showarrow=False)
                            ],
                            shapes=[
                                dict(type='line', x0=0, y0=0, x1=1, y1=0, line=dict(color='black', width=1)),
                                dict(type='line', x0=0, y0=0, x1=0, y1=1, line=dict(color='black', width=1))
                            ]
                        )
                    )
                ])
            ])
        ])
    ])
])

# Callbacks
@callback(
    Output('quarterly-detail-chart', 'figure'),
    Input('year-selector', 'value')
)
def update_quarterly_chart(selected_year):
    # Filter data for the selected year
    year_indices = range((selected_year-1)*4, selected_year*4)
    filtered_data = user_data.iloc[year_indices]
    
    # Create the figure
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            x=filtered_data['Quarter'],
            y=filtered_data['Total Users'],
            name='Total Users',
            marker_color=colors['primary']
        )
    )
    
    fig.add_trace(
        go.Bar(
            x=filtered_data['Quarter'],
            y=filtered_data['Paying Users'],
            name='Paying Users',
            marker_color=colors['accent']
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=filtered_data['Quarter'],
            y=filtered_data['Conversion Rate'],
            name='Conversion Rate (%)',
            mode='lines+markers',
            marker=dict(color='red'),
            line=dict(width=2, dash='dot'),
            yaxis='y2'
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title=f'Year {selected_year} Quarterly Detail',
        xaxis_title='Quarter',
        yaxis_title='Number of Users',
        yaxis2_title='Conversion Rate (%)',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        barmode='group',
        hovermode='x unified'
    )
    
    return fig

@callback(
    Output('revenue-breakdown-chart', 'figure'),
    Input('revenue-year-selector', 'value')
)
def update_revenue_breakdown(selected_year):
    # Filter data for the selected year
    filtered_data = revenue_streams[revenue_streams['Year'] == selected_year]
    
    # Create the figure
    fig = px.pie(
        filtered_data,
        values='Amount',
        names='Stream',
        title=f'Revenue Breakdown - {selected_year}',
        color_discrete_sequence=px.colors.sequential.Blues
    )
    
    fig.update_traces(textinfo='percent+label')
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8050)
