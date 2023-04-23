import streamlit as st
import pandas as pd
import requests
from scripts.category import CATEGORY, UNIQUENAME
from scripts.aodata import read_item_ids, get_prices_df

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

st.write("# Albion Online Farmer! 👨‍🌾")

item_ids = read_item_ids()

st.write(f"*️⃣ **Total: {item_ids.shape[0]}** ➖ 👨‍💼 **By: DEARFAD** ➖")

col_category, col_item, col_tier, col_quality, col_city, col_enchantment = st.columns(6)

with col_category:
    category = st.selectbox('类别', CATEGORY.keys())
with col_item:
    item = st.selectbox('ID', CATEGORY[category])
with col_tier:
    tiers = ['T1','T2','T3','T4','T5','T6','T7','T8']
    tier = st.multiselect('tier',tiers,tiers)
with col_quality:
    qualites = [1,2,3,4,5]
    quality = st.multiselect('quality',qualites,qualites)
with col_city:
    cities = ['Caerleon','Bridgewatch','Lymhurst','Fort Sterling','Thetford','Martlock']
    city = st.multiselect('city',cities,cities)
with col_enchantment:
    enchantments = ['0','1','2','3','4']
    enchantment = st.multiselect('enchantment',enchantments,enchantments)

prices_df = get_prices_df(UNIQUENAME[item])

columns = list(prices_df.columns)
column = st.multiselect('column',columns,columns)



view_df = prices_df.loc[
    (prices_df['city'].isin(city)) & 
    (prices_df['Tier'].isin(tier)) & 
    (prices_df['quality'].isin(quality)) &
    (prices_df['enchantment'].isin(enchantment)) 
]

names = view_df['Name_CN'].unique()
name = st.multiselect('Name',names,names)
print_df = view_df.loc[prices_df['Name_CN'].isin(name)]


st.dataframe(print_df[column],use_container_width=True)



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
