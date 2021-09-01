import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Div import Div
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import session
import datetime as dt
from sqlalchemy import Column, Date, Integer, Text, create_engine, inspect, String
from sqlalchemy.orm import sessionmaker, registry
import sqlite3
from sqlalchemy.sql.schema import Table


app = dash.Dash("Steam Games App", external_stylesheets=['./assets/style.css'])
app.title = "Steam Games Analytics"
server = app.server

#Read csv and create DF
df = pd.read_csv('version_02_df.csv')
game_names = df['name'].unique()

def run_query_withparms(sql):
    conn = sqlite3.connect("db_steam_v002.db")
    df = pd.read_sql_query(sql,conn)
    return df

def generate_table(dataframe, max_rows=10):
    return html.Table(
    # Header
    [html.Tr([
        html.Th(col) for col in dataframe.columns])] +

    # Body
    [html.Tr([
        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]) for i in range(min(len(dataframe), max_rows))])

def generate_image(dataframe):
    image_url = dataframe.iloc[0,0]
    url = str(image_url)
    url = url.replace('{"props": {"children": null,"src":', '')
    url = url.replace('},"type": "Img","namespace": "dash_html_components"}', '')
    return url


app.layout = html.Div(
            className="content",
            children=[
                html.Div(
                    className="left_menu",
                    children=[
                        html.Div(
                            'Gaming Zone'
                        ),
                        html.Div(children=[
                            dcc.Dropdown(
                                id='game_list',
                                className='games_list',
                                options=[{'label': i, 'value': i} for i in game_names],
                                value=game_names[0],
                                clearable=False
                            ),
                        html.Div(children=[
                            #html.Table('Thumbnail', className='thumb')
                        ]),
                        html.Img(className='img', id='sql_data_12', style={'height': '90%', 'width': '90%'})

                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data')
                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data_2')
                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data_3')
                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data_4')
                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data_5')
                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data_6')
                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data_7')
                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data_8')
                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data_9')
                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data_10')
                        ]),
                        html.Div(children=[
                            html.Table(className='games_table', id='sql_data_11')
                        ])
                    ]
                ),
                html.Div(
                    className="right_content",
                    children=[
                        html.Div(
                            className="top_metrics",
                            children=[
                                html.Img(src='./assets/steam.jpg', width=300)
                            ], style={'textAlign': 'center'}
                        ),
                    html.Div([
                        html.A(id='banner-logo',
                                children=[
                                    html.Img(src='./assets/games_sample.jpg', style={'height': '25%', 'width': '25%', 'padding': '25px'})
                                ], href='https://store.steampowered.com'
                            )
                    ],style={'textAlign': 'center'}),
                    html.Div(className='imgs',
                        children=[
                            html.Img(src='./assets/visuals.png', style={'height': '70%', 'width': '70%'})  
                        ]
                    )
                ]
            )
    ]
)


@app.callback(Output('sql_data', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql2 = "SELECT steam_appid FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql2))

@app.callback(Output('sql_data_2', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql3 = "SELECT required_age FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql3))

@app.callback(Output('sql_data_3', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql3 = "SELECT date FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql3))

@app.callback(Output('sql_data_4', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql3 = "SELECT windows, mac, linux FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql3))

@app.callback(Output('sql_data_5', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql3 = "SELECT price FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql3))

@app.callback(Output('sql_data_6', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql3 = "SELECT is_free FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql3))

@app.callback(Output('sql_data_7', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql2 = "SELECT review_score FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql2))

@app.callback(Output('sql_data_8', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql2 = "SELECT total_reviews FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql2))

@app.callback(Output('sql_data_9', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql3 = "SELECT publishers FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql3))

@app.callback(Output('sql_data_10', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql3 = "SELECT coming_soon FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql3))

@app.callback(Output('sql_data_11', 'children'),[Input('game_list', 'value')])

def run_query(value):
    sql3 = "SELECT website FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_table(run_query_withparms(sql3))

@app.callback(Output('sql_data_12', 'src'),[Input('game_list', 'value')])

def run_query(value):
    sql3 = "SELECT header_image FROM STEAM_GAMES WHERE name = '{}'".format(value)
    return generate_image(run_query_withparms(sql3))



# Running the server
if __name__ == "__main__":
    app.run_server(debug=True)


'''
table = STEAM_GAMES
columns = name, steam_appid, required_age, is_free, header_image, website, review_score, total_reviews, windows, mac, linux, publishers, price, comming_soon, date
'''