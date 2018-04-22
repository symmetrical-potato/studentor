import elasticsearch as esearch
import pandas as pd

es = esearch.Elasticsearch(hosts=['127.0.0.1'])


def find_by_string(string):
    '''
    Поиск по строке во всех дипломах и всех вакансих по строке (сейчас только по дипломам)
    :param string:
    :return: топ-10 результатов наиболее совпадающие по этому запросу
    [
        {
            'type': 'vacancy/document'
            'id': int
            'title': str
            'link' : str
            'score' : float
        }, ...
    ]
    '''
    quer = {
        'query':
            {
                'match':
                    {
                        'text': string,
                    }
            }
    }
    res = []

    cur = es.search(index='uni', doc_type='diploma', body=quer)
    for hit in cur['hits']['hits']:
        res.append({'id': int(hit['_id']),
                    'score': hit['_score'],
                    'title': hit['_source']['title'],
                    'link': hit['_source']['link'],
                    'type': 'diploma'})

    # TODO: Сделать поиск по вакансиям

    return res


def find_by_supervisor(supervisor):
    '''
    Все работы студентов с определенным научником
    :param supervisor str: фио научника
    :return: всес студенты определенного научника
        [
            {
                'student_name': str,
                'student_id': int
                'theme_name': str
            }, ...
        ]
    '''
    st_names = pd.read_csv('st_names.csv')
    quer = {
        'size': 30,
        'query':
            {
                'match':
                    {
                        'supervisor': supervisor,
                    }
            }
    }

    res = []

    cur = es.search(index='uni', doc_type='diploma', body=quer)
    for hit in cur['hits']['hits']:
        res.append({'student_id': int(hit['_id']),
                    'student_name': st_names.name[int(hit['_id'])],
                    'theme_name': hit['_source']['title']})

    return res


def find_students_by_theme(theme_name):
    '''
    Поиск наиболее подходящих студентов по теме работодателя
    :arg theme_name string
    :return: top-5 students sorted by distance
        [
                {
                    'student_name': str, фио студента
                    'student_id': integer,
                    'rating': float, нормированное число
                }, ...
            ]
    '''

    quer = {
        'query':
        {
            'match' :
            {
                'text' : theme_name,
            }
        }
    }
    # quer = {
    #     'size': 10000,
    #     'query':
    #         {
    #             'match_all':
    #                 {
    #
    #                 },
    #
    #         }
    # }
    res = []

    cur = es.search(index='uni', doc_type='diploma', body=quer)
    for hit in cur['hits']['hits']:
        res.append({'id': int(hit['_id']),
                    'score': hit['_score'],
                    'title': hit['_source']['title'],
                    'link': hit['_source']['link'],
                    'type': 'diploma'})

    return res


def find_event_by_string(string):
    '''
    Поиск по строке во всех event-ах
    :param string:
    :return: топ-10 результатов наиболее совпадающие по этому запросу
    [
        {
            'type': 'vacancy/document'
            'id': int
            'title': str
            'link' : str
            'score' : float
        }, ...
    ]
    '''
    quer = {
        'query':
            {
                'match':
                    {
                        'text': string,
                    }
            }
    }
    res = []

    cur = es.search(index='events', doc_type='internship', body=quer)
    for hit in cur['hits']['hits']:
        res.append({'id': int(hit['_id']),
                    'score': hit['_score'],
                    'text': hit['_source']['text'],
                    'date': hit['_source']['date']})

    return res


def add_event_to_index(content):
    """
    Add `content` (dict object) to elasticsearch index
    must be dict and contain folowing keys:
    - `id`
    - `text`
    - `date`
    :content (dict): 
    """

    try:
        new_content = dict()
        new_content['text'] = content['text']
        new_content['date'] = content['date']
        es.index(index='events', doc_type='internship', id=content['id'], body=content)
    except Exception as e:
        print(e)


def put_diploma_to_index(diploma):
    try:
        id = diploma['id']
        es.index(index='uni', doc_type='diploma', id=id, body=diploma, request_timeout=30)
    except Exception as e:
        print(e)


def patch_diploma_in_index(diploma):
    pass


def get_all_vacancies():
    doc = {
        'size': 10000,
        'query': {
            'match_all': {}
        }
    }
    cur = es.search(index='events', doc_type='internship', body=doc)

    res = []

    for hit in cur['hits']['hits']:
        res.append({'id': int(hit['_id']),
                    'text': hit['_source']['text']
                    })

    return res


{"uni": {"aliases": {},
         "mappings": {"diploma": {
             "properties": {"link": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                            "speciality": {"type": "text",
                                           "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                            "supervisor": {"type": "text",
                                           "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                            "text": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                            "title": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                            "type": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                            "university": {"type": "text",
                                           "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
                            "year": {"type": "long"}}}},
         "settings": {
             "index": {"creation_date": "1521973267912", "number_of_shards": "5", "number_of_replicas": "1",
                       "uuid": "VTzqXhJbS0SATdDEvyqn7A", "version": {"created": "6020399"}, "provided_name": "uni"}}}}
