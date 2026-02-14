def load_skills():
    with open("data/skills.txt") as f:
        return[skill.strip() for skill in f.readlines()]
    
def extract_skills(text):
    skills_db = load_skills()
    found_skills =[]

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)
    return list(set(found_skills))
          
