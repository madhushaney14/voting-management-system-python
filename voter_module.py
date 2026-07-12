import csv
import os
from validators import validate_id
from districts import SRI_LANKA_DISTRICTS

VOTER_FILE = "voter.csv"

def load_voters():
    """Reads voter.csv into memory as a dictionary, so that the app has existing voter data available on startup. Bad rows are skipped with a warning rather than crashing thr program"""
    voters = {}
    if not os.path.exists(VOTER_FILE):
        return voters

    with open(VOTER_FILE, "r", newline="") as f:
        reader = csv.reader(f)
        for line_num, row in enumerate(reader, start=1):
            if len(row) !=3:
                print(f"Warning: Skiping malformed row {line_num} in voter.csv: {row}")
                continue

            voter_id, district, age = row

            if not validate_id(voter_id):
                print(f"Warning: Skipping row {line_num} - invalid district: {district}")
                continue

            if not age.isdigit():
                print(f"Warning: Skipping row {line_num} - invalid age: {age}")
                continue

            voters[voter_id] = {"district": district, "age": int(age)}

        return voters


def save_voters(voters):
    """Saves the current voters dictionary to voter.csv so the data isn't lost when the program closes"""
    with open(VOTER_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for voter_id, data in voters.items():
            writer.writerow([voter_id, data["district"], data["age"]])

def add_voter(voters):
    voter_id = input("Enter Voter ID (10 digits): ").strip()

    if len(voter_id) != 10 or not voter_id.isdigit():
        print("Error: Voter ID must be exactly 10 digits.")
        return

    if not validate_id(voter_id):
        print("Error: Invalid Voter ID (check digit mismatch).")
        return

    if voter_id in voters:
        print("Error: Voter ID already registered.")
        return

    print("Districts:", ", ".join(SRI_LANKA_DISTRICTS))
    district = input("Enter District Name: ").strip()
    if district not in SRI_LANKA_DISTRICTS:
        print("Error: Invalid district name.")
        return

    age_input = input("Enter age (press Enter to default to 18): ").strip()
    if age_input == "":
        age = 18
    elif age_input.isdigit():
        age = int(age_input)
    else:
        print("Error: Age must be numeric.")
        return

    voters[voter_id] = {"district": district, "age": age}
    save_voters(voters)
    print(f"Voter {voter_id} registered successfully.")


def edit_voter(voters):
    voter_id = input("Enter Voter ID to edit: ").strip()

    if voter_id not in voters:
        print("Error: Voter ID not found.")
        return

    print(f"Current record: {voters[voter_id]}")
    print("Districts:", ", ".join(SRI_LANKA_DISTRICTS))
    new_district = input("Enter new District Name (Enter to keep current): ").strip()
    if new_district:
        if new_district not in SRI_LANKA_DISTRICTS:
            print("Error: Invalid district name.")
            return
        voters[voter_id]["district"] = new_district

    new_age = input("Enter new age (Enter to keep current): ").strip()
    if new_age:
        if not new_age.isdigit():
            print("Error: Age must be numeric.")
            return
        voters[voter_id]["age"] = int(new_age)

    save_voters(voters)
    print(f"Voter {voter_id} updated successfully.")


def search_voter(voters):
    voter_id = input("Enter Voter ID to search: ").strip()
    if voter_id in voters:
        data = voters[voter_id]
        print(f"Voter ID: {voter_id} | District: {data['district']} | Age: {data['age']}")
    else:
        print("Error: Voter ID not found.")


def delete_voter(voters):
    voter_id = input("Enter Voter ID to delete: ").strip()
    if voter_id not in voters:
        print("Error: Voter ID not found.")
        return

    confirm = input(f"Are you sure you want to delete voter {voter_id}? (y/n): ").strip().lower()
    if confirm == "y":
        del voters[voter_id]
        save_voters(voters)
        print(f"Voter {voter_id} deleted.")
    else:
        print("Deletion cancelled.")


def voter_menu(voters):
    while True:
        print("\n--- Voter Registration Menu ---")
        print("1. Add Voter")
        print("2. Edit Voter")
        print("3. Search Voter")
        print("4. Delete Voter")
        print("5. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_voter(voters)
        elif choice == "2":
            edit_voter(voters)
        elif choice == "3":
            search_voter(voters)
        elif choice == "4":
            delete_voter(voters)
        elif choice == "5":
            break
        else:
            print("Invalid option, try again.")

# if __name__ == "__main__":
#     test_voters = {
#     "3141592657": {"district": "Colombo", "age": 20},
#     "9876543215": {"district": "Kandy", "age": 22}
#     }
#
#     save_voters(test_voters)
#     print("Saved test voters to voter.csv")
#
#     loaded = load_voters()
#     print(f"Loaded voters: {loaded}")

if __name__ == "__main__":
    voters = load_voters()
    voter_menu(voters)