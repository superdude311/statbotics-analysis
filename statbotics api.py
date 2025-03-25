import statbotics
sb = statbotics.Statbotics()
epa_type = "max" # valid values: mean, max, current, recent
epa_threshold = 2050
currentyear = 2025 
global historical_epa 
historical_epa = []


def main():
    try:
        teams = []
        for i in range(0, 4):
            team_segmented = sb.get_teams(limit=1000, offset=(i*1000))
            teams = teams + team_segmented
        teams_over_x = [team for team in teams if team.get('norm_epa').get(epa_type) > epa_threshold]
        
        for team in teams_over_x:

            rookieyear = sb.get_team(team.get("team"), ["rookie_year"]).get("rookie_year") #get team rookie year
            if epa_type == "max":
                for i in range(rookieyear, currentyear + 1):
                    try:
                        yearinfo = sb.get_team_year(team.get("team"), i) 
                        yearEPA = (yearinfo.get("epa", {}).get("norm", 0.0), i) #tuple (epa, year)
                        historical_epa.append(yearEPA) # make array of team EPA
                    except Exception as e:
                        #print(f"skipping year {i} due to lack of data")
                        continue
                maxEPA = max(historical_epa) #max EPA of array of tuples

            team_number = team.get('team', 'Unknown')
            team_epa = team.get('norm_epa').get(epa_type)
            wlr = team.get('record').get('winrate')         
            print(f"Team {team_number} has a {epa_type} EPA of {team_epa} and a WLR of = {wlr}")
            if epa_type == "max":
                print(f"The team achieved their max EPA in {maxEPA[1]}")
                historical_epa.clear()
                i = 0
            
    except Exception as e:
        print("An error occurred while fetching or processing the data:", e)

if __name__ == "__main__":
    main()