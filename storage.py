import json
from datetime import date
from pathlib import Path

DATA_FILE =Path("problems.json")

def load_problems():

    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE ,'r',encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        
def save_problems(problems):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(problems,f,indent=4)

def add_problem(name,platform,difficulty,topics,status_list):
    problems = load_problems()

    if problems:
        new_id = max(p["id"] for p in problems) + 1 # OR simple len(problems) +1 
    else:
        new_id = 1

    problem = {
        "id" : new_id,
        "name" : name,
        "platform": platform,
        "difficulty" : difficulty,
        "status" : status_list,
        "topic" : topics, # List
        "Date Solved" : str(date.today()),
    }
    problems.append(problem)
    save_problems(problems)
    return problem

def update_problem_status(problem_id, new_status):
    problems = load_problems()
    for p in problems:
        if p["id"] == problem_id:
            p["status"] = new_status
            save_problems(problems)
            return True
    return False

def filter_problems(status=None, difficulty=None, topic=None):
    problems = load_problems()
    result = problems

    if status:
        result = [p for p in result if p["status"].lower() == status.lower()]
    if difficulty:
        result = [p for p in result if p["difficulty"].lower() == difficulty.lower()]
    if topic:
        result = [p for p in result if p["topic"].lower() == topic.lower()]

    return result

