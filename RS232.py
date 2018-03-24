import serial
import thread
import json

abortAction = False
portbz = False
SerPort = None


def readPort():
    try:
        print "Reading Started.."
        thread.start_new_thread(read, ())
    except Exception as e:
        print e


def read():
    global abortAction
    line = ""
    lnBeforePrg = ""
    writeStarted = False
    print "Hello"
    fileTowrite = None

    while not abortAction:
        byte = SerPort.read()
        print byte
        if len(byte) > 0:
            line += byte
            if (byte == '\n' or byte == '\r') and len(line) > 1:
                if line.startswith('O') or line.startswith('o'):
                    writeStarted = True
                    programName = findProgramName(line)
                    fileTowrite = open("./ncfiles/" + programName, "w+")
                    fileTowrite.write(lnBeforePrg)
                    lnBeforePrg = ""
                if writeStarted:
                    fileTowrite.write(line)
                else :
                    lnBeforePrg += line
                line = ""
            if writeStarted and byte is '%':
                fileTowrite.write('%\r')
                fileTowrite.close()
        else:
            if writeStarted:
                fileTowrite.close()


def openPort():
    global SerPort
    with open ('setting.json') as data_file:
        settings = json.load(data_file)
    SerPort = serial.Serial(port=settings["port"],
                            baudrate=int(settings["baudrate"]),
                            parity=settings["parity"],
                            stopbits=int(settings["stopbits"]),
                            bytesize=int(settings["bytesize"]),
                            xonxoff=bool(settings["xonxoff"]),        # enable software flow control
                            rtscts=bool(settings["rtscts"]),          # enable RTS/CTS flow control
                            writeTimeout=1,                           # set a timeout for writes
                            dsrdtr=bool(settings["dsrdtr"]),          # None: use rtscts setting, dsrdtr override if True or False
                            interCharTimeout=None,                    # Inter-character timeout, None to disable
                            timeout=1)
    return SerPort


def sendFile(filepath, currentline, sendtext):
    try:
        global portbz
        portbz = True
        thread.start_new_thread(send, (filepath, currentline, sendtext))
    except Exception as e:
        print e


def send(filepath, currentline, sendtext):
    global portbz
    global abortAction
    global SerPort
    #/dev/ttyAMA0
    abortAction = False
    fileToSend = open(filepath)
    try:
        for line in iter(fileToSend):
            print line
            # currentline.set(line)
            if abortAction == False:
                for ch in line:
                    SerPort.write(ch)
            else:
                print "Aborted"
                break
    except Exception as e:
        print e
    fileToSend.close()
    portbz = False
    sendtext.set("Program  >>>")


def abort():
    global portbz
    global abortAction
    portbz = False
    abortAction = True


def findProgramName(line):
    endIndex = -1
    if line.find(' ') > -1:
        endIndex = line.index(' ')
    else:
        if line.find('\n') > -1:
            endIndex = line.index('\n')
        else:
            if line.find('\r') > -1:
                endIndex = line.index('\r')
    return  line[:endIndex]
