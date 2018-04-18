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

if __name__ == '__main__':
   print(find_by_string(input()))
   
