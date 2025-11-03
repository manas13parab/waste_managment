import json

def query(handler, post_data):
    user_text = post_data.get('query', [''])[0]
    response = f"Bot received: {user_text}"
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps({'response': response}).encode())