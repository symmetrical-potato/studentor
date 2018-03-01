import elasticsearch as esearch
import pandas as pd

es = esearch.Elasticsearch()


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
            'match' : 
            {
                'text' : string,
            }
        }
    }
    res = []
    
    cur = es.search(index='uni', doc_type='diploma', body=quer)
    for hit in cur['hits']['hits']:
        res.append({'id'    : int(hit['_id']),
                   'score'  : hit['_score'],
                   'title'  : hit['_source']['title'],
                   'link'   : hit['_source']['link'],
                   'type'   : 'diploma'})
        
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
        'size' : 30,
        'query':
            {
                'match' : 
             {
                 'supervisor' : supervisor,
             }
            }
    }
    
    res = []
    
    cur = es.search(index='uni', doc_type='diploma', body=quer)
    for hit in cur['hits']['hits']:
        res.append({'student_id'    : int(hit['_id']),
                    'student_name'  : st_names.name[int(hit['_id'])],
                    'theme_name'    : hit['_source']['title']})
        
        
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
    res = []
    
    cur = es.search(index='uni', doc_type='diploma', body=quer)
    for hit in cur['hits']['hits']:
        res.append({'id'    : int(hit['_id']),
                   'score'  : hit['_score'],
                   'title'  : hit['_source']['title'],
                   'link'   : hit['_source']['link'],
                   'type'   : 'diploma'})
        
        
    return res


def find_vacancy_by_student(student_name):
    '''
    Поиск наиболее подходящих вакансий для студента
    :param student_name string: фио
    :return:top-5 vacancies sorted by distance
        [
            {
                'vacancy_name': str,
                'vacancy_id': integer,
                'rating': float
            }, ...
        ]
    '''
    pass

