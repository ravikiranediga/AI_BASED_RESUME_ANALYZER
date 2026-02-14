def calculate_ats(resume_skils,jd_skills):
    if not jd_skills:
        return 0

    matched=len(set(resume_skils)&set(jd_skills))
    score=(matched/len(jd_skills))*100
    return round(score,2)
