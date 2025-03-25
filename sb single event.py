import statbotics
import csv

sb = statbotics.Statbotics()
teamlist = [
    4451, 343, 342, 2815, 1287, 8575, 3490, 281, 1102, 3489, 8137, 6167,
    4864, 9571, 7085, 4533, 5130, 10367, 1758, 6366, 10591, 1051, 10599,
    1319, 10619, 6961, 10388, 10231
]

ranked = []

for i in range(len(teamlist)):
    stats = sb.get_team_year(teamlist[i], 2025)
    epa = stats.get("epa", {}).get("norm", 0.0)
    epa_team = (epa,teamlist[i])
    ranked.append(epa_team)

eparank = sorted(ranked, key=lambda tup: tup[0], reverse=True)
print(eparank)


filename = "2025fsc_dcmp.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(eparank)
