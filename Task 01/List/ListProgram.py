justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Number of members:", len(justice_league))
# OutPut Number of members: 6

# Adding Items to List
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Updated list:", justice_league)
# Updated list: ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']

# Move Wonder Woman to the beginning (make her the leader).
justice_league.remove("Wonder Woman")
# I removed Wonder women and then addded her back to the start of the list.
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman as leader:", justice_league)
# Wonder Woman as leader: ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']


# Separate Aquaman and Flash by inserting Superman or Green Lantern between them.
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("Conflict managed:", justice_league)
# Conflict managed: ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']

# Replace the entire list with a new team.
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League:", justice_league)
# New Justice League: ['Cyborg', 'Shazam', 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']


# Sort the Justice League alphabetically. Leader is now at index 0.
justice_league.sort()
print("Sorted Justice League:", justice_league)
# Sorted Justice League: ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']
print("New leader:", justice_league[0])
# New leader: Cyborg
