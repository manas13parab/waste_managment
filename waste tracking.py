import json
from utils import db_waste

def track(handler, post_data):
    waste_type = post_data.get('waste_type', [''])[0]
    quantity = float(post_data.get('quantity', ['0'])[0])
    restaurant_id = post_data.get('restaurant_id', [''])[0]

    db_waste.append({'waste_type': waste_type, 'quantity': quantity, 'restaurant_id': restaurant_id})
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps({'message': 'Waste tracked'}).encode())
