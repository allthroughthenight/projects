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

# TODO
# how to break out of loop
# or just log silently and wait for input to terminate?
while True:
    for x in sites:
        os.system("ping -qc 5 {}.com".format(x))

