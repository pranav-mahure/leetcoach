# LeetCoach CLI

LeetCoach is a simple command-line tool built with Python to help track your DSA / LeetCode problem-solving progress.
It stores your problems locally in a JSON file and provides easy commands for adding, listing, updating, and filtering problems.

> This project focuses on:

* practicing Python fundamentals
* working with JSON data
* building a clean CLI interface
* maintaining structured progress logs
---

## Features (Current State)

1. ✅ Add Problem

* Choose platform (LeetCode, GFG, HackerRank, etc.)
* Select multiple topics
* Choose difficulty (Easy/Medium/Hard)
* Choose status (understood, need_revision, attempting, to-do)
* Automatically assigns ID and date solved
<br>


2. ✅ List Problems
* Displays all logged problems with:
  - ID
  - Name
  - Platform
  - Difficulty
  - All topics (comma-separated)
  - Status
  - Date solved
<br>

* Supports both:

   - old single-topic entries ("topic")
   - new multi-topic entries ("topics")
<br>
3. ✅ Update Problem Status
* Update the status of a problem by its ID
<br>
4. ✅ Filter Problems
* Filter problems by:
  - Platform
  - Topic
  - Difficulty
  - Status
* Combine multiple filters for refined searches
<br>
5. ✅ Data Storage
* Problems are stored in a local JSON file (`problems.json`)
* Each problem entry includes:
  - ID
  - Name
  - Platform
  - Topics (list)
  - Difficulty
  - Status
  - Date solved
---
 ## Project Structure
```
leetcoach-cli/
│
├── main.py          # CLI interface and user interaction
├── storage.py       # File handling, JSON loading/saving, data operations
├── problems.json    # Local storage for all problem entries
└── README.md        # Project documentation
```
### How to Run
1. Ensure you have Python installed (version 3.6 or higher).
2. Clone the repository.

```
git clone <your-repo-url>
cd leetcoach-cli
```
3. Run the main script.

```
python main.py
```
4. Follow the on-screen prompts to add, list, update, or filter problems.
---

### Sample Usage:-
```
=== Add New Problem ===
Problem Name :- Two Sum
Choose Platform:
1. LeetCode
2. GFG
...
Choose Topic (multiple, comma-separated):
1. Arrays
2. Hash Table
...
Topics :- 1,2
Choose Difficulty:
1. Easy
2. Medium
Choose Status:
1. understood
2. need_revision
Saved! ID = 3
```
### List problems
```
[3] Two Sum | LeetCode | Easy | Arrays, Hash Table | understood | 2025-12-08
```
### Update problem status
```
Enter Problem ID :- 3
New Status :- need_revision
Status updated successfully!
```
### Data Format Example
```json
[
  {
    "id": 1,
    "name": "Reverse Linked List",
    "platform": "LeetCode",
    "topics": ["Linked List"],
    "difficulty": "Easy",
    "status": "understood",
    "date_solved": "2025-12-01"
  },
  {
    "id": 2,
    "name": "Longest Substring Without Repeating Characters",
    "platform": "LeetCode",
    "topics": ["Strings", "Sliding Window"],
    "difficulty": "Medium",
    "status": "need_revision",
    "date_solved": "2025-12-05"
  }
]
```
---
## Goal for the Project:
This project is intentionally beginner-friendly.
It helps practice:

* clean code architecture
* CLI design
* JSON-based storage
* handling lists vs strings (multi-topic logic)
* incremental improvements
* working like a real developer with commits

## Future Enhancements (Planned)
* ✅ Multi-topic support for problems
* Problem editing (change name/platform/topics)
* Delete a problem
* Stats (solved count, topic distribution, progress timeline)
* Export to CSV
* Turn it into a Flask app later if desired
* User authentication for multiple users
* Cloud storage integration (e.g., Google Drive, Dropbox)
* Integration with LeetCode API for automatic problem fetching
* Dockerize the application for easier deployment
---
## License
MIT License <br>
See LICENSE file for details.
