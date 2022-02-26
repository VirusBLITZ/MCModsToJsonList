import os
import json

USERNAME = os.getlogin()
MODSPATH = f"C:/Users/{USERNAME}/AppData/Roaming/.minecraft/mods/"
WRITETO = open("mods.json", "w")

mods = {}
for mod in [mod for mod in os.listdir(MODSPATH) if ".jar" in mod]:
    mods["".join(letter for letter in mod.split(".jar")[0] if letter.isalpha())] = ""
print(json.dumps(mods, indent=2))

WRITETO.write(json.dumps(mods, indent=2))
WRITETO.close()
