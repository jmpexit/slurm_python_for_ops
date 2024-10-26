if __name__ == '__main__':
    jun_skills = {"ops", "researching"}
    middle_skills = {"ops", "communications", "researching", "leading"}
    senior_skills = {"ops", "dev", "communications", "researching", "prototyping", "leading"}

    print(jun_skills.difference(middle_skills))
    print(jun_skills.intersection(senior_skills))

