import http.server
import socketserver
import RPi.GPIO as GPIO

#here you create a new handler, you had a new way to handle get request
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
       #this code execute when a GET request happen, then you have to check if the request happenned because the user pressed the button
        if self.path.find("turnlampon=true") != -1:
            #print("Lamp on")
            #GPIO.output(18,GPIO.HIGH)
            exec(open("turnon.py").read())
        else:
            #print("Lamp off")
            #GPIO.output(18,GPIO.LOW)
            exec(open("turnoff.py").read())
        return super().do_GET()


PORT = 8080
myHandler = Handler



with socketserver.TCPServer(("", PORT), myHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()