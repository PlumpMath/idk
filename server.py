import direct
from pandac.PandaModules import *
loadPrcFileData('', 'window-type none')
from direct.directbase.DirectStart import *
import random

from direct.distributed.ServerRepository import ServerRepository
from direct.distributed.ClientRepository import ClientRepository

class MyServerRepository(ServerRepository):
    def __init__(self):
        tcpPort = base.config.GetInt('server-port', 4400)
        dcFileNames = ['direct.dc', 'net.dc']
        
        ServerRepository.__init__(self, tcpPort, None, dcFileNames = dcFileNames)

server = MyServerRepository()

class MyAIRepository(ClientRepository):
    def __init__(self):
        dcFileNames = ['direct.dc', 'net.dc']
        
        ClientRepository.__init__(self, dcFileNames = dcFileNames,
                                  dcSuffix = 'AI')

        tcpPort = base.config.GetInt('server-port', 4400)
        url = URLSpec('http://127.0.0.1:%s' % (tcpPort))
        self.connect([url],
                     successCallback = self.connectSuccess,
                     failureCallback = self.connectFailure)
        
    def connectFailure(self, statusCode, statusString):
        raise StandardError, statusString

    def connectSuccess(self):
        self.acceptOnce('createReady', self.createReady)

    def createReady(self):
        self.timeManager = self.createDistributedObject(
            className = 'TimeManagerAI', zoneId = 1)

air = MyAIRepository()

run()
