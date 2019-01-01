import os

sites = ["goole",
        "yahoo",
        "facebook",
        "twitter",
        "amazon",
        "habatica",
        "duckduckgo",
        "discordapp",
        "youtube",
        "instagram",]

while True:
    for x in sites:
        os.system("ping -qc 5 {}.com".format(x))
