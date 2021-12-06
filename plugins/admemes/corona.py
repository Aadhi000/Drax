import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/Movies_World02')]])

@Client.on_message(filters.command("covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await message.reply_text(
        text=covid_info(query),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**𝗖𝗼𝘃𝗶𝗱 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻**--

𝐂𝐨𝐮𝐧𝐭𝐫𝐲 : `{country}`
𝐀𝐜𝐭𝐢𝐯𝐞 : `{active}`
𝐂𝐨𝐧𝐟𝐢𝐫𝐦𝐞𝐝 : `{confirmed}`
𝐃𝐞𝐚𝐭𝐡𝐬 : `{deaths}`
𝐈𝐃 : `{info_id}`
𝐋𝐚𝐬𝐭 𝐔𝐩𝐝𝐚𝐭𝐞 : `{last_update}`
𝐋𝐚𝐭𝐢𝐭𝐮𝐝𝐞 : `{latitude}`
𝐋𝐨𝐧𝐠𝐢𝐭𝐮𝐝𝐞 : `{longitude}`
𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝 : `{recovered}`"""
        return covid_info
    except Exception as error:
        return error

