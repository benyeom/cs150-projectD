import plotly.graph_objects as go
import pandas as pd


def income_comparison_bar_chart():
    average_user_income = 55466.67
    average_us_income = 39982
    fig = go.Figure(data=[
        go.Bar(
            name='Average User Income',
            x=['Income'],
            y=[average_user_income],
            marker_color='darkgreen'
        ),
        go.Bar(
            name='Average US Income',
            x=['Income'],
            y=[average_us_income],
            marker_color='grey'
        )
    ])
    fig.update_layout(
        barmode='group',
        title='<b>Income Comparison</b>',
        yaxis_title='Income (USD)',
        xaxis_title='',
        title_x=0.5
    )
    return fig


def income_comparison_slope_graph():
    average_user_income = 55466.67
    average_us_income = 39982
    percent_diff = (average_user_income - average_us_income) / average_us_income * 100
    fig = go.Figure(data=[
        go.Scatter(
            x=["Average US Income", "Average User Income"],
            y=[average_us_income, average_user_income],
            mode="lines+markers+text",
            text=[f"${average_us_income:,.2f}", f"${average_user_income:,.2f}"],
            textposition="top center",
            line=dict(width=4, color="darkblue")
        )
    ])
    fig.add_annotation(
        x=0.5,
        y=(average_user_income + average_us_income) / 2,
        xref="paper",
        text=f"<b>+{percent_diff:.2f}%</b>",
        showarrow=True,
        arrowhead=2,
        font=dict(size=18, color="black"),
        ax=0,
        ay=-40
    )
    fig.update_layout(
        title='<b>Income Slope Graph</b>',
        yaxis_title="Income (USD)",
        xaxis_title="",
        title_x=0.5
    )
    return fig


def social_media_usage_comparison_line_chart():
    # Read U.S. social media usage data from the CSV file
    df_usage = pd.read_csv(
        "Average hours per day spent on socializing and communicating by the U.S. population from 2009 to 2023.csv")
    df_usage['Characteristic'] = pd.to_numeric(df_usage['Characteristic'], errors='coerce')
    df_us = df_usage[(df_usage['Characteristic'] >= 2012) & (df_usage['Characteristic'] <= 2023)]

    # Read worldwide social networking usage data from the CSV file
    df_world = pd.read_csv(
        "Daily time spent on social networking by internet users worldwide from 2012 to 2024 - Sheet1.csv")
    df_world['Characteristic'] = pd.to_numeric(df_world['Characteristic'], errors='coerce')
    df_world = df_world[(df_world['Characteristic'] >= 2012) & (df_world['Characteristic'] <= 2023)]
    # Convert minutes per day to hours per day
    df_world['Hours'] = df_world["Minutes per day"] / 60

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_us["Characteristic"],
        y=df_us["All"],
        mode="lines+markers",
        name="In-person Interactions",
        line=dict(width=3, color="red")
    ))
    fig.add_trace(go.Scatter(
        x=df_world["Characteristic"],
        y=df_world["Hours"],
        mode="lines+markers",
        name="Social Media Interactions",
        line=dict(width=3, color="darkgreen")
    ))
    fig.update_layout(
        title='<b>Interaction Comparison (2012 - 2023)</b>',
        xaxis_title="Year",
        yaxis_title="Average Hours per Day",
        title_x=0.5
    )
    return fig


def jobs_vs_social_media_line_chart():
    # Read jobs data from the CSV file and filter for 2012-2023
    df_jobs = pd.read_csv(
        "Number of jobs created by start-up businesses that were less than one year old in the United States from 1994 to 2023 - Sheet1.csv")
    df_jobs['Characteristic'] = pd.to_numeric(df_jobs['Characteristic'], errors='coerce')
    df_jobs_filtered = df_jobs[(df_jobs['Characteristic'] >= 2012) & (df_jobs['Characteristic'] <= 2023)]
    df_jobs_filtered = df_jobs_filtered.sort_values("Characteristic")

    # Retrieve the jobs data from the proper column
    if "Jobs Created" in df_jobs_filtered.columns:
        jobs = df_jobs_filtered["Jobs Created"]
    else:
        jobs = df_jobs_filtered.iloc[:, 1]

    # Read social media interactions data from the worldwide CSV using the "Minutes per day" column
    df_social = pd.read_csv(
        "Daily time spent on social networking by internet users worldwide from 2012 to 2024 - Sheet1.csv")
    df_social['Characteristic'] = pd.to_numeric(df_social['Characteristic'], errors='coerce')
    df_social_filtered = df_social[(df_social['Characteristic'] >= 2012) & (df_social['Characteristic'] <= 2023)]
    df_social_filtered = df_social_filtered.sort_values("Characteristic")
    social = df_social_filtered["Minutes per day"]

    # Create the line chart with two traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_jobs_filtered["Characteristic"],
        y=jobs,
        mode="lines+markers",
        name="Jobs Created by Startups",
        line=dict(width=3, color="#228B22")
    ))
    fig.add_trace(go.Scatter(
        x=df_social_filtered["Characteristic"],
        y=social,
        mode="lines+markers",
        name="Social Media Usage",
        line=dict(width=3, color="lightgreen")
    ))

    fig.update_layout(
        title='<b>Jobs vs Social Media Usage</b>',
        xaxis_title="Year",
        yaxis_title="Value",
        title_x=0.5
    )
    return fig


