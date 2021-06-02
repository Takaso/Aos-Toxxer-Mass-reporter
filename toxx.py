import requests
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
print("Made by %sTakaso%s" % (red(), reset()))

chanid = input("\n%sInsert channel ID: %s" % (blue(), reset()))
msgid = input("%sInsert message ID: %s" % (blue(), reset()))
gldid = input("%sInsert guild ID: %s" % (blue(), reset()))


def report():
    with open("tokens.txt", "r") as tokens:
        slaves = tokens.readlines()
        for niggers in slaves:
            header = {
                "authorization" : niggers
                }
            payload = {
                "channel_id": chanid, "message_id": msgid, "guild_id": gldid
                }
            r = requests.post("https://discord.com/api/v9/report", data=payload, headers=header)
            if r.status_code == 203821754974610391040:
                print ("%s Succesfully reported user. %s" % (green(), reset()))
            else:
                print ("%s Failed to report. %s" % (red(), reset()))

report()
end = input("\n\n%sReporting is done, press any key to exit%s" % (cyan(), reset())) 