import streamlit as st
import pandas as pd
import requests
from scripts.category import CATEGORY, UNIQUENAME
from scripts.aodata import read_item_ids, get_prices_df

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

st.write("# Albion Online Farmer! 👨‍🌾")



item_ids = read_item_ids()

st.write(f"*️⃣ **Total: {item_ids.shape[0]}** ➖ 👨‍💼 **By: DEARFAD** ➖")


col_server, col_category, col_sub_category  = st.columns(3)

with col_server:
    server = st.selectbox('服务器', ['亚服','国际服'])
    api_dict = {
        '亚服': 'https://east.albion-online-data.com/api/v2/stats/',
        '国际服': 'https://albion-online-data.com/api/v2/stats/',
    }
    api_url = api_dict[server]

with col_category:
    category = st.selectbox('类别', CATEGORY.keys())

with col_sub_category:
    item = st.selectbox('亚类', CATEGORY[category])


col_tier, col_enchantment, col_quality = st.columns(3)
with col_tier:
    tiers = ['T1','T2','T3','T4','T5','T6','T7','T8']
    tier = st.multiselect('等阶',tiers,['T4'])

with col_enchantment:
    enchantments = ['0','1','2','3','4']
    enchantment = st.multiselect('附魔',enchantments,['1'])

with col_quality:
    qualites = [1,2,3,4,5]
    quality = st.multiselect('品质',qualites,[1])

col_city, col_item = st.column(2)

with col_city:
    cities = ['Caerleon','Bridgewatch','Lymhurst','Fort Sterling','Thetford','Martlock']
    city = st.multiselect('城市',cities,['Caerleon'])

prices_df = get_prices_df(api_url, UNIQUENAME[item])

with col_item:
    types = prices_df['type'].unique()
    type = st.multiselect('物品',types,types[0])

columns = list(prices_df.columns)
column = st.multiselect('显示',columns,['Name_CN','Tier','city','enchantment','quality','sell_price_min','sell_price_min_date','buy_price_max','buy_price_max_date','timestamp_24','avg_price_24','item_count_24'])



view_df = prices_df.loc[
    (prices_df['city'].isin(city)) & 
    (prices_df['Tier'].isin(tier)) & 
    (prices_df['quality'].isin(quality)) &
    (prices_df['enchantment'].isin(enchantment)) &
    (prices_df['type'].isin(type)) 
]

st.dataframe(view_df[column],use_container_width=True)



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
