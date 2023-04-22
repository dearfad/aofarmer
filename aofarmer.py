import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

st.write("# Albion Online Farmer! 👨‍🌾")

api_url = "https://east.albion-online-data.com/api/v2/stats/"

category_dict = {
    '配件': ['背包','披风'],
    '护甲': ['布甲','布帽','布鞋','皮甲','皮帽','皮鞋','板甲','板甲头盔','板甲长靴','稀有护甲','稀有头盔','稀有鞋子'],
    '神器': [],
    '城市资源': [],
    '消耗品': [],
    '农耕品': [],
    '家具': [],
    '采集装备': [],
    '工人': [],
    '奢侈品': [],
    '法术武器': ['奥术法杖', '自然法杖'],
    '基本材料': [],
    '近战武器': [],
    '坐骑': [],
    '副手': [],
    '其他': [],
    '制造品': [],
    '远程武器': [],
    '基础资源': ['布料', '纤维作物', '兽皮', '皮制品', '金属条', '矿石', '木条', '石材', '石砌块', '木材'],
    '书卷': [],
    '代币': [],
    '工具': [],
    '战利品装饰': [],
}

id_dict = {

    '背包': 'BAG',
    '披风': 'CAPE',

    '布帽': 'HEAD_CLOTH_SET1',
    '布甲': 'ARMOR_CLOTH_SET1',
    '布鞋': 'SHOES_CLOTH_SET1',

    '自然法杖': 'MAIN_NATURESTAFF',
    '奥术法杖': 'MAIN_ARCANESTAFF',

    # ==== 基础资源 ====
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

col_category, col_id = st.columns(2)

with col_category:
    category = st.selectbox('类别', category_dict.keys())
with col_id:
    id = st.selectbox('物品', category_dict[category])

item_id = id_dict[id]

item_list = ['BAG', 'BAG_INSIGHT']
bag_list = 'T2_BAG, T3_BAG'
for item in item_list:
    for tier in range(4,9):
        bag_list = bag_list + ', '+ f'T{tier}_{item}' 
search_url = api_url + 'prices/' + bag_list + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon'
st.write(len(search_url))
st.write(search_url)
r = requests.get(search_url)
prices = pd.DataFrame(r.json())
st.write(prices)

    # cities = ['Caerleon','Bridgewatch','Lymhurst','Fort Sterling','Thetford','Martlock']
    # cols_prices = st.columns(len(cities))
    # for i, city in enumerate(cities):
    #     with cols_prices[i]:
    #         sell_min_price = int(prices.loc[prices['city']==city, 'sell_price_min'])
    #         buy_max_price =  int(prices.loc[prices['city']==city, 'buy_price_max'])
    #         if sell_min_price == 0 or buy_max_price == 0:
    #             diff_price = None
    #         else:
    #             diff_price = buy_max_price-sell_min_price
    #         st.metric(f':classical_building: **{city}**', sell_min_price, diff_price)

#     history_hour_url = api_url + 'history/' + item_id + '.json?time-scale=1'
#     r_history_hour = requests.get(history_hour_url)
#     history_hour = pd.DataFrame(r_history_hour.json())

#     col_bridgewatch, col_limhurst,col_FortSterling,col_Thetford,col_Martlock,col_Caerleon = st.columns(6)
#     with col_bridgewatch:
#         item_history_hour = pd.DataFrame(history_hour.loc[history_hour['location']=='Bridgewatch','data'].values[0])
#         st.write('Bridgewatch')
#         st.write(item_history_hour.iloc[-9:-1,:2])
#     with col_limhurst:
#         item_history_hour = pd.DataFrame(history_hour.loc[history_hour['location']=='Lymhurst','data'].values[0])
#         st.write('Lymhurst')
#         st.write(item_history_hour.iloc[-9:-1,:2])
#     with col_FortSterling:
#         item_history_hour = pd.DataFrame(history_hour.loc[history_hour['location']=='Fort Sterling','data'].values[0])
#         st.write('Fort Sterling')
#         st.write(item_history_hour.iloc[-9:-1,:2])
#     with col_Thetford:
#         item_history_hour = pd.DataFrame(history_hour.loc[history_hour['location']=='Thetford','data'].values[0])
#         st.write('Thetford')
#         st.write(item_history_hour.iloc[-9:-1,:2])
#     with col_Martlock:
#         item_history_hour = pd.DataFrame(history_hour.loc[history_hour['location']=='Martlock','data'].values[0])
#         st.write('Martlock')
#         st.write(item_history_hour.iloc[-9:-1,:2])
#     with col_Caerleon:
#         item_history_hour = pd.DataFrame(history_hour.loc[history_hour['location']=='Caerleon','data'].values[0])
#         st.write('Caerleon')
#         st.write(item_history_hour.iloc[-9:-1,:2])
