from dash import Dash, dcc, html, Input, Output
import dash
import pandas as pd
import utils.components as drc
import utils.figures as figs

df = pd.read_excel("Social Meida Dataset.xlsx")

# calculate overall average social media usage using the updated column name
total_usage = df["Social Media Usage (Hours/Day)"].sum()
unique_consumer_count = df["Consumer ID"].nunique()
overall_avg = total_usage / unique_consumer_count

# calculate average income:
total_income = df["Income (USD)"].sum()
average_income = total_income / unique_consumer_count

# calculate the percentage of consumer IDs with "Bachelor's" Education Level
bachelor_count = df[df["Education Level"] == "Bachelor's"]["Consumer ID"].nunique()
bachelor_percentage = (bachelor_count / unique_consumer_count) * 100

app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1.0"}]
)
app.title = "Project D"
server = app.server

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    "A SOCIAL MEDIA USER",
                    style={
                        "margin": "5px 0",
                        "padding": "0",
                        "textAlign": "center",
                        "fontSize": "32px"
                    }
                ),
                html.H2(
                    "CS-150 Topics",
                    style={
                        "margin": "5px 0",
                        "padding": "0",
                        "textAlign": "center",
                        "fontSize": "17px"
                    }
                ),
                html.H3(
                    "Benjamin Yeom",
                    style={
                        "margin": "5px 0",
                        "padding": "0",
                        "textAlign": "center",
                        "fontSize": "13px"
                    }
                ),
            ],
            style={
                "width": "100%",
                "boxSizing": "border-box",
                "padding": "20px",
                "backgroundColor": "darkgreen",
                "color": "white",
                "textAlign": "center",
                "margin": "0"
            }
        ),
        html.Div(
            children=[
                # Box 1: average social media usage
                html.Div(
                    children=[
                        html.H4(
                            "Average Social Media Usage",
                            style={
                                "margin": "10px 0 40px 0",
                                "textAlign": "center",
                                "fontSize": "26px"
                            }
                        ),
                        html.P(
                            f"{overall_avg:.2f} hrs",
                            style={
                                "fontSize": "50px",
                                "fontWeight": "bold",
                                "textAlign": "center"
                            }
                        )
                    ],
                    style={
                        "flex": "1",
                        "border": "5px solid darkgreen",
                        "backgroundColor": "#e8f5e9",
                        "padding": "20px",
                        "marginRight": "10px"
                    }
                ),
                # Box 2: average user income
                html.Div(
                    children=[
                        html.H4(
                            "Average User Income",
                            style={
                                "margin": "10px 0 40px 0",
                                "textAlign": "center",
                                "fontSize": "26px"
                            }
                        ),
                        html.P(
                            f"${average_income:,.2f}",
                            style={
                                "fontSize": "50px",
                                "fontWeight": "bold",
                                "textAlign": "center"
                            }
                        ),
                        html.P(
                            "(Average US Income: $39,982)",
                            style={
                                "fontSize": "18px",
                                "textAlign": "center",
                                "margin": "5px 0"
                            }
                        )
                    ],
                    style={
                        "flex": "1",
                        "border": "5px solid darkgreen",
                        "backgroundColor": "#e8f5e9",
                        "padding": "20px",
                        "marginRight": "10px"
                    }
                ),
                # Box 3: percentage of users with Bachelor's degree
                html.Div(
                    children=[
                        html.P(
                            f"{bachelor_percentage:.0f}%",
                            style={
                                "fontSize": "60px",
                                "fontWeight": "bold",
                                "textAlign": "center",
                                "margin": "5px 0",
                                "margin-top": "35px",
                                "margin-bottom": "18px"
                            }
                        ),
                        html.P(
                            [
                                html.Span(
                                    "of Users Have Earned a ",
                                    style={
                                        "fontSize": "30px",
                                        "fontWeight": "normal"
                                    }
                                ),
                                html.Span(
                                    "BACHELOR'S DEGREE!",
                                    style={
                                        "fontSize": "36px",
                                        "fontWeight": "bold",
                                        "textTransform": "uppercase"
                                    }
                                )
                            ],
                            style={"textAlign": "center", "margin": "5px 0"}
                        )
                    ],
                    style={
                        "flex": "1",
                        "border": "5px solid darkgreen",
                        "backgroundColor": "#e8f5e9",
                        "padding": "20px"
                    }
                )
            ],
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "padding": "20px"
            }
        ),
        # Row: Two columns – Left: income chart with dropdown inside boxed container and Right: social media usage comparison line graph
        html.Div(
            children=[
                # Left column for Income Chart + Dropdown
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dcc.Graph(id="income-chart"),
                                # Use the reusable dropdown from components.py
                                drc.chart_dropdown()
                            ],
                            style={
                                "border": "5px solid darkgreen",
                                "backgroundColor": "#e8f5e9",
                                "padding": "20px",
                                "marginTop": "20px"
                            }
                        )
                    ],
                    style={"width": "50%", "padding": "20px"}
                ),
                # Right column for Social Media Usage Comparison Line Graph
                html.Div(
                    children=[
                        html.Div(
                            dcc.Graph(
                                id="social-line-chart",
                                figure=figs.social_media_usage_comparison_line_chart()
                            ),
                            style={
                                "border": "5px solid darkgreen",
                                "backgroundColor": "#e8f5e9",
                                "padding": "20px",
                                "marginTop": "20px"
                            }
                        )
                    ],
                    style={"width": "50%", "padding": "20px"}
                )
            ],
            style={"display": "flex", "width": "100%"}
        ),
        # Bottom row: Line Graph Comparing Jobs Created and Social Media Interactions (80% width, centered)
        html.Div(
            children=[
                html.Div(
                    dcc.Graph(
                        id="jobs-social-line-chart",
                        figure=figs.jobs_vs_social_media_line_chart()
                    ),
                    style={
                        "border": "5px solid darkgreen",
                        "backgroundColor": "#e8f5e9",
                        "padding": "20px",
                        "marginTop": "20px"
                    }
                )
            ],
            style={"width": "80%", "margin": "0 auto", "padding": "20px"}
        )
    ],
    style={"margin": "0", "padding": "0"}
)

# Callback to update the income chart based on the dropdown selection
@app.callback(
    Output("income-chart", "figure"),
    Input("chart-selector", "value")
)
def update_chart(chart_type):
    if chart_type == "slope":
        return figs.income_comparison_slope_graph()
    else:
        return figs.income_comparison_bar_chart()

if __name__ == "__main__":
    app.run(debug=True)
