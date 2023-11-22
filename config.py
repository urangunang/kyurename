"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link: https://t.me/PYRO_BOTZ
Repo Link: https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link: https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re
import os
import time

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "pyro-botz")
    DB_URL = os.environ.get("DB_URL", "")

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB = os.environ.get("FORCE_SUB", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))

class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hai {} 👋,
This Is An Advanced And Yet Powerful Rename Bot
Using This Bot You Can Rename & Change Thumbnail Of Your File
You Can Also Convert Video To File & File To Video
This Bot Also Supports Custom Thumbnail And Custom Caption
This Bot Was Created By : @Pyro_Botz 💞</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 My Name : {}
├🖥️ Developers : <a href=https://t.me/PYRO_BOTZ/53>Team Pyro Botz</a> 
├👨‍💻 Programmer : <a href=https://github.com/lntechnical2>Ln Technical Git</a>
├📕 Library : <a href=https://github.com/pyrogram>Pyrogram</a>
├✏️ Language: <a href=https://www.python.org>Python 3</a>
├💾 Data Base: <a href=https://cloud.mongodb.com>Mongo DB</a>
├📊 Build Version: <a href=https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT>Pyro Renamer V3.0.0</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
<b>•»</b> /start The Bot And Send Any Photo To Automatically Set Thumbnail.
<b>•»</b> /del_thumb Use This Command To Delete Your Old Thumbnail.
<b>•»</b> /view_thumb Use This Command To View Your Current Thumbnail.
📑 <b><u>How To Set Custom Caption</u></b>
<b>•»</b> /set_caption - Use This Command To Set A Custom Caption
<b>•»</b> /see_caption - Use This Command To View Your Custom Caption
<b>•»</b> /del_caption - Use This Command To Delete Your Custom Caption
Example:- /set_caption 📕 File Name: {filename}
💾 Size: {filesize}
⏰ Duration: {duration}
✏️ <b><u>How To Rename A File</u></b>
<b>•»</b> Send Any File And Type New File Name \nAnd Select The Format [ document, video, audio ].           
ℹ️ Any Other Help Contact :- <a href=https://t.me/PYRO_BOTZ_CHAT>Support Group</a>
"""

#⚠️ Don't Remove Our Credits @Pyro_Botz🙏🥲
    DEV_TXT = """<b><u>Special Thanks & Developers</b></u>
» Source Code : <a href=https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT>Pyro Renamer Bot</a>
» How To Deploy : <a href=https://youtu.be/GfulqsSnTv4>MoteCh YT</a>
• ❣️ <a href=https://github.com/lntechnical2>Ln Technical</a>
• ❣️ <a href=https://t.me/Mhd_rzn>Mhd_rzn</a>
• ❣️ <a href=https://youtu.be/GfulqsSnTv4>Motech YT</a>
• ❣️ <a href=https://t.me/mr_MKN>Mr.MKN TG</a>
• ❣️ <a href=https://t.me/GitHub_noob>GitHub Noob</a>
• ❣️ <a href=https://t.me/about_jeol>Jeol Paul</a> """
