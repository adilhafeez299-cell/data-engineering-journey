selected_option = 0

while selected_option not in range (1, 4):
    print("Menu")
    print("1. Start the game")
    print("2. Load saved game")
    print("3. Quit")

    try:
        selected_option = int(input("Please enter your choice (1-3):"))
    except ValueError as e:
        print(e)
        print("Try to select the option once again")

if selected_option == 1:
    print("Starting the game...")
if selected_option == 2:
    print("Loading saved game...")
if selected_option == 3:
    print("Quitting the game...")

