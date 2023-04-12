import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

api_url = "https://east.albion-online-data.com/api/v2/stats"

st.write("# Albion Online Farmer! 👨‍🌾")

item = api_url + '/api/v2/stats/prices/T4_BAG,T5_BAG.json?locations=Caerleon,Bridgewatch&qualities=2'

r = requests.get(item)

price = r.json()

st.write(price)
