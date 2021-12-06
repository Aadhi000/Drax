from pyrogram import Client, filters

# Sticker ID 
@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**𝐒𝐭𝐢𝐜𝐤𝐞𝐫 𝐈𝐃 ››**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** 𝐔𝐧𝐢𝐪𝐮𝐞 𝐈𝐃 ›› ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("𝐈𝐭𝐬 𝐍𝐨𝐭 𝐚 𝐒𝐭𝐢𝐜𝐤𝐞𝐫 𝐅𝐢𝐥𝐞")

