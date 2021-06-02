from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
from colors import green, red, yellow, white, cyan, reset, blue

print("""


   ▄████████  ▄██████▄     ▄████████          ███      ▄██████▄  ▀████    ▐████▀    ▄████████    ▄████████ 
  ███    ███ ███    ███   ███    ███      ▀█████████▄ ███    ███   ███▌   ████▀    ███    ███   ███    ███ 
  ███    ███ ███    ███   ███    █▀          ▀███▀▀██ ███    ███    ███  ▐███      ███    █▀    ███    ███ 
  ███    ███ ███    ███   ███                 ███   ▀ ███    ███    ▀███▄███▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀███████████ ███    ███ ▀███████████          ███     ███    ███    ████▀██▄     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ███ ███    ███          ███          ███     ███    ███   ▐███  ▀███      ███    █▄  ▀███████████ 
  ███    ███ ███    ███    ▄█    ███          ███     ███    ███  ▄███     ███▄    ███    ███   ███    ███ 
  ███    █▀   ▀██████▀   ▄████████▀          ▄████▀    ▀██████▀  ████       ███▄   ██████████   ███    ███ 
                                                                                                ███    ███ 


""")
print("Made by %sTakaso%s and fixed by %sGlobal Occult Coalition%s" % (red(), reset(), blue(), reset()))

chanid = input("\n%sInsert channel ID: %s" % (blue(), reset()))
msgid = input("%sInsert message ID: %s" % (blue(), reset()))
gldid = input("%sInsert guild ID: %s" % (blue(), reset()))
reason = input("%sChoose the reason: %s" % (blue(), reset()))

def report():
    with open("tokens.txt", "r") as tokens:
        slaves = tokens.readlines()
        for niggers in slaves:
            header = {
                "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
                "Authorization" : niggers,
                "Content-Type" : "application/json"
                }
            payload = {
                "channel_id": chanid, "message_id": msgid, "guild_id": gldid, "reason" : reason
                }
            while True:
                r = requests.post('https://discord.com/api/v9/report', headers=header, json=payload)
                if r.status_code == 201:
                    print ("%s Succesfully reported user. %s" % (green(), reset()))
                else:
                    print ("%s Failed to report. %s" % (red(), reset()))

report()
end = input("\n\n%sReporting is done, press any key to exit%s" % (cyan(), reset())) 
