import elasticsearch as esearch
import pandas as pd
from progressbar import ProgressBar

es= esearch.Elasticsearch()
es.indices.create(index='events', ignore=400)
doc_type = 'internship'

dtf = pd.read_csv('internships.csv')

bar = ProgressBar()
for st in bar(dtf.iterrows()):
    try:
        content = dict()

        content['date'] = st[1]['date']
        content['text'] = st[1]['text']


        es.index(index='events',  doc_type=doc_type, id=st[1]['id'], body=content)
    except:
        print('skip {}'.format(content['link']))
