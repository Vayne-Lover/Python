#!/usr/local/bin/python
from SocketServer import TCPServer,ForkingMixIn,StreamRequestHandler

class Server(ForkingMixIn,TCPServer):
  pass

class Handler(StreamRequestHandler):
  def handle(self):
    addr=self.request.getpeername()
    print 'Get connection',addr
    self.wfile.write('Thank you for your connection.')

server=Server(('',1234),Handler)
server.serve_forever()
