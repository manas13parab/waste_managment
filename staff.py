import json
from utils import db_staff

def add_staff(handler, post_data):
    name = post_data.get('name', [''])[0]
    restaurant_id = post_data.get('restaurant_id', [''])[0]

    db_staff.append({'name': name, 'restaurant_id': restaurant_id, 'id': len(db_staff)+1})
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps({'message': 'Staff added'}).encode())
