#coding=utf-8
from  BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
import urllib
from optparse import OptionParser
import os
import sys
import threading
import time
if ''.join(os.getcwd()) not in sys.path:
    sys.path.append(os.getcwd())
    
port_normal = 8001  
port_unknown = 8002  
port_malicous = 8003
Path_normal = './FRS_Normal.txt'
Path_unknown = './FRS_Unknown.txt'
Path_malicous = './FRS_Malicious.txt'

'''
def parse_cmd():
    parser = OptionParser()
    parser.add_option("-f", "--file", action="store", 
       dest="filename", 
       default="./FRS_Normal.txt", 
       help="the filename of pua query result") 
    parser.add_option("-p", "--port", action="store", 
       dest="port", 
       default=8001, 
       help="the port op pua server")
    options, arguments = parser.parse_args()
    filename = options.filename
    port = options.port
    print(filename)
    print(port)
    return filename,port
'''

class ServerHTTP(BaseHTTPRequestHandler):
    global filePath
    def do_GET(self):
        print 'current time is :',time.time()    
        pathLength = len(self.path)
        print 'request content length is :' , pathLength
        #print path
        port = self.server.server_address[1]
        #print address
        #port = address[1]
        print 'request server port is:', port
        if 8001 == port:
            filePath = Path_normal
        elif 8002 == port:
            filePath = Path_unknown
        else:
            filePath = Path_malicous       
        try:
            fi = open(filePath, "r")
            #self.send_response(200)
            #self.send_header("Content-type","text/html")
            #self.send_header("test","This is test!")
            #self.end_headers()
            content = fi.read()
            print 'start to send response :'
            print content
            self.wfile.write(content)
            #print 'send success'
        except IOError as err:
            print('File Error:'+str(err)) 
        finally:
            fi.close()


    def do_POST(self):
        print 'current time is :',time.time()
        pathLength = self.headers['content-length']
        print 'request content length is :' , pathLength
        #print path
        port = self.server.server_address[1]
        #print address
        #port = address[1]
        print 'request server port is:', port
        if 8001 == port:
            filePath = Path_normal
        elif 8002 == port:
            filePath = Path_unknown
        else:
            filePath = Path_malicous       
        try:
            fi = open(filePath, "r")
            #self.send_response(200)
            #self.send_header("Content-type","text/html")
            #self.send_header("test","This is test!")
            #self.end_headers()
            content = fi.read()
            print 'start to send response :'
            print content
            self.wfile.write(content)
            #print 'send success'
        except IOError as err:
            print('File Error:'+str(err)) 
        finally:
            fi.close()


def start_server():
    http_server_normal = HTTPServer(('', int(port_normal)), ServerHTTP)
    server_thread_normal = threading.Thread(target=http_server_normal.serve_forever)
    #http_server_normal.serve_forever()
    http_server_unknown = HTTPServer(('', int(port_unknown)), ServerHTTP)
    server_thread_unknown = threading.Thread(target=http_server_unknown.serve_forever)
    #http_server_unknown.serve_forever()
    http_server_malicous = HTTPServer(('', int(port_malicous)), ServerHTTP)
    server_thread_malicous = threading.Thread(target=http_server_malicous.serve_forever)
    #http_server_malicous.serve_forever()
    server_thread_normal.setDaemon(False)
    server_thread_unknown.setDaemon(False)
    server_thread_malicous.setDaemon(False)
    server_thread_normal.start()
    server_thread_unknown.start()
    server_thread_malicous.start()
        

if __name__ == "__main__":
    #global filePath
    #filePath,port = parse_cmd()
    start_server()