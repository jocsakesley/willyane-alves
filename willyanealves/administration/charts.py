import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from willyanealves.customer_service.models import CustomerService, ServiceItem

def barchart_billing_profit():
    date, total, profit = [], [], []
    custormerservice = CustomerService.objects.all()
    for cs in custormerservice:
        date.append(cs.date)
        total.append(float(cs.total_service.strip("R$ ")))
        total_profit = 0
        for si in cs.serviceitem.all():
            total_profit += float(si.profit)
        profit.append(total_profit)
    df = pd.DataFrame({"date": date, "total": total, "profit": profit})
    df = df.groupby('date')[['total','profit']].sum()
    df = pd.DataFrame(df)
    df = df.reset_index()

    fig = go.Figure(data=go.Bar(x=df['date'], y=df['total'], marker_color='rgb(26, 118, 255)', opacity=0.6, showlegend=False, hovertemplate=
        "<b>R$%{y:.2f}</b><br>" +
        "Data: %{x|%d/%m/%Y}<br>" +
        "Total: R$%{y:.2f}<br>" +
        "<extra></extra>"), layout={'template':'plotly_white','barmode':'overlay'})
    fig.add_trace(go.Scatter(x=df['date'], y=df['profit'], line=dict(color='rgb(40, 167, 69)', width=2), showlegend=False, hovertemplate=
        "<b>R$%{y:.2f}</b><br>" +
        "Data: %{x|%d/%m/%Y}<br>" +
        "Lucro: R$%{y:.2f}<br>" +
        "<extra></extra>"))

    fig.update_xaxes(tickformat='%d/%b', tickfont_size=8, tickmode='linear')

    return fig.to_html(config={'modeBarButtonsToRemove':['zoom2d', 'pan2d', 'select2d',
    'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian',
    'zoom3d', 'pan3d', 'resetCameraDefault3d', 'resetCameraLastSave3d', 'hoverClosest3d', 'orbitRotation',
    'tableRotation', 'zoomInGeo', 'zoomOutGeo', 'resetGeo', 'hoverClosestGeo', 'toImage', 'sendDataToCloud',
    'hoverClosestGl2d', 'hoverClosestPie', 'toggleHover', 'resetViews', 'toggleSpikelines', 'resetViewMapbox'], 'displaylogo': False})

def barchart_customer_service():
    date, service, qtd = [], [], []
    custormerservice = CustomerService.objects.all()
    for cs in custormerservice:
        for si in cs.serviceitem.all():

            date.append(si.customerservice.date)
            service.append(si.service.service)
            qtd.append(si.quantity)
    df = pd.DataFrame({'date': date, 'service': service, 'quantity': qtd})
    df = df.groupby(['date','service'])['quantity'].sum()
    df = pd.DataFrame(df)
    df = df.reset_index()
    df = df.tail(5)
    fig = px.bar(df, x=df['date'], y=df['quantity'], color=df['service'], barmode='group')
    fig.update_xaxes(tickformat='%d/%b', tickfont_size=8, tickmode='linear')
    return fig.to_html(config={'modeBarButtonsToRemove':['zoom2d', 'pan2d', 'select2d',
    'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian',
    'zoom3d', 'pan3d', 'resetCameraDefault3d', 'resetCameraLastSave3d', 'hoverClosest3d', 'orbitRotation',
    'tableRotation', 'zoomInGeo', 'zoomOutGeo', 'resetGeo', 'hoverClosestGeo', 'toImage', 'sendDataToCloud',
    'hoverClosestGl2d', 'hoverClosestPie', 'toggleHover', 'resetViews', 'toggleSpikelines', 'resetViewMapbox'], 'displaylogo': False})