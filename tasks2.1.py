import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('/Users/joaokasprowicz/Desktop/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Automobile Sales Analysis Dashboard"  # TASK 2.1

# Layout of the app
app.layout = html.Div([
    html.H1("Automobile Sales Dashboard", style={'text-align': 'center'}),

    # Dropdowns for selecting data (TASK 2.2)
    html.Div([
        html.Label("Select Vehicle Type:"),
        dcc.Dropdown(
            id='vehicle-type-dropdown',
            options=[{'label': vtype, 'value': vtype} for vtype in df['Vehicle_Type'].unique()],
            value=df['Vehicle_Type'].unique()[0],
            multi=False,
            style={'width': '50%'}
        ),
    ], style={'margin-bottom': '20px'}),

    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': year, 'value': year} for year in sorted(df['Year'].unique())],
            value=df['Year'].min(),
            multi=False,
            style={'width': '50%'}
        ),
    ], style={'margin-bottom': '20px'}),

    # Output Division (TASK 2.3)
    html.Div(id='output-container', className='output-div', style={'margin-top': '30px'}),

    # Graph for Recession Report Statistics (TASK 2.5)
    html.Div([
        dcc.Graph(id='recession-report-graph')
    ]),

    # Graph for Yearly Report Statistics (TASK 2.6)
    html.Div([
        dcc.Graph(id='yearly-report-graph')
    ])
])

# Callback to update the output container (TASK 2.4)
@app.callback(
    Output('output-container', 'children'),
    Input('vehicle-type-dropdown', 'value'),
    Input('year-dropdown', 'value')
)
def update_output(vehicle_type, year):
    return f"You selected Vehicle Type: {vehicle_type} and Year: {year}"

# Callback to update the Recession Report Graph (TASK 2.5)
@app.callback(
    Output('recession-report-graph', 'figure'),
    Input('vehicle-type-dropdown', 'value')
)
def update_recession_graph(vehicle_type):
    filtered_data = df[(df['Recession'] == 1) & (df['Vehicle_Type'] == vehicle_type)]
    fig = px.line(filtered_data, x='Date', y='Automobile_Sales', title=f"Recession Period Sales for {vehicle_type}")
    return fig

# Callback to update the Yearly Report Graph (TASK 2.6)
@app.callback(
    Output('yearly-report-graph', 'figure'),
    Input('year-dropdown', 'value')
)
def update_yearly_graph(year):
    filtered_data = df[df['Year'] == year]
    fig = px.bar(filtered_data, x='Vehicle_Type', y='Automobile_Sales', title=f"Yearly Sales for {year}")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
