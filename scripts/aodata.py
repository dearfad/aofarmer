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

# Item IDs
Item_IDs_Url = (
    "https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json"
)

# Location IDs
Location_IDs_Url = (
    "https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/world.json"
)


@st.cache_data(ttl=86400, show_spinner="Caching Item IDs Every 24 Hours...")
def get_ids():
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
    item_ids.drop(
        [
            "LocalizationNameVariable",
            "LocalizationDescriptionVariable",
            "LocalizedNames",
            "LocalizedDescriptions",
            "Index",
        ],
        axis=1,
        inplace=True,
    )

    location_ids = pd.read_json(Location_IDs_Url)

    return item_ids, location_ids


def get_prices(server='east', itemlist='T4_BAG', format='json'):
    r = requests.get(f'https://{server}.albion-online-data.com/api/v2/stats/Prices/{itemlist}.{format}')
    prices = pd.DataFrame(r.json())
    return prices