import json
from utils import db_suppliers

def add_supplier(handler, post_data):
    name = post_data.get('name', [''])[0]
    contact = post_data.get('contact', [''])[0]

    db_suppliers.append({'name': name, 'contact': contact})
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps({'message': 'Supplier added'}).encode())

def list_suppliers(handler, query):
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(db_suppliers).encode())