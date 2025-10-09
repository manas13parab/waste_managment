from flask import request, jsonify
from app import app, db
from models import Staff

@app.route('/staff/add', methods=['POST'])
def add_staff():
    data = request.get_json()
    if not data or 'name' not in data or 'restaurant_id' not in data:
        return jsonify({'error': 'Name and restaurant_id are required'}), 400
    staff = Staff(name=data['name'], restaurant_id=data['restaurant_id'])
    db.session.add(staff)
    db.session.commit()
    return jsonify({'message': 'Staff added', 'id': staff.id})