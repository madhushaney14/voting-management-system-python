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