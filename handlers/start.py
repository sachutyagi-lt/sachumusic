from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CRVA9-gABByMRYIZjxocQxAh3Z5UrUPwuLKCfIDMAAqgCAAI3yjBU3MpuQNTjE3oeBA")
    await message.reply_text(
                f""" <b>Hey {message.from_user.first_name}!  I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n๐ด Do you want me to play music in your Telegram groups'voice chats? Please click the \'๐ User Manual ๐\' button below to know how you can use me.\n\n๐ด The [Assistant](https://t.me/Chatuniversemusic1) must be in your group to play music in the voice chat of your group.\n\n๐ด More info & commands mentioned in the [User Manual](https://telegra.ph/Chatuniversemusic1bot-04-14)\n\nA project by @UNIQUEGURI ๐ฎ๐ณ\n\nโ Join our bots channel and group\n๐ฐ@Hindi_chattinggg_IND 
 </b>""",
      
       reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "๐ User Manual ๐", url="https://telegra.ph/Chatuniversemusic1bot-04-14")
                  ],[
                    InlineKeyboardButton(
                        "๐จโ๐ป Owner ๐จโ๐ป", url="https://t.me/UNIQUEGURI"
                    )
                   ],[
                    InlineKeyboardButton(
                        "Support channel๐๏ธ" , url="https://t.me/cuXmusic"
                  )
                ],[ 
                    InlineKeyboardButton(
                        "Support Chat ๐๏ธ", url="https://t.me/Hindi_chattinggg_IND"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )
        

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "๐ดcuXmusic player is online ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Support Channel", url="https://t.me/cuXmusic"
                    )
                ],[
                    InlineKeyboardButton(
                        "โ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No โ", callback_data="close"
                    )
                ]
            ]
        )
    )
