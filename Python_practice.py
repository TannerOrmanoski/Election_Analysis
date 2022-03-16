
counties = ["Arapahoe", "Denver", "Jefferson"]


if counties[1] == 'Denver':
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

print(counties_dict["Arapahoe"])

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(str(county), "county has", str(voters), "registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict.values())

for county_dict in voting_data:
    for value in county_dict:
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
message_to_candidate = (
    f"You recieved {candidate_votes:,} number of votes. "
    f"The toatal number of votes in the election was {total_votes:,}. "
    f"You revieved {candidate_votes / total_votes * 100:.2f}% of total votes.")

print(message_to_candidate)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")


for i in voting_data:
    print(f"{county}")       