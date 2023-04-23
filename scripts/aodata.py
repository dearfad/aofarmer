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

def get_prices(itemlist):
    query = f'T2_{itemlist[0]},T3_{itemlist[0]}'
    for item in itemlist:
        for tier in range(4,9):
            query = query + ','+ f'T{tier}_{item}' 
    search_url = api_url + 'prices/' + query + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon'
    st.write(len(search_url))
    st.write(search_url)
    r = requests.get(search_url)
    prices = pd.DataFrame(r.json())
    return prices

def get_prices_df(itemlist):
    prices_df = get_prices(itemlist)
    items_ids = read_item_ids()
    prices_df['Name_CN'] = prices_df['item_id'].apply(lambda x:items_ids.loc[items_ids['UniqueName']==x, 'Name_CN'])
    return prices_df