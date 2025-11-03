# server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Import all feature modules
import auth, restaurant, staff, waste, inventory, ordering, supplier, notify, reports, logs, chatbot, mobile, admin, api_docs

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query = parse_qs(parsed_url.query)

        # Map GET routes to feature handlers
        routes_get = {
            '/': self.home,
            '/auth/login': lambda h, q: h.send_error(405),  # use POST for login/register
            '/auth/register': lambda h, q: h.send_error(405),
            '/restaurant/register': lambda h, q: h.send_error(405),
            '/staff/add': lambda h, q: h.send_error(405),
            '/waste/analytics': waste.analytics,
            '/inventory/list': inventory.list_inventory,
            '/order/list': ordering.list_orders if hasattr(ordering, "list_orders") else self.dummy,
            '/supplier/list': supplier.list_suppliers,
            '/notify/list': notify.list_notifications,
            '/report/export': reports.export_report,
            '/logs/view': logs.view_logs,
            '/chatbot/query': lambda h, q: h.send_error(405),
            '/mobile/waste_summary': mobile.waste_summary,
            '/admin/dashboard': admin.dashboard,
            '/api/docs': api_docs.documentation,
        }

        handler = routes_get.get(path, self.not_found)
        handler(self, query)

    def do_POST(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len).decode('utf-8')
        post_data = parse_qs(post_body)

        # Map POST routes to feature handlers
        routes_post = {
            '/auth/login': auth.login,
            '/auth/register': auth.register,
            '/restaurant/register': restaurant.register,
            '/staff/add': staff.add_staff,
            '/waste/track': waste.track,
            '/inventory/add': inventory.add_inventory,
            '/order/manual': ordering.manual_order,
            '/order/auto': ordering.auto_order,
            '/supplier/add': supplier.add_supplier,
            '/notify/waste': notify.notify_waste,
            '/chatbot/query': chatbot.query,
        }

        handler = routes_post.get(path, self.not_found)
        handler(self, post_data)

    def home(self, handler, *args):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Welcome to Restaurant Waste Management System</h1>")

    def not_found(self, *args, **kwargs):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"404 Not Found")

    def dummy(self, *args, **kwargs):
        self.send_response(501)
        self.end_headers()
        self.wfile.write(b"Not Implemented")

def run():
    server = HTTPServer(('', 8080), RequestHandler)
    print("Running server on port 8080...")
    server.serve_forever()

if _name_ == '_main_':
    run()