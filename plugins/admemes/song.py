

from pyrogram import Client, filters

import youtube_dl
from youtube_search import YoutubeSearch
import requests

import os
import time

## Extra Fns -------------------------------

# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


## Commands --------------------------------

@Client.on_message(filters.command("song") & ~filters.channel & ~filters.edited)
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('`𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐒𝐨𝐧𝐠.....`')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"[𝙳𝚁𝙰𝚇 𝙼𝚄𝚂𝙸𝙲𝚂]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('**𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝 𝐀𝐧𝐲 𝐑𝐞𝐬𝐮𝐥𝐭.. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐭𝐫𝐲 𝐚𝐧𝐨𝐭𝐡𝐞𝐫 𝐬𝐨𝐧𝐠 𝐨𝐫 𝐮𝐬𝐞 𝐜𝐨𝐫𝐫𝐞𝐜𝐭 𝐬𝐩𝐞𝐥𝐥𝐢𝐧𝐠💕!**')
            return
    except Exception as e:
        m.edit(
            "**𝐄𝐧𝐭𝐞𝐫 𝐒𝐨𝐧𝐠 𝐍𝐚𝐦𝐞 𝐰𝐢𝐭𝐡 𝐂𝐨𝐦𝐦𝐚𝐧𝐝💕**❗\nFor 𝐄𝐱𝐚𝐦𝐩𝐥𝐞: `/song Alone Marshmellow`"
        )
        print(str(e))
        return
    m.edit("`𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠....𝐖𝐚𝐢𝐭.!`")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎶 <b>𝐓𝐢𝐭𝐥𝐞:</b> <a href="{link}">{title}</a>\n⏱️ <b>𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧:</b> <code>{duration}</code>\n✨ <b>𝐕𝐢𝐞𝐰𝐬:</b> <code>{views}</code>\n♻️ <b>𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐁𝐲:</b> {message.from_user.mention()} \n👩🏻‍💻 <b>𝑼𝒑𝒍𝒐𝒂𝒅𝒆𝒅 𝑩𝒚: @Movies_World02</b>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
        message.delete()
    except Exception as e:
        m.edit('**𝐀𝐧 𝐄𝐫𝐫𝐨𝐫 𝐎𝐜𝐜𝐮𝐫𝐞𝐝. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐈𝐧𝐟𝐨𝐫𝐦 ›› @BKC0001 !!**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
