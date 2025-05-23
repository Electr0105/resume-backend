from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient, exceptions

credential = DefaultAzureCredential()

client = CosmosClient(url="https://resume-cosmosdb.documents.azure.com:443", credential=credential)

database = client.get_database_client("resume-db")
container = database.get_container_client("resume-container")

def get_item(container):
    try:
        item = container.read_all_items(partition_key=item_id)
        return item
    except exceptions.CosmosResourceNotFoundError:
        return None

def increment_item_value(container, item_id):
    item = get_item(container, item_id)
    if item:
        item["value"] += 1
        container.replace_item(item=item_id, body=item)
        return item

item_id = "visitor-count"

items = get_item(container)
test = None
for item in items:
    test = item

print(test)
