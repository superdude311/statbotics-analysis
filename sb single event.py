import statbotics
import csv

sb = statbotics.Statbotics()
teamlist = [
    422, 1629, 449, 1731, 2106, 8592, 1727, 888, 1086, 620, 9072, 8590,
    836, 346, 686, 5338, 4821, 2199, 5804, 977, 2363, 10224, 1111, 2534,
    4638, 6802, 4505, 3136, 8230, 401, 8726, 5115, 614, 122, 1418, 1908,
    611, 3373, 6326, 540, 539, 1885, 3359, 2890, 3748, 1895, 4541, 116,
    2186, 3793, 8622, 339, 6863, 6213
]

ranked = []

for i in range(len(teamlist)):
    stats = sb.get_team_year(teamlist[i], 2025)
    epa = stats.get("epa", {}).get("norm", 0.0)
    epa_team = (epa,teamlist[i])
    ranked.append(epa_team)

eparank = sorted(ranked, key=lambda tup: tup[0], reverse=True)
print(eparank)


filename = "2025chs_dcmp.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(eparank)
