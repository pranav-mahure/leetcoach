from storage import add_problem, load_problems,update_problem_status,filter_problems


def add_problem_flow():
    platforms = ["LeetCode", "GFG", "HackerRank","CodeSignal","AlgoExpert","TopCoder"]
    topics = ["Arrays", "DP", "Graph", "Hash Table", "Pointers","Sorting","Linked Lists","Binary search","Backtracking",
              "Heaps","Stacks and queues","Trees","Binary Trees","greedy"]
    difficulty = ["Easy", "Medium","Hard"]
    status = ["understood","need_revision","Attempting","to-do"]

    print("\n=== Add New Problem ===")
    name = input("Problem Name :- ")

    print("Choose Platform:- ")
    for i, platform in enumerate(platforms, 1):
        print(f"{i}. {platform}")
    platform_index = int(input("Platform (select number): ")) - 1
    platform = platforms[platform_index]

    print("Choose Topic (multiple topics can be selected, seperated by commas):- ")
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic}")
    topic_indices =input("topics (selectnumber seperated by commas):- ")

    # input to list of indices
    topic_indices = [int(idx.strip()) -1 for idx in topic_indices.split(",") if idx.strip()]
    selected_topic = [topics[idx] for idx in topic_indices]

    print("Choose Difficulty:- ")
    for i,d in enumerate(difficulty,1):
        print(f"{i}.{d}")
    difficulty_idx =int(input("Difficulty (Select number):- ")) -1
    d = difficulty[difficulty_idx]

    print("Choose Status")
    for i,s in enumerate(status,1):
        print(f"{i}. {s}")
    status_idx = int(input("status (select number):- \n")) -1
    s = status[status_idx]


    problem = add_problem(name,platform,d, selected_topic,s)
    print(f"\nSaved! ID = {problem['id']}\n")


def list_problems_flow(problems = None):
    print("\n=== Your problems ===")
    if problems == None:
        problems = load_problems()

    if not problems:
        print("No problems saved yet.")
        return
    
    for p in problems:
        # both old data ("topic") and new data ("topics")
        topics_value = p.get("topics") or p.get("topic") or []

        if isinstance(topics_value, list):
            topic_str = ", ".join(topics_value)
        else:
            topic_str = topics_value
        print(
            f"[{p['id']}] {p['name']} | {p['platform']} | {p['difficulty']} | "
            f"{topic_str} | {p['status']} | {p['Date Solved']}"
        )
    print()

def update_status_flow():
    print("\n=== Update Problem Status ===")
    try:
        pid = int(input("Enter Problem ID :- "))
    except ValueError:
        print("Invalid ID. Must be a number.\n")
        return

    new_status = input("New Status (understood/need_revision) :- ")

    ok = update_problem_status(pid, new_status)
    if ok:
        print("Status updated successfully!\n")
    else:
        print("No problem found with that ID.\n")

def filter_problems_flow():
    print("\n=== Filter Problems ===")
    print("Leave blank if you don't want to filter by that field.\n")

    status = input("Status filter (TYPE understood/need_revision or blank) :- ").strip()
    difficulty = input("Difficulty filter (TYPE Easy/Medium/Hard or blank) :- ").strip()
    
    #  topic list and allowing numeric selection
    topics = ["Arrays", "DP", "Graph", "Hash Table", "Pointers", "Sorting", "Linked Lists", "Binary search",
            "Backtracking", "Heaps", "Stacks and queues", "Trees", "Binary Trees", "greedy"]

    print("Or pick from this list (numbers comma-separated):")
    for i, t in enumerate(topics, 1):
        print(f"{i}. {t}")
    pick = input("Pick by number or type names (press Enter to skip): ").strip()
    if pick:
        if all(c.isdigit() or c.isspace() or c == "," for c in pick):
            # numeric selection -> convert to names
            nums = [int(x.strip()) - 1 for x in pick.split(",") if x.strip()]
            selected = [topics[n] for n in nums if 0 <= n < len(topics)]
            topic = ",".join(selected)
        else:
            # treat as typed names
            topic = pick
    else:
        topic = None


    # empty strings to None
    status = status or None
    difficulty = difficulty or None
    topic = topic or None

    filtered = filter_problems(status=status, difficulty=difficulty, topic=topic)
    if not filtered:
        print("\nNo problems matched your filters.\n")
        return

    list_problems_flow(filtered)


def main():
    while True:
        print("\n=== LeetCoach CLI ===")
        print("1. Add Problem")
        print("2. List problems")
        print("3. Update Problem Status")
        print("4. Filter Problems")
        print("5. Exit")
        choice = input("Choose an option:- ")

        if choice == "1":
            add_problem_flow()
        elif choice == "2":
            list_problems_flow()
        elif choice == "3":
            update_status_flow()
        elif choice == "4":
            filter_problems_flow()
        elif choice == "5":
            print("Be consistent See you later !")
            break
        else:
            print("Inavlid Choice , Try Again.\n")

if __name__ == "__main__":
    main()