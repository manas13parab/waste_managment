import json
from utils import db_waste

def track(handler, post_data):
    waste_type = post_data.get('waste_type', [''])[0]
    quantity = float(post_data.get('quantity', ['0'])[0])
    restaurant_id = post_data.get('restaurant_id', [''])[0]
