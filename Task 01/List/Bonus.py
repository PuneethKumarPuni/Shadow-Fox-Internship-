
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Step 1 - Original Justice League:", justice_league)

# OutPut --> Step 1 - Original Justice League: ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern']

print("Number of members:", len(justice_league))
# OutPut --> Number of members: 6

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Step 2 - After adding Batgirl and Nightwing:", justice_league)
# OutPut --> Step 2 - After adding Batgirl and Nightwing: ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Step 3 - Wonder Woman as Leader:", justice_league)
# OutPut --> Step 3 - Wonder Woman as Leader: ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']

justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("Step 4 - Conflict resolved between Aquaman and Flash:", justice_league)
# OutPut --> Step 4 - Conflict resolved between Aquaman and Flash: ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']


justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Step 5 - New Justice League formed:", justice_league)
# OutPut --> Step 5 - New Justice League formed: ['Cyborg', 'Shazam', 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']

justice_league.sort()
print("Step 6 - Alphabetically Sorted Justice League:", justice_league)
# OutPut --> Step 6 - Alphabetically Sorted Justice League: ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']

print("Bonus - Predicted New Leader:", justice_league[0])
# OutPut --> Bonus - Predicted New Leader: Cyborg

