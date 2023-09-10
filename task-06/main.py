import interactions
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime


load_dotenv()

bot = interactions.Client(
    token=os.environ.get("TOKEN"),
    default_scope=os.environ.get("GUIILD_ID"),
)

url = "https://www.espncricinfo.com/live-cricket-score"

def parse(tag, attrib, findAll=False):
    raw_html = requests.get(url).text
    html = BeautifulSoup(raw_html, "lxml")
    if findAll: 
        return html.findAll(tag, attrs=attrib) 
    return html.find(tag, attrs=attrib)


command_data = []


metadata = {
"name": "list",
"description": "List all ongoing matches",
}
@bot.command(
    name=metadata["name"],
    description=metadata["description"],
)
async def list(ctx):
    await ctx.send("Fetching live match data...")
    matches = parse("div", {"class":"ds-text-tight-xs ds-truncate ds-text-typo-mid3"}, True)
        
    match_list = ""
    i=1
    for match in matches:
        if len(match_list + match.text)+2 <= 2000: match_list = match_list + str(i) + ' - ' + match.text + '\n'
        i = i+1

    await ctx.send(match_list)
command_data.append(metadata)

#------------------------------------------------------

metadata = {
"name": "livescore",
"description": "Shows live matches",
}
@bot.command(
    name=metadata["name"],
    description=metadata["description"],
)
async def livescore(ctx):
    await ctx.send("Fetching livescores...")
    match = parse("div", {"class":"ds-flex ds-flex-col ds-mt-2 ds-mb-2"})
    team1 = match.find_all("p")[0].text
    team2 = match.find_all("p")[1].text
    details= match.find_all("div", attrs={"class": "ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap"})

    if len(details) > 0: team1 += ' ' + details[0].text
    if len(details) > 1: team2 += ' ' + details[1].text
    status = parse("p", {"class":"ds-text-tight-s ds-font-regular ds-truncate ds-text-typo"})
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    await ctx.send(f"{team1} :zap: {team2}\n{status.text}\n{timestamp}")

    with open('livescores.csv', 'a', newline='') as csvfile:
        fieldnames = ['team1', 'team2', 'status', 'time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'team1': team1, 'team2': team2, 'status': status.text, 'time':timestamp})
command_data.append(metadata)

#------------------------------------------------------

metadata = {
    "name": "help",
    "description": "List all commands",
}
@bot.command(
    name=metadata["name"],
    description=metadata["description"],
)
async def help(ctx):
    msg = ""
    for data in command_data:
        msg += f"{data['name']} - {data['description']}\n"
    await ctx.send(msg)
command_data.append(metadata)

#------------------------------------------------------

metadata = {
"name": "generate",
"description": "Generates csv file of all matches fetched",
}
@bot.command(
    name=metadata["name"],
    description=metadata["description"],
)
async def generate(ctx):
    file_path = 'livescores.csv'
        
    with open(file_path, 'rb') as file:
        response = requests.post('https://file.io', files={'file': file})

    link = response.json()['link']
    await ctx.send(link)
command_data.append(metadata)


bot.start()