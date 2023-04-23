import streamlit as st
import pandas as pd
import requests
from scripts import CATEGORY

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

st.write("# Albion Online Farmer! 👨‍🌾")

api_url = "https://east.albion-online-data.com/api/v2/stats/"

item_ids_url = 'https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json'

@st.cache_data
def read_item_ids():
    ao_bin_dumps = pd.read_json(item_ids_url)
    item_ids = pd.DataFrame()
    item_ids['UniqueName'] = ao_bin_dumps['UniqueName']
    item_ids['Name_CN'] = ao_bin_dumps['LocalizedNames'].apply(lambda x:x["ZH-CN"] if x else '')
    item_ids['Description_CN'] = ao_bin_dumps['LocalizedDescriptions'].apply(lambda x:x["ZH-CN"] if x else '')
    item_ids['Name_EN'] = ao_bin_dumps['LocalizedNames'].apply(lambda x:x["EN-US"] if x else '')
    item_ids['Description_EN'] = ao_bin_dumps['LocalizedDescriptions'].apply(lambda x:x["EN-US"] if x else '')
    return item_ids

item_ids = read_item_ids()

st.write(item_ids)

st.write(CATEGORY)





# col_category, col_id, col_item = st.columns(2)

# with col_category:
#     category = st.selectbox('类别', category_dict.keys())
# with col_id:
#     id = st.selectbox('ID', category_dict[category])
# with col_item:
#     item = st.selectbox('ITEM', item_dict[id])


# item_id = id_dict[id]

# item_list = ['BAG', 'BAG_INSIGHT']
# bag_list = 'T2_BAG,T3_BAG'
# for item in item_list:
#     for tier in range(4,9):
#         bag_list = bag_list + ','+ f'T{tier}_{item}' 
# search_url = api_url + 'prices/' + bag_list + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon'
# st.write(len(search_url))
# st.write(search_url)
# r = requests.get(search_url)
# prices = pd.DataFrame(r.json())
# st.write(prices)

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
