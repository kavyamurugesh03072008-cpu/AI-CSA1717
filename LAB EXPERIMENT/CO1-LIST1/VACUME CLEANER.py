def vacuum_cleaner(room):
    position = 0

    while "Dirty" in room:
        if room[position] == "Dirty":
            print("Cleaning room", position + 1)
            room[position] = "Clean"
        else:
            print("Room", position + 1, "is already clean")

        position = (position + 1) % len(room)

    print("All rooms are clean")


rooms = ["Dirty", "Clean", "Dirty"]
vacuum_cleaner(rooms)
