import streamlit as st
import pandas as pd
import requests

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


@st.cache_data(show_spinner=False,ttl=600.0)
def get_prices(itemlist):
    query = [f'T2_{itemlist[0]},T3_{itemlist[0]}']
    n=0
    for item in itemlist:
        for tier in range(4,9):
            for enchantment in range(0,5):
                if len(query[n] + ','+ f'T{tier}_{item}@{enchantment}')>1800:
                    n = n+1
                    query.append('')
                if enchantment == 0:
                    query[n] = query[n] + ','+ f'T{tier}_{item}' 
                else:
                    query[n] = query[n] + ','+ f'T{tier}_{item}@{enchantment}' 

    prices = pd.DataFrame()
    history_24 = pd.DataFrame()
    history_6 = pd.DataFrame()
    for q in query:
        search_url = api_url + 'prices/' + q + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon'
        r = requests.get(search_url)
        prices_temp = pd.DataFrame(r.json())
        prices = pd.concat([prices, prices_temp], ignore_index=True)
        
        history_24_url = api_url + 'history/' + q + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon&time-scale=24'
        r = requests.get(history_24_url)
        history_temp = pd.DataFrame(r.json())
        history_24 = pd.concat([history_24, history_temp], ignore_index=True)

        history_6_url = api_url + 'history/' + q + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon&time-scale=1'
        r = requests.get(history_6_url)
        history_temp = pd.DataFrame(r.json())
        history_6 = pd.concat([history_6, history_temp], ignore_index=True)
    
    prices['mergekey'] = prices['item_id'].map(str) + '-' + prices['city'].map(str) + '-' + prices['quality'].map(str)
    history_24['mergekey'] = history_24['item_id'].map(str) + '-' + history_24['location'].map(str) + '-' + history_24['quality'].map(str)
    history_6['mergekey'] = history_6['item_id'].map(str) + '-' + history_6['location'].map(str) + '-' + history_6['quality'].map(str)
    prices = prices.merge(history_24, how='left', on='mergekey')
    prices = prices.merge(history_6, how='left', on='mergekey')
    st.write(prices.head(5))
    prices.drop(['mergekey','location','item_id_y','quality_y'],axis=1, inplace=True)
    prices.rename(columns={'item_id_x': 'item_id', 'quality_x': 'quality'}, inplace=True)
    # st.write(prices.data.loc[0])
    prices['timestamp'] = prices['data'].apply(lambda x:x[-1]['timestamp'] if isinstance(x, list) else 0)
    prices['avg_price'] = prices['data'].apply(lambda x:x[-1]['avg_price'] if isinstance(x, list) else 0)
    prices['item_count_24'] = prices['data'].apply(lambda x:x[-1]['item_count'] if isinstance(x, list) else 0)
    prices.drop('data', axis=1, inplace=True)
    return prices

def get_prices_df(itemlist):
    prices_df = get_prices(itemlist)
    item_ids = read_item_ids()
    prices_df['Name_CN'] = prices_df['item_id'].apply(lambda x:item_ids.loc[item_ids['UniqueName']==x, 'Name_CN'].values[0])
    prices_df['Tier'] = prices_df['item_id'].apply(lambda x:x.split('_')[0])
    prices_df['enchantment'] = prices_df['item_id'].apply(lambda x:x.split('@')[1] if '@' in x else '0')
    prices_df['type'] = prices_df['Name_CN'].apply(lambda x:x.split('级')[1])
    columns =["Name_CN","Tier","item_id","city","enchantment","quality","type","sell_price_min","sell_price_min_date","sell_price_max","sell_price_max_date","buy_price_min",
            "buy_price_min_date","buy_price_max","buy_price_max_date","timestamp","avg_price","item_count_24"]
    prices_df = prices_df.reindex(columns=columns)
    return prices_df