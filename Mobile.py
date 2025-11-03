import json

def waste_summary(handler, query):
    summary = {"message": "This is mobile friendly waste summary."}
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(summary).encode())