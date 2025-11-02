import json
from utils import db_notifications, db_waste, db_inventory

def notify_waste(handler, post_data):
    restaurant_id = post_data.get('restaurant_id', [''])[0]
    threshold = 50  # arbitrary threshold

    alerts = []
    for waste in db_waste:
        if waste['restaurant_id'] == restaurant_id and waste['quantity'] > threshold:
            msg = f"High waste alert: {waste['waste_type']} quantity {waste['quantity']}"
            db_notifications.append({'message': msg, 'restaurant_id': restaurant_id})
            alerts.append(msg)

    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps({'alerts': alerts}).encode())

def list_notifications(handler, query):
    rid = query.get('restaurant_id', [''])[0]
    filtered = [n for n in db_notifications if n['restaurant_id'] == rid]

    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(filtered).encode())