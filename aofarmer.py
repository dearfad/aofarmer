import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='Albion Online Farmer', page_icon='👨‍🌾', layout="wide")

st.write("# Albion Online Farmer! 👨‍🌾")

api_url = "https://east.albion-online-data.com/api/v2/stats/"

items_url = 'https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json'

image_url = 'https://render.albiononline.com/v1/item/'


@st.cache_data
def read_items_info():
    items = pd.read_json(items_url)
    # items.set_index('UniqueName', inplace=True)
    return items
items = read_items_info()

st.write(f"*️⃣ **Total: {items.shape[0]}** ➖ 👨‍💼 **By: DEARFAD** ➖")

st.write(items)

# col_eng, col_chn = st.columns(2)
# with col_eng:
#     input_name_en = st.text_input('英文模糊搜索：', 'ORE')
#     search_result_en = items[items.index.str.contains(input_name_en.strip(), case=False)]
#     st.write(search_result_en.index)

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
# with col_chn:
#     input_name_chn = st.text_input('中文模糊搜索：', '矿石')
#     search_result_chn = items[items.index.str.contains(input_name_chn.strip(), case=False)]
#     st.write(search_result_chn['UniqueName'])

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

# col_item_info, col_item_price = st.columns([1,3])



# with col_item_info:
#     if item_id in items.index.values:
#         item_name = items.loc[item_id, 'LocalizedNames']['ZH-CN']
#         item_description = items.loc[item_id, 'LocalizedDescriptions']['ZH-CN']
#         item_image_url = image_url + item_id + '.png' + '?quality=' + quality
#         st.image(item_image_url)
#     else:
#         item_image_url = 'https://render.albiononline.com/v1/destiny/ADVENTURER_ADEPT.png'
#         st.image(item_image_url)
#         item_name = '此物并不存在'
#         item_description = ''
#     st.header(item_name)
#     st.write(item_description)
#     st.write('UniqueName: ', item_id)

# with col_item_price:
#     search_url = api_url + 'prices/' + item_id + '.json?locations=Bridgewatch,Lymhurst,Fort Sterling,Thetford,Martlock,Caerleon&qualities=' + quality
#     r = requests.get(search_url)
#     prices = pd.DataFrame(r.json())
#     st.write(prices[['city','sell_price_min','buy_price_max']])

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

