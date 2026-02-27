import streamlit as st
import pickle
import pandas as pd

# ---------------------------
# Load Saved Files
# ---------------------------
df = pd.read_pickle("travel_df.pkl")
cosine_sim = pickle.load(open("cosine_sim.pkl", "rb"))

df = df.reset_index(drop=True)

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="AI Travel Planner", layout="wide")

st.title("AI-Powered Travel Recommendation System")
st.write("Discover similar tourist destinations across India.")

st.divider()

# ---------------------------
# User Selection
# ---------------------------
place_selected = st.selectbox(
    "Select a Place:",
    df['Name'].values
)

top_n = st.slider(
    "Number of Recommendations:",
    min_value=3,
    max_value=10,
    value=5,
    step=1
)

# ---------------------------
# Recommendation Logic
# ---------------------------
if st.button("Get Recommendations"):

    place_index = df[df['Name'] == place_selected].index[0]

    similarity_scores = list(enumerate(cosine_sim[place_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    similarity_scores = similarity_scores[1:top_n+1]
    place_indices = [i[0] for i in similarity_scores]

    recommendations = df.iloc[place_indices][
        ['Name', 'City', 'Type', 'Google review rating', 'Entrance Fee in INR']
    ].reset_index(drop=True)

    st.subheader("Recommended Places")

    # Scrollable compact table
    st.dataframe(
        recommendations,
        use_container_width=True,
        height=350
    )

    st.success("Recommendations generated successfully.")