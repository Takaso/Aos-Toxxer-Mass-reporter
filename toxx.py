import requests
from colors import green, red, yellow, white, cyan, reset, blue, magenta


# 0: {reason: 0, label: "Illegal Content",…}
# 1: {reason: 1, label: "Harassment",…}
# 2: {reason: 2, label: "Spam or Phishing Links",…}
# 3: {reason: 3, label: "Self Harm", description: "Person is at risk of claimed intent of self-harm."}
# 4: {reason: 4, label: "NSFW Content",…}

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
print("%s\nReasons:%s\n%s0 = Illegal Content\n1 = Harassment\n2 = Spam or phishing links\n3 = Self Harm\n4 = NSFW Content%s\n%s You have to choose one of these numbers as reason!%s" % (white(), reset(), magenta(), reset(), white(), reset()))


chanid = input("\n%sInsert channel ID: %s" % (blue(), reset()))
msgid = input("%sInsert message ID: %s" % (blue(), reset()))
gldid = input("%sInsert guild ID: %s" % (blue(), reset()))
reason = input("%sChoose the reason: %s" % (blue(), reset()))
numbersoftimes =  int(input("%sSelect the number of reports to do with each account: %s" % (blue(), reset())))

def report():
    with open("tokens.txt", "r", encoding="UTF-8") as tokens:
        slaves = tokens.read().splitlines()
        for niggers in slaves:
            header = {
                "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
                "Authorization" : niggers,
                "Content-Type" : "application/json"
                }
            payload = {
                "channel_id": chanid, "message_id": msgid, "guild_id": gldid, "reason" : reason
                }
            times = 1
            while times <= numbersoftimes:
                r = requests.post('https://discord.com/api/v9/report', headers=header, json=payload)
                if r.status_code == 201:
                    print (f"\n%s Succesfully reported user {times} times. %s" % (green(), reset()))
                    times += 1
                else:
                    print ("%s Failed to report. %s" % (red(), reset()))

report()
end = input("\n\n%sReporting is done, if you want it to be longer add more tokens, press any key to exit: %s" % (cyan(), reset()))
