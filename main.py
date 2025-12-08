from storage import add_problem, load_problems


def add_problem_flow():
    print("\n=== Add New Problem ===")
    name = input("Probelm Name :- ")
    platform = input("platform (LeetCode/GFg/ets.):- ")
    difficulty = input("Difficulty(Easy/Medium/Hard):- ")
    topic = input("Tpoic (Array/Dp/Graph/etc.):- ")
    status = input("Status (understood/need_revision):- ")

    problem = add_problem(name,platform,difficulty,topic,status)
    print(f"\nSaved! ID = {problem['id']}\n")


def list_problem_flow():
    print("\n=== Your problems ===")
    problems = load_problems()
    if not problems:
        print("No problems saved yet.")
        return
    
    for p in problems:
        print(
            f"[{p['id']}] {p['name']} | {p['platform']} | {p['difficulty']} | "
            f"{p['topic']} | {p['status']} | {p['Date Solved']}"
        )
    print()


def main():
    while True:
        print("\n=== LeetCoach CLI ===")
        print("1. Add Problem")
        print("2. List problems")
        print("3. Exit")
        choice = input("Choose an option:- ")

        if choice == "1":
            add_problem_flow()
        elif choice == "2":
            list_problem_flow()
        elif choice == "3":
            print("Be consistent See you later !")
            break
        else:
            print("Inavlid Choice , Try Again.\n")

if __name__ == "__main__":
    main()