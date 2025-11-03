def auto_order(handler, post_data):
    restaurant_id = post_data.get('restaurant_id', [''])[0]
    to_order = []

    for item in db_inventory:
        if item['restaurant_id'] == restaurant_id and item['quantity'] < item['threshold']:
            qty = item['threshold'] - item['quantity']
            to_order.append({'item_name': item['item_name'], 'quantity': qty})

            # Add to orders
            db_orders.append({'item_name': item['item_name'], 'quantity': qty, 'status': 'pending', 'restaurant_id': restaurant_id})

    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps({'orders': to_order}).encode())