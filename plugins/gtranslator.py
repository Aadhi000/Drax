from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from .list import list
from database.gtrans_mdb import find_one

@Client.on_message(filters.command(["tr"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tr")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			hehek = InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            "✮ 𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩 ✮", url="https://t.me/Movies_World02"
                                        )                                 
                                    ],
                                ]
                            )
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"Translated from **{fromt.capitalize()}** To **{to.capitalize()}**\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			except:
			   	await message.reply_text(f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			

		except :
			print("error")
	else:
			 ms = await message.reply_text("𝐑𝐞𝐩𝐥𝐲 𝐓𝐨 𝐓𝐡𝐞 𝐓𝐞𝐱𝐭 𝐓𝐡𝐚𝐭 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐓𝐫𝐚𝐧𝐬𝐥𝐚𝐭𝐞 😊")
			 await ms.delete()
