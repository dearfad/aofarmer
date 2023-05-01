"""
Filename: aodata.py
Author: dearfad
Contact: dearfad@sina.com

Albion Data Project
site: https://www.albion-online-data.com/
"""

import streamlit as st
import requests
import pandas as pd

# API Host URLs
West_Server_Url = "https://west.albion-online-data.com"
East_Server_Url = "https://east.albion-online-data.com"

# Item IDs
Item_IDs_Url = (
    "https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json"
)

# Location IDs
Location_IDs_Url = (
    "https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/world.json"
)


@st.cache_data(ttl=86400, show_spinner="Caching Item IDs Every 24 Hours...")
def get_item_ids():
    item_ids = pd.read_json(Item_IDs_Url)
    item_ids["Name_CN"] = item_ids["LocalizedNames"].apply(
        lambda x: x["ZH-CN"] if x else ""
    )
    item_ids["Description_CN"] = item_ids["LocalizedDescriptions"].apply(
        lambda x: x["ZH-CN"] if x else ""
    )
    item_ids["Name_EN"] = item_ids["LocalizedNames"].apply(
        lambda x: x["EN-US"] if x else ""
    )
    item_ids["Description_EN"] = item_ids["LocalizedDescriptions"].apply(
        lambda x: x["EN-US"] if x else ""
    )
    item_ids.drop(['LocalizedNames','LocalizedDescriptions'],axis=1, inplace=True)
    return item_ids
