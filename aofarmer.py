import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

api_url = "https://east.albion-online-data.com/api/v2/stats/"

st.write("# Albion Online Farmer! 👨‍🌾")

item = api_url + 'history/T4_BAG.json?locations=Caerleon&qualities=1&time-scale=1'
r = requests.get(item)
price = pd.DataFrame(r.json())
st.write(price)
