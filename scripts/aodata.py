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
    "https://github.com/ao-data/ao-bin-dumps/blob/master/formatted/items.json"
)

# Location IDs
Location_IDs_Url = (
    "https://github.com/ao-data/ao-bin-dumps/blob/master/formatted/world.json"
)


@st.cache_data(ttl=86400, show_spinner="Caching Item IDs Every 24 Hours...")
def read_item_ids():
    ao_bin_dumps = pd.read_json(Item_IDs_Url)
    item_ids = pd.DataFrame()
    item_ids["UniqueName"] = ao_bin_dumps["UniqueName"]
    item_ids["Name_CN"] = ao_bin_dumps["LocalizedNames"].apply(
        lambda x: x["ZH-CN"] if x else ""
    )
    item_ids["Description_CN"] = ao_bin_dumps["LocalizedDescriptions"].apply(
        lambda x: x["ZH-CN"] if x else ""
    )
    item_ids["Name_EN"] = ao_bin_dumps["LocalizedNames"].apply(
        lambda x: x["EN-US"] if x else ""
    )
    item_ids["Description_EN"] = ao_bin_dumps["LocalizedDescriptions"].apply(
        lambda x: x["EN-US"] if x else ""
    )
    return item_ids
