# main.py

def main():
    while True:
        print("\n==== MENU ====")
        print("1. Add User")
        print("2. View Users")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Add User selected")

        elif choice == "2":
            print("View Users selected")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

main()