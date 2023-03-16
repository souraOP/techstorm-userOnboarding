import streamlit as st
import pandas as pd
import csv

st.markdown("OMEGATRIX ONBOARDING")

names = pd.read_csv("data/omegatrix.csv")
name_item = st.selectbox(
    'Search Name',
    names['NAMES'].values)

uid = pd.read_csv("data/omegatrix.csv")
uid_item = st.selectbox(
    'Search UID',
    uid['UID'].values)

# if st.button('SEARCH'):
#     with open("data/omegatrix.csv") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if(row[1]==uid_item):
#                 st.write("Found", row[0])
#     st.write(uid_item)
#     st.write(name_item)