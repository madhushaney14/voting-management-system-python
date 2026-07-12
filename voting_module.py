import csv
import os
from validators import is_valid_date
from candidate_module import seat_taken

BALLOTS_FILE = "ballots.csv"

def load_ballots():
    """Reads ballots.csv into memory as a dictionary, keyed by voter_id."""
    ballots = {}
    if not os.path.exists(BALLOTS_FILE):
        return ballots

    with open(BALLOTS_FILE, "r", newline="") as f:
        reader = csv.reader(f)
        for line_num, row in enumerate(reader, start=1):
            if len(row) != 6:
                print(f"Warning: Skipping malformed row {line_num} in ballots.csv: {row}")
                continue

            date, voter_id, candidate_id, seat, age, district = row

            if not is_valid_date(date):
                print(f"Warning: Skipping row {line_num} — invalid date: {date}")
                continue
            if len(voter_id) != 10 or not voter_id.isdigit():
                print(f"Warning: Skipping row {line_num} — invalid voter_id: {voter_id}")
                continue
            if not age.isdigit():
                print(f"Warning: Skipping row {line_num} — invalid age: {age}")
                continue

            ballots[voter_id] = {
                "date": date,
                "candidate_id": candidate_id,
                "seat": seat,
                "age": int(age),
                "district": district
            }

    return ballots


def save_ballots(ballots):
    """Saves the current ballots dictionary to ballots.csv."""
    with open(BALLOTS_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for voter_id, data in ballots.items():
            writer.writerow([data["date"], voter_id, data["candidate_id"],
                              data["seat"], data["age"], data["district"]])

def cast_vote(voters, candidates, ballots):
    voter_id = input("Enter Voter ID: ").strip()
    seat = input("Enter Candidate Seat Number: ").strip()
    date_str = input("Enter Date (yyyy-mm-dd): ").strip()

    if voter_id not in voters:
        print("Error: Invalid Voter ID.")
        return

    if not seat_taken(candidates, seat):
        print("Error: Invalid Seat Number.")
        return

    if not is_valid_date(date_str):
        print("Error: Invalid Date. Use yyyy-mm-dd format.")
        return

    if voter_id in ballots:
        print("Error: Vote already cast by this voter.")
        return

    candidate_id = None
    for cid, data in candidates.items():
        if data["seat"] == seat:
            candidate_id = cid
            break

    voter_data = voters[voter_id]

    ballots[voter_id] = {
        "date": date_str,
        "candidate_id": candidate_id,
        "seat": seat,
        "age": voter_data["age"],
        "district": voter_data["district"]
    }

    save_ballots(ballots)
    print(f"Vote cast successfully for voter {voter_id}.")


def delete_vote(ballots):
    voter_id = input("Enter Voter ID to delete vote: ").strip()

    if voter_id not in ballots:
        print("Error: Vote does not exist for this Voter ID.")
        return

    confirm = input(f"Delete vote for voter {voter_id}? (y/n): ").strip().lower()
    if confirm == "y":
        del ballots[voter_id]
        save_ballots(ballots)
        print(f"Vote deleted. Voter {voter_id} may now cast a new vote.")
    else:
        print("Deletion cancelled.")


def voting_menu(voters, candidates, ballots):
    while True:
        print("\n--- Voting Menu ---")
        print("1. Cast Vote")
        print("2. Delete Vote")
        print("3. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            cast_vote(voters, candidates, ballots)
        elif choice == "2":
            delete_vote(ballots)
        elif choice == "3":
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    from voter_module import load_voters
    from candidate_module import load_candidates

    voters = load_voters()
    candidates = load_candidates()
    ballots = load_ballots()
    voting_menu(voters, candidates, ballots)