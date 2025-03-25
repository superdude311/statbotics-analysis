import statbotics
sb = statbotics.Statbotics();
teams = sb.get_teams()
processedteams = []

for team in teams:
    num = team.get("team")
    info = sb.get_team(num)
    processedteam = {**team, **info}
    processedteams.append(processedteam)


over2k = []
for team in processedteams:
    rawmax = team.get("norm_epa", {}).get("max", 0.0)
if rawmax is None:
        continue
    maxval = float(rawmax)
    if maxval > 2000:
        over2k.append(team)

for team in over2k:
    maxEPA = rawmax
    wlr = team.get("record", {}).get("winrate", 0.0)
    print("team " + str(num) +" has a max EPA of " + str(maxEPA) + " and a WLR of " + str(wlr))