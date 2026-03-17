import uuid

from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import QProcess, Signal, QObject, QIODevice

from PySide6.QtBluetooth import QBluetoothServer, QBluetoothServiceInfo, QBluetoothSocket, QBluetoothLocalDevice, QBluetoothServiceInfo, QBluetoothUuid


"""
the system communicates with ADS1293 via bluetooth (rfcomm)
simulators are also designed with bluetooth protocol in mind

this class internally handles:
1. binding baddr to virtual port
2. reading data from it
3. sending it to main application
4. look after QProcess
"""
class RFComm(QObject):

    com_started = Signal()

    """
    int should be -1 for errors
    1 for graceful exit
    """
    com_finished = Signal(int, str)
    
    def __init__(self, app):
        super(RFComm, self).__init__()

        self.service = QBluetoothServiceInfo()                
        self.server = QBluetoothServer(QBluetoothServiceInfo.RfcommProtocol, app)
        self.socket = None

        self.isReading = True

        self.server.newConnection.connect(self.on_new_connection)
        self.server.errorOccurred.connect(self.on_error_occurred)

    def start_server(self):
        if not self.server.isListening():
            local_adp = QBluetoothLocalDevice()
            if local_adp.isValid():
                l = self.server.listen(local_adp.address())
                if l:
                    self.register(local_adp)

    def register(self, local_adp: QBluetoothLocalDevice):
    
        protocol_seq = QBluetoothServiceInfo.Sequence()
        rfcomm_seq = QBluetoothServiceInfo.Sequence()
        l2dp = QBluetoothServiceInfo.Sequence()

        l2dp.append(QBluetoothUuid(QBluetoothUuid.ProtocolUuid.L2cap))

        rfcomm_seq.append(
            QBluetoothUuid.ProtocolUuid.Rfcomm
        )
        rfcomm_seq.append(
            QBluetoothUuid.ServiceClassUuid.SerialPort.value
        )
        
        # protocol_seq.append(l2dp)
        protocol_seq.append(rfcomm_seq)

        self.service.setServiceName("nid-24 data collection")
        self.service.setServiceUuid(str(uuid.uuid4()))
        self.service.setAttribute(
            QBluetoothServiceInfo.ProtocolDescriptorList.value,
            protocol_seq   
        )
        # self.service.setAttribute(QBluetoothServiceInfo.ServiceName.value, "nid-24 data collection")

        x = self.service.registerService(local_adp.address())
        if x:
            print("Service is now registered")


    def on_new_connection(self):
        print("New connection")
        self.socket = self.server.nextPendingConnection()
        com_started.emit()


    def on_error_occurred(self, error: QBluetoothServer.Error):
        self.com_finished(-1, str(error))

    def server_shutdown(self):
        self.server.close()
        self.service.unregisterService()
