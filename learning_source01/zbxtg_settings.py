# -*- coding: utf-8 -*-

tg_key = "XYZ"  # telegram bot api key

zbx_tg_prefix = "zbxtg"  # variable for separating text from script info 
zbx_tg_tmp_dir = "/tmp/" + zbx_tg_prefix  # directory for saving caches, uids, cookies, etc.
zbx_tg_signature = False  # the signature in your telegram message for example your company name

zbx_server = "http://localhost"  # zabbix server full url (ip or dns)
zbx_api_user = "api"      #user baraye zabbix
zbx_api_pass = "api"     #password of user
zbx_api_verify = True  # True - do not ignore self signed certificates, False - ignore

proxy_to_zbx = None
proxy_to_tg = None

#proxy_to_zbx = "proxy.local:3128"
#proxy_to_tg = "proxy.local:3128"

emoji_map = {
    "ok": "✅",
    "problem": "❗",
    "info": "ℹ️",
    "warning": "⚠️",
    "disaster": "❌",
    "bomb": "💣",
    "fire": "🔥",
    "hankey": "💩",
}