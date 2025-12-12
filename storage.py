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
    
    if topics is None:
        topics_list = []
    elif isinstance(topics, str):
        topics_list = [t.strip() for t in topics.split(",") if t.strip()]
    else:
        topics_list = [str(t).strip() for t in topics]

    problem = {
        "id" : new_id,
        "name" : name.strip(),
        "platform": platform.strip(),
        "difficulty" : difficulty.strip(),
        "status" : status_list.strip(),
        "topics" : topics_list, # List
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
        result = [p for p in result if str(p.get("status", "")).lower() == status.lower()]
    if difficulty:
        result = [p for p in result if str(p.get("difficulty", "")).lower() == difficulty.lower()]
    if topic:
        if isinstance(topic, str):
            desired = [t.strip().lower() for t in topic.split(",") if t.strip()]
        else:
            desired = [str(t).strip().lower() for t in topic]

        def matches_problem(p):
            p_topics = p.get("topics")
            if p_topics == None:
                p_topics = p.get("topic")  ## To handle old 
            if p_topics == None:
                return False
            
            if isinstance(p_topics, str):
                p_list = [p_topics.strip().lower()]
            else:
                p_list = [str(x).strip().lower() for x in p_topics]
            return any(d in p_list for d in desired)

        ##keeping  only those problems p inside result for which matches_problem(p) returns True.
        result = [p for p in result if matches_problem(p)]
    return result

