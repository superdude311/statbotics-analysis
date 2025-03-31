import statbotics
import csv

sb = statbotics.Statbotics()
teamlist = [7457, 868, 1501, 4272, 3940, 461, 45, 7617, 1741, 10021, 135, 7454, 234, 3494, 3176, 829, 10332, 5010, 4485, 5484, 1024, 5402, 292, 4926, 10492, 6721, 8430, 8103, 6956, 328, 3487, 2197, 1018, 5188, 2171, 1747, 447, 7657]


ranked = []

for i in range(len(teamlist)):
    stats = sb.get_team_year(teamlist[i], 2025)
    epa = stats.get("epa", {}).get("norm", 0.0)
    epa_team = (epa,teamlist[i])
    ranked.append(epa_team)

eparank = sorted(ranked, key=lambda tup: tup[0], reverse=True)
print(eparank)


filename = "2025fin_dcmp.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(eparank)
