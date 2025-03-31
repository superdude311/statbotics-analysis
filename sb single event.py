import statbotics
import csv

sb = statbotics.Statbotics()
teamlist = [
    4678, 2056, 7558, 3683, 5409, 4946, 4907, 4476, 4152, 4039,
    610, 2200, 8884, 5406, 781, 1114, 9098, 7520, 2935, 1241,
    188, 4976, 3739, 10015, 4917, 7480, 5912, 10554, 865, 4920,
    4069, 10167, 5032, 1325, 4940, 6865, 5024, 2702, 9785, 10611,
    10279, 5885, 1310, 1285, 8731, 9263, 3756, 3161, 1360, 7712,
    7476, 7902, 1305, 6135, 4308, 1229, 5031, 2708, 8089, 5036,
    2609, 5672, 2852, 5689, 9569, 8081, 854, 9580, 9262, 7623,
    771, 919, 7136, 6725, 9062, 6632, 2198, 7200, 10634, 9782,
    7659, 2706, 10027, 6978, 8729, 10218, 8764, 9525, 9659, 8349,
    1334, 6110, 5408, 5719, 4617, 5870, 6987, 9562, 4951, 772
]


ranked = []

for i in range(len(teamlist)):
    stats = sb.get_team_year(teamlist[i], 2025)
    epa = stats.get("epa", {}).get("norm", 0.0)
    epa_team = (epa,teamlist[i])
    ranked.append(epa_team)

eparank = sorted(ranked, key=lambda tup: tup[0], reverse=True)
print(eparank)


filename = "2025ont_dcmp.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(eparank)
