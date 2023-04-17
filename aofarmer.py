import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

st.write("# Albion Online Farmer! 👨‍🌾")

api_url = "https://east.albion-online-data.com/api/v2/stats/"

item_ids_url = 'https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json'

image_url = 'https://render.albiononline.com/v1/item/'


@st.cache_data
def read_items_info():
    ao_bin_dumps = pd.read_json(item_ids_url)
    item_ids = pd.DataFrame()
    item_ids['UniqueName'] = ao_bin_dumps['UniqueName']
    item_ids['Name_CN'] = ao_bin_dumps['LocalizedNames'].apply(lambda x:x["ZH-CN"] if x else '')
    item_ids['Description_CN'] = ao_bin_dumps['LocalizedDescriptions'].apply(lambda x:x["ZH-CN"] if x else '')
    item_ids['Name_EN'] = ao_bin_dumps['LocalizedNames'].apply(lambda x:x["EN-US"] if x else '')
    item_ids['Description_EN'] = ao_bin_dumps['LocalizedDescriptions'].apply(lambda x:x["EN-US"] if x else '')
    return item_ids

item_ids = read_items_info()

st.write(f"*️⃣ **Total: {item_ids.shape[0]}** ➖ 👨‍💼 **By: DEARFAD** ➖")

col_search, col_result, col_quality = st.columns([1,4,1])

with col_search:
    input_name = st.text_input('模糊搜索：', 'ORE')

with col_result:
    search_result = item_ids[item_ids['UniqueName'].str.contains(input_name.strip(), case=False) | item_ids['Name_CN'].str.contains(input_name.strip(), case=False) | item_ids['Name_EN'].str.contains(input_name.strip(), case=False)]
    if search_result:
        selected_item = st.selectbox('搜索结果：', search_result['Name_CN'] + ' = ' + search_result['UniqueName'] + ' = ' + search_result['Description_CN'])
    else:
        selected_item = st.selectbox('搜索结果', 'T4_BAG')

with col_quality:
    quality = st.selectbox('品质', ('1','2','3','4','5'))

col_item_info, col_item_price = st.columns([1,2])

with col_item_info:
    name, uniquename, description = selected_item.split(' = ')
    item_image_url = image_url + uniquename + '.png' + '?quality=' + quality
    st.image(item_image_url)
    st.header(name)
    st.write(description)
    st.write(uniquename)

with col_item_price:
    search_url = api_url + 'prices/' + uniquename + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon&qualities=' + quality
    r = requests.get(search_url)
    prices = pd.DataFrame(r.json())
    # st.write(prices[['city','sell_price_min','buy_price_max']])
    st.write(prices)

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




# category_dict = {
#     '配件': ['背包','披风'],
#     '护甲': ['布帽','布甲','布鞋'],
#     '法术武器': ['奥术法杖', '自然法杖'],
#     '基础资源': ['布料', '纤维作物', '兽皮', '皮制品', '金属条', '矿石', '木条', '石材', '石砌块', '木材'],
# }

# id_dict = {

#     '背包': 'BAG',
#     '披风': 'CAPE',

#     '布帽': 'HEAD_CLOTH_SET1',
#     '布甲': 'ARMOR_CLOTH_SET1',
#     '布鞋': 'SHOES_CLOTH_SET1',

#     '自然法杖': 'MAIN_NATURESTAFF',
#     '奥术法杖': 'MAIN_ARCANESTAFF',

#     # ==== 基础资源 ====
#     '布料': 'CLOTH',
#     '纤维作物': 'FIBER',
#     '兽皮': 'LEATHER',
#     '皮制品': 'HIDE',
#     '金属条': 'METALBAR',
#     '矿石': 'ORE',
#     '木条': 'PLANKS',
#     '石材': 'ROCK',
#     '石砌块': 'STONEBLOCK',
#     '木材': 'WOOD',
# }


# if search_result.empty:
#     st.warning('未找到相关信息...')
#     url_name = ''
# else:    
#     selected_name = st.selectbox('已发现：', search_result['UniqueName'])

# col_category, col_item, col_tier, col_enchantment, col_quality = st.columns(5)

# with col_category:
#     category = st.selectbox('类别', category_dict.keys())

# with col_item:
#     item = st.selectbox('物品', category_dict[category])

# with col_tier:
#     tier = st.selectbox('等阶', ('T1','T2','T3','T4','T5','T6','T7','T8'))

# with col_enchantment:
#     enchantment = st.selectbox('附魔', ('0','1','2','3','4'))

# with col_quality:
#     quality = st.selectbox('品质', ('1','2','3','4','5'))

# if category == '基础资源':
#     level = '_LEVEL' + enchantment
#     if enchantment == '0':
#         item_id = tier + '_' + id_dict[item]
#     else:
#         item_id = tier + '_' + id_dict[item] + '_LEVEL' + enchantment + '@' + enchantment
# else:
#     item_id = tier + '_' + id_dict[item]





