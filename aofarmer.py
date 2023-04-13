import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

api_url = "https://east.albion-online-data.com/api/v2/stats/"

category_dict = {
    '配件': ['背包','披风'],
    '护甲': ['布帽','布甲','布鞋'],
    '法术武器': ['奥术法杖', '自然法杖'],
    '基础资源': ['布料', '纤维作物', '兽皮', '皮制品', '金属条', '矿石', '木条', '石材', '石砌块', '木材'],
}

id_dict = {

    '背包': 'BAG',
    '披风': 'CAPE',

    '布帽': 'HEAD_CLOTH_SET1',
    '布甲': 'ARMOR_CLOTH_SET1',
    '布鞋': 'SHOES_CLOTH_SET1',

    '自然法杖': 'MAIN_NATURESTAFF',
    '奥术法杖': 'MAIN_ARCANESTAFF',

    '布料': 'CLOTH',
    '纤维作物': 'FIBER',
    '兽皮': 'LEATHER',
    '皮制品': 'HIDE',
    '金属条': 'METALBAR',
    '矿石': 'ORE',
    '木条': 'PLANKS',
    '石材': 'ROCK',
    '石砌块': 'STONEBLOCK',
    '木材': 'WOOD',
}

st.write("# Albion Online Farmer! 👨‍🌾")

col_category, col_tier, col3 = st.columns(3)

with col_category:
    category = st.selectbox('类别', category_dict.keys())

with col_tier:
    tier = st.radio('等阶',('T1','T2','T3','T4','T5','T6','T7','T8'),horizontal=True)
    
# qualities = st.radio('qualities',('1','2','3','4','5'),horizontal=True)


# level = st.radio('level',('0','1','2','3','4'),horizontal=True)



# aa = st.selectbox('aa',category[category])

# ll = '@' + level 
# if ll=='@0':
#     ll = ''
# item = api_url + 'prices/' + t + '_' + chn[aa] + ll + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon&qualities=' + qualities

# r = requests.get(item)

# price = pd.DataFrame(r.json())

# st.write(price)

# hour = api_url + 'history/' + t + '_' + chn[aa] + ll + '.json?time-scale=1'
# x = requests.get(hour)
# xp = pd.DataFrame(x.json())

# my = pd.DataFrame(xp.loc[xp['location']=='Caerleon','data'].values[0])
# st.write(my)
