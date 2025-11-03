db_waste.append({
    'waste_type': waste_type,
    'quantity': quantity,
    'location': post_data.get('location', [''])[0],
    'restaurant_id': restaurant_id
})