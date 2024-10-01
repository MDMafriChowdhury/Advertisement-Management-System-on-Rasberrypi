import http.server
import socketserver
import sqlite3
import json
from urllib.parse import urlparse, parse_qs

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/api/get_video_data'):
            query_params = parse_qs(urlparse(self.path).query)
            machine_id = query_params.get('machine_id', [None])[0]

            if machine_id is not None:
                conn = sqlite3.connect('schedule.db')
                cursor = conn.cursor()

                query = """
                SELECT start_time, end_time, video_id 
                FROM schedules 
                WHERE machine_id = ? 
                AND time(start_time) > time('now', 'localtime')
                """
                cursor.execute(query, (machine_id,))
                rows = cursor.fetchall()

                conn.close()

                if rows:
                    video_data_list = []
                    for row in rows:
                        start_time, end_time, video_id = row
                        video_data_list.append({
                            'start_time': start_time,
                            'end_time': end_time,
                            'video_id': video_id
                        })

                    response = json.dumps(video_data_list)
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(response.encode())
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    message = {'message': 'No data found for the given machine ID or future schedules'}
                    self.wfile.write(json.dumps(message).encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                message = {'message': 'Missing machine ID parameter'}
                self.wfile.write(json.dumps(message).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            message = {'message': 'Endpoint not found'}
            self.wfile.write(json.dumps(message).encode())


# Set up the HTTP server
PORT = 8080
handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
