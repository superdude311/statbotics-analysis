import statbotics

sb = statbotics.Statbotics()
team = 751
teaminfo = sb.get_team(team, ["rookie_year"])
rookieyear = teaminfo.get("rookie_year")
currentyear = 2025
historical_epa = []

for i in range(rookieyear, currentyear):
    try:
        yearinfo = sb.get_team_year(team, i)
        yearEPA = (yearinfo.get("epa", {}).get("norm", 0.0), i)
        historical_epa.append(yearEPA)
    except Exception as e:
        print(f"skipping year {i} due to lack of data")
        continue

maxEPA = max(historical_epa)

print(maxEPA)