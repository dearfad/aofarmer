import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

api_url = "https://east.albion-online-data.com/api/v2/stats/"

st.write("# Albion Online Farmer! 👨‍🌾")

qualities = st.radio('qualities',('1','2','3','4','5'),horizontal=True)

t = st.radio('T',('T1','T2','T3','T4','T5','T6','T7','T8'),horizontal=True)

name  = '_MAIN_NATURESTAFF'

item = api_url + 'prices/' + t + name + '.json?locations=Caerleon,Thetford,Fort Sterling,Lymhurst,Bridgewatch,Martlock&qualities=' + qualities

r = requests.get(item)

price = pd.DataFrame(r.json())

st.write(price)
