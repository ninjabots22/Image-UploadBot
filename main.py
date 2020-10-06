from pyrogram import Client, filters
import os, shutil
from creds import my
from telegraph import upload_file
import logging

logging.basicConfig(level=logging.INFO)


TGraph = Client(
    "Image upload bot",
    bot_token = my.BOT_TOKEN,
    api_id = my.API_ID,
    api_hash = my.API_HASH
)


@TGraph.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(f"<b>Hey {message.from_user.first_name}, Welcome to this bot</b>\n\nI can Upload Any Photos to Telegraph! Type /cmds to know the Available Commands\n\n<b>💠 I'm made by @Ninja_Bots</b>", True)
 
@TGraph.on_message(filters.command("cmds"))
async def cmds(client, message):
    await message.reply_text(f"<b>Available Commands\n\n/start - Restarts the Bot\n/help - How to use the Bot\n/cmds - Brings up this message\n/info - Info about the Bot\n\n💠 I'm made by @Ninja_Bots</b>", True)
 
@TGraph.on_message(filters.command("info"))
async def info(client, message):
    await message.reply_text(f"<b>I'm a Telegraph Photo Uploader Bot.\nYou can Send any photos and get the telegraph link in return\n\nⓂ️ I'm Hosted on 200$ VPS on Azure.\n\n💠 I'm made by @Ninja_Bots</b>", True)

@TGraph.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_text(f"<b>How to Use?</b>\n\nJust send any Photo and wait for few seconds.\nI will upload it to Telegraph and send it's link to you!", True)

@TGraph.on_message(filters.photo)
async def getimage(client, message):
    tmp = os.path.join("downloads",str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    imgdir = tmp + "/" + str(message.message_id) +".jpg"
    dwn = await message.reply_text("💠Processing Using Ninja Bots Server.", True)    
    await dwn.edit_text("💠Processing Using Ninja Bots Server..")
    await dwn.edit_text("💠Processing Using Ninja Bots Server...")
    await dwn.edit_text("💠Connecting to VPS..")
    await dwn.edit_text("💠Connecting to VPS...")
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("💠Successfully Uploaded!...")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    shutil.rmtree(tmp,ignore_errors=True)


TGraph.run()
