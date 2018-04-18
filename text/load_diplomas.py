import elasticsearch as esearch
import pandas as pd
from progressbar import ProgressBar

es= esearch.Elasticsearch()
es.indices.create(index='uni', ignore=400)
doc_type = 'diploma'

dtf = pd.read_csv('diplomas.csv')

bar = ProgressBar()
for st in bar(dtf.iterrows()):
    try:
        content = dict()

        content['university'] = st[1]['university']
        content['speciality'] = st[1]['speciality']
        content['supervisor'] = st[1]['supervisor']
        content['type'] = st[1]['type']
        content['title'] = st[1]['title']
        content['text'] = st[1]['text']
        content['year'] = st[1]['year']
        content['link'] = st[1]['link']

        es.index(index='uni',  doc_type=doc_type, id=st[1]['id'], body=content)
    except:
        print('skip {}'.format(content['link']))
