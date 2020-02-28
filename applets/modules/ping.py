# Ping various Five Nine sites to troubleshoot networking issues

import os

sites = ["google",
        "yahoo",
        "facebook",
        "twitter",
        "amazon",
        "duckduckgo",
        "discordapp",
        "youtube",
        "instagram"]
sites.sort()

# TODO: how to loop continuously, but still able to break-out whenever, could
# be done by multi-threading command and input listener
# TODO: should output be logged in the background to file and/or less 
# verbose printout(s)
def run():
    print("Sites to Ping")
    for x in sites:
        print(" - {}".format(x))
    for x in sites:
        os.system("ping -qc 5 {}.com".format(x))