import statbotics
import csv

sb = statbotics.Statbotics()
teamlist = [9496, 4534, 900, 8738, 587, 4795, 4561, 9032, 2059, 6502, 2640, 1533, 6894, 4861, 8429, 5727, 8727, 7763, 4828, 6500, 10077, 7443, 3737, 9297, 5511, 4829, 2642, 10260, 10583, 9008, 9298, 5190, 2724, 9198, 3822, 8746, 6639, 3506, 3459, 6729]
ranked = []

for i in range(len(teamlist)):
    stats = sb.get_team_year(teamlist[i], 2025)
    epa = stats.get("epa", {}).get("norm", 0.0)
    epa_team = (epa,teamlist[i])
    ranked.append(epa_team)

eparank = sorted(ranked, key=lambda tup: tup[0], reverse=True)
print(eparank)


filename = "2025fnc_dcmp.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(eparank)
