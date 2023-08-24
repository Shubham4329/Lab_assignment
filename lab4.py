class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing
        self.next_match = None

    def __str__(self):
        return f"{self.team1} vs {self.team2} at {self.location} ({self.timing})"

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, location, team1, team2, timing):
        new_match = Match(location, team1, team2, timing)
        self.matches.append(new_match)

    def get_matches_by_team(self, team):
        team_matches = [match for match in self.matches if match.team1 == team or match.team2 == team]
        return team_matches

    def get_matches_by_location(self, location):
        location_matches = [match for match in self.matches if match.location == location]
        return location_matches

    def get_matches_by_timing(self, timing):
        timing_matches = [match for match in self.matches if match.timing == timing]
        return timing_matches

def main():
    flight_table = FlightTable()

    flight_table.add_match("Mumbai", "India", "Sri Lanka", "DAY")
    flight_table.add_match("Delhi", "England", "Australia", "DAY-NIGHT")
    flight_table.add_match("Chennai", "India", "South Africa", "DAY")
    flight_table.add_match("Indore", "England", "Sri Lanka", "DAY-NIGHT")
    flight_table.add_match("Mohali", "Australia", "South Africa", "DAY-NIGHT")
    flight_table.add_match("Delhi", "India", "Australia", "DAY")

    print("Choose a search parameter:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")

    choice = int(input())
    matches = []

    if choice == 1:
        team = input("Enter the team name: ")
        matches = flight_table.get_matches_by_team(team)
    elif choice == 2:
        location = input("Enter the location: ")
        matches = flight_table.get_matches_by_location(location)
    elif choice == 3:
        timing = input("Enter the timing: ")
        matches = flight_table.get_matches_by_timing(timing)
    else:
        print("Invalid choice.")
        return

    if not matches:
        print("No matches found.")
    else:
        print("Search Results:")
        for match in matches:
            print(match)

if __name__ == "__main__":
    main()
