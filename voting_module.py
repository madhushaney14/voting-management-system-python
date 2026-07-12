import csv
import os
from validators import is_valid_date

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