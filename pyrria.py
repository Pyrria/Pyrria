#! /usr/bin/env python
from twisted.internet import reactor, protocol

class Server(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print(data)
        cmd = data[5]
        if cmd == '\x01':
            print('Got a connect request, accepting')
            self.transport.write('\x03\x00\x00\x00\x00')
        elif cmd == '\x02':
            print('Got disconnect')

    def connectionLost(self, reason=None):
        print(' * Lost connection')

def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Server
    reactor.listenTCP(7777, factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
