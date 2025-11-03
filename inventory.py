import json
from utils import db_inventory

def add_inventory(handler, post_data):
    item_name = post_data.get('item_name', [''])[0]
    quantity = float(post_data.get('quantity', ['0'])[0])
    threshold = float(post_data.get('threshold', ['0'])[0])
    restaurant_id = post_data.get('restaurant_id', [''])[0]

    db_inventory.append({
        'item_name': item_name,
        'quantity': quantity,
        'threshold': threshold,
        'restaurant_id': restaurant_id
    })
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps({'message': 'Inventory added'}).encode())

def list_inventory(handler, query):
    rid = query.get('restaurant_id', [''])[0]
    filtered = [i for i in db_inventory if i['restaurant_id'] == rid]
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(filtered).encode())