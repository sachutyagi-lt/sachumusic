
from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is the music assistant service of @chatuniversemusic1.\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin from @Hindi_chattinggg_IND will see your message and join chat\n    - Don't add this user to secret groups.\n   - Don't Share private info here\n\n **FEEL FREE TO CONTACT US @Hindi_chattinggg_IND**")
  return                        
