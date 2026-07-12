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



if __name__ == "__main__":
    test_voters = {
    "3141592657": {"district": "Colombo", "age": 20},
    "9876543215": {"district": "Kandy", "age": 22}
    }

    save_voters(test_voters)
    print("Saved test voters to voter.csv")

    loaded = load_voters()
    print(f"Loaded voters: {loaded}")