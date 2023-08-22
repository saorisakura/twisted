from twisted.internet import protocol


class Echo(protocol.Protocol):
    """
    Protocol that echoes back all data written to it.
    """

    def dataReceived(self, data):
        """
        Write back the data.
        """
        self.transport.write(data)

    def connectionMade(self):
        print("Connection made")

    def connectionLost(self, reason):
        print("Connection lost")

    def connectionFailed(self, reason):
        print("Connection failed")

    def connectionRefused(self):
        print("Connection refused")


class EchoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return Echo()

    def startedConnecting(self, connector):
        print("Started connecting")

    def clientConnectionLost(self, connector, reason):
        print("Client connection lost")

    def clientConnectionFailed(self, connector, reason):
        print("Client connection failed")


class EchoClient(protocol.Protocol):

    def dataReceived(self, data):
        print("Data received")

    def connectionMade(self):
        print("Connection made")

    def connectionLost(self, reason):
        print("Connection lost")

    def connectionFailed(self, reason):
        print("Connection failed")

    def connectionRefused(self):
        print("Connection refused")


class EchoClientFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        return EchoClient()

    def startedConnecting(self, connector):
        print("Started connecting")

    def clientConnectionLost(self, connector, reason):
        print("Client connection lost")

    def clientConnectionFailed(self, connector, reason):
        print("Client connection failed")


if __name__ == "__main__":
    from twisted.internet import reactor
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "server":
        # Run the server
        reactor.listenTCP(9090, EchoFactory())
        reactor.run()
    else:
        # Run the client
        reactor.connectTCP("localhost", 9090, EchoClientFactory())
        reactor.run()
