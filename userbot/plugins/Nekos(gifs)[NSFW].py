#Serious Kangers can take the Credits xD, by @WhySooSerious
#From Nekos API
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
from userbot import CMD_HELP

@borg.on(admin_cmd("sologif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Solo GIF..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
            await borg.send_message(chat, "/sologif")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @KeikoSDbot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("cumgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Henti Cum GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
            await borg.send_message(chat, "/cumgif")
            response = await response
        except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
        if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
            await event.delete()
            await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("ngif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Neko GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/ngif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("tickle"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Tickle GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/tickle")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("feed"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Feeding GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/feed")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("bjgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Blow Job GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/bjgif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
    #By @WhySooSerious

@borg.on(admin_cmd("analgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Anal GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/bj")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("poke"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Poke GIF..```\n**Oh! It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/poke")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("pussygif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Pussy GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/pussygif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious

@borg.on(admin_cmd("hentaigif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/hentaigif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious

@borg.on(admin_cmd("classic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Classic GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/classic")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("kuni"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Pussy Lick GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/kuni")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("cuddle"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Cuddle GIF..```\n**WARNING : It's Really Kawaii**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/cuddle")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("titsgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Tits GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/titsgif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#by @WhySooSerious
@borg.on(admin_cmd("smug"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Smug GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/smug")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd("baka"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Baka GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/bj")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)

#By @WhySooSerious

@borg.on(admin_cmd("lesbian"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an A Hentai Lesbian GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/lesbian")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious

@borg.on(admin_cmd("nsfwneko"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an A Hentai Neko GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/nekonsfw")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious

@borg.on(admin_cmd("kiss"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an an Anime Kissing GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/kiss")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious


CMD_HELP.update({
    "nekos(gifs)":
    "**Nekos (gifs) [NSFW]**\n\n\
    What it Does?\
    Sends a Random (NSFW/SFW) Gifs to your current Chat.\n\n\
    ???????? Commands ????????\n\n\
    .kiss - Sends Random Kissing GIFs\
    \n.sologif -  Sends Random Solo GIFs.\
    \n.cumgif - Sends Random Cum GIFs.\
    \n.ngif- Sends Random Neko GIFs.\
    \n.tickle - Sends Random Tickle GIFs.\
    \n.feed - Sends Random Feeding GIFs.\
    \n.bjgif - Sends Random Blow Job GIFs.\
    \n.analgif - Sends Random Anal GIFs.\
    \n.poke - Sends Random Poke GIFs.\
    \n.pussygif - Sends Random Pussy GIFs.\
    \n.hentaigif - Sends Random Hentai GIFs.\
    \n.classic - Sends Random Classic Hentai GIFs.\
    \n.kuni - Sends Random Pussy Lick GIFs.\
    \n.cuddle -  Sends Random Cuddle GIFs.\
    \n.titsgif - Sends Random Tits GIFs.\
    \n.smug - Sends Random Smug GIFs.\
    \n.baka - Sends Random Baka Shout GIFs.\
    \n.lesbian - Sends Random Les Source GIFs.\
    \n.nsfwneko - Sends Random NSFW Neko source GIFs.\
    \n\nPlugin by @WhySooSerious"
})