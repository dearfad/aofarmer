import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

api_url = "https://east.albion-online-data.com/api/v2/stats/"

st.write("# Albion Online Farmer! 👨‍🌾")

qualities = st.radio('qualities',('1','2','3','4','5'),horizontal=True)

t = st.radio('T',('T1','T2','T3','T4','T5','T6','T7','T8'),horizontal=True)

type = {
    '附件': ['背包','披风'],
    '护甲': ['布帽','布甲','布鞋']
}

cat = st.selectbox('cat',('附件','护甲'))

aa = st.selectbox('aa',type[cat])

chn = {
    '背包': 'BAG',
    '披风': 'CAPE',
    '布帽': 'HEAD_CLOTH_SET1',
    '布甲': 'ARMOR_CLOTH_SET1',
    '布鞋': 'SHOES_CLOTH_SET1',
}

item = api_url + 'prices/' + t + '_' + chn[aa] + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon&qualities=' + qualities

r = requests.get(item)

price = pd.DataFrame(r.json())

st.write(price)
