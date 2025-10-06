
from flask import request, jsonify
from app import app, db
from models import Restaurant

@app.route('/restaurant/register', methods=['POST'])
def register_restaurant():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    # Create a new Restaurant instance
    rest = Restaurant(name=data['name'])
    db.session.add(rest)
    db.session.commit()

    return jsonify({'message': 'Restaurant registered', 'id': rest.id})

#test commit