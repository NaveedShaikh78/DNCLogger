import serial
import thread

abortSending = False
portbz = False

def readPort() :
    ser = openPort()
    

def openPort() :
    return serial.Serial(port='COM1',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
        xonxoff=False,         # enable software flow control
        rtscts=False,          # enable RTS/CTS flow control
        writeTimeout=1,        # set a timeout for writes
        dsrdtr=False,          # None: use rtscts setting, dsrdtr override if True or False
        interCharTimeout=None, # Inter-character timeout, None to disable
        timeout=1) 

def sendFile(filepath,currentline,sendtext) :
    try:
        global portbz
        portbz = True
        thread.start_new_thread(send,(filepath,currentline,sendtext))
    except Exception as e:
        print e
        
def send(filepath,currentline,sendtext):
    global portbz
    global abortSending
    #/dev/ttyAMA0
    ser = openPort()
    abortSending = False
    file = open(filepath)
    try:
            for line in iter(file) :
                print line
                #currentline.set(line)
                if abortSending == False :
                    for ch in line :
                        ser.write(ch)
                else :
                    print "Aborted" 
                    break
    except Exception as e:
        print e
    file.close
    portbz = False
    sendtext.set("Program  >>>")

def abort():
    global portbz
    global abortSending
    portbz = False
    abortSending = True
    

    
