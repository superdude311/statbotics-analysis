import statbotics
import csv

sb = statbotics.Statbotics()
teamlist = [
    2910, 1778, 9450, 2046, 3663, 5468, 2930,
    957, 9442, 955, 3674, 1318, 3636, 360,
    1540, 1425, 2412, 488, 4061, 2147, 948,
    6696, 4915, 9567, 9023, 3826, 7034, 4513,
    9036, 2522, 3574, 4043, 5937, 4469, 6343,
    2550, 10416, 9446, 4131, 997, 3218, 2471,
    6443, 4918, 10079, 4450, 2557, 2976, 4125,
    6831
]
ranked = []

for i in range(len(teamlist)):
    stats = sb.get_team_year(teamlist[i], 2025)
    epa = stats.get("epa", {}).get("norm", 0.0)
    epa_team = (epa,teamlist[i])
    ranked.append(epa_team)

eparank = sorted(ranked, key=lambda tup: tup[0], reverse=True)
print(eparank)


filename = "2025pnw_dcmp.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(eparank)
