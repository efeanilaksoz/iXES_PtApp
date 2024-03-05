import dash
from dash import dcc, html
import dash_daq as daq
#import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True)
server = app.server

if __name__ == '__main__':
	app.run_server(debug=False)
