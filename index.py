from os import listdir
from os.path import isfile, join, exists
import json

search_attributes = keys = ['ShortTitle', 'LastUpdated', 'PublishedOn', 'Title', 'Subtitle', 'SponsoredBy', 'Standards', 'Keywords']
lessons = [f for f in listdir('./') if not isfile(join('./', f)) and f[0] != "."]
index = []

assert len(lessons)!= 0, 'No lessons found...'

for lesson in lessons:
    json_path = lesson + '/LESSON.json'

    if exists(json_path):
        with open(json_path) as file:
            lesson_json = json.load(file)
            filtered_attributes = [x for x in search_attributes if x in lesson_json.keys()]
            search_terms = {attribute: lesson_json[attribute] for attribute in filtered_attributes}
            index += search_terms

    else:
        print("No LESSON.json found...")

with open('index.json', 'w') as json_file:
    json.dump(index, json_file)
