import statbotics
import csv

sb = statbotics.Statbotics()
teamlist = [1574, 1577, 1690, 1937, 1942, 2096, 2230, 2231, 3065, 3075, 3083, 3211, 3316, 3339, 3388, 4320, 4338, 4416, 4586, 4590, 4661, 4744, 5135, 5554, 5614, 5635, 5654, 5715, 5987, 5990, 6104, 6738, 7039, 7067, 7112, 7845, 8175, 8223, 9738, 9740]
ranked = []

for i in range(len(teamlist)):
    stats = sb.get_team_year(teamlist[i], 2025)
    epa = stats.get("epa", {}).get("norm", 0.0)
    epa_team = (epa,teamlist[i])
    ranked.append(epa_team)

eparank = sorted(ranked, key=lambda tup: tup[0], reverse=True)
print(eparank)


filename = "2025isr_dcmp.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(eparank)
