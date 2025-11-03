#
import json
from utils import db_logs

def view_logs(handler, query):
    logs = db_logs[-50:]  # last 50 logs
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(logs).encode())