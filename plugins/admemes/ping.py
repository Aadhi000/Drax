"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "വെറുതെ 𝐀𝐥𝐢𝐯𝐞 അടിച്ചു വെറുപ്പിക്കാതട ഞാൻ ഇവിടെ ജീവനോടെ ഒക്കെ തന്നെ ഒണ്ട്. ചത്തൊന്നും പോയിട്ടില്ല😁😄\n\n ✮𝐌𝐲 𝐜𝐫𝐞𝐚𝐭𝐨𝐫: [Aadhi](https://t.me/BKC0001)\n\n✮𝐌𝐲 𝐬𝐮𝐩𝐩𝐨𝐫𝐭: @cinemahubmoviesS\n\n⍟𝐌𝐲 𝐮𝐩𝐝𝐚𝐭𝐞𝐬: @NewOTTmoviesAll\n\n⍟𝐌𝐲 𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐫: @MagnusTG"
HELP = "𝐅𝐢𝐧𝐝 𝐘𝐨𝐮𝐫 𝐎𝐰𝐧 𝐖𝐚𝐲 𝐁𝐫𝐨..😁"
REPO = "https://github.com/Aadhi000/Drax"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
