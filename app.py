# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Config ---
st.set_page_config(page_title="NBA Data App", layout="wide")

# --- Header ---
st.title("🏀 NBA Players Stats Explorer")
st.markdown("**Explore how NBA players have evolved over time through physical attributes.**")

st.image("https://upload.wikimedia.org/wikipedia/en/0/03/NBA_logo.svg", width=100)

# --- Sidebar ---
st.sidebar.title("📊 Choose a Graph")
chart_option = st.sidebar.radio(
    "Select an insight to view:",
    [
        "📏 Distribution of Heights",
        "📈 Avg Height by Decade",
        "⚖️ Height vs. Weight",
    ]
)

# --- Load and prep data ---
@st.cache_data
def load_data():
    url = 'https://www.dropbox.com/scl/fi/dp276p1m6sz2izmg5kugw/Players.csv?rlkey=gfrwg66zeeof6vjs5jxfoyhym&dl=1'
    df = pd.read_csv(url)
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    df = df.drop_duplicates()
    df['decade'] = (df['born'] // 10) * 10
    return df

df = load_data()

# --- Plot 1: Height Distribution ---
if chart_option == "📏 Distribution of Heights":
    st.subheader("📏 Distribution of NBA Player Heights")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df['height'], kde=True, color='dodgerblue', ax=ax)
    ax.set_title('Distribution of NBA Player Heights')
    ax.set_xlabel('Height (cm)')
    ax.set_ylabel('Number of Players')
    ax.grid(True)
    st.pyplot(fig)
    st.info("Most NBA players are between 190–210 cm tall, showing a strong preference for taller athletes.")

# --- Plot 2: Avg Height by Decade ---
elif chart_option == "📈 Avg Height by Decade":
    st.subheader("📈 Average Height by Birth Decade")
    avg_height = df.groupby('decade')['height'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=avg_height, x='decade', y='height', marker='o', color='orange', ax=ax)
    ax.set_title('Average Height of NBA Players by Decade')
    ax.set_xlabel('Decade')
    ax.set_ylabel('Average Height (cm)')
    ax.grid(True)
    st.pyplot(fig)
    st.info("Player height has steadily increased over the decades, reflecting evolving game strategies.")

# --- Plot 3: Height vs Weight ---
elif chart_option == "⚖️ Height vs. Weight":
    st.subheader("⚖️ Height vs Weight Relationship")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x='height', y='weight', alpha=0.7, color='purple', ax=ax)
    ax.set_title('Height vs. Weight of NBA Players')
    ax.set_xlabel('Height (cm)')
    ax.set_ylabel('Weight (kg)')
    ax.grid(True)
    st.pyplot(fig)
    st.info("As expected, taller players tend to weigh more, forming a natural upward trend.")

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ using [Streamlit](https://streamlit.io) · Data from [Kaggle](https://www.kaggle.com/datasets/drgilermo/nba-players-stats)")
