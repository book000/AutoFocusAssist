import discord
import subprocess
import os
import json

if not os.path.exists("config.json"):
    print("config not found")

with open("config.json", "r") as f:
    config = json.load(f)
    userid = int(config["userid"])
    token = config["token"]

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)


class AutoFocusAssist(discord.Client):
    async def on_ready(self):
        print("Logged on as {}".format(self.user))

    async def on_voice_state_update(self, member, before, after):
        if userid != member.id:
            return

        if after.self_stream:
            print("Start GoLive")
            subprocess.call(
                ["python3", "wnfun/script_python/WnfDump.py", "-w", "WNF_SHEL_QUIET_MOMENT_SHELL_MODE_CHANGED", "1"])
        else:
            print("Stop GoLive")
            subprocess.call(
                ["python3", "wnfun/script_python/WnfDump.py", "-w", "WNF_SHEL_QUIET_MOMENT_SHELL_MODE_CHANGED", "0"])


client = AutoFocusAssist()
client.run(token)
