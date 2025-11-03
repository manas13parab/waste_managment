import json
from utils import db_restaurants

def register(handler, post_data):
    name = post_data.get('name', [''])[0]

    db_restaurants.append({'name': name, 'id': len(db_restaurants)+1})
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps({'message': 'Restaurant registered'}).encode())