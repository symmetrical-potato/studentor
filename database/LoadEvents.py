import pandas as pd
import random

from progressbar import ProgressBar
from database.Models import *


path_to_events = "/home/artyom/PycharmProjects/HRHakaton/data/internships.csv"

companies = [("Macrosoft", "macrosoft@gmail.com", "1"), ("Giggle", "giggle@gmail.com", "1")]
companies_ids = []

for company in companies:
    empl = Employer()
    empl.name = company[0]
    empl.login = company[1]
    empl.set_password(company[2])

    db.session.add(empl)
    db.session.commit()

    companies_ids.append(empl.id)


es= esearch.Elasticsearch()
dtf = pd.read_csv(path_to_events)

bar = ProgressBar()
for st in bar(dtf.iterrows()):
    try:
        company_ind = random.randint(0, len(companies)-1)

        content = dict()

        content['name'] = "Стажировка от {}".format(companies[company_ind][0])
        content['description'] = st[1]['text']
        content['diploma'] = False
        content['employer_id'] = companies_ids[company_ind]

        event = Event(**content)
        event.create()
    except:
        print('skiped')

