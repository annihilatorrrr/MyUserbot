"""use command .ducduckgo
     Ā© Ultroid"""

from telethon import events
import os
import requests
import json
from uniborg.util import admin_cmd


@borg.on(admin_cmd("ducduckgo (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ","+"))
    if sample_url:
        link = sample_url.rstrip()
        await event.edit("Let me š¦ DuckDuckGo that for you:\nš [{}]({})".format(input_str, link))
    else:
        await event.edit("Something is Wrong. Please Try Again Later.")
