import statbotics
import csv

sb = statbotics.Statbotics()
teamlist = [6919, 2974, 1771, 8866, 1833, 1648, 1683, 6340, 1261, 6829, 6023, 7538, 3318, 10376, 4026, 1002, 9260, 5109, 7451, 10482, 9480, 4112, 9477, 3635, 5293, 8080, 1414, 8865, 4459, 9522, 6944, 4468, 8849, 5074, 8736, 5608, 5900, 6925, 6705, 832, 8100, 4240, 3344, 2415, 4188]


ranked = []

for i in range(len(teamlist)):
    stats = sb.get_team_year(teamlist[i], 2025)
    epa = stats.get("epa", {}).get("norm", 0.0)
    epa_team = (epa,teamlist[i])
    ranked.append(epa_team)

eparank = sorted(ranked, key=lambda tup: tup[0], reverse=True)
print(eparank)


filename = "2025pch_dcmp.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(eparank)
