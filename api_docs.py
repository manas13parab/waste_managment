import json

def documentation(handler, query):
    docs = {
        'endpoints': [
            '/auth/login', '/auth/register',
            '/waste/track', '/waste/analytics',
            '/order/manual', '/order/auto',
            # etc...
        ],
        'description': 'API documentation for waste management project.'
    }
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(docs).encode())