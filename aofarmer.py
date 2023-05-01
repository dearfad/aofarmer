"""
Filename: aofarmer.py
Author: dearfad
Contact: dearfad@sina.com
"""

import streamlit as st

# from scripts.category import CATEGORY, UNIQUENAME
# from scripts.aofcore import read_item_ids, get_prices_df
from scripts.aodata import get_ids, get_prices


st.set_page_config(page_title="Albion Online Farmer", page_icon="👨‍🌾", layout="wide")

st.write("# Albion Online Farmer! 👨‍🌾")


item_ids, location_ids = get_ids()
st.write(
    f"➖ **Item IDs: {item_ids.shape[0]}** ➖ **Location IDs: {location_ids.shape[0]}** ➖ 👨‍💼 **By: DEARFAD** ➖ "
)

st.write(get_prices(itemlist=["T5_BAG", "T6_BAG"]), use_container_width=True)

# col_server, col_category, col_sub_category = st.columns(3)

# with col_server:
#     server = st.selectbox("服务器", ["亚服", "国际服"])
#     api_dict = {
#         "亚服": "https://east.albion-online-data.com/api/v2/stats/",
#         "国际服": "https://albion-online-data.com/api/v2/stats/",
#     }
#     api_url = api_dict[server]

# with col_category:
#     category = st.selectbox("类别", CATEGORY.keys())

# with col_sub_category:
#     item = st.selectbox("亚类", CATEGORY[category])


# col_tier, col_enchantment, col_quality = st.columns(3)
# with col_tier:
#     tiers = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"]
#     tier = st.multiselect("等阶", tiers, ["T4"])

# with col_enchantment:
#     enchantments = ["0", "1", "2", "3", "4"]
#     enchantment = st.multiselect("附魔", enchantments, ["1"])

# with col_quality:
#     qualites = [1, 2, 3, 4, 5]
#     quality = st.multiselect("品质", qualites, [1])

# col_city, col_item = st.columns(2)

# with col_city:
#     cities = [
#         "Caerleon",
#         "Bridgewatch",
#         "Lymhurst",
#         "Fort Sterling",
#         "Thetford",
#         "Martlock",
#     ]
#     city = st.multiselect("城市", cities, ["Caerleon"])

# prices_df = get_prices_df(api_url, UNIQUENAME[item])

# with col_item:
#     types = prices_df["type"].unique()
#     type = st.multiselect("物品", types, types[0])

# columns = list(prices_df.columns)
# column = st.multiselect(
#     "显示",
#     columns,
#     [
#         "Name_CN",
#         "Tier",
#         "city",
#         "enchantment",
#         "quality",
#         "sell_price_min",
#         "sell_price_min_date",
#         "buy_price_max",
#         "buy_price_max_date",
#         "timestamp_24",
#         "avg_price_24",
#         "item_count_24",
#     ],
# )


# view_df = prices_df.loc[
#     (prices_df["city"].isin(city))
#     & (prices_df["Tier"].isin(tier))
#     & (prices_df["quality"].isin(quality))
#     & (prices_df["enchantment"].isin(enchantment))
#     & (prices_df["type"].isin(type))
# ]

# st.dataframe(view_df[column], use_container_width=True)
