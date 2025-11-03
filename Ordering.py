import json
from utils import db_orders

def manual_order(handler, post_data):
    item_name = post_data.get('item_name', [''])[0]
    quantity = float(post_data.get('quantity', ['0'])[0])
    restaurant_id = post_data.get('restaurant_id', [''])[0]

    db_orders.append({'item_name': item_name, 'quantity': quantity, 'status': 'pending', 'restaurant_id': restaurant_id})
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps({'message': 'Manual order placed'}).encode())