#shoot-take.py


import streamlit as st
import pandas as pd
import datetime as dt


 from google.cloud import firestore
 from firestore import credentials, firestore
 


# --- Data ---
# Precreated list of names
#names = ["John Doe", "Jane Doe", "Peter Pan", "Wendy Darling", "Captain Hook"]  
names = ["Lex Hallenberger", "Pete W", "Barack Obama", "Nancy Pelosi", "Elizabeth Warren", "Gavin Newsom", "Kamala Harris"]

# Duck types
duck_types = ["Mallard", "Teal", "Wood Duck", "Gadwall", "Wigeon", "Pintail"]


# --- Layout ---
st.title("Duck Hunting Log")

# --- Form ---
with st.form("hunting_log"):
   
    # Name selection
    name = st.selectbox("Name:", names)

    # Day of shoot draw number
    day_of_shoot = st.selectbox("Day of Shoot Draw Number:", range(1, 12))

   
    # Time of day
    time_of_day = st.radio("Time of Day:", ["Morning", "Afternoon"])
    shoot_datetime = dt.datetime.now()
   



    # Duck count
    st.subheader("Duck Count (max 14 each)")
    duck_count = {}
    for duck in duck_types:
        duck_count[duck] = st.slider(f"{duck}:", 0, 14, 0)


     # Map (centered on Lafayette, CA)
    st.map(pd.DataFrame({
        'lat': [37.8933],  # Latitude of Lafayette, CA
        'lon': [-122.1239]  # Longitude of Lafayette, CA
    }))


    # Submit button
    submitted = st.form_submit_button("Submit")

# --- Results ---
if submitted:
    st.success("Log submitted successfully!")
    st.write("**Hunter:**", name)
    st.write("**Time of Day:**", time_of_day)
    st.write("**Duck Count:**")
    for duck, count in duck_count.items():
        if count > 0:
            st.write(f"  - {duck}: {count}")
    st.write("**Day of Shoot Draw Number:**", day_of_shoot)
    st.write("**Specific Date-Time:**",  shoot_datetime )









