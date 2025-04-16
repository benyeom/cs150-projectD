from dash import dcc

def chart_dropdown():
    return dcc.Dropdown(
        id="chart-selector",
        options=[
            {"label": "Compare Incomes", "value": "bar"},
            {"label": "View Difference", "value": "slope"}
        ],
        value="bar",
        clearable=False,
        style={"width": "50%", "margin": "20px auto 0 auto"}
    )
