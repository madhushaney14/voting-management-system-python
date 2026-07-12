import csv
import os
from validators import validate_id

CANDIDATE_FILE = "candidate.csv"


def load_candidates():
    """Reads candidate.csv into memory as a dictionary, keyed by candidate_id.
    Skips and reports any malformed rows instead of crashing."""
    candidates = {}
    if not os.path.exists(CANDIDATE_FILE):
        return candidates

    with open(CANDIDATE_FILE, "r", newline="") as f:
        reader = csv.reader(f)
        for line_num, row in enumerate(reader, start=1):
            if len(row) != 3:
                print(f"Warning: Skipping malformed row {line_num} in candidate.csv: {row}")
                continue

            candidate_id, name, seat = row

            if not validate_id(candidate_id):
                print(f"Warning: Skipping row {line_num} — invalid Candidate ID: {candidate_id}")
                continue
            if not name.isalpha() or len(name) > 10:
                print(f"Warning: Skipping row {line_num} — invalid name: {name}")
                continue
            if len(seat) != 2 or not seat.isdigit():
                print(f"Warning: Skipping row {line_num} — invalid seat: {seat}")
                continue

            candidates[candidate_id] = {"name": name, "seat": seat}

    return candidates


def save_candidates(candidates):
    """Saves the current candidates dictionary to candidate.csv."""
    with open(CANDIDATE_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for candidate_id, data in candidates.items():
            writer.writerow([candidate_id, data["name"], data["seat"]])


def seat_taken(candidates, seat_number):
    """Checks if a seat number is already assigned to any candidate."""
    return any(data["seat"] == seat_number for data in candidates.values())

def add_candidate(candidates):
    candidate_id = input("Enter Candidate ID (10 digits): ").strip()

    if len(candidate_id) != 10 or not candidate_id.isdigit():
        print("Error: Candidate ID must be exactly 10 digits.")
        return

    if not validate_id(candidate_id):
        print("Error: Invalid Candidate ID (check digit mismatch).")
        return

    if candidate_id in candidates:
        print("Error: Candidate ID already registered.")
        return

    name = input("Enter First Name (letters only, max 10 chars): ").strip()
    if not name.isalpha() or len(name) > 10:
        print("Error: Name must contain letters only and be at most 10 characters.")
        return

    seat = input("Enter Candidate Seat Number (2 digits): ").strip()
    if len(seat) != 2 or not seat.isdigit():
        print("Error: Seat number must be exactly 2 digits.")
        return
    if seat_taken(candidates, seat):
        print("Error: Seat number already assigned to another candidate.")
        return

    candidates[candidate_id] = {"name": name, "seat": seat}
    save_candidates(candidates)
    print(f"Candidate {name} registered to seat {seat}.")


def view_candidates(candidates):
    if not candidates:
        print("No candidates registered yet.")
        return

    print("\n--- Registered Candidates ---")
    print(f"{'Candidate ID':<15}{'Name':<12}{'Seat':<5}")
    for candidate_id, data in candidates.items():
        print(f"{candidate_id:<15}{data['name']:<12}{data['seat']:<5}")


def candidate_menu(candidates):
    while True:
        print("\n--- Candidate Registration Menu ---")
        print("1. Add Candidate")
        print("2. View Candidates")
        print("3. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_candidate(candidates)
        elif choice == "2":
            view_candidates(candidates)
        elif choice == "3":
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    candidates = load_candidates()
    candidate_menu(candidates)