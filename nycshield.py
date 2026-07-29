# cd '/Users/zhujiaqi/Desktop/ds & ai/Project'
# streamlit run app.py

import streamlit as st
import pandas as pd
import pydeck as pdk

# --- 1. Page Config ---
st.set_page_config(page_title="NYC Shield", layout="wide")

# --- 2. Title & LL18 Background ---
st.title("🛡️ NYC Shield: Illegal Housing Detector")
st.markdown("### *Predictive Analysis of Short-Term Rental Compliance*")

with st.expander("📖 Background: Local Law 18 (LL18) Context"):
    st.write("""
    **New York City** is currently grappling with a severe housing shortage and skyrocketing rent prices. 
    A significant driver of this is the illegal conversion of residential apartments into high-priced, 
    short-term rentals via platforms like Airbnb.
    
    In response, NYC implemented **Local Law 18 (LL18)** in September 2023. This law requires:
    * All short-term rental hosts to register with the Mayor’s Office of Special Enforcement (OSE).
    * Prohibits rentals of an entire apartment for less than 30 days unless the host is physically present.
    
    *Our project utilizes machine learning to identify listings that may be circumventing these regulations.*
    """)

st.divider()

# --- 3. Data Loading ---
DATA_PATH = r"/Users/zhujiaqi/Desktop/ds & ai/Project/Data/all_compliant_listings_by_risk.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df['id'] = df['id'].astype(str)
    df['host_id'] = df['host_id'].astype(str)
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading CSV: {e}")
    st.stop()

# --- 4. Map Section (Empty by default) ---
st.subheader("📍 Geospatial Risk Distribution")
map_placeholder = st.empty()

# --- 5. Search Filters (Optimized Alignment) ---
st.subheader("Search & Audit Filters")

col_mode, col_val, col_btn = st.columns([2, 3, 1])

with col_mode:
    filter_mode = st.radio(
        "Select Filtering Mode:",
        ["Probability Threshold", "Audit Capacity Limit"],
        help="Choose whether to filter by a risk score or by a fixed number of top listings."
    )

with col_val:
    if filter_mode == "Probability Threshold":
        threshold = st.number_input("Enter Probability Threshold (0.0 - 1.0):", 0.0, 1.0, 0.80, 0.01)
    else:
        capacity = st.number_input("Enter Audit Capacity (Top N listings):", min_value=1, max_value=len(df), value=1000, step=100)

with col_btn:
    st.markdown('<div style="padding-top: 28px;"></div>', unsafe_allow_html=True)
    search_clicked = st.button("Search / Refresh", use_container_width=True)

# --- 6. Logic & Display ---
if search_clicked:
    # Check if lat/lon exist to prevent KeyError
    if 'latitude' in df.columns and 'longitude' in df.columns:
        # --- 2 Mode ---
        if filter_mode == "Probability Threshold":
            # Mode A：Threshold
            filtered_df = df[df['prob_illegal'] >= threshold].sort_values(by='prob_illegal', ascending=False)
            mode_label = f"Threshold >= {threshold}"
        else:
            # Mode B：Audit Capacity
            filtered_df = df.sort_values(by='prob_illegal', ascending=False).head(capacity)
            mode_label = f"Top {capacity} Listings"
        
        # --- Update Map ---
        view_state = pdk.ViewState(latitude=40.7128, longitude=-74.0060, zoom=10, pitch=0)
        layer = pdk.Layer(
            "ScatterplotLayer",
            filtered_df,
            get_position=["longitude", "latitude"],
            get_color="[255, 75, 75, 180]",
            get_radius=200,
            pickable=True,
        )
        with map_placeholder:
            st.pydeck_chart(pdk.Deck(
                map_style='light',
                initial_view_state=view_state,
                layers=[layer],
                tooltip={"text": "Risk: {prob_illegal}"}
            ), use_container_width=True)

        # --- Update Table ---
        st.subheader("🔍 Detailed Risk Audit Table")
        st.success(f"Found {len(filtered_df)} suspicious listings.")
        
        # Safely drop columns only if they exist
        display_df = filtered_df.drop(columns=[c for c in ['latitude', 'longitude'] if c in filtered_df.columns])
        
        st.dataframe(display_df, use_container_width=True, height=400)
    else:
        st.error("Missing 'latitude' or 'longitude' in the CSV file! Please regenerate the data.")
else:
    # Default state: Show an empty map with NYC view
    with map_placeholder:
        st.pydeck_chart(pdk.Deck(
            map_style='light',
            initial_view_state=pdk.ViewState(latitude=40.7128, longitude=-74.0060, zoom=10),
            layers=[]
        ))