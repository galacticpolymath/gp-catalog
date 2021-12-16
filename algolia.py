import os, json
from algoliasearch.search_client import SearchClient

client = SearchClient.create(
    'RY691ZY7L3',
    os.environ.get("ALGOLIA_ADMIN_KEY")
)

index = client.init_index('search_index')

with open('./index.json', 'r') as file:
    content = f.read()

data = json.loads(content)

index.save_objects(data)