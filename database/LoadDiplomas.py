import pandas as pd
import random

from progressbar import ProgressBar
from database.Models import *


path_to_events = "/home/artyom/PycharmProjects/HRHakaton/data/diplomas.csv"
path_to_names = "/home/artyom/PycharmProjects/HRHakaton/data/st_names.csv"

dtf = pd.read_csv(path_to_events)
names_dtf = pd.read_csv(path_to_names)

bar = ProgressBar()
for st, st2 in bar(zip(dtf.iterrows(), names_dtf.iterrows())):
    try:
        content = dict()

        content['university'] = st[1]['university']
        content['supervisor'] = st[1]['supervisor']
        content['type'] = st[1]['type']
        content['title'] = st[1]['title']
        content['text'] = st[1]['text']
        content['year'] = st[1]['year']
        content['link'] = st[1]['link']

        id = int(st2[1]['id'])
        name = st2[1]['name']

        student = Student()
        student.name = name
        student.id = id
        student.set_password(id)
        student.login = "{}@gmail.com".format(id)

        db.session.add(student)
        db.session.commit()

        document = Document(filename="", student_id = student.id, **content)
        document.create()
    except:
        print('skiped')