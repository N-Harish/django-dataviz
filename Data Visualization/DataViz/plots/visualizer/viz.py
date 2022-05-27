import pandas as pd
import plotly.express as px
from plotly.offline import plot
import numpy as np
import plotly.graph_objs as go


def data_loader(path):
    data = pd.read_excel(path)
    new_header = data.iloc[0]
    df = data[1:]
    df.columns = new_header
    return df


def pie_bucket(df):
    li = list(df.Bucket.value_counts())
    colors = ['gold', 'mediumturquoise', 'lightgreen']
    li = [np.round((x * 100 / df.Bucket.count()), decimals=2) for x in li]

    fig = go.Figure(
        data=[go.Pie(labels=df.Bucket.value_counts().index.to_list(), values=li)])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))

    plot_buc = plot(fig, show_link=False, link_text="",
                    output_type='div', config={"displaylogo": False})
    return plot_buc


def pie_division(df):
    li = list(df.Division.value_counts())
    colors = ['gold', 'mediumturquoise', 'lightgreen', 'darkorange']
    li = [np.round((x * 100 / df.Division.count()), decimals=2) for x in li]

    fig = go.Figure(
        data=[go.Pie(labels=df.Division.value_counts().index.to_list(), values=li)])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))

    plot_div = plot(fig, show_link=False, link_text="", output_type='div', config={
                    "displaylogo": False, 'modeBarButtonsToRemove': []})
    return plot_div


def box_bucket(df):
    fig3 = px.box(df, x='Bucket', y='Payment', points='all')

    plot_buc_vs_pay = plot(fig3, show_link=False, link_text="",
                           output_type='div', config={"displaylogo": False})

    return plot_buc_vs_pay
