import requests
import json
import os
import datetime

from config import Config

def load_data():
    try:
        result = []

        last_loaded_data_id = get_last_loaded_data_id()
        offset = 0
        need_load_more = True
        new_last_loaded_data_id = None

        while need_load_more:
            data = download_data(offset)

            if "error" in data:
                write_error_message(json.dumps(data))
                return

            items = data["response"]["items"]
            if not items:
                break
            if new_last_loaded_data_id is None:
                new_last_loaded_data_id = items[0]["id"]
            need_load_more = len(items) == 100
            offset += 100

            for item in items:
                if last_loaded_data_id and item["id"] == last_loaded_data_id:
                    need_load_more = False
                    break

                text = item["text"]
                title, description = text.split("\n\n", 1)
                event_type, rest_title = title.split(" ", 1)
                if event_type == "Стажировка":
                    _, company_name = rest_title.split(" ", 1)
                    company_name = company_name[:-1]
                    result.append(("internship", company_name, description))
                else:
                    *_, company_name = rest_title.split(" ", 2)
                    company_name = company_name[:-1]
                    result.append(("diploma", company_name, description))


        
    except Exception as e:
        write_error_message(str(e))



def download_data(offset):
    parameters = {"owner_id": "-165384603", "offset":offset, "access_token": Config.VK_API_KEY, \
                                                                      "v": "5.74"}

    r = requests.get(r"https://api.vk.com/method/wall.get", params=parameters)
    text = r.text
    data = json.loads(text)

    return data

def get_last_loaded_data_id():
    cache_file = Config.PATH_TO_DATA_LOADER_CACHE
    if not os.path.isfile(cache_file):
        return None

    last_loaded_data_id = int(open(cache_file, "r").read())

    return last_loaded_data_id

def save_last_loaded_data_id(id):
    cache_file = Config.PATH_TO_DATA_LOADER_CACHE
    open(cache_file, "w").write(id)

def write_error_message(message):
    now = datetime.datetime.now()
    date_str = now.strftime("%H:%M:%S %Y/%m/%d")

    record = "Error while loading data. Time: {}. Message: {}.".format(date_str, message)

    log_file = Config.PATH_TO_DATA_LOADER_LOG
    open(log_file, "w+").write(record)

if __name__ == "__main__":
    load_data()