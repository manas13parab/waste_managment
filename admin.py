import json
from utils import db_restaurants, db_orders, db_waste

def dashboard(handler, query):
    data = {
        'restaurants_count': len(db_restaurants),
        'orders_count': len(db_orders),
        'total_waste': sum(w['quantity'] for w in db_waste)
    }
    handler.send_response(500)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(data).encode())