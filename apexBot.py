import discord
import requests
import os

#token = 'XXXXXXXXX-XXXXXXXX'
#key = {'TRN-Api-Key': "XXXXXXXXX-XXXXXXXXXX"}

client = discord.Client()

@client.event 
async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!help'):
            msg = '''Go to Apex Tracker and follow the instructions to sync the correct data. The bot currently tracks\n
                    Total Kills (Unlock kills tracker for all legends)\n
                    Kills Per Match (Unlock games played and kills tracker for all legends)\n
                    Damage Per Match (Unlock games played and damage done tracker for all legends)\n
                    Total Damage (Unlock damage done tracker for all legends)\n
                    Total Matches Played (Unlock games played tracker for all legends)\n
            In order to get accurate stats, go to each legend in game and unlock the trackers for the stats listed above.\n
            Or follow Apex Tracker website instructions.'''
            await client.send_message(message.channel, msg)
            return

        if message.content.startswith('!stats'):
            
            userName = ''
            userName += message.content[len('!stats')+1:]

            URL = "https://public-api.tracker.gg/apex/v1/standard/profile/5/"+userName

            try:
                r = requests.get(url=URL, headers=key)
                data = r.json()

                lengthOfStatsArray = len(data['data']['stats'])
                keys = []

                for x in range(0, lengthOfStatsArray):
                    statsArray = data['data']['stats'][x]['metadata']['key']
                    keys.append(statsArray)

                if "Level" in keys:
                    level = data['data']['stats'][keys.index("Level")]['value']
                else:
                    level = "No Data. Unlock the tracker."

                if "Kills" in keys:
                    totalKills = data['data']['stats'][keys.index("Kills")]['value']
                else:
                    totalKills = "'NO DATA. UNLOCK THE TRACKER.'"
                
                if "Damage" in keys:
                    totalDamage = data['data']['stats'][keys.index("Damage")]['value']
                else:
                    totalDamage = "'NO DATA. UNLOCK THE TRACKER.'"

                if "KillsPerMatch" in keys: 
                    killsPerMatch = data['data']['stats'][keys.index("KillsPerMatch")]['value']
                else:
                    killsPerMatch = "'NO DATA. UNLOCK THE TRACKER.'"

                if "DamagePerMatch" in keys:
                    dmgPerMatch = data['data']['stats'][keys.index("DamagePerMatch")]['value']
                else: 
                    dmgPerMatch = "'NO DATA. UNLOCK THE TRACKER.'"

                if "MatchesPlayed" in keys:
                    totalMatchesPlayed = data['data']['stats'][keys.index("MatchesPlayed")]['value']
                else:
                    totalMatchesPlayed = "'NO DATA. UNLOCK THE TRACKER.'"

                name = data['data']['metadata']['platformUserHandle']

                #msg = '%s\nLevel: %s\nKills Per Match: %s\nDamage Per Match: %s\nTotal Kills: %s\nTotal Damage: %s\nTotal Matches Played: %s' %(name, level, killsPerMatch, dmgPerMatch, totalKills, totalDamage, totalMatchesPlayed)
                msg = f'{name}\nLevel: {level}\nTotal Kills: {totalKills}\nTotal Damage: {totalDamage}\nTotal Matches Played: {totalMatchesPlayed}\nKills Per Match: {killsPerMatch}\nDamage Per Match: {dmgPerMatch}'
            except: 
                msg = 'Major error, talk to ya boii to see what you broke.'
            

            await client.send_message(message.channel, msg)
            return

            
@client.event
async def on_ready():
    print('ready')

client.run(os.environ.get('token'))
