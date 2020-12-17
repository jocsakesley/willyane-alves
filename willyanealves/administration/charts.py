import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from willyanealves.customer_service.models import CustomerService, ServiceItem

def barchart_billing_profit(date_bp, total, profit):

    df = pd.DataFrame({"date": date_bp, "total": total, "profit": profit})
    df = df.groupby('date')[['total','profit']].sum()
    df = pd.DataFrame(df)
    df = df.reset_index()
    try:
        fig = px.bar(df, x='date', y='total')
    except:
        df = pd.DataFrame([[0,0],[0,0]], index=['date', 'total']).T
        fig = px.bar(df, x='date', y='total')
    fig.add_scatter(x=df['date'], y=df['profit'], hovertemplate=
                      "<b>R$%{y:.2f}</b><br>" +
                      "Data: %{x|%d/%m/%Y}<br>" +
                      "Total: R$%{y:.2f}<br>" +
                      "<extra></extra>")
    fig.update_layout(
        showlegend=False,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )

    fig.update_traces(hovertemplate=
                      "<b>R$%{y:.2f}</b><br>" +
                      "Data: %{x|%d/%m/%Y}<br>" +
                      "Total: R$%{y:.2f}<br>" +
                      "<extra></extra>")
    fig.update_xaxes(tickformat='%d/%b', tickfont_size=8, tickmode='linear')

    return fig.to_html(config={'modeBarButtonsToRemove':['zoom2d', 'pan2d', 'select2d',
    'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian',
    'zoom3d', 'pan3d', 'resetCameraDefault3d', 'resetCameraLastSave3d', 'hoverClosest3d', 'orbitRotation',
    'tableRotation', 'zoomInGeo', 'zoomOutGeo', 'resetGeo', 'hoverClosestGeo', 'toImage', 'sendDataToCloud',
    'hoverClosestGl2d', 'hoverClosestPie', 'toggleHover', 'resetViews', 'toggleSpikelines', 'resetViewMapbox'], 'displaylogo': False})

def barchart_customer_service(date_cs, service, qtd):
    df = pd.DataFrame({'date': date_cs, 'service': service, 'quantity': qtd})
    df = df.groupby(['date','service'])['quantity'].sum()
    df = pd.DataFrame(df)
    df = df.reset_index()
    try:
        fig = px.bar(df, x=df['date'], y=df['quantity'], color=df['service'], barmode='group')
    except:
        df = pd.DataFrame([[0,0],[0,0],[0,0]], index=['date', 'service', 'quantity']).T
        fig = px.bar(df, x=df['date'], y=df['quantity'], color=df['service'], barmode='group')

    fig.update_layout(
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        legend_title_text=None
    )

    fig.update_xaxes(tickformat='%d/%b', tickfont_size=8, tickmode='linear')
    return fig.to_html(config={'modeBarButtonsToRemove':['zoom2d', 'pan2d', 'select2d',
    'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian',
    'zoom3d', 'pan3d', 'resetCameraDefault3d', 'resetCameraLastSave3d', 'hoverClosest3d', 'orbitRotation',
    'tableRotation', 'zoomInGeo', 'zoomOutGeo', 'resetGeo', 'hoverClosestGeo', 'toImage', 'sendDataToCloud',
    'hoverClosestGl2d', 'hoverClosestPie', 'toggleHover', 'resetViews', 'toggleSpikelines', 'resetViewMapbox'], 'displaylogo': False})