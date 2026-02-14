def generate_suggestions(missing_skills,ats_score,similarity):
    tips=[]

    if ats_score <60:
        tips.append("Improve skill matching for better ATS score/All the best for Next Time.")

    if similarity <65:
        tips.append("Resume content is not semantically aligned with job description.")

    if missing_skills:
        tips.append("Please Check and Add missing skills:" + ",".join(missing_skills))


    if ats_score >= 60 and similarity >= 65 and not missing_skills:
        tips.append("Congratulations, you are an excellent fit for this role.")

    return tips
