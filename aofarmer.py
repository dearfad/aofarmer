import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

api_url = "https://east.albion-online-data.com/api/v2/stats/"

items_url = 'https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json'

image_url = 'https://render.albiononline.com/v1/item/'

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

@st.cache_data
def read_items_info():
    items = pd.read_json(items_url)
    items.set_index('UniqueName', inplace=True)
    return items
items = read_items_info()

st.write("# Albion Online Farmer! 👨‍🌾")

col_category, col_item, col_tier, col_enchantment, col_quality = st.columns(5)

with col_category:
    category = st.selectbox('类别', category_dict.keys())

with col_item:
    item = st.selectbox('物品', category_dict[category])

with col_tier:
    tier = st.selectbox('等阶', ('T1','T2','T3','T4','T5','T6','T7','T8'))

with col_enchantment:
    enchantment = st.selectbox('附魔', ('0','1','2','3','4'))

with col_quality:
    quality = st.selectbox('品质', ('1','2','3','4','5'))

if category == '基础资源':
    level = '_LEVEL' + enchantment
    if enchantment == '0':
        item_id = tier + '_' + id_dict[item]
    else:
        item_id = tier + '_' + id_dict[item] + '_LEVEL' + enchantment + '@' + enchantment
else:
    item_id = tier + '_' + id_dict[item]

col_item_info, col_item_price = st.columns([1,3])



with col_item_info:
    if item_id in items.index.values:
        item_name = items.loc[item_id, 'LocalizedNames']['ZH-CN']
        item_description = items.loc[item_id, 'LocalizedDescriptions']['ZH-CN']
        item_image_url = image_url + item_id + '.png' + '?quality=' + quality
        st.image(item_image_url)
    else:
        item_image_url = 'https://render.albiononline.com/v1/destiny/ADVENTURER_ADEPT.png'
        st.image(item_image_url)
        item_name = '此物并不存在'
        item_description = ''
    st.header(item_name)
    st.write(item_description)
    st.write('UniqueName: ', item_id)

with col_item_price:
    search_url = api_url + 'prices/' + item_id + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon&qualities=' + quality
    r = requests.get(search_url)
    prices = pd.DataFrame(r.json())
    prices.set_index('city', inplace=True)
    st.markdown('**:red[Caerleon]**:')
    st.write(prices.loc['Caerleon', 'sell_price_min'], '--', prices.loc['Caerleon', 'buy_price_max'])
    st.markdown('**:orange[Bridgewatch]**: ')
    st.markdown('**:green[Lymhurst]**: ')
    st.markdown('**:blue[Fort Sterling]**: ')
    st.markdown('**:violet[Thetford]**: ')
    st.markdown('**Martlock**: ')
    st.write(prices)

# hour = api_url + 'history/' + t + '_' + chn[aa] + ll + '.json?time-scale=1'
# x = requests.get(hour)
# xp = pd.DataFrame(x.json())

# my = pd.DataFrame(xp.loc[xp['location']=='Caerleon','data'].values[0])
# st.write(my)

