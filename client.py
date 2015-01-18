from direct.directbase.DirectStart import *
from direct.distributed.ClientRepository import ClientRepository
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.controls.GravityWalker import GravityWalker
from pandac.PandaModules import *
import sys
import random


class MyClientRepository(ClientRepository):
    def __init__(self):
        dcFileNames = ['direct.dc', 'net.dc']
        
        ClientRepository.__init__(self, dcFileNames = dcFileNames)

class World(DirectObject):

    rotateSpeed = 180

    moveSpeed = 20
       
    def __init__(self):
        DirectObject.__init__(self)
        base.camera.hide()
        self.access = 0

        self.av = None

        self.ToonSpeedFactor = 1.25
        self.ToonForwardSpeed = 16.0 * self.ToonSpeedFactor
        self.ToonJumpForce = 24.0
        self.ToonReverseSpeed = 8.0 * self.ToonSpeedFactor
        self.ToonRotateSpeed = 80.0 * self.ToonSpeedFactor
    


        self.moveKeyList = [
            'arrow_left', 'arrow_right', 'arrow_up', 'arrow_down'
            ]

        self.moveKeys = {}
        for key in self.moveKeyList:
            self.moveKeys[key] = False
            self.accept(key, self.moveKeyStateChanged, extraArgs = [key, True])
            self.accept(key + '-up', self.moveKeyStateChanged, extraArgs = [key, False])



        tcpPort = base.config.GetInt('server-port', 4400)
        hostname = base.config.GetString('server-host', '127.0.0.1')
        self.url = URLSpec('http://%s:%s' % (hostname, tcpPort))

        self.cr = MyClientRepository()
        
        self.waitingText = OnscreenText(
            'Connecting to %s.\nPress ESC to cancel.' % (self.url),
            scale = 0.1, fg = (1, 1, 1, 1), shadow = (0, 0, 0, 1))

        self.accept('escape', self.escape)

        base.disableMouse()

        base.cTrav = CollisionTraverser()

        self.cr.connect([self.url],
                        successCallback = self.connectSuccess,
                        failureCallback = self.connectFailure)

    def moveKeyStateChanged(self, key, newState):
        self.moveKeys[key] = newState


    def escape(self):
        sys.exit()
        
    def connectFailure(self, statusCode, statusString):
        self.waitingText.destroy()
        self.failureText = OnscreenText(
            'Failed to connect to %s: %s.\nPress ESC to quit.' % (self.url, statusString),
            scale = 0.15, fg = (1, 0, 0, 1), shadow = (0, 0, 0, 1))

    def connectSuccess(self):
        self.waitingText.destroy()
        self.waitingText = OnscreenText(
            'Waiting for server.',
            scale = 0.1, fg = (1, 1, 1, 1), shadow = (0, 0, 0, 1))

        self.cr.setInterestZones([1])

        self.acceptOnce('gotTimeSync', self.syncReady)

    def syncReady(self):
        if self.cr.haveCreateAuthority():
            self.createReady()
        else:
            self.acceptOnce('createReady', self.createReady)

    def createReady(self):
        self.waitingText.destroy()

        self.av = self.cr.createDistributedObject(
            className = 'DistributedToon', zoneId = 2)
        self.av.setupLocalAvatar()
        
        self.offset = 3.2375
        base.camera.reparentTo(self.av)
        base.camera.setPos(0, -10.0 - self.offset, self.offset)
        base.camera.hide()
        

        self.av.startPosHprBroadcast()
    def changeAvZone(self, zoneId):
        if zoneId == 999 and self.access >= 100:
            self.cr.setObjectZone(self.av, zoneId)
        elif zoneId == 999 and self.access <=100:
            print "Insufficient access"
        else:
            self.cr.setObjectZone(self.av, zoneId)
            strZoneId = str(zoneId)
            print "Went to room "+ strZoneId +""
        

    def moveAvatar(self, task):
    
        wallBitmask = BitMask32(1)
        floorBitmask = BitMask32(2)
        base.cTrav = CollisionTraverser()
        def getAirborneHeight():
            return offset + 0.025000000000000001
        walkControls = GravityWalker(legacyLifter=True)
        walkControls.setWallBitMask(wallBitmask)
        walkControls.setFloorBitMask(floorBitmask)
        walkControls.setWalkSpeed(self.ToonForwardSpeed, self.ToonJumpForce, self.ToonReverseSpeed, self.ToonRotateSpeed)
        walkControls.initializeCollisions(base.cTrav, self.model, floorOffset=0.025, reach=4.0)
        walkControls.setAirborneHeightFunc(getAirborneHeight)
        walkControls.enableAvatarControls()
        self.model.physControls = walkControls
        
        def setWatchKey(key, input, keyMapName):
            def watchKey(active=True):
                if active == True:
                    inputState.set(input, True)
                    keyMap[keyMapName] = 1
                else:
                    inputState.set(input, False)
                    keyMap[keyMapName] = 0
            base.accept(key, watchKey, [True])
            base.accept(key+'-up', watchKey, [False])
     
        keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'control':0}
         
        setWatchKey('arrow_up', 'forward', 'forward')
        setWatchKey('control-arrow_up', 'forward', 'forward')
        setWatchKey('alt-arrow_up', 'forward', 'forward')
        setWatchKey('shift-arrow_up', 'forward', 'forward')
        setWatchKey('arrow_down', 'reverse', 'backward')
        setWatchKey('control-arrow_down', 'reverse', 'backward')
        setWatchKey('alt-arrow_down', 'reverse', 'backward')
        setWatchKey('shift-arrow_down', 'reverse', 'backward')
        setWatchKey('arrow_left', 'turnLeft', 'left')
        setWatchKey('control-arrow_left', 'turnLeft', 'left')
        setWatchKey('alt-arrow_left', 'turnLeft', 'left')
        setWatchKey('shift-arrow_left', 'turnLeft', 'left')
        setWatchKey('arrow_right', 'turnRight', 'right')
        setWatchKey('control-arrow_right', 'turnRight', 'right')
        setWatchKey('alt-arrow_right', 'turnRight', 'right')
        setWatchKey('shift-arrow_right', 'turnRight', 'right')
        setWatchKey('control', 'jump', 'control')
         
        self.movingNeutral, movingForward = (False, False)
        self.movingRotation, movingBackward = (False, False)
        self.movingJumping = False
     
        def setMovementAnimation(loopName, playRate=1.0):
            if 'jump' in loopName:
                self.movingJumping = True
                self.movingForward = False
                self.movingNeutral = False
                self.movingRotation = False
                self.movingBackward = False
            elif loopName == 'run':
                self.movingJumping = False
                self.movingForward = True
                self.movingNeutral = False
                self.movingRotation = False
                self.movingBackward = False
            elif loopName == 'walk':
                self.movingJumping = False
                self.movingForward = False
                self.movingNeutral = False
                if playRate == -1.0:
                    self.movingBackward = True
                    self.movingRotation = False
                else:
                    self.movingBackward = False
                    self.movingRotation = True
            elif loopName == 'neutral':
                self.movingJumping = False
                self.movingForward = False
                self.movingNeutral = True
                self.movingRotation = False
                self.movingBackward = False
            else:
                self.movingJumping = False
                self.movingForward = False
                self.movingNeutral = False
                self.movingRotation = False
                self.movingBackward = False
            ActorInterval(self.model, loopName, playRate=playRate).loop()
     
        def handleMovement(task):
            global movingNeutral, movingForward
            global movingRotation, movingBackward, movingJumping
            if keyMap['control'] == 1:
                if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
                    if self.movingJumping == False:
                        if self.model.physControls.isAirborne:
                            setMovementAnimation('running-jump-idle')
                        else:
                            if keyMap['forward']:
                                if self.movingForward == False:
                                    setMovementAnimation('run')
                            elif keyMap['backward']:
                                if self.movingBackward == False:
                                    setMovementAnimation('walk', playRate=-1.0)
                            elif keyMap['left'] or keyMap['right']:
                                if self.movingRotation == False:
                                    setMovementAnimation('walk')
                    else:
                        if not self.model.physControls.isAirborne:
                            if keyMap['forward']:
                                if self.movingForward == False:
                                    setMovementAnimation('run')
                            elif keyMap['backward']:
                                if self.movingBackward == False:
                                    setMovementAnimation('walk', playRate=-1.0)
                            elif keyMap['left'] or keyMap['right']:
                                if self.movingRotation == False:
                                    setMovementAnimation('walk')
                else:
                    if self.movingJumping == False:
                        if self.model.physControls.isAirborne:
                            setMovementAnimation('jump-idle')
                        else:
                            if self.movingNeutral == False:
                                setMovementAnimation('neutral')
                    else:
                        if not self.model.physControls.isAirborne:
                            if self.movingNeutral == False:
                                setMovementAnimation('neutral')
            elif keyMap['forward'] == 1:
                if self.movingForward == False:
                    if not self.model.physControls.isAirborne:
                        setMovementAnimation('run')
            elif keyMap['backward'] == 1:
                if self.movingBackward == False:
                    if not self.model.physControls.isAirborne:
                        setMovementAnimation('walk', playRate=-1.0)
            elif keyMap['left'] or keyMap['right']:
                if self.movingRotation == False:
                    if not self.model.physControls.isAirborne:
                        setMovementAnimation('walk')
            else:
                if not self.model.physControls.isAirborne:
                    if self.movingNeutral == False:
                        setMovementAnimation('neutral')
            return Task.cont
     
        base.taskMgr.add(handleMovement, 'controlManager')

        dt = globalClock.getDt()
        
def runInjectorCode():
        global text
        exec (text.get(1.0, "end"),globals())
    
def openInjector():
    import Tkinter as tk
    from direct.stdpy import thread
    root = tk.Tk()
    root.geometry('600x400')
    root.title('Python Injector')
    root.resizable(False,False)
    global text
    frame = tk.Frame(root)
    text = tk.Text(frame,width=70,height=20)
    
    text.insert(1.0,"")
    
    text.pack(side="left")
    tk.Button(root,text="Inject!",command=runInjectorCode).pack()
    scroll = tk.Scrollbar(frame)
    scroll.pack(fill="y",side="right")
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    frame.pack(fill="y")
    
    thread.start_new_thread(root.mainloop,())

#openInjector()

base.w = World()
run()
