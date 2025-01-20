import json, base64 as b64, os

roTxtFile = open(input("What is the name of the RoTxt file(.rtx(p)) you want to import? "), "r")
robloxAuto = input("Would you like to automatically search for Roblox? (N)o ")
def getDir():
    ftlt = []
    fs = []
    if os.path.isdir(os.path.expandvars("%LocalAppData%/Roblox/Versions")): ftlt.append(os.path.expandvars("%LocalAppData%\\Roblox\\Versions"))
    if os.path.isdir(os.path.expandvars("%LocalAppData%/Bloxstrap/Versions")): ftlt.append(os.path.expandvars("%LocalAppData%\\Bloxstrap\\Versions"))
    for f in ftlt:
        for r, f, _ in os.walk(f):
            if "content" in f:
                fs.append(r)

    return fs
robloxDirs = getDir() if not robloxAuto.lower() == "n" else [input("What is your Roblox directory? ")]
roTxtDir = "\\content\\roTxt"

def parse(f):
    roTxt = json.load(parse)
    roTxtFile.close()
    for f in robloxDirs:
        pathtofo = f + roTxtDir + roTxt["AssetDirectory"].replace("/", "\\")
        pathtofi = pathtofo + "\\" + roTxt["AssetFileName"]
        print(f'Writing to "{pathtofi}"')
        if not os.path.exists(pathtofo): os.makedirs(pathtofo)
        txtFile = open(pathtofi, "wb")
        txtFile.write(b64.b64decode(roTxt["Asset"]))
        txtFile.close()

    print(f'Use "rbxasset://roTxt{roTxt["AssetDirectory"]}/{roTxt["AssetFileName"]}" in Roblox to access this asset.')


if roTxtFile.endswith(".rtxp"):
    for x in roTxtFile.split("ﬁ"):
        parse(x)
elif roTxt.endswith(".rtx"):
    parse(roTxtFile)
