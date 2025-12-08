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

def add_problem(name,platform,difficulty,topic,status):
    problems = load_problems()

    new_id = (problems[-1]["id"]+1) if problems else 1

    problem = {
        "id" : new_id,
        "name" : name,
        "platform": platform,
        "difficulty" : difficulty,
        "status" : status,
        "topic" : topic,
        "Date Solved" : date.today().isoformat(),
    }
    problems.append(problem)
    save_problems(problems)
    return problem

