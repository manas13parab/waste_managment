def analytics(handler, query):
    total_by_type = {}
    for record in db_waste:
        wt = record['waste_type']
        total_by_type[wt] = total_by_type.get(wt, 0) + record['quantity']
    handler.send_response(200)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(total_by_type).encode())