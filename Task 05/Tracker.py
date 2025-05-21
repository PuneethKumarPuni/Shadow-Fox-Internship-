completed = 0
total = 100
set_size = 10

while completed < total:
    completed += set_size
    print(f"\nYou completed {completed} jumping jacks.")
    
    if completed == total:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            print(f"{total - completed} jumping jacks remaining.")
    else:
        print(f"{total - completed} jumping jacks remaining.")
