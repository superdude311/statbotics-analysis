import statbotics
sb = statbotics.Statbotics()
team = 841
info = sb.get_team(team)
wlr = info.get('record').get('winrate')
wins = info.get('record').get('wins')
losses = info.get('record').get('losses')
ties = info.get('record').get('ties')
max = info.get('norm_epa').get('max')
mean = info.get('norm_epa').get('mean')
print(f"team {team}'s historic high EPA was {max}, and their average is {mean}")
print(f"their lifetime WLR is {wlr}, with a record of {wins}-{losses}-{ties}")