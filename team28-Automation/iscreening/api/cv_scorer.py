from bs4 import BeautifulSoup

def get_cv_dict(filename, static_fields, dynamic_fields):
    """
    Returns dict with keys: total_experience, highest_degree, previous_degree_1[Institute, GPA], skill_sets(d), previous_company_name(d)
    """
    cv_dict = {}
    soup = BeautifulSoup(open(filename, 'r'), 'html.parser')
    for static_field in static_fields:
        if len(soup.find(static_field).contents) > 0:
            cv_dict[static_field] = soup.find(static_field).contents[0]
        else:
            cv_dict[static_field] = None
    for dynamic_field in dynamic_fields:
        i = 1
        while(True):
            cur_field = dynamic_field + '_' + str(i)
            if soup.find(cur_field) is not None:
                if len(soup.find(cur_field)) > 0:
                    cv_dict[cur_field] = soup.find(cur_field).contents[0]
                else:
                    cv_dict[cur_field] = None
                i += 1
            else:
                break
    return cv_dict

def get_cv_score(cv_dict, university_dict, company_dict, degree_dict, required_skills):
    index = cv_dict['total_experience'].find('Year')
    total_exp = int(cv_dict['total_experience'][:index])
    static_company = 'current_company_name'
    prior_exp = 0
    for skill in required_skills:
        if static_company.find(skill) != -1:
            prior_exp += 1
    dynamic_company = 'previous_project_summmary'
    index = 1
    while(True):
        curr = dynamic_company + '_' + str(index)
        if curr in cv_dict:
            for skill in required_skills:
                if cv_dict[curr].lower().find(skill.lower()) != -1:
                    prior_exp += 1
            index += 1
        else:
            break
    skill_score = 0
    skills = 'skills_set'
    index = 1
    while(True):
        curr = skills + '_' + str(index)
        if curr in cv_dict:
            for skill in required_skills:
                if skill.lower() == cv_dict[curr].lower():
                    skill_score += 1
            index += 1
        else:
            break
    educational_score = 0
    if cv_dict['highest_degree'] in university_dict:
        educational_score += university_dict[cv_dict['hightest_degree']]
    index = 1
    while(True):
        curr = 'previous_degree' + '_' + str(index)
        if curr in cv_dict:
            if cv_dict[curr] in university_dict:
                educational_score += university_dict[cv_dict[curr]]
            index += 1
        else:
            break
    cv_score = 0.4 * total_exp + 0.3 * prior_exp + 0.3 * skill_score + 0.2 * educational_score
    return cv_score

def main():
    filename = './cv_parsed.txt'
    static_fields = ['total_experience', 'highest_degree', 'resume_context', 'current_company_name', 'current_project_summary']
    dynamic_fields = ['skills_set', 'previous_company_name', 'previous_designation', 'previous_project_summmary', 'previous_degree', 'previous_education_description']
    university_dict = {"Carnegie Mellon University": '0.9', "Princeton University": '0.91',
                       "Harvard University": '0.92', "Yale University": '0.79', "Columbia University": '0.89',
                       "Stanford University": '0.85', "Massachusetts Institute of Technology": '0.89',
                       "University of Pennsylvania": '0.72', "California Institute of Technology": '0.81',
                       "Johns Hopkins University": '0.68', "Dartmouth College": '0.75', "Northwestern University": '0.64',
                       "Brown University": '0.52', "Cornell University": '0.79', "Georgetown University": '0.44',
                       "IIT Bombay": '0.42', "IIT Madras": '0.46', "IISC Bangalore": '0.69',
                       "IIIT Vadodara": '0.41', "ISI Kolkata": '0.65'}

    company_dict = {"Google": '0.95', "Facebook": '0.93', "Amazon": '0.90', "Intel": '0.85',
                "Goldman Sachs": '0.86', "IBM": '0.82', "Mathworks": '0.60', "Microsoft": '0.92',
                "Hapramp": '0.55', "Neurala": '0.45', "Soma Analytics": '0.42', "Innoplexus": '0.62',
                "CERN": '0.97', "NASA": '0.75', "ISRO": '0.83', "Fossasia": '0.72',
                "Haskell": '0.71', "Bash.ai": '0.66', "Chase": '0.35', "Tesla": '0.78'}
    degree_dict = {"Bachelor"}
    required_skills = ['Java', 'Python', "Haskell"]
    cv_dict = get_cv_dict(filename, static_fields, dynamic_fields)
    cv_score = get_cv_score(cv_dict, university_dict, company_dict, degree_dict, required_skills)
    print(cv_score)

if __name__ == '__main__':
    main()
