#!/usr/local/bin/python
from SocketServer import TCPServer,StreamRequestHandler

class Handler(StreamRequestHandler):
  def handle(self):
    addr=self.request.getpeername()
    print 'Get connection',addr
    self.wfile.write('Thank you for your connection.')
server=TCPServer(('',1234),Handler)
server.serve_forever()
