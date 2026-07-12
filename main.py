from voter_module import load_voters, voter_menu
from candidate_module import load_candidates, candidate_menu
from voting_module import load_ballots, voting_menu
from reports import reports_menu


def main():
    print("=== Voter Management System (VMS) — Python Module ===")

    voters = load_voters()
    candidates = load_candidates()
    ballots = load_ballots()

    print(f"Loaded {len(voters)} voters, {len(candidates)} candidates, {len(ballots)} ballots.")

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Voter Registration")
        print("2. Candidate Registration")
        print("3. Voting")
        print("4. Reports (Trend Graph)")
        print("5. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            voter_menu(voters)
        elif choice == "2":
            candidate_menu(candidates)
        elif choice == "3":
            voting_menu(voters, candidates, ballots)
        elif choice == "4":
            reports_menu(candidates, ballots)
        elif choice == "5":
            print("Exiting VMS. Goodbye.")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()