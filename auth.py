import json
from utils import db_users

def register(handler, post_data):
    username = post_data.get('username', [''])[0]
    password = post_data.get('password', [''])[0]
    role = post_data.get('role', [''])[0]

    for user in db_users:
        if user['username'] == username:
            handler.send_response(400)
            handler.end_headers()
            handler.wfile.write(b"Username exists")
            return

    db_users.append({'username': username, 'password': password, 'role': role})
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps({'message': 'User registered'}).encode())

def login(handler, post_data):
    username = post_data.get('username', [''])[0]
    password = post_data.get('password', [''])[0]
    for user in db_users:
        if user['username'] == username and user['password'] == password:
            handler.send_response(200)
            handler.send_header('Content-Type', 'application/json')
            handler.end_headers()
            handler.wfile.write(json.dumps({'message': 'Login success', 'role': user['role']}).encode())
            return
    handler.send_response(401)
    handler.end_headers()
    handler.wfile.write(b"Invalid credentials")