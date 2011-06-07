#! /usr/bin/env python
from twisted.internet import reactor, protocol

class Server(protocol.Protocol):
    def dataReceived(self, data):
        self.output(data, 'self.stream.send(\'')
        buff = data
        while buff:
            packet = buff[0:ord(buff[0])+4]
            buff = buff[ord(buff[0])+4:]
#            self.output(packet, 'p: ')

#            self.output(data)
            cmd = packet[4]
            if cmd == '\x01':
                print('Got a connect request, accepting')
                self.transport.write('\x00\x00\x00\x00\x03\x00\x00\x00\x00')
            elif cmd == '\x02':
                print('Got disconnect')
            elif cmd == '\x04':
                print('Got character data')
                print('  ID: %s' % ord(data[5]))
                print('  Hair Style: %s' % ord(data[6]))
                print('    Hair (R)GB: %s' % ord(data[7]))
                print('    Hair R(G)B: %s' % ord(data[8]))
                print('    Hair RG(B): %s' % ord(data[9]))
            elif cmd == '\x05':
#                print('Got inventory data')
                pass
            elif cmd == '\x06':
                print('Got request for world data')
                
            elif cmd == '\x08':
                print('Got request for block')
                print('   (%s, %s)' % (data[6], data[7]))
            elif cmd == '\x0f':
                print('Got unknown command, 0x0f')
            elif cmd == '\x10':
                print('Got Player health from %s' % packet[5])
            elif cmd == '\x15':
                print('Got item info')
            elif cmd == '\x26':
                print('Got password response')
            elif cmd == '\x2a':
                print('Got player mana level')
                
            elif cmd == '\x16':
                print('Got item owner info')
                
    def output(self, data, pre=''):
        string = ''
        for char in data:
            string += '\\x' + str(ord(char)) + ':'
        print(pre + string)

    def _send(self, data):
        length = len(data)

    def _join(self, playerid):
        pass

    def _server_msg(self, msg):
        self.transport.write('\x0d\x00\x00\x00\x19\x08\xff\xff\xffHi World')

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
