from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("Share Your Link" ,url=f"https://t.me/share/url?url=https://t.me/SHRENAME_BOT?start={message.from_user.id}") ]   ])
    await message.reply_text(f"Refer And Earn Get 1000MB Upload Limit\nPer Refer 1000MB\n Your Link :- https://t.me/SHRENAME_BOT?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
