import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict


def show_votes_trend_chart(candidates, ballots):
    """Plots cumulative votes over time, one line per candidate."""
    if not ballots:
        print("No votes cast yet — nothing to plot.")
        return

    candidate_votes = defaultdict(list)
    for data in ballots.values():
        candidate_votes[data["candidate_id"]].append(data["date"])

    plt.figure(figsize=(9, 6))

    for cid, dates in candidate_votes.items():
        dates_sorted = sorted(dates, key=lambda d: datetime.strptime(d, "%Y-%m-%d"))
        x_dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates_sorted]
        y_cumulative = list(range(1, len(x_dates) + 1))

        name = candidates.get(cid, {}).get("name", cid)
        plt.plot(x_dates, y_cumulative, marker="o", label=name)

    plt.xlabel("Date")
    plt.ylabel("Cumulative Votes")
    plt.title("Vote Trend Over Time by Candidate")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def reports_menu(candidates, ballots):
    print("\n--- Reports Menu ---")
    print("Generating trend chart...")
    show_votes_trend_chart(candidates, ballots)

if __name__ == "__main__":
    from candidate_module import load_candidates
    from voting_module import load_ballots

    candidates = load_candidates()
    ballots = load_ballots()
    reports_menu(candidates, ballots)