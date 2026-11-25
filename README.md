# 🗳️ Voting Management System (Python)

A menu-driven voting management system built in Python as university coursework at the Informatics Institute of Technology (IIT), Sri Lanka.

## ✨ Features

- 👤 **Voter management**: load, save, add, edit, search and delete voters
- 🧾 **Candidate management**: register and view candidates
- ✅ **ID validation**: generate and verify 10-digit IDs with a check digit
- 🗳️ **Voting**: cast and record ballots
- 🗺️ **District results** and 📈 **trend graphs** in the reports module

## 🗂️ Project structure

| File | Purpose |
|---|---|
| `main.py` | Main menu that links all the modules |
| `voter_module.py` | Voter menu and records |
| `candidate_module.py` | Candidate registration and listing |
| `voting_module.py` | Voting logic |
| `validators.py` | ID generation and check-digit validation |
| `districts.py` | District data |
| `reports.py` | Results and trend graphs |
| `*.csv` | Sample voter, candidate and ballot data |

## 🚀 Run it

```bash
git clone https://github.com/madhushaney14/voting-management-system-python.git
cd voting-management-system-python
python main.py
```

## 🔁 See also

The same system built in Java with Maven and JUnit: [voting-management-system-java](https://github.com/madhushaney14/voting-management-system-java)
