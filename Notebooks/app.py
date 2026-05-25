import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from datetime import datetime
import pytz


# PAGE CONFIGURATION
st.set_page_config(page_title="Google Play Store Analytics Dashboard", page_icon="*", layout="wide")


# GOOGLE THEME COLORS
GOOGLE_COLORS = {
    "blue": "#4285F4",
    "green": "#34A853",
    "yellow": "#FBBC05",
    "red": "#EA4335"
}


# DASHBOARD TITLE
st.title("Google Play Store Analytics Dashboard")

st.markdown(
    """
    Interactive analytics dashboard built using Google Play Store Apps and Reviews datasets.
    """
)


# SIDEBAR
st.sidebar.header("Dashboard Controls")


# IST TIME FUNCTIONS
def get_ist_hour():
    india_tz = pytz.timezone("Asia/Kolkata")
    current_time = datetime.now(india_tz)
    return current_time.hour

def is_time_between(start_hour, end_hour):
    current_hour = get_ist_hour()
    return start_hour <= current_hour < end_hour


# LOAD MAIN DATASET
df = pd.read_csv("..\\Data\\Cleaned_Data\\aggregated_merged_dataset.csv")


# SIDEBAR FILTERS
selected_categories = st.sidebar.multiselect(
    "Select Categories",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

selected_rating = st.sidebar.slider(
    "Minimum Rating",
    min_value=float(df["Rating"].dropna().min()),
    max_value=float(df["Rating"].dropna().max()),
    value=float(3.5),
    step=0.1
)

selected_type = st.sidebar.multiselect(
    "Select App Type",
    options=df["Type"].unique(),
    default=df["Type"].unique()
)

install_range = st.sidebar.slider(
    "Select Install Range",
    min_value=int(df["Installs"].min()),
    max_value=int(df["Installs"].max()),
    value=(
        int(df["Installs"].min()),
        int(df["Installs"].max())
    )
)


# APPLY FILTERS
filtered_df = df[
    (df["Category"].isin(selected_categories)) &
    (df["Rating"] >= selected_rating) &
    (df["Type"].isin(selected_type)) &
    (df["Installs"] >= install_range[0]) &
    (df["Installs"] <= install_range[1])
]


# KPI SECTION
st.subheader("Dashboard KPIs")
total_apps = filtered_df["App"].nunique()
avg_rating = round(filtered_df["Rating"].mean(), 2)
total_installs = int(filtered_df["Installs"].sum())
total_revenue = round(filtered_df["Revenue"].sum(), 2)
avg_reviews = int(filtered_df["Reviews"].mean())

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Apps", f"{total_apps:,}")

with col2:
    st.metric("Average Rating", avg_rating)

with col3:
    st.metric("Total Installs", f"{total_installs:,}")

with col4:
    st.metric("Total Revenue", f"${total_revenue:,.0f}")

with col5:
    st.metric("Average Reviews", f"{avg_reviews:,}")


# TASK 1
st.divider()

st.subheader("Task 1: Rating vs Reviews Analysis")

if is_time_between(15, 17):
    task1_df = pd.read_csv("..\\Data\\Task_wise_dataset\\task1_grouped.csv")
    fig1 = make_subplots(specs=[[{"secondary_y": True}]])

    google_palette = [
        GOOGLE_COLORS["blue"],
        GOOGLE_COLORS["green"],
        GOOGLE_COLORS["yellow"],
        GOOGLE_COLORS["red"]
    ]

    fig1.add_trace(
        go.Bar(
            x=task1_df["Category"],
            y=task1_df["Rating"],
            name="Average Rating",
            marker_color=google_palette * 3,
            width=0.35,
            offsetgroup=1
        ),
        secondary_y=False
    )

    fig1.add_trace(
        go.Bar(
            x=task1_df["Category"],
            y=task1_df["Reviews"],
            name="Total Reviews",
            marker_color=[
                GOOGLE_COLORS["red"],
                GOOGLE_COLORS["yellow"],
                GOOGLE_COLORS["blue"],
                GOOGLE_COLORS["green"]
            ] * 3,
            width=0.35,
            offsetgroup=2
        ),
        secondary_y=True
    )

    fig1.update_layout(
        template="plotly_white",
        height=600,
        title={
            "text":
            "Top 10 App Categories: Average Rating vs Reviews",
            "x": 0.5
        }
    )

    st.plotly_chart(fig1, use_container_width=True)
else:
    st.warning("Task 1 chart is available only between 3 PM and 5 PM IST.")


# TASK 2
st.divider()

st.subheader("Task 2: Global Installs Choropleth")

if is_time_between(18, 20):
    task2_df = pd.read_csv("..\\Data\\Task_wise_dataset\\task2_grouped.csv")
    task2_df["Country"] = [
        "India",
        "United States",
        "Brazil",
        "Germany",
        "South Africa"
    ]

    fig2 = px.choropleth(
        task2_df,
        locations="Country",
        locationmode="country names",
        color="Installs",
        hover_name="Category",
        color_continuous_scale=[
            GOOGLE_COLORS["blue"],
            GOOGLE_COLORS["green"],
            GOOGLE_COLORS["yellow"],
            GOOGLE_COLORS["red"]
        ]
    )

    fig2.update_layout(template="plotly_white", height=650)
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("Task 2 chart is available only between 6 PM and 8 PM IST.")


# TASK 3
st.divider()
st.subheader("Task 3: Free vs Paid Apps Analysis")

if is_time_between(13, 14):
    task3_df = pd.read_csv("..\\Data\\Task_wise_dataset\\task3_grouped .csv")
    fig3 = make_subplots(specs=[[{"secondary_y": True}]])

    for app_type, color in zip(["Free", "Paid"], [GOOGLE_COLORS["blue"], GOOGLE_COLORS["green"]]):
        temp_df = task3_df[task3_df["Type"] == app_type]
        fig3.add_trace(
            go.Bar(
                x=temp_df["Category"],
                y=temp_df["Installs"],
                name=f"{app_type} Installs",
                marker_color=color
            ),
            secondary_y=False
        )

    for app_type, color in zip(["Free", "Paid"], [GOOGLE_COLORS["yellow"], GOOGLE_COLORS["red"]]):
        temp_df = task3_df[task3_df["Type"] == app_type]
        fig3.add_trace(
            go.Scatter(
                x=temp_df["Category"],
                y=temp_df["Revenue"],
                mode="lines+markers",
                name=f"{app_type} Revenue",
                line=dict(
                    color=color,
                    width=4
                )
            ),
            secondary_y=True
        )

    fig3.update_layout(template="plotly_white", height=650)
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.warning("Task 3 chart is available only between 1 PM and 2 PM IST.")

# TASK 4
st.divider()
st.subheader("Task 4: Installs Trend Analysis")

if is_time_between(18, 21):
    task4_df = pd.read_csv("..\\Data\\Task_wise_dataset\\task4_grouped.csv")
    task4_df["Category"] = (
        task4_df["Category"]
        .replace({
            "Beauty": "सौंदर्य",
            "Business": "வணிகம்",
            "Dating": "Partnersuche"
        })
    )

    fig4 = go.Figure()
    colors = [
        GOOGLE_COLORS["blue"],
        GOOGLE_COLORS["green"],
        GOOGLE_COLORS["yellow"],
        GOOGLE_COLORS["red"]
    ]

    top_categories = (
        task4_df.groupby("Category")["Installs"]
        .sum()
        .sort_values(ascending=False)
        .head(4)
        .index
    )

    task4_df = task4_df[task4_df["Category"].isin(top_categories)]

    for category, color in zip(task4_df["Category"].unique(), colors * 5):
        category_df = task4_df[task4_df["Category"] == category]
        fig4.add_trace(
            go.Scatter(
                x=category_df["Year_Month"],
                y=category_df["Installs"],
                mode="lines",
                name=category,
                line=dict(
                    color=color,
                    width=3
                )
            )
        )

    fig4.update_layout(template="plotly_white", height=700, yaxis_type="log")
    st.plotly_chart(fig4, use_container_width=True)
else:
    st.warning("Task 4 chart is available only between 6 PM and 9 PM IST.")


# TASK 5
st.divider()
st.subheader("Task 5: Bubble Chart Analysis")

if is_time_between(17, 19):
    task5_df = pd.read_csv("..\\Data\\Task_wise_dataset\\task5_grouped.csv")
    task5_df["Category"] = (
        task5_df["Category"]
        .replace({
            "BEAUTY": "सौंदर्य",
            "BUSINESS": "வணிகம்",
            "DATING": "Partnersuche"
        })
    )

    color_map = {
        "GAME": "pink",
        "सौंदर्य": GOOGLE_COLORS["blue"],
        "வணிகம்": GOOGLE_COLORS["green"],
        "COMICS": GOOGLE_COLORS["yellow"],
        "COMMUNICATION": GOOGLE_COLORS["red"]
    }

    fig5 = px.scatter(
        task5_df,
        x="Size",
        y="Rating",
        size="Installs",
        color="Category",
        color_discrete_map=color_map,
        hover_name="App",
        size_max=60
    )

    fig5.update_layout(template="plotly_white", height=700)
    st.plotly_chart(fig5, use_container_width=True)
else:
    st.warning("Task 5 chart is available only between 5 PM and 7 PM IST.")

# TASK 6
st.divider()
st.subheader("Task 6: Stacked Area Chart")

if is_time_between(16, 18):
    task6_df = pd.read_csv("..\\Data\\Task_wise_dataset\\task6_grouped.csv")
    task6_df["Category"] = (
        task6_df["Category"]
        .replace({
            "TRAVEL_AND_LOCAL": "Voyage_Local",
            "PRODUCTIVITY": "Productividad",
            "PHOTOGRAPHY": "写真"
        })
    )

    fig6 = go.Figure()
    colors = [
        GOOGLE_COLORS["blue"],
        GOOGLE_COLORS["green"],
        GOOGLE_COLORS["yellow"],
        GOOGLE_COLORS["red"]
    ]

    for category, color in zip(task6_df["Category"].unique(), colors * 5):
        category_df = task6_df[task6_df["Category"] == category]
        fig6.add_trace(
            go.Scatter(
                x=category_df["Year_Month"],
                y=category_df["Cumulative_Installs"],
                mode="lines",
                stackgroup="one",
                name=category,
                line=dict(
                    color=color,
                    width=2
                )
            )
        )

    fig6.update_layout(template="plotly_white",height=700)
    st.plotly_chart(fig6, use_container_width=True)
else:
    st.warning("Task 6 chart is available only between 4 PM and 6 PM IST.")

# FOOTER
st.divider()
st.caption("Google Play Store Analytics Dashboard | Developed by Om Chauhan | Data Source: Google Play Store Apps and Reviews Datasets")