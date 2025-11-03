import json
from utils import db_waste, db_orders

def export_report(handler, query):
    report = {
        'total_waste': sum(w['quantity'] for w in db_waste),
        'total_orders': len(db_orders)
    }
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(report).encode())