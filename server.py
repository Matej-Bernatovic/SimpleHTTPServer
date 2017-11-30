import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    Page= """
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
</head>
<body class="container">
<h1>Hello, web!</h1>
<div class="container"> This is test server ! </div>
</body>
</html>
"""
    #obradi get request
    def do_GET(self):        
        page = self.create_page()
        self.send_page(page)

    def create_page(self):
        page = self.Page
        return page
    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-Type","text/html")       
        self.send_header("Content-Length", str(len(page))) 
        self.end_headers()
        self.wfile.write(page)

if __name__ == '__main__':
    print "Starting web server..."
    print "Loading..."
    print "Plese wait . . . "
    serverAddress = ('',8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

