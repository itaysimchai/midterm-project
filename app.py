# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="NBA Players Analysis", layout="wide")

# ---- HEADER ----
st.title("🏀 NBA Players Analysis")
st.markdown("""
This interactive Streamlit app explores trends in NBA player physical attributes using a historical dataset.
We highlight three key visual insights from decades of data.
""")

# ---- LOAD DATA ----
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

# ---- PLOT 1: Height Distribution ----
st.subheader("📏 Distribution of Player Heights")

fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.histplot(df['height'], kde=True, color='dodgerblue', ax=ax1)
ax1.set_title('Distribution of NBA Player Heights')
ax1.set_xlabel('Height (cm)')
ax1.set_ylabel('Number of Players')
ax1.grid(True)
st.pyplot(fig1)

# ---- PLOT 2: Average Height by Decade ----
st.subheader("📈 Average Height Over Time")

avg_height = df.groupby('decade')['height'].mean().reset_index()
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.lineplot(data=avg_height, x='decade', y='height', marker='o', color='orange', ax=ax2)
ax2.set_title('Average Height of NBA Players by Decade')
ax2.set_xlabel('Decade')
ax2.set_ylabel('Average Height (cm)')
ax2.grid(True)
st.pyplot(fig2)

# ---- PLOT 3: Height vs. Weight ----
st.subheader("⚖️ Height vs. Weight Relationship")

fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df, x='height', y='weight', alpha=0.7, color='purple', ax=ax3)
ax3.set_title('Height vs. Weight of NBA Players')
ax3.set_xlabel('Height (cm)')
ax3.set_ylabel('Weight (kg)')
ax3.grid(True)
st.pyplot(fig3)

# ---- FOOTER ----
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit · Data from [Kaggle](https://www.kaggle.com/datasets/drgilermo/nba-players-stats)")
