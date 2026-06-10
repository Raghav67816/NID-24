RFCommProcess class is responsible for managing the rfcomm process and it's state. It starts the rfcomm process and observes it's state. This class inherits from **QProcess** and runs the rfcomm process by executing:

```bash
sudo rfcomm listen hci0
```

This also adds an SDP profile internally. When a device connects or disconnects the state is emitted by the class.


## Signals

`com_finished`: Emitted when process is finished. The signal returns **int exit_code** and **str message**


!!! info
    The class contains a **cleanup()** function. If you are making your own utilities with rfcomm make sure that you call this function on application exit.
