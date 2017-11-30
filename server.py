import BaseHTTPServer
import os 

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    #obradi get request
    def do_GET(self):
        #os.getcwd -> get_current_working_directory
        #self.path -> putanja do filea kojeg browser trazi        
        print os.getcwd() + self.path
        try:
            if self.path == "/":
                full_path = os.getcwd() + "/index.html"
            else:
                full_path=os.getcwd() + self.path
                
            if not os.path.exists(full_path):
                raise Exception("%s not found"%self.path)
            elif os.path.isfile(full_path):
                self.handle_file(full_path)
        except Exception as msg:
            self.handle_error(msg)
            
    def handle_error(self , msg):
        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        page = self.read_file(os.getcwd()+"/404.html")
        print page
        page = page.replace("{msg_placeholder}", str(msg))
        self.send_header("Content-Length", str(len(page))) 
        self.end_headers()
        self.wfile.write(page)

    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-Type","text/html")    

        self.send_header("Content-Length", str(len(page))) 
        self.end_headers()
        self.wfile.write(page)
    def handle_file(self,path):
        try:
            with open(path , "rb") as reader:
                content = reader.read()
            self.send_page(content)
        except IOError as msg:
            msg= "Nije pronadena stranica !"
    def read_file(self, path):
        try: 
            with open(path, "rb") as reader:
                content = reader.read()
            return content
        except IOError as msg:
            msg = "Nije pronadjena stranica"

if __name__ == '__main__':
    print "Starting web server..."
    print "Loading..."
    print "Plese wait . . . "
    serverAddress = ('',8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

